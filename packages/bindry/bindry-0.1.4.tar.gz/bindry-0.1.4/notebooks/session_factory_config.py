from dataclasses import dataclass


@dataclass
class SessionFactoryConfig:
    SQLALCHEMY_POSTGRESQL_DATABASE_URI: str
