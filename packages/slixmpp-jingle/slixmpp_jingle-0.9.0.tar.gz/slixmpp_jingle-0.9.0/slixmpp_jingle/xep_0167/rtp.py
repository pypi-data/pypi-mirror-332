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
from slixmpp_jingle.xep_0167 import stanza, Description, PayloadType, RtcpMux, Encryption, Bandwidth, Parameter, Crypto#,  RtcpFB --> xep_0293

import re

log = logging.getLogger(__name__)


class XEP_0167(BasePlugin):

    name = 'xep_0167'
    description = 'XEP-0167: Jingle'
    dependencies = set(['xep_0166'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content,True)
        register_stanza_plugin(Content,Description)
        register_stanza_plugin(Description,PayloadType,True)
        register_stanza_plugin(Description,RtcpMux)
        register_stanza_plugin(Description,Encryption)
        register_stanza_plugin(Description,Bandwidth)
        register_stanza_plugin(Description,RtcpMux)
        register_stanza_plugin(PayloadType,Parameter,True)
#        register_stanza_plugin(PayloadType,RtcpFB)  --> xep_0293
        register_stanza_plugin(Encryption,Crypto)

        self.xmpp.register_handler(
            Callback('Rtp Jingle Description',
                StanzaPath('iq/jingle/content/description'),
                self._handle_content_description))


#    def session_bind(self, jid):
#        pass

#    def plugin_end(self):
#        pass

#######################################################################


    def _handle_content_description(self, message):
        self.xmpp.event('jingle_content_description', message['jingle']['content']['description'])

    def make_description(self,sdp,media):
        m = re.search(r'^m='+media+' +(\d+) +([\w/]+)([ \d]*)\r$',sdp,re.M)
        if m:
            description = Description()
            description['media'] = media
#            if self.xmpp['xep_0294']:
#               hdrexts = self.xmpp['xep_0294'].make_hdrexts(sdp)
#               for hdrext in hdrexts:
#                   description.append(hdrext)
            if m.group(3):
                for id in m.group(3).split():
                    iter = re.finditer(r'^a=rtpmap:'+id+' +([\w\-.]+)(?:/(\d+)(?:/(\S+))?)?\r$',sdp,re.M)
                    m = re.search(r'^a=ptime:(\S+)\r$',sdp,re.M)
                    ptime = None
                    if m:
                        ptime = m.group(1)
                    m = re.search(r'^a=maxptime:(\S+)\r$',sdp,re.M)
                    maxptime = None
                    if m:
                        maxptime = m.group(1)
                    for m in iter:
                        payload = PayloadType()
                        payload['id'] = id
                        payload['name'] = m.group(1)
                        if m.group(2):
                            payload['clockrate'] = m.group(2)
                        if m.group(3):
                            payload['channels'] = m.group(3)
                        if ptime:
                            payload['ptime'] = ptime
                        if maxptime:
                            payload['maxptime'] = maxptime
                        m1 = re.search(r'^a=fmtp:'+id+' *(.*)\r$',sdp,re.M)
                        if m1:
                            for line in m1.groups():
                                m2 = re.findall(r' *; *([^=;\r]+(?:=[^; \r]+)?)',f';{line}')
                                if m2:
                                    for p in m2:
                                        if p:
                                            parameter = Parameter()
                                            s = p.split('=')
                                            if len(s)>1:
                                                parameter['name'] = s[0]
                                                parameter['value'] = s[1]
                                            else:
                                                parameter['value'] = s[0]
                                            payload.append(parameter)
                        if self.xmpp['xep_0293']:
                            ret = self.xmpp['xep_0293'].make_rtcpfb(sdp,id)
                            for rtcpfb in ret:
                                payload.append(rtcpfb)
                        description.append(payload)
            m = re.search(r'^a=crypto:(\d+) +(\S+) +(\S+) +(\S+)\r$',sdp,re.M)
            if m:
                encryption = Encryption()
                crypto = Crypto()
                crypto['tag'] = m.group(1)
                crypto['crypto-suite'] = m.group(2)
                crypto['key-params'] = m.group(3)
                crypto['session-params'] = m.group(4)
                encryption.append(crypto)
                description.append(encryption)
            if self.xmpp['xep_0293']:
                ret = self.xmpp['xep_0293'].make_rtcpfb(sdp)
                for rtcpfb in ret:
                    payload.append(rtcpfb)
            if self.xmpp['xep_0294']:
                hdrexts = self.xmpp['xep_0294'].make_hdrexts(sdp)
                for hdrext in hdrexts:
                    description.append(hdrext)
                hdrextallowmixed = self.xmpp['xep_0294'].make_extmapallowmixed(sdp)
                if hdrextallowmixed!=None:
                    description.append(hdrextallowmixed)
            if self.xmpp['xep_0339']:
               ret = self.xmpp['xep_0339'].make_ssrcgroup(sdp)
               if ret:
                   description.append(ret[0])
                   for source in ret[1]:
                       description.append(source)
               else:
                   source = self.xmpp['xep_0339'].make_source(sdp)
                   if source:
                       description.append(source)
            # hier müsste noch geprüft werden, ob \w+ in "a=group:BUNDLE X Y" vorhkommt.
            m = re.search(r'^a=mid: *\w+\r$',sdp,re.M)
            if m:
                rtcpmux = RtcpMux()
                description.append(rtcpmux)
            return description
        return None
