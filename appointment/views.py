from django.shortcuts import render, redirect
from appointment.models import Item, User

# Create your views here.
def MainPage(request):
	if request.method == 'POST':

		client = User.objects.create()
		Item.objects.create(
			name = request.POST['name'],
			email = request.POST['email'], 
			contact = request.POST['contact'],
			address = request.POST['address'], 
			date = request.POST['date'],
			clock = request.POST['clock'],
			)
		return redirect('bookpage')

		inp = Item()
		inp.name = name
		inp.email = email
		inp.contact = contact
		inp.address = address
		inp.date = date
		inp.clock = clock
		inp.save()
	return render(request,'mainpage.html')



def BookPage(request):
	inp = Item.objects.all().order_by('name')
	return render(request,'bookpage.html', {'inp': inp})



"""
return redirect('next')
		name = request.POST['name']
		email = request.POST['email']
		contact = request.POST['contact']
		address = request.POST['address']
		date = request.POST['date']
		time = request.POST['clock']
"""