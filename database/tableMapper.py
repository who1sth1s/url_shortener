from sqlalchemy import Table, Column, Integer, String
from database.databaseSetting import meta_data

contractionUrl = Table('contractionUrl', meta_data,
                       Column('number', Integer, primary_key=True),
                       Column('registeredUrl', String(45)),
                       Column('visitsNumber', Integer)
                       )
