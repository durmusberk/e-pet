import vet_operations

# Pytest is used to run the test


def test_invalid_search_pet():
    assert vet_operations.search_pet(123123123123) == -1
