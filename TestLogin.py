import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test case is run.
        Initialize a Firefox webdriver, define the URL, username, and password.
        """
        self.driver = webdriver.Firefox()
        self.url = "https://editor.giscloud.com/"
        self.username = "Edin_Jugo"
        self.password = "Realmadrid12"

    def test_login_success(self):
        """
        Test a successful login by entering valid credentials and verifying the result.
        """
        self.driver.get(self.url)

        # Get form elements
        email = self.driver.find_element(By.ID, "loginField")
        password = self.driver.find_element(By.NAME, 'password')

        # Set values
        email.send_keys(self.username)
        password.send_keys(self.password)

        # Click the login button
        self.driver.find_element(By.ID, "loginSubmitButton").click()

        # Verify that the page was loaded successfully
        button_create_new_map = self.driver.find_element(By.ID, "hp_create_map")
        assert button_create_new_map.text == 'Create New Map'

    def test_login_failed(self):
        """
        Test a failed login by entering incorrect credentials and verifying the error message.
        """
        self.driver.get(self.url)

        # Get form elements
        email = self.driver.find_element(By.ID, "loginField")
        password = self.driver.find_element(By.NAME, 'password')

        # Set values
        email.send_keys(self.username)
        password.send_keys("wrongpassword")

        # Click the login button
        self.driver.find_element(By.ID, "loginSubmitButton").click()

        # Verify the error message
        login_failed_msg = self.driver.find_element(By.XPATH, "//*[@class='message error']")
        assert login_failed_msg.text == "Username or password is incorrect."

    def tearDown(self):
        """
        Clean up after each test case by quitting the webdriver.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
