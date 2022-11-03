#!/bin/bash#
# -*- coding: utf-8 -*-


build_cmd="poetry run mkdocs build -d ./mkdocs_site -c "
eval $build_cmd
