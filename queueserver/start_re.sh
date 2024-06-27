#! /bin/sh

qserver-list-plans-devices  --startup-script ./00-start.py
/usr/local/bin/start-re-manager  --startup-script=./00-start.py --existing-plans-devices=./existing_plans_and_devices.yaml --user-group-permissions=./user_group_permissions.yaml --zmq-data-proxy-addr zmq-proxy:5568 --redis-addr redis:6379 --zmq-publish-console ON --keep-re
#/usr/local/bin/start-re-manager  --startup-script=./00-start.py --existing-plans-devices=./existing_plans_and_devices.yaml --user-group-permissions=./user_group_permissions.yaml --zmq-data-proxy-addr bliss_data:5577 --redis-addr redis:6379 --zmq-publish-console ON --keep-re
