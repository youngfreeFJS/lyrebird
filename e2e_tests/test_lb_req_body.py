import os, sys, time, hashlib, base64, json, gzip, requests
from urllib import parse


curPath = os.path.abspath(os.path.dirname(__file__))


def setup_module():
    os.system("nohup python serve.py > /dev/null 2>&1 & ")
    os.system("nohup lyrebird -b > /dev/null 2>&1 & ")
    print("init serve")
    time.sleep(3)


def teardown_module():
    os.system(
        "ps -ef|grep serve.py | grep -v grep|awk '{printf $2}'|xargs kill -9"
    )
    os.system(
        "ps -ef|grep lyrebird | grep -v grep|awk '{printf $2}'|xargs kill -9"
    )
    print("teardown")

serve_uri = "http://127.0.0.1:5000/e2e_serve"
mock_uri = "http://127.0.0.1:9090/mock/"
uri = mock_uri + serve_uri


class TestSuite:
    def test_img_data(self):
        print("==============================================")
        print(requests.post(serve_uri,data="1").status_code)
        print(requests.post(serve_uri,data="1").text)
        print(requests.post(uri,data="1").status_code)
        print(requests.post(uri,data="1").text)
    