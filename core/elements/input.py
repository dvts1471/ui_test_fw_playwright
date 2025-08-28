from core.elements import BaseElement


class Input(BaseElement):
    element_type = 'input'

    def __init__(self, role='textbox', name=None, text=None, locator=None, test_id=None):
        super().__init__(
            role=role,
            name=name,
            text=text,
            locator=locator,
            test_id=test_id
        )

    def fill(self, text):
        self.wait_element_visible()
        self.clear()
        self.element.fill(text)
        self.logger.debug(f'Fill {self.__class__.__name__}({self.locator}) "{text}"')


    def clear(self):
        self.logger.debug(f"Clear {self.__class__.__name__}({self.locator})")
        self.element.click()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Delete')
