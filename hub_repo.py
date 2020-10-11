#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2020 Bumsoo Kim <bskim45@gmail.com>
#
# MIT Licence http://opensource.org/licenses/MIT

from __future__ import print_function, unicode_literals

import sys

from utils import create_workflow
from workflow import Workflow3


def list_repo(wf):
    # type: (Workflow3) -> None
    hubs = wf.settings['hubs'].viewitems()

    for name, conf in hubs:
        wf.add_item(
            title=name,
            subtitle='Enabled' if conf['enabled'] else 'Disabled',
            arg=name,
            valid=True,
            icon=wf.workflowfile(conf['icon'])
        )

    wf.send_feedback()


def toggle_repo(wf, repo_name):
    # type: (Workflow3, str) -> None
    log = wf.logger
    log.info('toggle repo: "%s"', repo_name)

    prev_enabled = wf.settings['hubs'][repo_name]['enabled']
    wf.settings['hubs'][repo_name]['enabled'] = not prev_enabled

    wf.settings.save()

    print('{} is {}'.format(
        repo_name, 'disabled' if prev_enabled else 'enabled'))


def main(wf):
    # type: (Workflow3) -> None
    if len(wf.args) == 2 and wf.args[0] == 'repo' and wf.args[1] == 'list':
        list_repo(wf)
    elif len(wf.args) == 3 and wf.args[0] == 'repo' and wf.args[1] == 'toggle':
        toggle_repo(wf, wf.args[2])
    else:
        pass


if __name__ == '__main__':
    wf = create_workflow()
    sys.exit(wf.run(main))
