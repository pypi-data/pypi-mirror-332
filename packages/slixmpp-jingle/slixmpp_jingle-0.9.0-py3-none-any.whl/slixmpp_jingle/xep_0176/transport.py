# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

import logging

from typing import Iterable, Tuple, Optional

from slixmpp import JID, Iq
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.xmlstream.handler import Callback
from slixmpp.xmlstream.matcher import StanzaPath
from slixmpp_jingle.xep_0166 import Jingle, Content
from slixmpp_jingle.xep_0176 import stanza, Transport, Candidate, RemoteCandidate

import re
from hashlib import md5 # Elmar Test!


log = logging.getLogger(__name__)

class XEP_0176(BasePlugin):

    name = 'xep_0176'
    description = 'XEP-0176: Ice-Udp Transport'
    dependencies = set(['xep_0166'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content,True)
        register_stanza_plugin(Content,Transport)
        register_stanza_plugin(Transport,Candidate,True)
        register_stanza_plugin(Transport,RemoteCandidate)

        self.xmpp.register_handler(
            Callback('Rtp Jingle Ice-Udp Transport',
                StanzaPath('iq/jingle/content/transport'),
                self._handle_content_transport))

#    def session_bind(self, jid):
#        pass

#    def plugin_end(self):
#        pass


#######################################################################

    def _handle_content_transport(self, message):
        self.xmpp.event('jingle_content_transport', message['jingle']['content']['transport'])

    def make_candidate(self,sdp):
        candidates = []
        iter= re.finditer(r'^a=candidate:(\S+) +(\d+) +(\S+) +(\d+) +(\S+) +(\d+) +typ +(\S+)(?: +(raddr) +(\S+) +(rport) +(\d+))?(?: +(tcptype) +(\S+))?(?: +(generation) +(\d+))?(?: +(network-id) +(\d+))?(?: +(network-cost) +(\d+))?\r$',sdp,re.M)
        if iter:
            for m in iter:
                # required 'foundation', 'component', 'transport', 'priority', 'ip', 'port', 'type'
                # optional 'raddr', 'rport', 'tcptype', 'generation', 'network-id', 'network-cost'
                candidate = Candidate()
                candidate['foundation'] = m.group(1)
                candidate['component'] = m.group(2)
                candidate['protocol'] = m.group(3)
                candidate['priority'] = m.group(4)
                candidate['ip'] = m.group(5)
                candidate['port'] = m.group(6)
                candidate['type'] = m.group(7)
                candidate['network'] = '0' # Test Elmar!
                candidate['generation'] = '0' # Test Elmar!
                candidate['id'] = md5(sdp.encode('utf-8')).hexdigest() # Test Elmar!
                for n,v in zip(*[m.groups()[7:][i::2] for i in range(2)]):
                    if n=='raddr':
                        candidate['rel-addr'] = v
                    elif n=='rport':
                        candidate['rel-port'] = v
                    else:
                        candidate[n] = v
                candidates.append(candidate)
        return candidates

    def make_transport(self,sdp):
        m = re.search(r'^m=\S+ +(\S+)',sdp,re.M)
        if m is None or m.group(1)!='0':
            return None
        transport = Transport()
        hastransport = False
        m = re.search(r'^a=ice-ufrag:(\S+)\r$',sdp,re.M)
        if m:
            hastransport = True
            transport['ufrag'] =  m.group(1)
        m = re.search(r'^a=ice-pwd:(\S+)\r$',sdp,re.M)
        if m:
            hastransport = True
            transport['pwd'] = m.group(1)
        if self.xmpp['xep_0320']:
            fingerprint = self.xmpp['xep_0320'].make_fingerprint(sdp)
            if fingerprint:
                hastransport = True
                transport.append(fingerprint)
        candidates = self.make_candidate(sdp)
        if candidates:
            hastransport = True
            for candidate in candidates:
                transport.append(candidate)
        if hastransport:
            return transport
        return None
