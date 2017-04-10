from flask import Flask, request
from service.url.urlRegister import UrlRegister
from service.url.urlAccess import UrlAccess
from service.url.urlStats import UrlStats

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    request_data = request.get_json(force=True)
    result = UrlRegister(request_data).execute()

    return result


@app.route('/<int:url_number>', methods=['GET'])
def access(url_number):
    request_args = dict(request.args)
    result = UrlAccess(request_args, url_number).execute()

    return result


@app.route('/<int:url_number>/stats', methods=['GET'])
def stats(url_number):
    request_args = dict(request.args)
    result = UrlStats(request_args, url_number).execute()

    return result

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
