from sqlalchemy import Column, Integer, String, DateTime
from repository.session import Base
import datetime


class IpV4(Base):
    __tablename__ = 'ip_v4'

    id = Column(Integer, primary_key=True)
    ip = Column(String(15), nullable=False, unique=True)
    provider = Column(String(120), nullable=False)
    service_type = Column(String(120), nullable=True)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, ip, provider, service_type):
        self.ip = ip
        self.provider = provider
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'IpV4({self.ip}, {self.provider})'

    def __str__(self):
        return self.ip
