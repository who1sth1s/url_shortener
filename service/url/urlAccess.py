from database.databaseSetting import db_session
from database.models import ContractionUrl


class UrlAccess:

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

            return {
                'error': {
                    'message': 'no registered url'
                }
            }

        registered_url = contraction_url_information.registeredUrl
        ContractionUrl.query.filter(ContractionUrl.number == self.url_number).update({'visitsNumber': ContractionUrl.visitsNumber + 1})
        db_session.commit()

        return {
            'registered_url': registered_url
        }
