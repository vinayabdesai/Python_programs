import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

#creating a simple test case for checking login of  a page
class TestEYPage(unittest.TestCase):		

	def setUp(self):
		self.driver = webdriver.Firefox()
		#self.driver.set_page_load_timeout(30)
		self.driver.implicitly_wait(20)
		self.driver.get("http://www.ey.com/")
		#self.driver.maximize_window()
		
		
	def test_page(self):
		driver = self.driver
		print" Title = ",driver.title
		try:
			WebDriverWait(driver, 3).until(EC.alert_is_present(),
												'Timed out waiting for PA creation ' +
												'confirmation popup to appear.')

			alert = driver.switch_to.alert()
			alert.accept()
			print "alert accepted"
		except TimeoutException:
			print "no alert"

		#window_before = driver.window_handles[0]
		#print window_before

		#driver.find_elements(By.TAG_NAME,'a')
		driver.find_element_by_link_text("Insights").click()
		
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "insights-recent-insights")))
		#time.sleep(20)
		print "Next page titlr = ",driver.title
		for handle in driver.window_handles:
			print handle
			
		#window_after = driver.window_handles[0]
		#driver.switch_to_window(window_after)
		#print window_after

		items = driver.find_elements_by_tag_name('a')
		for item in items:
			print item.text.encode('utf-8')
			print "Href =", item.get_attribute("href")
			if(item.text.encode('utf-8') == 'Browse by topic'):
				print " YES"
				item.click()
				break
			
			
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()	