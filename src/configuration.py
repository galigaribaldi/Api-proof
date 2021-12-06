class BaseConfig(object):
    """Baseconfig

    Parameters
    ----------
    object : [type]
        [description]
    """
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgres://nnckmgzasylosx:99b170dfe60bb4771b0ac9edf19939df386bc88cf1222aa7fe69ce6446a4a254@ec2-44-196-68-164.compute-1.amazonaws.com:5432/ddaui1ic2hdida"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'