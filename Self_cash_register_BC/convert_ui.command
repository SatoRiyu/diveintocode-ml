#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

echo $SCRIPT_DIR

cd $SCRIPT_DIR/WORK_UI
for ui_file in *.ui ; do
    pyuic5 -o ../UI/${ui_file%.ui}.py ../UI/$ui_file
    mv $ui_file done/
done
