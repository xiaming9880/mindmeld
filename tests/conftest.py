# -*- coding: utf-8 -*-

"""
conftest
----------------------------------

Configurations for tests. Include shared fixtures here.
"""
# pylint: disable=locally-disabled,redefined-outer-name
from __future__ import unicode_literals

import os

import pytest
import codecs

from mmworkbench.tokenizer import Tokenizer
from mmworkbench.query_factory import QueryFactory
from mmworkbench.resource_loader import ResourceLoader

APP_NAME = 'kwik_e_mart'
APP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), APP_NAME)
AENEID_FILE = 'aeneid.txt'
AENEID_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), AENEID_FILE)


@pytest.fixture
def lstm_entity_config():
    return {
        'model_type': 'tagger',
        'label_type': 'entities',

        'model_settings': {
            'classifier_type': 'lstm',

            'tag_scheme': 'IOB',
            'feature_scaler': 'max-abs'

        },
        'params': {
            'number_of_epochs': 1
        },
        'features': {
            'in-gaz-span-seq': {},
        }
    }


@pytest.fixture
def kwik_e_mart_app_path():
    return APP_PATH


@pytest.fixture
def tokenizer():
    """A tokenizer for normalizing text"""
    return Tokenizer()


@pytest.fixture
def query_factory(tokenizer):
    """For creating queries"""
    return QueryFactory(tokenizer)


@pytest.fixture
def resource_loader(query_factory):
    """A resource loader"""
    return ResourceLoader(APP_PATH, query_factory)


@pytest.fixture
def aeneid_path():
    return AENEID_PATH


@pytest.fixture
def aeneid_content(aeneid_path):
    with codecs.open(aeneid_path, mode='r', encoding='utf-8') as f:
        return f.read()
