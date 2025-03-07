# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.plugins.base import register_plugin

from slixmpp_jingle.xep_0166.stanza import Jingle, Content, Reason, Alternative_Session, Busy, Cancel, Connectivity_Error, Decline, Expired, Failed_Application, Failed_Transport, General_Error, Gone, Incompatible_Parameters, Media_Error, Security_Error, Success, Timeout, Unsupported_Applications, Unsupported_Transports, Thread, Text
from slixmpp_jingle.xep_0166.jingle import XEP_0166

register_plugin(XEP_0166)
