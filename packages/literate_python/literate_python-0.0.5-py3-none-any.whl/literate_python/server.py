import ast
import importlib
import os
import sys
from flask import Flask, request, jsonify

import traceback

from contextlib import redirect_stdout
from contextlib import redirect_stderr
from io import StringIO
from io import StringIO

import logging

from textwrap import shorten
from literate_python.loader import (
    register_literate_modules,
    register_literate_module_finder,
)

from literate_python.inspector import _inspect

logger = logging.getLogger(__name__)

app = Flask(__name__)


def get_top_level_names(code):
    tree = ast.parse(code)
    variables = []
    functions = []
    classes = []

    for node in tree.body:
        if isinstance(node, ast.Assign):
            # Handle assignments like x = 1 or x, y = 2, 3.
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables.append(target.id)
                elif isinstance(target, ast.Tuple):
                    for elt in target.elts:
                        if isinstance(elt, ast.Name):
                            variables.append(elt.id)
        elif isinstance(node, ast.AnnAssign):
            # Handle annotated assignments like: x: int = 1.
            if isinstance(node.target, ast.Name):
                variables.append(node.target.id)
        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return variables, functions, classes


#: app locals in current port
server_locals = {}


def ensure_module(module_name, module_create_method):
    """Ensure a module is loaded and return it."""
    if module_name in sys.modules:
        return sys.modules[module_name]

    match module_create_method:
        case "create":
            spec_module = importlib.util.spec_from_loader(module_name, loader=None)
            module = importlib.util.module_from_spec(spec_module)
            sys.modules[module_name] = module
            return module
        case "import":
            importlib.import_module(module_name)
            return sys.modules[module_name]
        case "import_or_create":
            if importlib.util.find_spec(module_name):
                importlib.import_module(module_name)
                return sys.modules[module_name]
            else:
                spec_module = importlib.util.spec_from_loader(module_name, loader=None)
                module = importlib.util.module_from_spec(spec_module)
                sys.modules[module_name] = module
                return module
        case _:
            msg = f"Module {module_create_method} doesn't exist"
            raise ValueError(msg)


def process_a_message(message):
    stdout_stream = StringIO()
    stderr_stream = StringIO()
    error = None
    result = None
    locals = []
    with redirect_stdout(stdout_stream):
        with redirect_stderr(stderr_stream):
            try:
                type = message["type"]
                code = message["code"]
                dict = globals()
                module_name = message["module"] if "module" in message else None
                if module_name:
                    module_create_method = message.get("module-create-method", "import")
                    module = ensure_module(module_name, module_create_method)
                    dict = module.__dict__

                if type == "eval":
                    exec(compile(code, module_name or "code", "exec"), dict)
                    message.get("result-name", "_")
                    result = dict.get("_", None)
                elif type == "exec":
                    result = exec(compile(code, module_name or "code", "exec"), dict)
                    vars_, funcs, classes = get_top_level_names(code)
                    for local in vars_ + funcs + classes:
                        if local in server_locals:
                            _local = server_locals[local]
                            if hasattr(_local, "__module__"):
                                _module_name = _local.__module__
                                if _module_name == module_name:
                                    # update the local with the new value
                                    server_locals[local] = getattr(module, local)
                                    locals.append(local)

                elif type == "quit":
                    result = None
                else:
                    error = "Unknown type: {}".format(type)
                    raise ValueError(error)
            except Exception as e:
                # printing stack trace
                traceback.print_exc()
                error = str(e)
    if error is None:
        return_value = {
            "result": _inspect(result),
            "type": "result",
            "locals": locals,
            "stdout": stdout_stream.getvalue(),
            "stderr": stderr_stream.getvalue(),
        }
    else:
        return_value = {
            "error": error,
            "type": "error",
            "stdout": stdout_stream.getvalue(),
            "stderr": stderr_stream.getvalue(),
        }

    if type == "quit":
        sys.exit(0)
    else:
        return return_value


def register(request):
    # Get JSON data
    data = request.get_json()

    # Process the data (example)
    logger.debug(
        "/register Received:%s", shorten(str(data), width=100, placeholder="...")
    )
    try:
        register_literate_modules(data)
        return_value = {"type": "done"}
    except Exception as e:
        # printing stack trace
        return_value = {"type": "error", "stderr": str(e)}
        traceback.print_exc()

    # Return a response
    logger.debug("/register Returning:%s", return_value)
    return jsonify(return_value)


@app.route("/lpy/register", methods=["POST"])
def register_router():
    return register(request)


def _execute(request):
    # Get JSON data
    data = request.get_json()

    # Process the data (example)
    logger.debug(
        "/execute Received:%s", shorten(str(data), width=100, placeholder="...")
    )
    return_value = process_a_message(data)

    # Return a response
    logger.debug("/execute Returning:%s", return_value)
    return jsonify(return_value)


@app.route("/lpy/execute", methods=["POST"])
def execute():
    return _execute(request)


def _status(request):
    return jsonify({"status": "ok"})


@app.route("/lpy/status", methods=["GET"])
def status():
    return _status(request)


def run_server():
    host = "127.0.0.1"
    port = 7330
    if "LITERATE_PYTHON_HOST" in os.environ:
        host = os.environ["LITERATE_PYTHON_HOST"]
    if "LITERATE_PYTHON_PORT" in os.environ:
        port = int(os.environ["LITERATE_PYTHON_PORT"])
    register_literate_module_finder()
    app.run(debug=True, port=port, host=host, use_reloader=False)
