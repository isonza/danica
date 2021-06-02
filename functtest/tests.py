from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import time

MAX_WAIT = 10


class BagongClientTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	#def tearDown(self):
		#self.browser.quit()


	def wait_para_sa_row_in_list_table(self, row_text):
		start_time = time.time()

	def test_gawa_list_para_sa_one_user(self):
		html = self.browser.find_element_by_tag_name('html')
		head = self.browser.find_element_by_tag_name('head')
		body = self.browser.find_element_by_tag_name('body')

		self.browser.get(self.live_server_url)
		self.assertIn('Shinee Smiles: Book Dental Appointment', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Book Dental Appointment', header_text)

		p1 = self.browser.find_element_by_id('p1').text
		self.assertIn('Fill up this form first then we will contact you once your schedule is confirmed', p1)
		l1 = self.browser.find_element_by_id('fullname').text
		self.assertIn('Full Name:', l1)

		name = self.browser.find_element_by_id('name')  
		self.assertEqual(name.get_attribute('placeholder'),'Enter Full Name')
		name = self.browser.find_element_by_id('name').send_keys("Danica Isonza")
		time.sleep(2)

		l2 = self.browser.find_element_by_id('emailaddress').text
		self.assertIn('Email Address:', l2)
		email = self.browser.find_element_by_id('email')  
		self.assertEqual(email.get_attribute('placeholder'),'Enter Email Address')
		email = self.browser.find_element_by_id('email').send_keys("entmt.danicaisonza@gmail.com")
		time.sleep(2)

		l3 = self.browser.find_element_by_id('contactnumber').text
		self.assertIn('Contact Number:', l3)
		contact = self.browser.find_element_by_id('contact')  
		self.assertEqual(contact.get_attribute('placeholder'),'Enter Contact Number')
		contact = self.browser.find_element_by_id('contact').send_keys("09128126166")
		time.sleep(2)
		
		l4 = self.browser.find_element_by_id('fulladdress').text
		self.assertIn('Full Address:', l4)
		address = self.browser.find_element_by_id('address')  
		self.assertEqual(address.get_attribute('placeholder'),'Enter Full Address')
		address = self.browser.find_element_by_id('address').send_keys("B4 L28 San Miguel 2 Dasma Cavite")
		time.sleep(2)

		p2 = self.browser.find_element_by_id('p2').text
		self.assertIn('(Note: Dental clinic is open every Thursday and Saturday only. Regular holidays are excluded)', p2)
		l5 = self.browser.find_element_by_id('scheduledate').text
		self.assertIn('Schedule Date:', l5)
		date = self.browser.find_element_by_id('date')  
		self.assertEqual(date.get_attribute('placeholder'),'Enter Desired Date')
		date = self.browser.find_element_by_id('date').send_keys("2021-04-29")
		time.sleep(3)

		p3 = self.browser.find_element_by_id('p3').text
		self.assertIn('(Note: Dental clinic hours is from 10AM to 4PM only. Please be reminded that maximum of 2hrs is only alloted for brace and denture procedures)', p3)
		l6 = self.browser.find_element_by_id('scheduletime').text
		self.assertIn('Schedule Time:', l6)
		clock = self.browser.find_element_by_id('clock')  
		self.assertEqual(clock.get_attribute('placeholder'),'Enter Desired Time')
		clock = self.browser.find_element_by_id('clock').send_keys("2PM")
		time.sleep(2)


		booknow = self.browser.find_element_by_id('booknow')
		self.assertEqual(booknow.get_attribute('onclick'),'myFunction()')
		booknow.click()
		time.sleep(1)

		BookPage = self.browser.current_url
		self.assertRegex(BookPage, '/book/')
		self.browser.quit()


	def test_pangalawang_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Shinee Smiles: Book Dental Appointment', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Book Dental Appointment', header_text)

		p1 = self.browser.find_element_by_id('p1').text
		self.assertIn('Fill up this form first then we will contact you once your schedule is confirmed', p1)
		l1 = self.browser.find_element_by_id('fullname').text
		self.assertIn('Full Name:', l1)

		name = self.browser.find_element_by_id('name')  
		self.assertEqual(name.get_attribute('placeholder'),'Enter Full Name')
		name = self.browser.find_element_by_id('name').send_keys("Danica Isonza")
		time.sleep(2)

		l2 = self.browser.find_element_by_id('emailaddress').text
		self.assertIn('Email Address:', l2)
		email = self.browser.find_element_by_id('email')  
		self.assertEqual(email.get_attribute('placeholder'),'Enter Email Address')
		email = self.browser.find_element_by_id('email').send_keys("entmt.danicaisonza@gmail.com")
		time.sleep(2)

		l3 = self.browser.find_element_by_id('contactnumber').text
		self.assertIn('Contact Number:', l3)
		contact = self.browser.find_element_by_id('contact')  
		self.assertEqual(contact.get_attribute('placeholder'),'Enter Contact Number')
		contact = self.browser.find_element_by_id('contact').send_keys("09128126166")
		time.sleep(2)
		
		l4 = self.browser.find_element_by_id('fulladdress').text
		self.assertIn('Full Address:', l4)
		address = self.browser.find_element_by_id('address')  
		self.assertEqual(address.get_attribute('placeholder'),'Enter Full Address')
		address = self.browser.find_element_by_id('address').send_keys("B4 L28 San Miguel 2 Dasma Cavite")
		time.sleep(2)

		p2 = self.browser.find_element_by_id('p2').text
		self.assertIn('(Note: Dental clinic is open every Thursday and Saturday only. Regular holidays are excluded)', p2)
		l5 = self.browser.find_element_by_id('scheduledate').text
		self.assertIn('Schedule Date:', l5)
		date = self.browser.find_element_by_id('date')  
		self.assertEqual(date.get_attribute('placeholder'),'Enter Desired Date')
		date = self.browser.find_element_by_id('date').send_keys("2021-04-29")
		time.sleep(3)

		p3 = self.browser.find_element_by_id('p3').text
		self.assertIn('(Note: Dental clinic hours is from 10AM to 4PM only. Please be reminded that maximum of 2hrs is only alloted for brace and denture procedures)', p3)
		l6 = self.browser.find_element_by_id('scheduletime').text
		self.assertIn('Schedule Time:', l6)
		clock = self.browser.find_element_by_id('clock')  
		self.assertEqual(clock.get_attribute('placeholder'),'Enter Desired Time')
		clock = self.browser.find_element_by_id('clock').send_keys("2PM")
		time.sleep(2)


		booknow = self.browser.find_element_by_id('booknow')
		self.assertEqual(booknow.get_attribute('onclick'),'myFunction()')
		booknow.click()
		time.sleep(1)

		BookPage = self.browser.current_url
		self.assertRegex(BookPage, '/book/')
		self.browser.quit()

"""
		alert = self.browser.find_element_by_id('alert')
		self.assertIn('Hello my dear client.\nPlease wait for the confirmation of your schedule. Always wear your mask and face shields before entering the clinic.\nStay safe. God Bless!', alert)
		self.assertEqual(alert.get_attribute('function'),'alert')
		alertmessage.click()
		time.sleep(5)

table = self.browser.find_element_by_id('listTable')
		row = table.find_elements_by_tag_name('tr')
"""
		

