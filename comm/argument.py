from enum import Enum, unique


@unique
class Argument(Enum):
    """
    'dev', #开发环境
    'production' :生产环境
    local : 本地环境
    
    apps: 所有app集合名称
    """
    Local = 'local'
    Dev = 'dev'
    Production = 'production'
    Apps = 'apps'

environment = Argument.Local.value

apps = Argument.Apps.value
