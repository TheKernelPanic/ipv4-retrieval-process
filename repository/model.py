from sqlalchemy import Column, Integer, String, DateTime
from repository.session import Base
import datetime


class IpV4(Base):
    __tablename__ = 'ip_v4'

    id = Column(Integer, primary_key=True)
    ip = Column(String(15), nullable=False, unique=True)
    provider = Column(String(120), nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, ip, provider):
        self.ip = ip
        self.provider = provider
        self.created_at = datetime.datetime.now()

    def __repr__(self) -> str:
        return f'IpV4({self.ip}, {self.provider})'

    def __str__(self) -> Column:
        return self.ip
