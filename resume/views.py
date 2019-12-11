from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})


def about(request):
	f_name = "Bill"
	l_name = "Elder"
	return render(request, 'about.html', {'first_name': f_name, 'last_name': l_name})



