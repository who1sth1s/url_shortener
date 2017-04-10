from database.databaseSetting import db_session
from database.models import ContractionUrl


class UrlRegister:

    def __init__(self, request):
        self.request = request

    def execute(self):
        result = getattr(self, self.request.get('method').lower())()

        db_session.close()

        return result

    def post(self):
        register_url = self.request.get('url')

        if register_url is None:

            return {
                'error': {
                    'message': 'url is null'
                }
            }

        # 0 is visit count
        registered_url = self._get_duplicate_registered_url(register_url)
        status_code = 200

        if registered_url is None:
            create_data = [register_url, 0]
            table_information = ContractionUrl(*create_data)

            db_session.add(table_information)
            db_session.commit()

            registered_url = 'http://localhost:3000/' + str(table_information.number)
            status_code = 201

        return {
            'url': registered_url,
        }, status_code

    def _get_duplicate_registered_url(self, register_url):
        registered_url_data = ContractionUrl.query.filter(ContractionUrl.registeredUrl == register_url).first()

        if registered_url_data is not None:
            registered_url = 'http://localhost:3000/' + str(registered_url_data.number)

            return registered_url

        return None
