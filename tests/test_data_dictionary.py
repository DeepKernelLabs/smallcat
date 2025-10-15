# import pytest

# from data_dictionary import DataDictionary


# @pytest.fixture
# def example_dictionary(local_conn):
#     return {
#         'entries': {
#             'foo': {
#                 'connection': local_conn,
#                 'file_format': 'csv',
#                 'load_options': {'header': True},
#                 'save_options': None,
#             }
#         }
#     }


# def test_data_dictionary_dict(example_dictionary):
#     dictionary = DataDictionary.from_dict(example_dictionary)
#     loader = dictionary.get_data_loader('foo')
#     assert isinstance(loader, CSVLoader)
#     with pytest.raises(KeyError):
#         dictionary.get_data_loader('missing_key')
