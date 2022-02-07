import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('username', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column('password', sqlalchemy.String, primary_key=True),
    sqlalchemy.Column('register_date', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean),
)