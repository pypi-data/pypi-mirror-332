# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0320.stanza import Fingerprint
from slixmpp_jingle.xep_0320.fingerprint import XEP_0320

register_plugin(XEP_0320)
