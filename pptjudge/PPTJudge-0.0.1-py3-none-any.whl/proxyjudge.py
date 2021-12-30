#    DATE: 28 DEC 2021 - Today
#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# LICENSE: AGPL3.0
# RELEASE: 0.1.1

import flask

app = flask.Flask(__name__)


@app.route('/ip', methods=['GET'])
def index_ip():
    if flask.request.method == 'GET':
        return flask.jsonify(flask.request.remote_addr)


@app.route('/judge', methods=['GET'])
def index_judge():
    return flask.jsonify(ip=flask.request.remote_addr,
                         headers=headers_proxy_check(flask.request.headers))


def headers_proxy_check(headers):
    _headers = {}
    for item_header in headers:
        _headers.update({item_header[0]: item_header[1]})
    return _headers


# app.run(host='0.0.0.0', port=5000, debug=True)

def run():
    print("HELLO WORLD!!!")