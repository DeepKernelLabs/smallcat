import pytest


@pytest.fixture
def local_conn(tmp_path):
    conn = {"conn_type": "fs", "extra": {"base_path": str(tmp_path)}}
    return conn
