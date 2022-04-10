import pytest


if __name__ == "__main__":
    # pytest.main(["-x", "test/home_page_test.py"])
    # pytest.main(["-v", "--junitxml=home_page_test.xml", "test/home_page_test.py"])
    # pytest.main(["-x", "test/fantastic_group_test.py"])
    # pytest.main(["-x", "test/save_search_data_test.py"])
    # pytest.main(["-v", "--junitxml=save_search_data_test.xml", "test/save_search_data_test.py"])
    # pytest.main(["-v", "--junitxml=save_search_work_one_file.xml", "test/save_search_work_one_file.py"])
    # pytest.main(["-x", "test/marketplace_test.py"])
    '''It start code marketplace. Must unput password'''
    # pytest.main(["-x", "test/marketplace_one_page_test.py"])
    '''It start code marketplace. no password'''
    pytest.main(["-x", "test/marketplace_one_page_test.py"])
    # pytest.main(["-x", "test/"])
    # ReadWriteTest.test_group()
    # pytest.main(["-k", "ReadWrite", "-v"])



