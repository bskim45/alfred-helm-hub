#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2022 Bumsoo Kim <bskim45@gmail.com>
#
# MIT Licence http://opensource.org/licenses/MIT

from __future__ import annotations

import os
from typing import List

import requests


class Chart(object):
    def __init__(self, chart_id, description, version, web_url, icon):
        self.chart_id = chart_id
        self.description = description
        self.version = version
        self.web_url = web_url
        self.icon = icon

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __unicode__(self):
        return '{0} ({1})'.format(self.chart_id, self.version)


class ChartClient(object):
    NAME = ''
    CACHE_KEY = ''
    ICON_PATH = ''

    @classmethod
    def get_cache_key(cls, query=None):
        return '{0}-charts-{1}'.format(cls.CACHE_KEY, query).replace(
            os.sep, '_'
        )

    def get_charts(self, query=None):
        # type: (str) -> List[Chart]
        if not query:
            return []

        charts = self.get_chart_request(query=query)
        return charts

    def get_chart_request(self, query=None):
        # type: (str) -> List[Chart]
        raise NotImplementedError()

    def get_chart_url(self, chart_id):
        # type: (str) -> str
        raise NotImplementedError()


class HubClient(ChartClient):
    NAME = 'hub.helm.sh'
    CACHE_KEY = 'hub'
    ICON_PATH = 'icons/hub.png'

    CHART_SERVICE_BASE_URL = 'https://hub.helm.sh/api/chartsvc'
    CHART_SERVICE_SEARCH_URL = CHART_SERVICE_BASE_URL + '/v1/charts/search'
    HUB_BASE_URL = 'https://hub.helm.sh'

    def get_chart_request(self, query=None):
        params = dict(q=query)
        r = requests.get(self.CHART_SERVICE_SEARCH_URL, params)

        r.raise_for_status()

        result = r.json()

        charts = [
            Chart(
                chart['id'],
                chart['attributes']['description'],
                chart['relationships']['latestChartVersion']['data'][
                    'version'
                ],
                self.get_chart_url(chart['id']),
                self.ICON_PATH,
            )
            for chart in result['data']
        ]
        return charts

    def get_chart_url(self, chart_id):
        return '{0}/charts/{1}'.format(self.HUB_BASE_URL, chart_id)


class ChartCenterClient(ChartClient):
    NAME = 'chartcenter.io'
    CACHE_KEY = 'chartcenter'
    ICON_PATH = 'icons/chartcenter.png'

    API_BASE_URL = 'https://chartcenter.io/api'
    API_SEARCH_URL = API_BASE_URL + '/ui/search'
    BASE_URL = 'https://chartcenter.io'

    def get_chart_request(self, query=None):
        params = dict(name_fragment=query)
        r = requests.get(self.API_SEARCH_URL, params)

        r.raise_for_status()

        result = r.json()

        charts = [
            Chart(
                '{0}/{1}'.format(chart['namespace'], chart['name']),
                chart['description'],
                chart['latest_chart_version'],
                self.get_chart_url(
                    '{0}/{1}'.format(chart['namespace'], chart['name'])
                ),
                self.ICON_PATH,
            )
            for chart in result['chart']
        ]
        return charts

    def get_chart_url(self, chart_id):
        return 'https://chartcenter.io/{0}'.format(chart_id)


class ArtifactHubClient(ChartClient):
    NAME = 'artifacthub.io'
    CACHE_KEY = 'artifacthub'
    ICON_PATH = 'icons/artifacthub.png'

    API_BASE_URL = 'https://artifacthub.io/api'
    API_SEARCH_URL = API_BASE_URL + '/v1/packages/search'
    BASE_URL = 'https://artifacthub.io'

    def get_chart_request(self, query=None):
        params = dict(
            facets=False,
            limit=30,
            offset=0,
            kind=0,  # helm chart
            ts_query_web=query,
        )
        r = requests.get(self.API_SEARCH_URL, params)

        r.raise_for_status()

        result = r.json()

        charts = [
            Chart(
                '{0}/{1}'.format(chart['repository']['name'], chart['name']),
                chart['description'],
                chart['version'],
                self.get_chart_url(
                    '{0}/{1}'.format(
                        chart['repository']['name'], chart['name']
                    )
                ),
                self.ICON_PATH,
            )
            for chart in result['packages']
        ]
        return charts

    def get_chart_url(self, chart_id):
        return '{0}/packages/helm/{1}'.format(self.BASE_URL, chart_id)
