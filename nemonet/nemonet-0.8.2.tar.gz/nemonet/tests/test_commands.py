# Created by Jan Rummens at 12/01/2021
import unittest
import copy

from nemonet.runner.runner import Runner

import logging.config

logging.config.fileConfig(fname='../../vision_logger.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class CommandsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.config = {
            "driver": {
                "tool": "selenium",
                "tool_config": {
                    "webdriver": "chrome",
                    "webdriver_config": {
                        "headless": True,
                        "experimental_flags": [
                            "same-site-by-default-cookies@2",
                            "cookies-without-same-site-must-be-secure@2"],
                        "remote_settings": None
                    }
                }
            },
            "screen_recording": {
                "enable": False
            }
        }

        self.runner = Runner(config=self.config)

    def tearDown(self) -> None:
        # quit driver of runner that weren't used (didn't call execute_scenario)
        if not self.runner.driver.has_quit():
            self.runner.driver.quit()

    def remote_chrome(self):
        # Before running this test, make sure Selenium Grid has been set up locally
        # Then change the method name to "test_remote_chrome"
        remote_config = copy.deepcopy(self.config)
        remote_settings = {"command_executor": "http://127.0.0.1:4444"}
        remote_config["driver"]["tool_config"]["webdriver_config"]["remote_settings"] = remote_settings
        remote_runner = Runner(config=remote_config)

        remote_runner.execute_scenario("command-current-pos")

    def test_chrome_options(self):
        self.runner.execute_scenario("dummy")

    def test_chrome_headless_current_pos(self):
        headless_config = copy.deepcopy(self.config)
        headless_config["driver"]["tool_config"]["webdriver_config"]["headless"] = True
        headless_runner = Runner(config=headless_config)

        headless_runner.execute_scenario("command-current-pos")

    def test_save_records(self):
        self.runner.execute_scenario("commands-save-records")

    def test_double_click(self):
        self.runner.execute_scenario("commands-double-mouse-click")

    def test_drag_and_drop(self):
        self.runner.execute_scenario("commands-drag-and-drop")

    def test_drag_and_drop_mouse(self):
        self.runner.execute_scenario("commands-drag-and-drop-mouse")

    def test_drag_and_drop_offset(self):
        self.runner.execute_scenario("commands-drag-and-drop-offset")

    def test_explicit_waits(self):
        self.runner.execute_scenario("commands-explicit-waits")

    def test_remove_html_element(self):
        self.runner.execute_scenario("commands-remove-html-element")

    def test_right_mouse(self):
        self.runner.execute_scenario("command-right-mouse")

    def test_tabs(self):
        self.runner.execute_scenario("command-tabs")

    def test_current_pos(self):
        self.runner.execute_scenario("command-current-pos")

    def test_site_settings(self):
        # chrome only
        self.runner.execute_scenario("commands-site-settings")

    def test_open_formatted_url(self):
        self.runner.execute_scenario("commands-reformat-url")

    def test_tab_and_text(self):
        self.runner.execute_scenario("command-tab-and-text")

    def test_set_env(self):
        self.runner.execute_scenario("command-set-env")


if __name__ == '__main__':
    unittest.main()
