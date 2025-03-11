import os
from ._version import __version__
from .handlers import setup_handlers
from typing import List, Dict, Any

__all__ = ["__version__", "setup_handlers"]


def _jupyter_server_extension_paths() -> List[Dict[str, str]]:
    return [{"module": "escrowai_jupyter"}]


def jupyter_serverproxy_servers() -> Dict[str, Any]:
    """
    Return a dict of server configurations for jupyter-server-proxy.
    This is used by jupyter-server-proxy to start the service.
    """
    icon_path = os.path.join(os.path.dirname(__file__), "icons", "escrowai.svg")

    return {
        "escrowai-jupyter": {
            "command": ["python", "-m", "escrowai_jupyter.main"],
            "environment": {},
            "launcher_entry": {"title": "EscrowAI Jupyter", "icon_path": icon_path},
        }
    }


def load_jupyter_server_extension(nbapp) -> None:
    setup_handlers(nbapp.web_app)
    nbapp.log.info("EscrowAI Jupyter loaded.")
