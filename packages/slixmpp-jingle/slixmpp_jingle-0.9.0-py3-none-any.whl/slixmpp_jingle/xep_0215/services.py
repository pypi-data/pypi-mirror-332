# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

import logging


from slixmpp import Iq
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.xmlstream.handler import Callback
from slixmpp.xmlstream.matcher import StanzaPath
from slixmpp_jingle.xep_0215 import stanza, Services,  Credentials,  Service


log = logging.getLogger(__name__)


class XEP_0215(BasePlugin):

    name = 'xep_0215'
    description = 'XEP-0215: Services'
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Services)
        register_stanza_plugin(Services,Service, True)
        register_stanza_plugin(Iq,Credentials)
        register_stanza_plugin(Credentials,Service, True)

#        self.xmpp.register_handler(
#            Callback('Add Services',
#                StanzaPath('iq/services@type=add'),
#                self._handle_services_add))
#
#        self.xmpp.register_handler(
#            Callback('Delete Services',
#                StanzaPath('iq/services@type=delete'),
#                self._handle_services_delete))
#
#        self.xmpp.register_handler(
#            Callback('Modify Services',
#                StanzaPath('iq/services@type=modify'),
#                self._handle_services_modify))

        self.xmpp.register_handler(
            Callback('Services',
                StanzaPath('iq/services'),
                self._handle_services))

        self.xmpp.register_handler(
            Callback('Credentials',
                StanzaPath('iq/credentials'),
                self._handle_credentials))

#######################################################################


    def _handle_services_add(self, message):
        self.xmpp.event('services_add', message)

    def _handle_services_delete(self, message):
        self.xmpp.event('services_delete', message)

    def _handle_services_modify(self, message):
        self.xmpp.event('services_modify', message)

    def _handle_services(self, message):
        self.xmpp.event('services', message)

    def _handle_credentials(self, message):
        self.xmpp.event('credentials', message)


#######################################################################
#
#    def make_services(self):
#        return Services()
#
#    def make_credentials(self):
#        return Credentials()
