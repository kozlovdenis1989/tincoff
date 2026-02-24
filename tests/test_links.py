import pytest
from pages.links import Links
from data.urls import JOURNAL_MAIN
from data.data_test import DataTestLinks



@pytest.mark.parametrize("link_name, expected_url, current_text", DataTestLinks.MENU_ITEMS)
def test_link_navigation_menu(page, link_name, expected_url, current_text):

    obj = Links(page)
    obj.open(JOURNAL_MAIN)

    container = obj.get_locator(role="navigation", role_name="Разделы", exact=True)
    locator_link = obj.get_locator(role="link", container=container, role_name=link_name)

    response = obj.click_link_get_response(locator=locator_link)
    
    assert response.status == 200
    obj.check_url(expected_url)
    obj.check_text(text=current_text, root_locator="h1")







    













    


    
    
   
   