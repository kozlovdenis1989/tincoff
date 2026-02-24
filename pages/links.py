from playwright.sync_api import expect

from .base import BaseMethod


class Links(BaseMethod):

    def click_link_get_response(
        self, locator=None, timeout=10000, exact=False
    ):
        
        with self.page.expect_navigation(
            wait_until="domcontentloaded", timeout=timeout
        ) as response_info:
            locator.click()

        return response_info.value
    
    def check_url(self, url, timeout=10000):
        expect(self.page).to_have_url(url, timeout=timeout)

    def check_text(self, text, root_locator="body", timeout=10000):
        expect(self.page.locator(root_locator)).to_contain_text(
            text, timeout=timeout, ignore_case=True
        )