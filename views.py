from flask import Flask, request
from service.url.urlRegister import UrlRegister
from service.url.urlAccess import UrlAccess
from service.url.urlStats import UrlStats

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    request_data = _make_request_data(request)
    result = UrlRegister(request_data).execute()

    return result


@app.route('/<int:url_number>', methods=['GET'])
def access(url_number):
    request_data = _make_request_data(request)
    result = UrlAccess(request_data, url_number).execute()

    return result


@app.route('/<int:url_number>/stats', methods=['GET'])
def stats(url_number):
    request_data = _make_request_data(request)
    result = UrlStats(request_data, url_number).execute()

    return result


@app.errorhandler(404)
def page_not_found(error):

    return '404 Page Not Found', 404


def _make_request_data(request):

    if request.method == 'GET':
        request_data = dict(request.args)
        request_data['method'] = request.method

    else:
        request_data = request.get_json(force=True)
        request_data['method'] = request.method

    return request_data


if __name__ == '__main__':
    app.run(port=3000, threaded=True, debug=True)
