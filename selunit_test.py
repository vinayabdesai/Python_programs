import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#creating a simple test case for checking login of  a page
class TestLogin(unittest.TestCase):		

	def setUp(self):
		self.driver = webdriver.Firefox()
		
	#this test should work unless network connectivity fails
	def test_getpage(self):
		driver = self.driver
		driver.get('http://seleniumhq.org/')
		driver.maximize_window()
		self.assertEqual(driver.title,"Selenium - Web Browser Automation")
		
		link = driver.find_element_by_link_text('Documentation')
		link.send_keys(Keys.RETURN)
		print("Title =", driver.title)
		
		ele = driver.find_element_by_name("q")
		ele.clear()
		ele.send_keys("python Selenium")
		ele.send_keys(Keys.RETURN)
		print("Title =", driver.title)
		
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()