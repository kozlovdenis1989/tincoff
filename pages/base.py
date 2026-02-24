from playwright.sync_api import Page, expect


class BaseMethod:
    def __init__(self, page: Page):
        self.page = page

    def get_container_h(
        self, container_selector="div", container_text=None, header=None
    ):
        if header:
            selector = (
                f"{container_selector}:has({header}:has-text('{container_text}'))"
            )
        else:
            selector = f"{container_selector}:has-text('{container_text}')"

        return self.page.locator(selector).last

    def get_locator(
        self,
        container=None,
        role=None,
        role_name=None,
        placeholder=None,
        text=None,
        locator=None,
        exact=False,
    ):

        base = container if container else self.page
        if locator:
            return base.locator(locator)
        if placeholder:
            return base.get_by_placeholder(placeholder, exact=exact)

        if role:
            return base.get_by_role(role=role, name=role_name, exact=exact)
        if text:
            return base.get_by_text(text)

        return base

    def click_element(self, locator, index=0, exact=False, force=False):

        target_elem = locator.nth(index)
        expect(target_elem).to_be_visible(timeout=10000)
        target_elem.click(force=force)

    def click_role_link(self, role="link", name="", exact=False, timeout=10000):
        locator = self.page.get_by_role(role=role, name=name, exact=exact)
        expect(locator).to_be_visible(timeout=timeout)
        locator.click()

    def click_role_button(self, role="button", name="", exact=False, timeout=10000):
        locator = self.page.get_by_role(role=role, name=name, exact=exact)
        expect(locator).to_be_visible(timeout=timeout)
        locator.click()

    def get_text(self, locator):

        expect(locator.first).to_be_visible()
        return locator.first.inner_text()

    def input_text(self, locator, text_input=""):

        expect(locator).to_be_visible(timeout=10000)
        locator.fill(text_input)
        

    def open(self, url: str):
        self.page.goto(url)