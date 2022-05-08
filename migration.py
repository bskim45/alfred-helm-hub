#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2022 Bumsoo Kim <bskim45@gmail.com>
#
# MIT Licence http://opensource.org/licenses/MIT

from __future__ import annotations

from workflow import Workflow3
from workflow.update import Version

from api import ChartCenterClient


def migrate(wf):
    # type: (Workflow3) -> None
    if not wf.last_version_run or wf.last_version_run == wf.version:
        return

    wf.logger.info(
        'Version upgraded: {0} -> {1}'.format(wf.last_version_run, wf.version)
    )

    if wf.last_version_run < Version('1.2.0'):
        migrate_to_1_2_0(wf)
        wf.logger.info('Migration to 1.2.0 complete')


def migrate_to_1_2_0(wf):
    # type: (Workflow3) -> None
    wf.settings['hubs'][ChartCenterClient.NAME]['enabled'] = False
    wf.settings.save()
