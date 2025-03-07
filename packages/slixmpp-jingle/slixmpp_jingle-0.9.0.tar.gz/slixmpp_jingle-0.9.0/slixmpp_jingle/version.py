# Slixmpp: The Slick XMPP Library
# Copyright (C) 2024  Meyer Elmar
# This file is part of Slixmpp-Jingle.
# See the file LICENSE for copying permission.
# We don't want to have to import the entire library
# just to get the version info for setup.py

__all__ = [ "__version__" ]

__version__ = '0.9.0'
__version__["short"] = "0.9.0"
__version__["tag"] = "beta"
__version__["full"] = f"{__version__['short']}-{__version__['tag']}"
