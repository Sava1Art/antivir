from drivers.driver_configuration import setup_driver


class BrowserActions:
    driver = None

    def go_to_url(self, url, full_screen=True):
        self.driver = setup_driver()
        self.driver.get(url=url)
        if full_screen:
            self.driver.fullscreen_window()

    def get_driver(self):
        return self.driver

    def close_page(self):
        self.driver.close()

    def close_browser(self):
        self.driver.quit()
