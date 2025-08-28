from core.components import BaseComponent


class BaseDashboardComponent(BaseComponent):
    title_name: str

    def __init__(self):
        class_name = "oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget"
        locator = f'//div[@class="{class_name}" and .//p[contains(., "{self.title_name}")]]'
        super().__init__(locator)