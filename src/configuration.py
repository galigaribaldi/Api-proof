"""
Configuration
-------------
Archivo de configuraciones para cada etapa del proyecto
"""
class BaseConfig():
    """Configuración de tipo Base en la cual se ponen los siguientes parametros::
    
        | 1.- Secret key
        | 2.- Debug
        | 3.- Testing
        | 4.- SqlAlchemy Database URI
        | 5.- SqlAlchemy Track Modifications
    """
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgres://nnckmgzasylosx:99b170dfe60bb4771b0ac9edf19939df386bc88cf1222aa7fe69ce6446a4a254@ec2-44-196-68-164.compute-1.amazonaws.com:5432/ddaui1ic2hdida"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    """Configuración de producción
    
    Parameters
    -----------
    BaseConfig : class
        Configuración base
    """
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    """Configuración de Desarrollo
    
    Parameters
    -----------
    BaseConfig : class
        Configuración base
    """
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'