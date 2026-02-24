import re

from playwright.sync_api import expect
from .base import BaseMethod





class AverageIncomeCalcs(BaseMethod):

    def input_text(self, locator, func_text_output=None, text_input=""):

        expect(locator).to_be_visible(timeout=10000)
        old_value = locator.input_value()
        locator.fill(text_input)
        if func_text_output:
            ouput = func_text_output(text_input)
            text_output = ouput if ouput != "no_change" else old_value
        else:
            text_output = text_input
        expect(locator).to_have_value(re.compile(rf"^{text_output}"))

    def add_income_field(self, locator_add, locator_field, timeout=5000):
        expect(locator_field.first).to_be_visible(timeout=timeout)
        initial_count = locator_field.count()
        self.click_element(locator_add)
        expect(locator_field).to_have_count(initial_count + 2, timeout=timeout)

    def fill_income(self, locator_add, locator_field, data_income):

        self.add_income_field(locator_add, locator_field)
        name, value = data_income
        self.input_text(locator_field.nth(-2), text_input=name)
        self.input_text(
            locator_field.nth(-1),
            text_input=value,
            func_text_output=self.text_output_income,
        )

    def delete_income_field(self, locator, index=-1, timeout=5000):
        expect(locator.first).to_be_visible(timeout=timeout)
        initial_count = locator.count()
        self.click_element(locator, index=index)
        expect(locator).to_have_count(initial_count - 1, timeout=timeout)

    def get_result(self, locator):
        raw_text = locator.inner_text()
        return "".join(filter(str.isdigit, raw_text)) or 0

    def text_output_family(self, text_input):
        digits = "".join(filter(str.isdigit, str(text_input)))

        if not digits or int(digits) <= 0:
            return ""
        return digits[:2]

    def text_output_income(self, text_input):
        digits = "".join(filter(str.isdigit, str(text_input)))

        if not digits or int(digits) <= 0:
            return ""
        if len(digits) > 7:
            return "no_change"
        return f"{int(digits):,}".replace(",", "\u00a0")

    def change_stepper(self, locator_field, locator_step, action="increase"):
        old_text = locator_field.input_value()
        old_num = int(self.text_output_family(old_text) or 0)

        target_num = old_num + 1 if action == "increase" else old_num - 1

        expected_value = self.text_output_family(str(target_num))

        locator_step.first.click()

        try:
            expect(locator_field).to_have_value(
                re.compile(rf"^{expected_value}"), timeout=1000
            )
        except AssertionError:
            locator_step.first.click()
            expect(locator_field).to_have_value(re.compile(rf"^{expected_value}"))
