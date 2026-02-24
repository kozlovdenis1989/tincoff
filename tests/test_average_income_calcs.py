import pytest
import re
from playwright.sync_api import expect
from data.urls import UrlsNav
from data.data_test import DataTestAverageIncomeCalcs as d
from pages.avarage_income import AverageIncomeCalcs


@pytest.fixture()
def calc_page(page):
    obj = AverageIncomeCalcs(page)
    obj.open(UrlsNav.JOURNAL_CALCULS)
    locator_element = obj.get_locator(role="link", role_name="калькулятор среднедушевого дохода")
    obj.click_element(locator_element)
    locator_res = obj.get_locator(locator="div[class*='_result_']")
    return obj, locator_res




def field_family_period(calc_page, container_text, data):
    obj, _ = calc_page

    container_field = obj.get_container_h(container_selector='div[class^="_inner_"]', container_text=container_text)
 

    locator_field = obj.get_locator(container=container_field, placeholder="0")
    locator_plus = obj.get_locator(container=container_field, role="button", role_name="+1", exact=True)
    locator_minus = obj.get_locator(container=container_field, role="button", role_name="-1", exact=True)
    

    for item in data:

        obj.input_text(locator=locator_field, text_input=item, func_text_output=obj.text_output_family)

        obj.change_stepper(locator_field=locator_field, locator_step=locator_plus, action="increase")
        obj.change_stepper(locator_field=locator_field, locator_step=locator_minus, action="decrease")


def field_income(calc_page,container_text, data):
    obj, locator_res = calc_page

    

    container_field = obj.get_container_h(container_selector='div[class^="_inner_"]', container_text=container_text)

    locator_add_income = container_field.get_by_text("добавить еще доход")
    locator_delete = container_field.locator('button[class*="_deleteBtn_"]')
    locator_month = container_field.get_by_text("В месяц")

    locator_all_period = container_field.get_by_text("За весь период")

    locator_field = obj.get_locator(container=container_field, role="textbox", role_name="")
    
    for item in data:
        obj.fill_income(locator_add_income, locator_field, item) 
    
    obj.delete_income_field(locator_delete, index=-3)


    result = obj.get_result(locator_res)
    obj.click_element(locator_all_period)
    assert result != obj.get_result(locator_res)
    obj.click_element(locator_month)
    assert result == obj.get_result(locator_res)
    
    

def field_other_income(calc_page, container_text, data):
    obj, locator_res = calc_page 
    container_field = obj.get_container_h(container_selector='div[class^="_header_"]', container_text=container_text)
    locator_click = obj.get_locator(container=container_field, role="button", role_name="open block")
    locator_click.first.press("Enter")
  
    field_income(calc_page, container_text=container_text, data=data)




def test_field_family(calc_page):
    field_family_period(calc_page, d.header_family, d.data_test_family_period)
    

def test_field_period(calc_page):
    field_family_period(calc_page, d.header_period, d.data_test_family_period)


def test_field_your_income(calc_page):
    field_income(calc_page, container_text=d.header_your, data=d.data_test_income)


def test_field_wife_husband_income(calc_page):
    field_other_income(calc_page=calc_page, container_text=d.header_husband, data=d.data_test_income)
    
    

def test_field_child_income(calc_page):

    field_other_income(calc_page=calc_page, container_text=d.header_child, data=d.data_test_income)
    

def test_e_2_e(calc_page):

    obj, locator_rez = calc_page

    field_family_period(calc_page, d.header_family, d.data_test_family_period)
    field_family_period(calc_page, d.header_period, d.data_test_family_period)
    field_income(calc_page, container_text=d.header_your, data=d.data_test_income)
    field_other_income(calc_page=calc_page, container_text=d.header_husband, data=d.data_test_income)
    field_other_income(calc_page=calc_page, container_text=d.header_child, data=d.data_test_income)
    
    expect(locator_rez).to_have_text(re.compile(d.result))