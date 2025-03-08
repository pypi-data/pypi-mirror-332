# ruff: noqa: F811
from __future__ import annotations

import os
import pytest
from fitrequest.method_config import MethodConfig
from fixtures import config, config_with_url, config_with_auto_version, Config
from importlib.metadata import version
from fitrequest.errors import UnexpectedNoneBaseURLError


def test_client_name(config_with_url):
    assert config_with_url.client_name == 'client_with_url'


def test_config_without_base_url(config):
    with pytest.raises(UnexpectedNoneBaseURLError):
        assert config.session.request(MethodConfig(name='test', endpoint='/'))


@pytest.mark.asyncio
async def test_async_config_without_base_url(config):
    with pytest.raises(UnexpectedNoneBaseURLError):
        assert await config.session.async_request(MethodConfig(name='test', endpoint='/'))


def test_base_url(config_with_url):
    assert str(config_with_url.base_url) == 'https://test.skillcorner'


def test_base_url_set_as_environment_variable(config):
    os.environ['CLIENT_BASE_URL'] = 'https://downloadmoreram.com/'
    assert str(config.base_url) == 'https://downloadmoreram.com/'
    os.environ.pop('CLIENT_BASE_URL')


def test_client_version(config, config_with_url, config_with_auto_version):
    assert config.version == '0.0.1'
    assert config_with_url.version == '{version}'
    assert config_with_auto_version.version == version('fitrequest')


def test_forbidden_extra_attributes():
    with pytest.raises(ValueError):
        Config(cowsay='moooh')
