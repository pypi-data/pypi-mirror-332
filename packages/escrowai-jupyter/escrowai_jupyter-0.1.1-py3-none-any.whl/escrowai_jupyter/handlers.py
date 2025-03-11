from jupyter_server.base.handlers import APIHandler
import tornado.web
import subprocess
import os
import sys


class RunScriptHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):
        # Use the absolute path to main.py
        script_path = os.path.join(os.path.dirname(__file__), "main.py")
        result = subprocess.run(
            [sys.executable, script_path], capture_output=True, text=True
        )
        self.finish({"output": result.stdout, "error": result.stderr})


def setup_handlers(web_app):
    """
    Sets up the API route for the extension.
    """
    host_pattern = ".*$"
    base_url = web_app.settings["base_url"]

    # Route pattern without server proxy prefix
    route_pattern = f"{base_url}escrowai_jupyter/run-script"
    handlers = [(route_pattern, RunScriptHandler)]
    web_app.add_handlers(host_pattern, handlers)
