# -*- coding: utf-8 -*-

from rest_framework import throttling


class BurstRateThrottle(throttling.AnonRateThrottle):
    scope = 'burst'


class SustainedRateThrottle(throttling.AnonRateThrottle):
    scope = 'sustained'
