# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0294.stanza import HdrExt, Parameter, ExtMapAllowMixed
from slixmpp_jingle.xep_0294.hdrext import XEP_0294

register_plugin(XEP_0294)
