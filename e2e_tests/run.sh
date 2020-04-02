#!/usr/bin/env bash

source ../venv/bin/activate

nohup python serve.py > /dev/null 2>&1 & 

nohup lyrebird -b > /dev/null 2>&1 & 

sleep 3

pytest -v -s 

ps -ef|grep serve.py | grep -v grep|awk '{printf $2}'|xargs kill -9

ps -ef|grep lyrebird | grep -v grep|awk '{printf $2}'|xargs kill -9
