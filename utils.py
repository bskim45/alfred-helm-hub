#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2020 Bumsoo Kim <bskim45@gmail.com>
#
# MIT Licence http://opensource.org/licenses/MIT

from __future__ import print_function, unicode_literals

from api import ArtifactHubClient, ChartCenterClient, HubClient
from workflow import Workflow3

SUPPORTED_REPOS = {
    ArtifactHubClient.NAME: ArtifactHubClient,
    ChartCenterClient.NAME: ChartCenterClient,
    HubClient.NAME: HubClient,
}

DEFAULT_REPO_CONFIG = {
    name: {
        'enabled': True,
        'icon': repo.ICON_PATH
    }
    for name, repo in SUPPORTED_REPOS.viewitems()
}

DEFAULT_REPO_CONFIG[HubClient.NAME]['enabled'] = False


def create_workflow():
    # type: () -> Workflow3
    wf = Workflow3(
        default_settings={
            'hubs': DEFAULT_REPO_CONFIG
        },
        update_settings={
            'github_slug': 'bskim45/alfred-helm-hub',
            'frequency': 7,  # a week
        })
    wf.settings.save()

    hub_settings = DEFAULT_REPO_CONFIG
    hub_settings.update(wf.settings['hubs'])
    wf.settings['hubs'] = hub_settings
    wf.settings.save()

    return wf


def is_hub_enabled(wf):
    # type: (Workflow3) -> bool
    return wf.settings['hubs'][HubClient.NAME]['enabled']


def is_chartcenter_enabled(wf):
    # type: (Workflow3) -> bool
    return wf.settings['hubs'][ChartCenterClient.NAME]['enabled']


def is_artifacthub_enabled(wf):
    # type: (Workflow3) -> bool
    return wf.settings['hubs'][ArtifactHubClient.NAME]['enabled']
