from django.urls import path
from . import views

urlpatterns = [
    path('download', views.download, name='download'),
    path('count', views.count, name='count'),

    #CASE CONVERTER

    path('', views.caseConverter, name='caseConverter'),
    path('upperCase', views.upperCase, name='upperCase'),
    path('lowerCase', views.lowerCase, name='lowerCase'),
    path('sentanceCase', views.sentanceCase, name='sentanceCase'),
    path('titleCase', views.titleCase, name='titleCase'),
    path('swapCase', views.swapCase, name='swapCase'),
    path('camelCase', views.camelCase, name='camelCase'),
    path('snakeCase', views.snakeCase, name='snakeCase'),
    path('kebabCase', views.kebabCase, name='kebabCase'),
    path('pascalCase', views.pascalCase, name='pascalCase'),
    path('upperSnakeCase', views.upperSnakeCase, name='upperSnakeCase'),

    #ASCII CONVERTER
    path('ascii-text-converter', views.asciiConverter, name='asciiConverter'),
    path('asciiConversion', views.asciiConversion, name='asciiConversion'),

    #Binary CONVERTER
    path('binary-text-converter', views.binaryConverter, name='binaryConverter'),
    path('binaryConversion', views.binaryConversion, name='binaryConversion'),

    #Octal CONVERTER
    path('octal-text-converter', views.octalConverter, name='octalConverter'),
    path('octalConversion', views.octalConversion, name='octalConversion'),

    #Hexadecimal CONVERTER
    path('hex-text-converter', views.hexConverter, name='hexConverter'),
    path('hexConversion', views.hexConversion, name='hexConversion'),

    #Word Occurrence Counter
    path('word-occurrence', views.wordOccurrence, name='wordOccurrence'),
    path('word-occurrence-counter', views.wordOccurrenceCounter, name='wordOccurrenceCounter'),

    #Extract Email From Text
    path('extract-email', views.extractEmail, name='extractEmail'),
    path('emailExtractor', views.emailExtractor, name='emailExtractor'),

    # Extract URLS From Text
    path('extract-urls', views.extractUrl, name='extractUrl'),
    path('urlExtractor', views.urlExtractor, name='urlExtractor'),

    # Extract Phone Numbers From Text
    path('extract-phone-nos', views.extractPhoneno, name='extractPhoneno'),
    path('phonenoExtractor', views.phonenoExtractor, name='phonenoExtractor'),

    #Find Subtext From Text
    path('find-subtext', views.findSubText, name='findSubText'),
    path('subTextFinder', views.subTextFinder, name='subTextFinder'),

    #Replace Subtext From Text
    path('replace-subtext', views.replaceSubText, name='replaceSubText'),
    path('subTextReplacer', views.subTextReplacer, name='subTextReplacer'),

]
