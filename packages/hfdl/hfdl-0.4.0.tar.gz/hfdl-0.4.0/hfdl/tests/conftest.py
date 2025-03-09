import pytest
from unittest.mock import Mock
from huggingface_hub import HfApi
from pathlib import Path
import tempfile
import shutil

@pytest.fixture
def mock_api():
    """Create a mock HfApi instance that can be shared across tests"""
    api = Mock(spec=HfApi)
    return api

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files"""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    # Cleanup after test
    shutil.rmtree(temp_path)

@pytest.fixture
def real_model_repo():
    """Real model repository for testing"""
    return {
        'id': "MaziyarPanahi/Qwen2.5-7B-Instruct-GGUF",
        'url': "https://huggingface.co/MaziyarPanahi/Qwen2.5-7B-Instruct-GGUF",
        'type': "model"
    }

@pytest.fixture
def real_dataset_repo():
    """Real dataset repository for testing"""
    return {
        'id': "Anthropic/hh-rlhf",
        'url': "https://huggingface.co/datasets/Anthropic/hh-rlhf",
        'type': "dataset"
    }

@pytest.fixture
def fake_repos():
    """Fake repositories for testing error cases"""
    return {
        'model': {
            'id': "fake-user/nonexistent-model",
            'url': "https://huggingface.co/fake-user/nonexistent-model",
            'type': "model"
        },
        'dataset': {
            'id': "fake-user/nonexistent-dataset",
            'url': "https://huggingface.co/datasets/fake-user/nonexistent-dataset",
            'type': "dataset"
        }
    }

@pytest.fixture
def sample_repo_files():
    """Sample repository file list for testing"""
    return [
        "README.md",
        "config.json",
        "model.bin",
        "tokenizer.json",
        "vocab.txt"
    ]

@pytest.fixture
def sample_file_sizes():
    """Sample file sizes for testing (in bytes)"""
    return {
        "README.md": 1024,  # 1KB
        "config.json": 2048,  # 2KB
        "model.bin": 200 * 1024 * 1024,  # 200MB
        "tokenizer.json": 50 * 1024,  # 50KB
        "vocab.txt": 150 * 1024 * 1024  # 150MB
    }

def pytest_configure(config):
    """Configure pytest for our tests"""
    # Add markers for different test types
    config.addinivalue_line(
        "markers",
        "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers",
        "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers",
        "slow: mark test as a slow test"
    )

@pytest.fixture(autouse=True)
def setup_logging():
    """Configure logging for tests"""
    import logging
    logging.basicConfig(level=logging.DEBUG)
    yield
    # Reset logging after test
    logging.getLogger().handlers = []