#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2022 Bumsoo Kim <bskim45@gmail.com>
#
# MIT Licence http://opensource.org/licenses/MIT

from __future__ import annotations

import sys

from workflow import ICON_INFO

from api import ArtifactHubClient, ChartCenterClient, HubClient
from migration import migrate
from utils import (
    create_workflow,
    is_artifacthub_enabled,
    is_chartcenter_enabled,
    is_hub_enabled,
)


def add_default_item(wf):
    if is_artifacthub_enabled(wf):
        wf.add_item(
            title='Go to ArtifactHub',
            subtitle=ArtifactHubClient.BASE_URL,
            arg=ArtifactHubClient.BASE_URL,
            valid=True,
            icon=wf.workflowfile(ArtifactHubClient.ICON_PATH),
        )

    if is_chartcenter_enabled(wf):
        wf.add_item(
            title='Go to ChartCenter',
            subtitle=ChartCenterClient.BASE_URL,
            arg=ChartCenterClient.BASE_URL,
            valid=True,
            icon=wf.workflowfile(ChartCenterClient.ICON_PATH),
        )

    if is_hub_enabled(wf):
        wf.add_item(
            title='Go to Helm Hub',
            subtitle=HubClient.HUB_BASE_URL,
            arg=HubClient.HUB_BASE_URL,
            valid=True,
            icon=wf.workflowfile(HubClient.ICON_PATH),
        )


def generate_search_key(chart):
    wf.logger.info(chart)
    elements = [chart.chart_id]
    return ' '.join(elements)


def main(wf):
    log = wf.logger

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    log.info('user query: "%s"', query)

    # do workflow migration
    migrate(wf)

    if wf.update_available:
        wf.add_item(
            'New version is available',
            subtitle='Click to install the update',
            autocomplete='workflow:update',
            icon=ICON_INFO,
        )

    if not query:
        add_default_item(wf)
        wf.send_feedback()
        return 0

    charts = []

    if is_artifacthub_enabled(wf):

        def search():
            api = ArtifactHubClient()
            return api.get_charts(query)

        charts.extend(
            wf.cached_data(
                ArtifactHubClient.get_cache_key(query), search, max_age=30
            )
        )

    if is_chartcenter_enabled(wf):

        def search():
            api = ChartCenterClient()
            return api.get_charts(query)

        charts.extend(
            wf.cached_data(
                ChartCenterClient.get_cache_key(query), search, max_age=30
            )
        )

    if is_hub_enabled(wf):

        def search():
            api = HubClient()
            q = query
            if '/' in q:
                q = q.split('/')[-1]
            return api.get_charts(q)

        charts.extend(
            wf.cached_data(HubClient.get_cache_key(query), search, max_age=30)
        )

    log.info('%d charts found', len(charts))

    if query:
        # filter results that query only appears in the chart id
        charts = wf.filter(query, charts, key=generate_search_key)

    for chart in charts:
        wf.add_item(
            title='{0} ({1})'.format(chart.chart_id, chart.version),
            subtitle=chart.description,
            arg=chart.web_url,
            valid=True,
            icon=wf.workflowfile(chart.icon),
        )

    if not charts:
        if '/' in query:
            chart_name = query.split('/')[-1]
            wf.add_item(
                title='Do you want to try with "{0}"?'.format(chart_name),
                subtitle='Try to search without a repository name',
                autocomplete=chart_name,
            )

        if is_artifacthub_enabled(wf):
            wf.add_item(
                'No charts found for "{0}"'.format(query),
                subtitle='Click to search in ArtifactHub',
                arg=ArtifactHubClient.BASE_URL,
                valid=True,
            )

        if is_chartcenter_enabled(wf):
            wf.add_item(
                'No charts found for "{0}"'.format(query),
                subtitle='Click to search in ChartCenter',
                arg=ChartCenterClient.BASE_URL,
                valid=True,
            )

        if is_hub_enabled(wf):
            wf.add_item(
                'No charts found for "{0}"'.format(query),
                subtitle='Click to see the results in Helm Hub',
                arg='{0}/charts?q={1}'.format(HubClient.HUB_BASE_URL, query),
                valid=True,
            )
    else:
        add_default_item(wf)

    wf.send_feedback()


if __name__ == '__main__':
    wf = create_workflow()
    sys.exit(wf.run(main))
