# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0262.stanza import Zrtp
from slixmpp_jingle.xep_0262.zrtp import XEP_0262

register_plugin(XEP_0262)
