from django.shortcuts import redirect, render
from .models import Item, User

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
		return redirect('book')
		
		
		obj = Item()
		obj.name = name
		obj.email = email
		obj.contact = contact
		obj.address = address
		obj.date = date
		obj.clock = clock
		obj.save()


	return render(request,'mainpage.html')


def BookPage(request):
	obj = Item.objects.all().order_by('name')
	return render(request,'bookpage.html', {'obj': obj})





"""
return redirect('next')
		name = request.POST['name']
		email = request.POST['email']
		contact = request.POST['contact']
		address = request.POST['address']
		date = request.POST['date']
		time = request.POST['clock']




from django.shortcuts import render, HttpResponse
from .models import Item, User

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

		obj = Item()
		obj.name = name
		obj.email = email
		obj.contact = contact
		obj.address = address
		obj.date = date
		obj.clock = clock
		obj.save()

		return render(request,'mainpage.html')


def BookPage(request):
	obj = Item.objects.all().order_by('name')
	return render(request,'bookpage.html', {'obj': obj})



"""