# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

import logging


from slixmpp import Iq
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.xmlstream.handler import Callback
from slixmpp.xmlstream.matcher import StanzaPath
from slixmpp_jingle.xep_0166 import stanza, Jingle, Content, Reason, Alternative_Session, Busy, Cancel, Connectivity_Error, Decline, Expired, Failed_Application, Failed_Transport, General_Error, Gone, Incompatible_Parameters, Media_Error, Security_Error, Success, Timeout, Unsupported_Applications, Unsupported_Transports, Thread, Text

import re

log = logging.getLogger(__name__)


class XEP_0166(BasePlugin):

    name = 'xep_0166'
    description = 'XEP-0166: Jingle'
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content, True)
        register_stanza_plugin(Jingle,Reason)
        register_stanza_plugin(Reason,Text)
        register_stanza_plugin(Jingle,Thread)

        self.xmpp.register_handler(
            Callback('Accept Content',
                StanzaPath('iq/jingle@action=content-accept'),
                self._handle_content_accept))

        self.xmpp.register_handler(
            Callback('Add Content',
                StanzaPath('iq/jingle@action=content-add'),
                self._handle_content_add))

        self.xmpp.register_handler(
            Callback('Modify Content',
                StanzaPath('iq/jingle@action=content-modify'),
                self._handle_content_modify))

        self.xmpp.register_handler(
            Callback('Reject Content',
                StanzaPath('iq/jingle@action=content-reject'),
                self._handle_content_reject))

        self.xmpp.register_handler(
            Callback('Remove Content',
                StanzaPath('iq/jingle@action=content-remove'),
                self._handle_content_remove))

        self.xmpp.register_handler(
            Callback('Description Info',
                StanzaPath('iq/jingle@action=description-info'),
                self._handle_description_info))

        self.xmpp.register_handler(
            Callback('Security Info',
                StanzaPath('iq/jingle@action=security-info'),
                self._handle_security_info))

        self.xmpp.register_handler(
            Callback('Accept Session',
                StanzaPath('iq/jingle@action=session-accept'),
                self._handle_session_accept))

        self.xmpp.register_handler(
            Callback('Info Session',
                StanzaPath('iq/jingle@action=session-info'),
                self._handle_session_info))

        self.xmpp.register_handler(
            Callback('Initiate Session',
                StanzaPath('iq/jingle@action=session-initiate'),
                self._handle_session_initiate))

        self.xmpp.register_handler(
            Callback('Terminate Session',
                StanzaPath('iq/jingle@action=session-terminate'),
                self._handle_session_terminate))

        self.xmpp.register_handler(
            Callback('Accept Transport',
                StanzaPath('iq/jingle@action=transport-accept'),
                self._handle_transport_accept))

        self.xmpp.register_handler(
            Callback('Info Transport',
                StanzaPath('iq/jingle@action=transport-info'),
                self._handle_transport_info))

        self.xmpp.register_handler(
            Callback('Reject Transport',
                StanzaPath('iq/jingle@action=transport-reject'),
                self._handle_transport_reject))

        self.xmpp.register_handler(
            Callback('Replace Transport',
                StanzaPath('iq/jingle@action=transport-replace'),
                self._handle_transport_replace))

#    def session_bind(self, jid):
#        pass

#    def plugin_end(self):
#        pass

#    def getSDP(self, jingle, username, userid, version):
#        ip = jingle['content']['description']['transport'].getRtpIP()
#        ret = "\r\no=%s %s %s IN IP4 %s" % (username, userid, version, ip or '127.0.0.1')
#        ret += "\r\ns="+jingle['name']
#        ret += "\r\nt=0 0"
#        ret += jingle['content']['description']['transport'].getSDP(self['transport']) or ''
#        return ret

