import pytest
from parse_validation import parse_validation_save_data


@pytest.fixture
def json_input():
    return[
        {'formula': '343.3 != ""',
        'metadata': {'validation': 'Value present',
        'reference': '70001',
        'period': '201912',
        'survey': '003',
        'validationid': 23412,
        'bpmid': ''},
        'triggered': True},
        {'formula': '12.3 != ""',
        'metadata': {'validation': 'Value present',
        'reference': '70001',
        'period': '201912',
        'survey': '003',
        'validationid': 23413,
        'bpmid': ''},
        'triggered': True}]


@pytest.fixture
def json_output():
    return {'validation_outputs':
        [{'formula': '343.3 != ""',
        'triggered': True,
        'validation': 'Value present',
        'reference': '70001',
        'period': '201912',
        'survey': '003',
        'validationid': 23412,
        'bpmid': '',
        'instance': 0},
        {'formula': '12.3 != ""',
        'triggered': True,
        'validation': 'Value present',
        'reference': '70001',
        'period': '201912',
        'survey': '003',
        'validationid': 23413,
        'bpmid': '',
        'instance': 0}]}


def test_output_data(json_input, json_output):
    returned_data = parse_validation_save_data(json_input)
    print('return', returned_data)
    assert returned_data == json_output
