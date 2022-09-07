#!/usr/bin/env bash
export DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
python ${DIR}/build.py
export content=$(cat ${DIR}/output.html)
sed "s#@@MAIN_CONTENT@@#$content#g" ${DIR}/template.html > ${DIR}/index.html
mv ${DIR}/index.html ../output/
