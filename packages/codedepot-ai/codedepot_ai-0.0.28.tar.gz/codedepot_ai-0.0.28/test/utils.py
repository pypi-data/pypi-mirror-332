import pytest
import py
import os

from ai.api import create_provider
from ai.config import AIConfig

# Define a fixture that returns the path to your resource file
@pytest.fixture
def provider_test():
    res_file = py.path.local(__file__).dirpath(os.path.join('resources', 'provider_test.yaml'))
    return res_file.strpath

@pytest.fixture
def cluster_test():
    res_file = py.path.local(__file__).dirpath(os.path.join('resources', 'cluster_test.yaml'))
    return res_file.strpath

@pytest.fixture
def config():
    res_file = py.path.local(__file__).dirpath(os.path.join('resources', 'config.json'))
    return AIConfig.from_file(res_file.strpath)
