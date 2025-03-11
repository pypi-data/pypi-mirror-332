#!/usr/bin/python3
"""Tests for package log utility functions"""

import logging
import os
import sys
from pathlib import PurePath

# noinspection PyUnresolvedReferences
from pytest_mock import mocker

os.chdir(os.path.dirname(__file__))
sys.path.append('../src')

# noinspection PyUnresolvedReferences
from maven_check_versions.logutils import (  # noqa: E402
    configure_logging, log_skip_if_required,
    log_search_if_required, log_invalid_if_required
)


# noinspection PyShadowingNames
def test_configure_logging(mocker):
    mock_logging = mocker.patch('logging.basicConfig')
    mocker.patch('builtins.open', mocker.mock_open(read_data='{}'))
    configure_logging({'logfile_off': False})
    mock_logging.assert_called_once_with(
        level=logging.INFO, handlers=[mocker.ANY, mocker.ANY],
        format='%(asctime)s %(levelname)s: %(message)s'
    )
    handlers = mock_logging.call_args[1]['handlers']
    assert isinstance(handlers[0], logging.StreamHandler)
    assert isinstance(handlers[1], logging.FileHandler)
    assert PurePath(handlers[1].baseFilename).name == 'maven_check_versions.log'
    mocker.stopall()


# noinspection PyShadowingNames
def test_log_skip_if_required(mocker):
    mock_logging = mocker.patch('logging.warning')
    args = {'show_skip': True}
    log_skip_if_required({}, args, 'group', 'artifact', '1.0')
    mock_logging.assert_called_once_with("Skip: group:artifact:1.0")


# noinspection PyShadowingNames
def test_log_search_if_required(mocker):
    args = {'show_search': True}
    mock_logging = mocker.patch('logging.warning')
    log_search_if_required({}, args, 'group', 'artifact', '${version}')
    mock_logging.assert_called_once_with("Search: group:artifact:${version}")

    mock_logging = mocker.patch('logging.info')
    log_search_if_required({}, args, 'group', 'artifact', '1.0')
    mock_logging.assert_called_once_with("Search: group:artifact:1.0")


# noinspection PyShadowingNames
def test_log_invalid_if_required(mocker):
    mock_logging = mocker.patch('logging.warning')
    args = {'show_invalid': True}
    log_invalid_if_required({}, args, mocker.Mock(), 'group', 'artifact', '1.0', False)
    mock_logging.assert_called_once_with("Invalid: group:artifact:1.0")
