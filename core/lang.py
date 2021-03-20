# -*- coding: utf-8 -*-
"""This core module handles functions related to multi-language.

The fundamental of this module depends on Flask-Language, a 
Flask extension that makes handling a client-side language 
cookie easier.

Note:
    For more information, please visit:
    https://flask-language.readthedocs.io/en/latest/

"""

import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
from flask import current_app
from flask_language import Language, current_language

LANGS_PATH = './langs'

lang = Language()
allowed_langs = []
lang_dict = {}

def init_lang(app):
    """The function initializes `lang` with the provided context.

    Args:
        app (flask.app.Flask): A Flask application

    """
    lang.init_app(app)

    # Load language packs from LANGS_PATH
    langs_list = [l.split('.')[0] for l in listdir(LANGS_PATH) if isfile(join(LANGS_PATH, l))]
    for lang_name in langs_list:
        load_lang(lang_name)


def load_lang(name):
    tree = ET.parse(join(LANGS_PATH, name+'.xml'))
    root = tree.getroot()
    current_dict = {}
    for s in root.iter('string'):
        current_dict[s.attrib['name']] = s.text
    allowed_langs.append(name)
    lang_dict[name] = current_dict


def get_str(key, language=None):
    if language is None:
        # When lang is None, use the default language
        language = current_app.config['DEFAULT_LANGUAGE']

    # Not default language
    if lang_dict.get(language, None) is not None and language is not current_app.config['DEFAULT_LANGUAGE']:
        string = lang_dict[language].get(key, None)
        if string is not None:
            return string
        current_app.logger.warning(f'Key "{key}" is not implemented in {language}.xml.')
    
    # Use default language
    language = current_app.config['DEFAULT_LANGUAGE']
    if lang_dict.get(language, None) is not None:
        string = lang_dict[language].get(key, None)
        if string is not None:
            return string
        else:
            current_app.logger.warning(f'Key "{key}" is not implemented in {language}.xml.')
            return ''
    else:
        current_app.logger.critical(f'Default language {language} is not found.')
    
    return ''


@lang.allowed_languages
def get_allowed_languages():
    return allowed_langs


@lang.default_language
def get_default_language():
    return current_app.config['DEFAULT_LANGUAGE']


if __name__ == '__main__':
    
    print(lang_dict)