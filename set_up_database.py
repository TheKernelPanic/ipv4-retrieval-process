from repository.session import Base, engine
from repository.model import IpV4

Base.metadata.create_all(engine)
