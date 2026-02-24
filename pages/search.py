from playwright.sync_api import expect
from .base import BaseMethod


class SearchModule(BaseMethod):
    def input_text(self, locator, text_input=""):
        super().input_text(locator, text_input)
        locator.press("Enter")


    def check_value_in_field(self, locator, text_check):
        
        expect(locator).to_have_value(text_check)

    def check_text(self, text, root_locator="body", timeout=10000):
        expect(self.page.locator(root_locator)).to_contain_text(
            text, timeout=timeout, ignore_case=True
        )

    def check_rezult_search_positive(
        self, contains_text, role="heading", index=0, exact=False
    ):
        articles = self.page.get_by_role(role, level=4)
        articles.nth(index).click()
        self.check_text(text=contains_text)

    def check_rezult_search_count(self, role="heading", count=0):
        articles = self.page.get_by_role(role, level=4)
        expect(articles).to_have_count(count)