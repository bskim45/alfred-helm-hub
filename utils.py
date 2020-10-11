#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2020 Bumsoo Kim <bskim45@gmail.com>
#
# MIT Licence http://opensource.org/licenses/MIT

from __future__ import print_function, unicode_literals

from workflow import Workflow3

HELM_HUB_NAME = 'hub.helm.sh'
CHARTCENTER_NAME = 'chartcenter.io'


def create_workflow():
    # type: () -> Workflow3
    wf = Workflow3(
        default_settings={
            'hubs': {
                HELM_HUB_NAME: {
                    'enabled': True,
                    'icon': 'icons/hub.png'
                },
                CHARTCENTER_NAME: {
                    'enabled': True,
                    'icon': 'icons/chartcenter.png'
                }
            }
        },
        update_settings={
            'github_slug': 'bskim45/alfred-helm-hub',
            'frequency': 7,  # a week
        })
    wf.settings.save()
    return wf


def is_hub_enabled(wf):
    # type: (Workflow3) -> bool
    return wf.settings['hubs'][HELM_HUB_NAME]['enabled']


def is_chartcenter_enabled(wf):
    # type: (Workflow3) -> bool
    return wf.settings['hubs'][CHARTCENTER_NAME]['enabled']
