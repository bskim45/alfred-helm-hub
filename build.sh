#!/usr/bin/env bash

WORKFLOW_NAME=alfred-helm-hub.alfredworkflow

SCRIPT_HOME=$(dirname "$(realpath "$0")")
echo "Home path: $SCRIPT_HOME"

cd "$SCRIPT_HOME/alfred-workflow/workflow"
git clean -nx

read -p "Continue? " -n 1 -r
echo    # new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git clean -fx
fi

cd "$SCRIPT_HOME" || exit
rm -f $WORKFLOW_NAME
zip -r $WORKFLOW_NAME -@ < includes.list
