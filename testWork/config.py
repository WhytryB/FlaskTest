import os
basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    POSTGRES_URL = get_env_variable("POSTGRES_URL")
    POSTGRES_USER = get_env_variable("POSTGRES_USER")
    POSTGRES_PW = get_env_variable("POSTGRES_PW")
    POSTGRES_DB = get_env_variable("POSTGRES_DB")
    POSTGRES_PORT = get_env_variable("POSTGRES_PORT")
    if len(POSTGRES_PW) > 0:
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}:{port}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,
                                                                                      url=POSTGRES_URL,port=POSTGRES_PORT,
                                                                                      db=POSTGRES_DB)
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}@{url}:{port}/{db}'.format(user=POSTGRES_USER,
                                                                                 url=POSTGRES_URL,
                                                                                 port=POSTGRES_PORT,
                                                                                 db=POSTGRES_DB)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

