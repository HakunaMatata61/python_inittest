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
        unittest.TestCase().assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # Timeout for test result of script
        time.sleep(5)
        # Close browser
        browser.quit()

   
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Input user firstname
        input_user_first_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        print(input_user_first_name)
        input_user_first_name.send_keys("Mikolka")

        # Input user email
        input_user_email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        #input3 = browser.find_element(by='class name', value='form-control.city')
        print(input_user_email)
        input_user_email.send_keys("test@test.com")
    
        # Send request
        button = browser.find_element_by_xpath('/html/body/div/form/button')
        button.click()

        # Timeout 1 second    
        time.sleep(1)

        # Choose element with text
        welcome_text_elt2 = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt2.text

        # Test registration
        unittest.TestCase().assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # Timeout for test result of script
        time.sleep(5)
        # Close browser
        browser.quit()

if __name__ == "__main__":
    unittest.main()
