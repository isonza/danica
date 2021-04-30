from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from appointment.views import MainPage
from django.urls import resolve
#For Models testing
from appointment.models import Item, User


	#Refactored
class IndexTest(TestCase):

	def html_index_root_mainpage_yung_html(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

		
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')


		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'mainpage.html')
		self.assertIn('<title>Shinee Smiles: Book Dental Appointment</title>', html)
		self.assertIn('<h1>Book Dental Appointment</h1>', html)
		self.assertIn('<p1 id="p1">Fill up this form first then we will contact you once your schedule is confirmed</p1>', html)
		self.assertIn('<label id="fullname"><b>Full Name:</b></label>', html)
		self.assertIn('<input type="text" name="name" id="name" placeholder="Enter Full Name" required>', html)
		self.assertIn('<label id="emailaddress"><b>Email Address:</b></label>', html)
		self.assertIn('<input type="text" name="email" id="email" placeholder="Enter Email Address" required>', html)
		self.assertIn('<label id="fulladdress"><b>Full Address:</b></label>', html)
		self.assertIn('<input type="text" name="address" id="address" placeholder="Enter Full Address" required>', html)
		self.assertIn('<label id="scheduledate"><b>Schedule Date:</b></label>', html)
		self.assertIn('<input type="Date" name="date" id="date" placeholder="yyyy-mm-dd" value="" min="2021-04-29" max="2022-04-30" required>', html)
		self.assertIn('<p2 id="p2" style="font-size: 13px">(Note: Dental clinic is open every Thursday and Saturday only. Regular holidays are excluded)</p2>', html)		
		self.assertIn('<label id="scheduletime"><b>Schedule Time:</b></label>', html)
		self.assertIn('<input type="text" name="clock" id="clock" placeholder="Enter Desired Time" required>', html)
		self.assertIn('<p3 id="p3" style="font-size: 13px">(Note: Dental clinic hours is from 10AM to 4PM only. Please be reminded that maximum of 2hrs is only alloted for brace and denture procedures)</p3>', html)	

		self.assertIn('<button id=booknow onclick="myFunction()">Book now</button>', html)
		self.assertTrue(html.strip().endswith('</html>'))
	

class LiveViewTest(TestCase):

	def test_uses_list_template(self):
		client = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	def test_uses_home_template(self):
		response = self.client.get('/book/')
		self.assertTemplateUsed(response, 'bookpage.html')
	def test_displays_all_list_items(self):
		client = User.objects.create()
		name = Item.objects.create(name='name')
		email = Item.objects.create(email='email')
		contact = Item.objects.create(contact='contact')
		address = Item.objects.create(address='address')
		date = Item.objects.create(date='2000-10-08')
		clock = Item.objects.create(clock='clock')
		response = self.client.get('/')
		self.assertIn('name', response.content.decode())
		self.assertIn('email', response.content.decode())
		self.assertIn('contact', response.content.decode())
		self.assertIn('address', response.content.decode())
		self.assertIn('date', response.content.decode())
		self.assertIn('clock', response.content.decode())
		name = Item.objects.create(name='name')
		email = Item.objects.create(email='email')
		contact = Item.objects.create(contact='contact')
		address = Item.objects.create(address='address')
		date = Item.objects.create(date='2000-10-08')
		clock = Item.objects.create(name='clock')
		self.assertEqual(Item.objects.count(), 12)


class Models(TestCase):
	def modelo(self,
		client="test1",
		name="test2",
		email="test3",
		contact="test4",
		address="test5",
		date="test6",
		clock="test7"):

		return User.objects.create()
		return Item.objects.create(
			client="client",
			name="name",
			email="email",
			contact="contact",
			address="address",
			date="2000-10-08",
			clock="clock", )

	def test_whatever_creation(self):
		w=self.modelo()
		self.assertTrue(isinstance(w, User))
		self.assertFalse(isinstance(w, Item))


