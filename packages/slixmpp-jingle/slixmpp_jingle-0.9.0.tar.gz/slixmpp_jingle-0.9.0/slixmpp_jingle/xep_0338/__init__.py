# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0338.stanza import Group, Content
from slixmpp_jingle.xep_0338.group import XEP_0338

register_plugin(XEP_0338)
