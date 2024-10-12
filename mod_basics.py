from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


# create an instance of metadata
metadata = MetaData()

db = SQLAlchemy(metadata = metadata)

class User(db.Mode1):
    pass