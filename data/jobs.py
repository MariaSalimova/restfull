import sqlalchemy
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session, relation
import sqlalchemy.ext.declarative as dec
from data.db_session import SqlAlchemyBase
from datetime import datetime


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=True)
    team_leader = sqlalchemy.Column(sqlalchemy.ForeignKey('users.id'), nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String(1000), nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    leader = orm.relation('User')
