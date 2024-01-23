import unittest
from Selenium import webdriver

class TestDrivingSchoolApp(unittest.TestCase):

    def setUp(self):
        # Set up the Selenium WebDriver (assuming a Flask app is running locally)
        chrome_path = r"C:\Users\PC\Desktop\Driving School\chrome-win64\chrome.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_path)

    def tearDown(self):
        # Clean up after the test
        if self.driver:
            self.driver.quit()

    def test_booking_functionality(self):
        # Navigate to the booking page and perform some actions
        self.driver.get("http://127.0.0.1:5000/booking")

        # Example: Fill out the form
        self.driver.find_element_by_id("student_name").send_keys("John Doe")
        self.driver.find_element_by_id("lesson_type").send_keys("Introductory")
        self.driver.find_element_by_id("instructor_id").send_keys("1")

        # Submit the form
        self.driver.find_element_by_id("submit_button").click()

        success_message = self.driver.find_element_by_id("success_message").text
        self.assertEqual(success_message, "Booking successful!")

    def test_navigation(self):
        # Example: Test navigation to different pages
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element_by_id("link_to_booking").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/booking")

if __name__ == '__main__':
    unittest.main()
