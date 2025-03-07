# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.xmlstream import ElementBase

class Services(ElementBase):
    name = 'services'
    namespace = 'urn:xmpp:extdisco:2'
    plugin_attrib = 'services'
    interfaces = {'type'}

class Credentials(ElementBase):
    name = 'credentials'
    namespace = 'urn:xmpp:extdisco:2'
    plugin_attrib = 'credentials'
    interfaces = {}

class Service(ElementBase):
    name = 'service'
    namespace = 'urn:xmpp:extdisco:2'
    plugin_attrib = 'service'
    interfaces = {'action', 'expires', 'host', 'name', 'password', 'port', 'restricted', 'transport', 'type', 'username'}
    plugin_multi_attrib = 'services'
