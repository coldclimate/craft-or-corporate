#!/usr/bin/env bash
set -eux
python build.py
export content=$(cat output.html)
sed "s#@@MAIN_CONTENT@@#$content#g" template.html > index.html
mv index.html ../output/