class ORM_First_Input(TestCase):
	def test_savings(self):

		item_ = Item()
		item_.save()


		l1 = Item()
		l1.name = 'Danica Isonza'
		l1.item_ = item_
		l1.save()
		l2 = Item()
		l2.email = 'entmt.danicaisonza@gmail.com'
		l2.item_ = item_
		l2.save()
		l3 = Item()
		l3.contact = '09128126166'
		l3.item_ = item_
		l3.save()
		l4 = Item()
		l4.address = 'B4 L28 San Miguel 2 Dasma Cavite'
		l4.item_ = item_
		l4.save()
		l5 = Item()
		l5.date = '2021-04-29'
		l5.item_ = item_
		l5.save()
		l6 = Item()
		l6.clock = '2PM'
		l6.save()

		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 7)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]		
		self.assertEqual(l1.name, 'Danica Isonza')
		self.assertEqual(l2.email, 'entmt.danicaisonza@gmail.com')
		self.assertEqual(l3.contact, '09128126166')
		self.assertEqual(l4.address, 'B4 L28 San Miguel 2 Dasma Cavite')
		self.assertEqual(l5.date, '2021-04-29')
		self.assertEqual(l6.clock, '2PM')


class Views(TestCase):
	def setUp(self):
		name = Item.objects.create()
		email = Item.objects.create() 
		contact = Item.objects.create()
		address = Item.objects.create()
		date = Item.objects.create()
		clock = Item.objects.create()

		Item.objects.create(
			name = 'Danica Isonza',
			email = 'entmt.danicaisonza@gmail.com',
			contact =  '09128126166',
			address = 'B4 L28 San Miguel 2 Dasma Cavite',
			date = '2021-04-29',
			clock = '2PM',
			)
		self.client.post('book/')

	def test_second_html_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/book/')
		self.assertTemplateUsed(response, 'bookpage.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertIn('<meta charset="UTF-8">', html)
		self.assertTrue(html.strip().endswith('</html>'))


	def test_get(self):
		name = Item.objects.get(name = 'Danica Isonza')
		email = Item.objects.get(email = 'entmt.danicaisonza@gmail.com') 
		contact = Item.objects.get(contact =  '09128126166')
		address = Item.objects.get(address = 'B4 L28 San Miguel 2 Dasma Cavite')
		date = Item.objects.get(date = '2021-04-29')
		clock = Item.objects.get(clock = '2PM')
		#response = self.client.post('/book/')
		#self.assertRedirects(response, '/book/')


		self.assertEqual(Item.objects.count(), 7)
		name = Item.objects.first()
		clock = Item.objects.last()

class URL(TestCase):
	def urls(self):
		found = resolve()
		self.assertEqual(found.func, MainPage)
		self.assertEqual(found.func, BookPage)

		url = reverse('mainpage')
		self.assertEqual(resolve(url).func, MainPage)

		url = reverse('book')
		self.assertEqual(resolve(url).func, BookPage)



"""

	def test_get(self):
		name = Item.objects.get(name = 'Danica Isonza')
		email = Item.objects.get(email = 'entmt.danicaisonza@gmail.com') 
		contact = Item.objects.get(contact =  '09128126166')
		address = Item.objects.get(address = 'B4 L28 San Miguel 2 Dasma Cavite')
		date = Item.objects.get(date = '2021-04-29')
		clock = Item.objects.get(clock = '2PM')
		#response = self.client.post('/book/')
		#self.assertRedirects(response, '/book/')


l1 = Item()
		l1.name = 'Danica Isonza'
		l1.save()
		l2 = Item()
		l2.email = 'entmt.danicaisonza@gmail.com'
		l2.save()
		l3 = Item()
		l3.contact = '09128126166'
		l3.save()
		l4 = Item()
		l4.address = 'B4 L28 San Miguel 2 Dasma Cavite'
		l4.save()
		l5 = Item()
		l5.date = '2021-04-29'
		l5.save()
		l6 = Item()
		l6.clock = '2PM'
		l6.save()
"""