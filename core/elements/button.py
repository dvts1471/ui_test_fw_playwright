from core.elements import BaseElement


class Button(BaseElement):
    element_type = 'button'

    def __init__(self, role='button', name=None, text=None, locator=None, test_id=None):
        super().__init__(
            role=role,
            name=name,
            text=text,
            locator=locator,
            test_id=test_id
        )