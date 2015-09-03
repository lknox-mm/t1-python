# -*- coding: utf-8 -*-
"""Provides supply source object."""

from __future__ import absolute_import
from ..entity import Entity


class SupplySource(Entity):
    """SupplySource object"""
    collection = 'supply_sources'
    resource = 'supply_source'
    _relations = {
        'parent_supply',
    }
    _rtb_types = Entity._enum({'STANDARD', 'MARKETPLACE'}, None)
    _supply_types = Entity._enum({'exchange', 'data'}, None)
    _pull = {
        'id': int,
        'bidder_exchange_identifier': int,
        'code': None,
        'created_on': Entity._strpt,
        'default_seat_identifier': Entity._strpt,
        'distribute': Entity._int_to_bool,
        'has_display': Entity._int_to_bool,
        'has_mobile_display': Entity._int_to_bool,
        'has_mobile_video': Entity._int_to_bool,
        'has_video': Entity._int_to_bool,
        'is_proservice': Entity._int_to_bool,
        'mm_safe': Entity._int_to_bool,
        'parent_supply_id': int,
        'pixel_tag': None,
        'pmp_enabled': Entity._int_to_bool,
        'rtb_enabled': Entity._int_to_bool,
        'rtb_type': None,
        'seat_enabled': Entity._int_to_bool,
        'status': Entity._int_to_bool,
        'supply_type': None,
        'updated_on': Entity._strpt,
        'use_pool': Entity._int_to_bool,
        'version': int,
    }
    _push = _pull.copy()

    def __init__(self, session, properties=None, **kwargs):
        super(SupplySource, self).__init__(session, properties, **kwargs)
