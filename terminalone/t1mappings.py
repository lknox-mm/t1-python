# -*- coding: utf-8 -*-
"""Provides lookup dicts for t1 classes and child paths."""
from __future__ import absolute_import

from .reports import Report
from .models import *

CLASSES = {
    'ad_servers': AdServer,
    'advertisers': Advertiser,
    'agencies': Agency,
    'atomic_creatives': AtomicCreative,
    'audience_segments': AudienceSegment,
    'budget_flights': BudgetFlight,
    'campaigns': Campaign,
    'concepts': Concept,
    'contacts': Contact,
    'creative_approvals': CreativeApproval,
    'creatives': Creative,
    'deals': Deal,
    'organizations': Organization,
    'permissions': Permission,
    'pixel_bundles': PixelBundle,
    'pixel_providers': PixelProvider,
    'pixels': ChildPixel,
    'placement_slots': PlacementSlot,
    'publisher_sites': PublisherSite,
    'publishers': Publisher,
    'reports': Report,
    'retired_audience_segments': RetiredAudienceSegment,
    'retired_strategy_audience_segments': RetiredStrategyAudienceSegment,
    'rmx_strategies': RMXStrategy,
    'rmx_strategy_roi_target_pixels': RMXStrategyROITargetPixel,
    'seats': Seat,
    'site_lists': SiteList,
    'site_placements': SitePlacement,
    'strategies': Strategy,
    'strategy_audience_segments': StrategyAudienceSegment,
    'strategy_concepts': StrategyConcept,
    'strategy_deals': StrategyDeal,
    'strategy_day_parts': StrategyDayPart,
    'strategy_domain_restrictions': StrategyDomain,
    'strategy_supply_sources': StrategySupplySource,
    'strategy_targeting_segments': StrategyTargetingSegment,
    'supply_sources': SupplySource,
    'target_dimensions': TargetDimension,
    'target_values': TargetValue,
    'target_value_counts': TargetValue,
    'users': User,
    'vendor_contracts': VendorContract,
    'vendor_domains': VendorDomain,
    'vendor_pixel_domains': VendorPixelDomain,
    'vendor_pixels': VendorPixel,
    'vendors': Vendor,
    'verticals': Vertical,
}

MODEL_PATHS = {v: k for k, v in CLASSES.items()}

SINGULAR = {
    'ad_server': AdServer,
    'advertiser': Advertiser,
    'agency': Agency,
    'atomic_creative': AtomicCreative,
    'audience_segment': AudienceSegment,
    'budget_flight': BudgetFlight,
    'campaign': Campaign,
    'concept': Concept,
    'contact': Contact,
    'creative': Creative,
    'creative_approval': CreativeApproval,
    'deal': Deal,
    'organization': Organization,
    'permission': Permission,
    'pixel': ChildPixel,
    'pixel_bundle': PixelBundle,
    'pixel_provider': PixelProvider,
    'placement_slot': PlacementSlot,
    'publisher': Publisher,
    'publisher_site': PublisherSite,
    'report': Report,
    'retired_audience_segment': RetiredAudienceSegment,
    'retired_strategy_audience_segment': RetiredStrategyAudienceSegment,
    'rmx_strategy': RMXStrategy,
    'rmx_strategy_roi_target_pixel': RMXStrategyROITargetPixel,
    'seat': Seat,
    'site_list': SiteList,
    'site_placement': SitePlacement,
    'strategy': Strategy,
    'strategy_audience_segment': StrategyAudienceSegment,
    'strategy_concept': StrategyConcept,
    'strategy_deal': StrategyDeal,
    'strategy_day_part': StrategyDayPart,
    'strategy_domain_restriction': StrategyDomain,
    'strategy_supply_source': StrategySupplySource,
    'strategy_targeting_segment': StrategyTargetingSegment,
    'supply_source': SupplySource,
    'target_dimension': TargetDimension,
    'target_value': TargetValue,
    'target_value_count': TargetValue,
    'user': User,
    'vendor': Vendor,
    'vendor_contract': VendorContract,
    'vendor_domain': VendorDomain,
    'vendor_pixel': VendorPixel,
    'vendor_pixel_domain': VendorPixelDomain,
    'vertical': Vertical,
}

CHILD_PATHS = {
    'acl': ('acl', 0),
    'audience_segments': ('audience_segments', 0),
    'audio': ('target_dimensions', 22),
    'browser': ('target_dimensions', 4),
    'budget_flight': ('budget_flights', 0),
    'budget_flights': ('budget_flights', 0),
    'channels': ('target_dimensions', 16),
    'concepts': ('concepts', 0),
    'connection speed': ('target_dimensions', 2),
    'content initiation': ('target_dimensions', 21),
    'country': ('target_dimensions', 14),
    'day_parts': ('day_parts', 0),
    'device': ('target_dimensions', 24),
    'dma': ('target_dimensions', 1),
    'fold position': ('target_dimensions', 19),
    'isp': ('target_dimensions', 3),
    'linear format': ('target_dimensions', 20),
    'mathselect250': ('target_dimensions', 8),
    'os': ('target_dimensions', 5),
    'permission': ('permissions', 0),
    'permissions': ('permissions', 0),
    'player size': ('target_dimensions', 23),
    'region': ('target_dimensions', 7),
    'safety': ('target_dimensions', 15),
    'supplies': ('supplies', 0),
    'deals': ('deals', 0),
    'retired_audience_segments': ('retired_audience_segments', 0),
    'targeting_segments': ('targeting_segments', 0),
}
