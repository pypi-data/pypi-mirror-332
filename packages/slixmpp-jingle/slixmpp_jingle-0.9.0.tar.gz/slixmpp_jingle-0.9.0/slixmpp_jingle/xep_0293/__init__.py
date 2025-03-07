# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0293.stanza import RtcpFB, Parameter, RtcpFBTrrInt
from slixmpp_jingle.xep_0293.rtcpfb import XEP_0293

register_plugin(XEP_0293)
