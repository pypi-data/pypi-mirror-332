import sys
from unittest.mock import MagicMock

import httpx
import pytest
import respx
from typer.testing import CliRunner

from tests.demo_cli import RestApiClient, client_cli

runner = CliRunner()


@pytest.fixture
def cli_database() -> dict:
    return {
        'items': {
            1: {'item_id': 1, 'item_name': 'ball', 'detail_id': 11},
            2: {'item_id': 2, 'item_name': 'gloves', 'detail_id': 22},
        },
        'details': {
            11: {
                'detail_id': 11,
                'detail': 'Durable ball made from soft synthetic leather with wider seams and bright colors',
            },
            22: {
                'detail_id': 22,
                'detail': (
                    'Small, light, made from soft material that fits snugly. Textured fingertips provide excellent grip'
                ),
            },
        },
    }


def mock_requests(cli_database):
    item_list = list(cli_database['items'].values())
    respx.get(
        f'{client_cli.base_url}/items/',
    ).mock(return_value=httpx.Response(200, json=item_list))

    for item in cli_database['items'].values():
        item_id = item['item_id']
        detail_id = item['detail_id']
        detail = cli_database['details'][detail_id]

        respx.get(
            f'{client_cli.base_url}/items/{item_id}',
        ).mock(return_value=httpx.Response(200, json=item))

        respx.get(
            f'{client_cli.base_url}/items/{item_id}/details/{detail_id}',
        ).mock(return_value=httpx.Response(200, json=item | detail))


@respx.mock
def test_get_items(cli_database):
    mock_requests(cli_database)

    # Test methods
    assert [elem.model_dump() for elem in client_cli.get_items()] == [
        {'item_id': 1, 'item_name': 'ball', 'detail_id': 11},
        {'item_id': 2, 'item_name': 'gloves', 'detail_id': 22},
    ]

    # Test CLI
    result = runner.invoke(client_cli.cli_app(), ['get-items'])
    assert result.exit_code == 0
    assert 'ball' in result.stdout
    assert 'gloves' in result.stdout


@respx.mock
def test_get_item(cli_database):
    mock_requests(cli_database)

    # Test methods
    assert client_cli.get_item(item_id=1).model_dump() == {'item_id': 1, 'item_name': 'ball', 'detail_id': 11}
    assert client_cli.get_item(item_id=2).model_dump() == {'item_id': 2, 'item_name': 'gloves', 'detail_id': 22}

    # Test CLI
    result = runner.invoke(client_cli.cli_app(), ['get-item', '1'])
    assert result.exit_code == 0
    assert 'ball' in result.stdout

    result = runner.invoke(client_cli.cli_app(), ['get-item', '2'])
    assert result.exit_code == 0
    assert 'gloves' in result.stdout


@respx.mock
def test_get_item_details(cli_database):
    mock_requests(cli_database)

    # Test methods
    assert client_cli.get_item_details(item_id=1, detail_id=11).model_dump() == {
        'item_id': 1,
        'item_name': 'ball',
        'detail_id': 11,
        'detail': 'Durable ball made from soft synthetic leather with wider seams and bright colors',
    }
    assert client_cli.get_item_details(item_id=2, detail_id=22).model_dump() == {
        'item_id': 2,
        'item_name': 'gloves',
        'detail_id': 22,
        'detail': 'Small, light, made from soft material that fits snugly. Textured fingertips provide excellent grip',
    }

    # Test CLI
    result = runner.invoke(client_cli.cli_app(), ['get-item-details', '1', '11'])
    cleaned_output = result.stdout.replace('\n', ' ').replace('  ', ' ')

    assert result.exit_code == 0
    assert 'ball' in cleaned_output
    assert 'Durable ball made from soft synthetic leather with wider seams and bright colors' in cleaned_output

    result = runner.invoke(client_cli.cli_app(), ['get-item-details', '2', '22'])
    cleaned_output = result.stdout.replace('\n', ' ').replace('  ', ' ')

    assert result.exit_code == 0
    assert 'gloves' in cleaned_output
    assert (
        'Small, light, made from soft material that fits snugly. Textured fingertips provide excellent grip'
        in cleaned_output
    )


@respx.mock
def test_get_details(cli_database):
    mock_requests(cli_database)

    # Test methods
    assert [elem.model_dump() for elem in client_cli.get_details()] == [
        {
            'item_id': 1,
            'item_name': 'ball',
            'detail_id': 11,
            'detail': 'Durable ball made from soft synthetic leather with wider seams and bright colors',
        },
        {
            'item_id': 2,
            'item_name': 'gloves',
            'detail_id': 22,
            'detail': (
                'Small, light, made from soft material that fits snugly. Textured fingertips provide excellent grip'
            ),
        },
    ]

    # Test CLI
    result = runner.invoke(client_cli.cli_app(), ['get-details'])
    cleaned_output = result.stdout.replace('\n', ' ').replace('  ', ' ')

    assert result.exit_code == 0
    assert 'ball' in cleaned_output
    assert 'gloves' in cleaned_output
    assert 'Durable ball made from soft synthetic leather with wider seams and bright colors' in cleaned_output
    assert (
        'Small, light, made from soft material that fits snugly. Textured fingertips provide excellent grip'
        in cleaned_output
    )


@respx.mock
def test_cli_request_error(cli_database):
    err_msg = 'Item not found!'

    respx.get(
        f'{client_cli.base_url}/items/3',
    ).mock(return_value=httpx.Response(404, text=err_msg))

    mock_requests(cli_database)

    # Test methods
    with pytest.raises(httpx.HTTPError) as err:
        client_cli.get_item(item_id=3)

    assert str(err.value) == err_msg

    # Test CLI
    result = runner.invoke(client_cli.cli_app(), ['get-item', '3'])
    assert result.exit_code == 1
    assert err_msg in result.stdout


def test_cli_run():
    RestApiClient.cli_app = MagicMock()
    RestApiClient.cli_run()
    RestApiClient.cli_app.assert_called()
