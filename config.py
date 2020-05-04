class Config:
    SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/project_we_facilito'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
