#!/bin/sh

CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    touch $CONTAINER_ALREADY_STARTED
    echo "--------------------------- First container startup -----------------------------"
    flask db init
else
    echo "--========================= Not first container startup --======================="
fi

flask db migrate
flask db upgrade
