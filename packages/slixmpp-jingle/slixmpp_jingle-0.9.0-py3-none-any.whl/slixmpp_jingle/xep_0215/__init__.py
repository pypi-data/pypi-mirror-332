# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0215.stanza import Services,  Credentials, Service
from slixmpp_jingle.xep_0215.services import XEP_0215

register_plugin(XEP_0215)
