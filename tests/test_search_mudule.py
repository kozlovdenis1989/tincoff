import pytest
from urllib.parse import unquote
from pages.search import SearchModule
from data.urls import JOURNAL_MAIN
from data.data_test import DataTestSearch


@pytest.fixture()
def main_page(page):
    obj = SearchModule(page)
    obj.open(JOURNAL_MAIN)
    return obj


def search_input_text(main_page, input_text, contains_text):
    obj = main_page
    locator_search = obj.get_locator(role="button", role_name="Поиск")
    locator_search_text = obj.get_locator(role="searchbox", role_name="Поле поиска")

    obj.click_element(locator_search)
    obj.input_text(locator=locator_search_text, text_input=input_text)

    locator_search_text = obj.get_locator(role="textbox", role_name="Что вам найти?")
    
    obj.check_value_in_field(locator=locator_search_text, text_check=input_text)
    return {"obj": obj, "locator_search_text": locator_search_text}


@pytest.mark.parametrize("input_text, contains_text", DataTestSearch.POSITIVE_QUERIES)
def test_search_result_positive(main_page, input_text, contains_text):

    search_input = search_input_text(main_page, input_text, contains_text)
    locator_search_text = search_input["locator_search_text"]
    obj: SearchModule = search_input["obj"]

    obj.check_rezult_search_positive(contains_text=contains_text, index=0)
    obj.page.go_back()
    obj.check_value_in_field(locator=locator_search_text, text_check=input_text)
    obj.check_rezult_search_positive(contains_text=contains_text, index=-1)

    


@pytest.mark.parametrize("input_text, contains_text", DataTestSearch.NEGATIVE_QUERIES)
def test_search_result_negative_bad_params(main_page, input_text, contains_text):

    search_input = search_input_text(main_page, input_text, contains_text)
    obj: SearchModule = search_input["obj"]

    obj.check_rezult_search_count(count=0)
    obj.check_text(text=contains_text)


def test_search_paginator(main_page):

    
    search_input = search_input_text(main_page, *DataTestSearch.search_text)
    obj: SearchModule = search_input["obj"]
    obj.check_rezult_search_count(count=30)

    obj.click_role_link(name="3", exact=True)
    assert "page=3" in unquote(obj.page.url)

    obj.click_role_link(name="Следующая страница", exact=True)
    assert "page=4" in unquote(obj.page.url)

    obj.click_role_link(name="5", exact=True)
    assert "page=5" in unquote(obj.page.url)

    obj.click_role_link(name="Предыдущая страница", exact=True)
    assert "page=4" in unquote(obj.page.url)

    obj.click_role_link(name="1", exact=True)
    assert "q=ставка" in unquote(obj.page.url)