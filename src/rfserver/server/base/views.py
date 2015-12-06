#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author Jan Löser <jloeser@suse.de>
# Published under the GNU Public Licence 2
from rfserver.config import URL, REDFISH_VERSION, REDFISH_VERSION_MAJOR
from rfserver.server.base.models import Server
from flask import Blueprint, render_template, redirect, g, current_app,\
        url_for
from rfserver.server.sessions.decorators import login_required

module = Blueprint('base', __name__)

@module.before_request
def set_server_object():
    g.server = Server()

@module.route(URL['ROOT'], methods=['GET'])
def show_version():
    return render_template('base/Version.json',
        version=REDFISH_VERSION_MAJOR,
        url=URL['SERVICEROOT']
     )

@module.route(URL['SERVICEROOT'], methods=['GET'])
def redirect_serviceroot():
    return redirect(URL['SERVICEROOT'] + '/')

@module.route(URL['SERVICEROOT'] + '/', methods=['GET'])
def show_serviceroot():
    return render_template('base/ServiceRoot.1.0.0.json',
            redfish_version=REDFISH_VERSION
    )

@module.route(URL['SERVICEROOT'] + '/Registries', methods=['GET'])
@login_required
def show_registries():
    return current_app.send_static_file('Registries.json')

@module.route(URL['SERVICEROOT'] + '/Registries/Base', methods=['GET'])
@login_required
def show_base_registry():
    return current_app.send_static_file('Registries/Base.json')

@module.route(URL['SERVICEROOT'] + '/Registries/RedfishServer',
        methods=['GET']
)
@login_required
def show_redfishserver_registry():
    return current_app.send_static_file('Registries/RedfishServer.json')

@module.route(URL['SERVICEROOT'] +\
        '/RegistryStore/registries/en/Base.json', methods=['GET']
)
@login_required
def show_base_registry_full():
    return current_app.send_static_file(
            'RegistryStore/registries/en/Base.json'
    )

@module.route(URL['SERVICEROOT'] +\
        '/RegistryStore/registries/en/RedfishServer.json', methods=['GET']
)
@login_required
def show_redfishserver_registry_full():
    return current_app.send_static_file(
            'RegistryStore/registries/en/RedfishServer.json'
    )


