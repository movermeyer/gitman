"""pytest configuration."""
# pylint:disable=E1101

import os

import pytest
import yorm


ROOT = os.path.dirname(__file__)
FILES = os.path.join(ROOT, 'files')


def pytest_runtest_setup(item):
    """pytest setup."""
    if 'integration' in item.keywords:
        yorm.settings.fake = False
    else:
        yorm.settings.fake = True
