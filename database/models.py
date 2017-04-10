from sqlalchemy.orm import mapper

from database.tableMapper import contractionUrl
from database.databaseSetting import db_session


class ContractionUrl(object):
    query = db_session.query_property()

    def __init__(self, registeredUrl=None, visitsNumber=0):
        self.registeredUrl = registeredUrl
        self.visitNumber = visitsNumber

    def __repr__(self):
        return '<Issue %r>' % self.registeredUrl

mapper(ContractionUrl, contractionUrl)