#######################################################################


    def _handle_jingle(self, message):
        self.xmpp.event('jingle', message)

    def _handle_content_accept(self, message):
        self.xmpp.event('jingle_content_accept', message)

    def _handle_content_add(self, message):
        self.xmpp.event('jingle_content_add', message)

    def _handle_content_modify(self, message):
        self.xmpp.event('jingle_content_modify', message)

    def _handle_content_reject(self, message):
        self.xmpp.event('jingle_content_reject', message)

    def _handle_content_remove(self, message):
        self.xmpp.event('jingle_content_remove', message)

    def _handle_description_info(self, message):
        self.xmpp.event('jingle_description_info', message)

    def _handle_security_info(self, message):
        self.xmpp.event('jingle_security_info', message)

    def _handle_session_accept(self, message):
        self.xmpp.event('jingle_session_accept', message)

    def _handle_session_info(self, message):
        self.xmpp.event('jingle_session_info', message)

    def _handle_session_initiate(self, message):
        self.xmpp.event('jingle_session_initiate', message)

    def _handle_session_terminate(self, message):
        self.xmpp.event('jingle_session_terminate', message)

    def _handle_transport_accept(self, message):
        self.xmpp.event('jingle_transport_accept', message)

    def _handle_transport_info(self, message):
        self.xmpp.event('jingle_transport_info', message)

    def _handle_transport_reject(self, message):
        self.xmpp.event('jingle_transport_reject', message)

    def _handle_transport_replace(self, message):
        self.xmpp.event('jingle_transport_replace', message)


#######################################################################


#    def accept(self, mto: JID, sid: str, descriptions: Iterable[Tuple[str, str]], *, mfrom: Optional[JID] = None):
#        msg = self.xmpp.make_jingle(mto, mfrom=mfrom)
#        msg['jingle_propose']['id'] = sid
#        msg['jingle_propose']['descriptions'] = descriptions
#        msg.send()

    def make_jingle(self,sdp, initiator):
        jingle = Jingle()
        m = re.search(r'^o=(\S+) +(\S+)',sdp,re.M)
        if m:
            jingle['initiator'] = initiator
#            jingle['initiator'] = m.group(1)
            jingle['sid'] = m.group(1)

        if self.xmpp['xep_0338']:
            group = self.xmpp['xep_0338'].make_group(sdp)
            if group:
                jingle.append(group)

        iter= re.finditer(r'^m=(\S+)',sdp,re.M)
        counter = -1
        for m in iter:
            counter += 1
            content = Content()
            content['creator'] = 'initiator'
            content['name'] = str(counter) #m.group(1)
            # the mapext are only valid for the upper last media specified
            msubsdp = re.search(r'^(m='+m.group(1)+'(?:.|\r|\n)+?)(?=m=)',sdp+'m=end-of-file',re.M)
            if self.xmpp['xep_0167']:
                description = self.xmpp['xep_0167'].make_description(msubsdp.group(1),m.group(1))
                if description:
                    content.append(description)
            if self.xmpp['xep_0176']:
                transport = self.xmpp['xep_0176'].make_transport(sdp)
                if transport:
                    content.append(transport)
            if self.xmpp['xep_0177']:
                transport = self.xmpp['xep_0177'].make_transport(sdp)
                if transport:
                    content.append(transport)
            m = re.search(r'^a=(sendrecv|recvonly|sendonly)\r$',msubsdp.group(1),re.M)
            if m:
                switcher = {'recvonly':'initiator', 'sendonly':'responder', 'sendrecv':'both'}
                content['senders'] = switcher[m.group(1)]
            jingle.append(content)
        return jingle

    def make_terminate(self, cause):
        reason = Reason()
        if cause=='alternative-session':
            reason.append(Alternative_Session())
        elif cause=='busy':
            reason.append(Busy())
        elif cause=='bancel':
            reason.append(Cancel())
        elif cause=='connectivity-error':
            reason.append(Connectivity_Error())
        elif cause=='decline':
            reason.append(Decline())
        elif cause=='expired': 
            reason.append(Expired())
        elif cause=='failed-application':
            reason.append(Failed_Application())
        elif cause=='failed-transport':
            reason.append(Failed_Transport())
        elif cause=='general-error':
            reason.append(General_Error())
        elif cause=='gone':
            reason.append(Gone())
        elif cause=='incompatible-parameters':
            reason.append(Incompatible_Parameters())
        elif cause=='media-error':
            reason.append(Media_Error())
        elif cause=='security-error':
            reason.append(Security_Error())
        elif cause=='success':
            reason.append(Success())
        elif cause=='timeout': 
            reason.append(Timeout())
        elif cause=='unsupported-applications':
            reason.append(Unsupported_Applications())
        elif cause=='unsupported-transports':
            reason.append(Unsupported_Transports())
        return reason
