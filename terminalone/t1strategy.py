# -*- coding: utf-8 -*-
"""Provides strategy object.

Python library for interacting with the T1 API. Uses third-party module Requests
(http://docs.python-requests.org/en/latest/) to get and post data, and ElementTree
to parse it.
"""

import re
from .t1object import T1Object

PIXEL_PATTERN = re.compile(r'\[(\d+)\]')
OPERATOR_PATTERN = re.compile(r'(AND|OR)')

class T1Strategy(T1Object):
	"""docstring for T1Strategy."""
	collection = 'strategies'
	type = 'strategy'
	_relations = {
		'campaign', 'currency', 'time_zone',
	}
	_aud_seg_exc = T1Object._enum({'AND', 'OR'}, 'OR')
	_aud_seg_inc = T1Object._enum({'AND', 'OR'}, 'OR')
	_freq_int = T1Object._enum({'hour', 'day', 'week', 'month', 'campaign',
					'not-applicable'}, 'not-applicable')
	_freq_type = T1Object._enum({'even', 'asap', 'no-limit'}, 'no-limit')
	_goal_type = T1Object._enum({'spend', 'reach', 'cpc', 'cpe', 'cpa', 'roi'},
								'cpc')
	_media_type = T1Object._enum({'DISPLAY', 'VIDEO'}, 'DISPLAY')
	_pac_int = T1Object._enum({'hour', 'day'}, 'day')
	_pac_type = T1Object._enum({'even', 'asap'}, 'even')
	_site_selec = T1Object._enum({'MATHSELECT_250', 'EXCLUDE_UGC', 'ALL',
								'REDUCED'}, 'REDUCED')
	_supply_type = T1Object._enum({'RTB', 'RMX_API', 'T1_RMX'}, 'RTB')
	_type = T1Object._enum({'REM', 'GBO', 'AUD'}, 'GBO')
	
	_pull = {
		'audience_segment_exclude_op': None,
		'audience_segment_include_op': None,
		'bid_aggresiveness': float,
		'bid_price_is_media_only': T1Object._int_to_bool,
		'budget': float,
		'campaign_id': int,
		'created_on': T1Object._strpt,
		'description': None,
		'end_date': T1Object._strpt,
		'feature_compatibility': None,
		'frequency_amount': int,
		'frequency_interval': None,
		'frequency_type': None,
		'goal_type': None,
		'goal_value': float,
		'id': int,
		'impression_cap': int,
		'max_bid': float,
		'media_type': None,
		'name': None,
		'pacing_amount': float,
		'pacing_interval': None,
		'pacing_type': None,
		'pixel_target_expr': None,
		'run_on_all_exchanges': T1Object._int_to_bool,
		'run_on_all_pmp': T1Object._int_to_bool,
		'run_on_display': T1Object._int_to_bool,
		'run_on_mobile': T1Object._int_to_bool,
		'run_on_streaming': T1Object._int_to_bool,
		'site_restriction_transparent_urls': T1Object._int_to_bool,
		'site_selectiveness': None,
		'start_date': T1Object._strpt,
		'status': T1Object._int_to_bool,
		'supply_type': None,
		'type': None,
		'updated_on': T1Object._strpt,
		'use_campaign_end': T1Object._int_to_bool,
		'use_campaign_start': T1Object._int_to_bool,
		'use_mm_freq': T1Object._int_to_bool,
		'use_optimization': T1Object._int_to_bool,
		'version': int,
	}
	_push = _pull.copy()
	_push.update({
		'audience_segment_exclude_op': _aud_seg_exc,
		'audience_segment_include_op': _aud_seg_inc,
		'bid_price_is_media_only': int,
		'end_date': T1Object._strft,
		'frequency_interval': _freq_int,
		'frequency_type': _freq_type,
		'goal_type': _goal_type,
		'media_type': _media_type,
		'pacing_interval': _pac_int,
		'pacing_type': _pac_type,
		'run_on_all_exchanges': int,
		'run_on_all_pmp': int,
		'run_on_display': int,
		'run_on_mobile': int,
		'run_on_streaming': int,
		'site_restriction_transparent_urls': int,
		'site_selectiveness': _site_selec,
		'start_date': T1Object._strft,
		'status': int,
		'supply_type': _supply_type,
		'type': _type,
		'use_campaign_end': int,
		'use_campaign_start': int,
		'use_mm_freq': int,
		'use_optimization': int,
	})
	_readonly = T1Object._readonly.copy()
	def __init__(self, session, properties=None, **kwargs):
		super(T1Strategy, self).__init__(session, properties, **kwargs)
		try:
			self.pixel_target_expr
		except AttributeError:
			self.pixel_target_expr = ''
		self._deserialize_target_expr()

	def _deserialize_target_expr(self):
		if 'AND NOT' in self.pixel_target_expr:
			include_string, exclude_string = self.pixel_target_expr.split('AND NOT')
		elif 'NOT' in self.pixel_target_expr:
			include_string, exclude_string = self.pixel_target_expr.split('NOT')
		elif self.pixel_target_expr:
			include_string = self.pixel_target_expr
			exclude_string = ''
		else:
			include_string = ''
			exclude_string = ''
		include_operator = OPERATOR_PATTERN.search(include_string)
		exclude_operator = OPERATOR_PATTERN.search(exclude_string)
		if include_operator:
			include_operator = include_operator.group(0)
		if exclude_operator:
			exclude_operator = exclude_operator.group(0)
		self.pixel_target_expr = {
			'include': {
				'pixels': set([int(pix) for pix in PIXEL_PATTERN.findall(include_string)]),
				'operator': include_operator,
			},
			'exclude': {
				'pixels': set([int(pix) for pix in PIXEL_PATTERN.findall(exclude_string)]),
				'operator': exclude_operator,
			},
		}

	def _serialize_target_expr(self):
		include_bool = '] {} ['.format(self.pixel_target_expr['include']['operator'] or 'OR')
		include_pixels = self.pixel_target_expr['include']['pixels']
		exclude_bool = '] {} ['.format(self.pixel_target_expr['exclude']['operator'] or 'OR')
		exclude_pixels = self.pixel_target_expr['exclude']['pixels']
		include_string = '( [{}] )'.format(include_bool.join(
			str(pix) for pix in include_pixels)) if include_pixels else ''
		exclude_string = 'NOT ( [{}] )'.format(exclude_bool.join(
			str(pix) for pix in exclude_pixels)) if exclude_pixels else ''
		if include_string and exclude_string:
			return '{} AND {}'.format(include_string, exclude_string)
		else:
			return include_string + exclude_string

	def save(self, **kwargs):
		self.pixel_target_expr = self._serialize_target_expr()
		super(T1Strategy, self).save(**kwargs)
		self._deserialize_target_expr()

	@property
	def pixel_target_expr_string(self):
		return self._serialize_target_expr()
