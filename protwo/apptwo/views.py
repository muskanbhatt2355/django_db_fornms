from django.shortcuts import render
from apptwo.models import User
from apptwo.forms import NewUserForm

# Create your views here.

def home(request):
	return render(request,'apptwo/index.html')

def users(request):
	user_list = User.objects.order_by('first_name')
	user_dict = {'users': user_list}
	return render(request,'apptwo/list.html', context=user_dict)

def signup_form(request):
	form = NewUserForm()
	if request.method=='POST':
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return home(request)
		else:
			print('ERROR! FORM INVALID')

	return render(request,'apptwo/signup.html',{'form':form})

