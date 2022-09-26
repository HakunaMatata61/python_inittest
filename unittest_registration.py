from selenium import webdriver
from selenium.webdriver.common.by import By
import time, unittest

class TestAbs(unittest.TestCase):

    def test_registration(self):
    
        link = "http://suninjuly.github.io/registration1.html"
    
        browser = webdriver.Chrome()
        browser.get(link)

        # Input user firstname
        input_first_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        print(input_first_name)
        input_first_name.send_keys("Ivan")

        # Input user lastname
        input_last_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        print(input_last_name)
        input_last_name.send_keys("Petrov")

        # Input user email
        input_email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        print(input_email)
        input_email.send_keys("test@test.com")

        # Send request
        button = browser.find_element_by_xpath('/html/body/div/form/button')
        button.click()

        # Timeout 1 second    
        time.sleep(1)

        # Choose element with text
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Test registration
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
