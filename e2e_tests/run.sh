#!/usr/bin/env bash

source ../venv/bin/activate

pytest -v -s ./test_lb_req_body.py
