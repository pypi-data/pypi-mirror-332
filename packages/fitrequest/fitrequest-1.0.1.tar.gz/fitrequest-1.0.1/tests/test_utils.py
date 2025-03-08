from __future__ import annotations

import sys
import pytest
import jinja2


from pydantic import BaseModel
from dataclasses import dataclass

from unittest.mock import patch, MagicMock
from fitrequest.decorators import retry
from fitrequest.utils import extract_method_params, string_varnames, format_url


def test_extract_method_params():
    def hello(name: str, team: str) -> str:
        return f'Hello! My name is {name}, and I work on the {team} team.'

    assert extract_method_params(hello, {'name': 'lucien', 'team': 'dev', 'age': 33}) == {
        'name': 'lucien',
        'team': 'dev',
    }
    assert extract_method_params(hello, {'name': 'lucien', 'age': 33}) == {'name': 'lucien'}


def test_string_varnames():
    jinja_env = jinja2.Environment(
        variable_start_string='{',
        variable_end_string='}',
        autoescape=True,  # ruff S701
    )

    assert string_varnames(jinja_env, 'Hello {name}, do you have the {amount} € you owe me ?') == {'name', 'amount'}
    assert string_varnames(jinja_env, 'Hey, No') == set()

    with pytest.raises(jinja2.exceptions.TemplateSyntaxError):
        string_varnames(jinja_env, 'Late fees are going up by {}%.')


def test_format_url():
    assert format_url('https://toto.com///index.html') == 'https://toto.com/index.html'
    assert format_url('https://toto.com//index.html') == 'https://toto.com/index.html'
    assert format_url('https://toto.com/index.html') == 'https://toto.com/index.html'
    assert format_url('https://toto.com') == 'https://toto.com'
