import json

import pandas as pd
import pyarrow as pa
import pytest
import yaml

from smallcat.catalog import Catalog
from smallcat.datasets.csv_dataset import CSVDataset


@pytest.fixture
def example_catalog(local_conn):
    return {
        'entries': {
            'foo': {
                'connection': local_conn,
                'file_format': 'csv',
                'location': 'foo.csv',
                'load_options': {'header': True},
                'save_options': {'header': True},
            },
            'bar': {
                'connection': 'local_connection',
                'file_format': 'excel',
                'location': 'my_spreadsheets/bar.xlsx',
                'load_options': {'header': True},
                'save_options': None,
            }
        }
    }


def test_catalog_dict(example_catalog, example_df):
    catalog = Catalog.from_dict(example_catalog)
    dataset = catalog.get_dataset('foo')
    assert isinstance(dataset, CSVDataset)
    with pytest.raises(KeyError):
        catalog.get_dataset('missing_key')

    catalog.save_pandas('foo', example_df)
    loaded_df = catalog.load_pandas('foo')

    filtered_df = catalog.load_pandas('foo', where="amount > 10")
    expected_filtered = example_df[example_df["amount"] > 10].reset_index(drop=True)

    loaded_arrow = catalog.load_arrow('foo', where="amount > 10")
    assert isinstance(loaded_arrow, pa.Table)
    arrow_filtered_df = loaded_arrow.to_pandas().reset_index(drop=True)

    pd.testing.assert_frame_equal(example_df, loaded_df)
    pd.testing.assert_frame_equal(expected_filtered, filtered_df.reset_index(drop=True))
    pd.testing.assert_frame_equal(expected_filtered, arrow_filtered_df)


def test_catalog_yaml(example_catalog, tmp_path):
    catalog_path = tmp_path / 'catalog.yaml'
    with catalog_path.open("w") as f:
        yaml.dump(example_catalog, f)

    # Check with Pathlib
    catalog = Catalog.from_yaml(catalog_path)
    dataset = catalog.get_dataset('foo')
    assert isinstance(dataset, CSVDataset)

    # Check with string path
    catalog = Catalog.from_yaml(str(catalog_path))
    dataset = catalog.get_dataset('foo')
    assert isinstance(dataset, CSVDataset)



def test_catalog_airflow_var(example_catalog, local_conn, monkeypatch):
    monkeypatch.setenv("AIRFLOW_VAR_EXAMPLE_CATALOG", json.dumps(example_catalog))

    catalog = Catalog.from_airflow_variable('example_catalog')
    dataset = catalog.get_dataset('foo')
    assert isinstance(dataset, CSVDataset)
    with pytest.raises(KeyError):
        catalog.get_dataset('missing_key')

    monkeypatch.setenv("AIRFLOW_CONN_LOCAL_CONNECTION", json.dumps(local_conn))
    dataset = catalog.get_dataset('bar')

    with pytest.raises(KeyError):
        catalog = Catalog.from_airflow_variable("missing_catalog")
