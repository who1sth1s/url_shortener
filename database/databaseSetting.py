from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql://who1sth1s:kjrlove69@10.211.55.24/url_shortener?charset=utf8', convert_unicode=True)
meta_data = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def init_db():
    meta_data.create_all(bind=engine)
