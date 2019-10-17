import pytest
import json
from parse_validation import parse_validation_save_data


@pytest.fixture
def input_data():
    [{'formula': '343.3 != ""',
    'metadata': {'validation': 'Value present',
    'reference': '70001',
    'period': '201912',
    'survey': '003',
    'validationid': 23412,
    'bpmid': ''},
    'triggered': 'true'},
    {'formula': '12.3 != ""',
    'metadata': {'validation': 'Value present',
    'reference': '70001',
    'period': '201912',
    'survey': '003',
    'validationid': 23413,
    'bpmid': ''},
    'triggered': 'true'}]


@pytest.fixture
def output_data():
    {'validation_outputs':
    [{'formula': '343.3 != ""',
    'triggered': 'true',
    'validation': 'Value present',
    'reference': '70001',
    'period': '201912',
    'survey': '003',
    'validationid': 23412,
    'bpmid': ''},
    {'formula': '12.3 != ""',
    'triggered': 'true',
    'validation': 'Value present',
    'reference': '70001',
    'period': '201912',
    'survey': '003',
    'validationid': 23413,
    'bpmid': ''}]}

def test_output_data(input_data, output_data):
    returned_data = parse_validation_save_data(input_data)
    assert  returned_data == output_data
