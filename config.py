
class BaseConfig(object):
    """ Base config class. This fields will use by production and development server """

    ORIGINS = ["*"]
    SECRET_KEY = '4)-.W\xad\x80\x97`\x8e\xc1\xcd\x10\xd7\x11\xd6\x00\xf7M\x89\x18\xceCg'


class Development(BaseConfig):
    """ Development config. We use Debug mode """

    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    APPNAME = "OpenMonitoringDev"

class Production(BaseConfig):
    """ Production config. We use Debug mode false """

    PORT = 8080
    DEBUG = False
    TESTING = False
    ENV = 'production'
    APPNAME = "OpenMonitoringProd"

