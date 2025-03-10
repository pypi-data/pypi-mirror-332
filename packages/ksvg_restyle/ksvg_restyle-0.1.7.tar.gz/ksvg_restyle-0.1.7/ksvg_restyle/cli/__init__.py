# -*- coding: utf-8 -*-
"""
This package contains CLI-related parts of the application

Modules:
    cmd: CLI entrypoint, holds Click app initialization
    handlers: callbacks for click arguments and options, call core functions
"""
from ksvg_restyle.cli import handlers
from ksvg_restyle.cli.cmd import run

# Export only stuff required at top-level usage
__all__ = [handlers, run]
