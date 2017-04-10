from database.databaseSetting import db_session
from database.models import ContractionUrl


class UrlStats:

    def __init__(self, request, url_number):
        self.request = request
        self.url_number = url_number

    def execute(self):
        result = getattr(self, self.request.get('method').lower())()
        db_session.close()

        return result

    def get(self):
        contraction_url_information = ContractionUrl.query.filter(ContractionUrl.number == self.url_number).first()

        if contraction_url_information is None:
            result = {
                'error': {
                    'message': 'no registered url'
                }
            }

            return result, 400

        visits_number = contraction_url_information.visitsNumber

        return {
            'visit': visits_number
        }, 200
