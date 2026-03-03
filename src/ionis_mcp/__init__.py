"""ionis-mcp — MCP server for IONIS HF propagation analytics."""

import os
import sys

__version__ = "1.1.0"


def default_data_dir() -> str:
    """Return the platform-specific default data directory.

    - Linux/macOS: ~/.ionis-mcp/data
    - Windows: %LOCALAPPDATA%\\ionis-mcp\\data
    """
    if sys.platform == "win32":
        base = os.environ.get("LOCALAPPDATA", os.path.expanduser("~"))
        return os.path.join(base, "ionis-mcp", "data")
    return os.path.join(os.path.expanduser("~"), ".ionis-mcp", "data")
