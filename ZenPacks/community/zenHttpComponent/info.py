from ZenPacks.community.ConstructionKit.ClassHelper import *

def HttpComponentgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class HttpComponentInfo(ClassHelper.HttpComponentInfo):
    ''''''

from ZenPacks.community.zenHttpComponent.datasources.HttpComponentDataSource import *
def HttpComponentRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(HttpComponentDataSource.onRedirectOptions)

def HttpComponentDataSourcegetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class HttpComponentDataSourceInfo(ClassHelper.HttpComponentDataSourceInfo):
    ''''''


