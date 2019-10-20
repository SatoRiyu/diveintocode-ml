#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

echo $SCRIPT_DIR

cd $SCRIPT_DIR/WORK_UI

for qrc_file in *.qrc ; do
    pyrcc5 -o ../${qrc_file%.qrc}_rc.py ../UI/$qrc_file
    mv $qrc_file done/
done
