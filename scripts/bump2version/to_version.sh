#!/bin/bash#
# -*- coding: utf-8 -*-
version=$1  # 0.1.0
part=$2     # minor
bump_cmd="bump2version --new-version $version $part"

eval $bump_cmd
