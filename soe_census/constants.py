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

VERBS = [
    'get',
    'count',
]

GAMES = [
    'eq2',
    'ps2',
    'ps2-beta',
]

IMAGE_TYPES = [
    'paperdoll',
    'headshot',
]

SERVICE_ID_FMT = 's:{service_id}'

SEARCH_MODIFIERS = '<[>]^!'

QUERY_COMMAND_FMT = 'c:{query_command}'

QUERY_COMMANDS = [
    # Start with the Nth object within the results of the query
    # EX: c:start=10
    'start',
    # Limit the results to at most N objects
    # EX: c:limit=20
    'limit',
    # Only include the provided fields from the object within the result
    # (multiple field names separated by a comma)
    # EX: c:show=field,field
    'show',
    # Include all field except the provided fields from the object within the
    # result (multiple field names separated by a comma)
    # EX: c:hide=field,field
    'hide',
    # Sort the results by the field(s) provided (multiple field names separated
    # by a comma). The sort direction
    # EX: c:sort=field[:1],field
    'sort',
    # Include objects where the specified field exists, regardless of the value
    # within that field (multiple field names separated by a comma).
    # EX: c:has=field
    'has',
    # "Resolve" information by merging data from another collection and include
    # the detailed object information for the provided fields from the object
    # within the result (multiple field names separated by a comma)
    # EX: c:resolve=field,field
    'resolve',
    # Set whether a search should be case-sensitive
    # EX: c:case=true
    'case',
]

API_ENDPOINT = 'http://census.soe.com'

URL_PATH_FMT = '/{service_id}/{verb}/{game}/{collection}/{collection_id}/{image_type}'
