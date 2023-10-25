from pydantic import Field
from pydantic_settings import BaseSettings


class Base(BaseSettings):
    driver: str = Field(..., alias='driver')
    db_dir: str = Field('', alias='db_dir')
    db_file: str = Field('', alias='db_file')
    mysql_dsn: str = Field('', alias='mysql_dsn')
    postgres_dsn: str = Field('', alias='postgres_dsn')

    class Config:
        env_file = '.env'


class GenericSettings(Base):
    def __init__(self, env: str = 'pdl'):
        if env == '':
            raise Exception('Invalid env value')
        if env == 'pdl':
            env = env + '_'
        else:
            env = 'pdl_' + env + '_'
        super().__init__(_env_prefix=env)


class DevSettings(GenericSettings):
    def __init__(self):
        super().__init__('development')


class TestSettings(GenericSettings):
    def __init__(self):
        super().__init__('test')


class ProdSettings(GenericSettings):
    def __init__(self):
        super().__init__('production')
