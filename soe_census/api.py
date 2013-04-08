# -*- coding: utf-8 -*-

# Python interface to SOE Census API
# Copyright (C) 2013  Alex Headley <aheadley@waysaboutstuff.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import logging

from .util import clean_url_path
import .constants

class CallProxy(object):
    def __init__(self, parent, name):
        self._parent = parent
        self._name = name

    def __str__(self):
        return '.'.join(reversed(self.walk_chain(False)))

    def __getattr__(self, name):
        return self.__class__(self, name)

    def __len__(self):
        return self.parent_api.do_api_call('count', self)

    def __call__(self, *pargs, **kwargs):
        return self.parent_api.do_api_call('get', self, pargs, kwargs)

    @property
    def parent_api(self):
        return [self.walk_chain()][-1]

    def walk_chain(self, include_api=True):
        node = self
        while isinstance(node, self.__class__):
            yield node
            node = node._parent
        if include_api:
            # last entry is the api
            yield node

class CensusApi(object):
    GAME = None

    def __init__(self, service_id=None):
        self._init_logger()

        self._init_service_id(service_id)

        if self.GAME not in constants.GAMES:
            self._log.warning('Unrecognized game: %s', self.GAME)

        self._connector = requests.Session()

    def __getattr__(self, name):
        return CallProxy(self, name)

    def _init_logger(self):
        self._log = logging.getLogger('soe_census.api.' + self.__class__.__name__)

    def _init_service_id(self, service_id):
        self._service_id = service_id
        if self._service_id:
            self._log.info('API init with service ID: %s', self._service_id)
        else:
            self._log.info('API init without service ID')

    def _build_url(self, verb, collection, collection_id=None, image_type=None,
            **kwargs):
        cleaned_args = dict((constants.QUERY_COMMAND_FMT.format(query_command=k), v) \
            for (k, v) in kwargs.iteritems())
        return (
            constants.API_ENDPOINT + clean_url_path(
                constants.URL_PATH_FMT.format(
                    service_id=constants.SERVICE_ID_FMT.format(
                        service_id=self._service_id) if self._service_id else '',
                    verb=verb,
                    game=self.GAME,
                    collection=collection,
                    collection_id=collection_id if collection_id is not None else '',
                    image_type=image_type if image_type is not None else ''
                )),
            cleaned_args,
        )

    def _send_request(self, url, args):
        try:
            response = self._connector.get(url, params=payload)
        except requests.exceptions.RequestException as err:
            # TODO: actually do something here
            raise err
        return response

    def _parse_response(self, response):
        pass


class PlanetSide2Api(CensusApi):
    GAME = 'ps2'

class PlanetSide2BetaApi(CensusApi):
    GAME = 'ps2-beta'

class Everquest2Api(CensusApi):
    GAME = 'eq2'
