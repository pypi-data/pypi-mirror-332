# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0167.stanza import Description, PayloadType, RtcpMux, Encryption, Bandwidth, Parameter, Crypto #, RtcpFB  --> xep_0293
from slixmpp_jingle.xep_0167.rtp import XEP_0167

register_plugin(XEP_0167)
