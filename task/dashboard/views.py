from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Doctor, Patient
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
	return render(request,'welcome.html')

def doctorregister(request):
	
	if request.method =='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		username = request.POST.get('username')
		email = request.POST.get('email')
		photo = request.POST.get('photo')
		password = request.POST.get('password')
		address = request.POST.get('address')
		password2 = request.POST.get('password2')
		context = {'fname':fname,'lname':lname,'username':username,'password':password2,'email':email,'photo':photo,'address':address}
		if password == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request,'Email Already used')
				return redirect('doctorregister')
			elif User.objects.filter(username=username).exists():
				messages.info(request,'Username Already used')
				return redirect('doctorregister')
			else:
				user = User.objects.create_user(username =username,email =email,password =password)
				user.save();
				data = Doctor.objects.create(fname=fname,lname =lname,username=username,password=password2,email=email,photo=photo,address=address)
				data.save();
				return redirect('login')
		else:
			messages.info(request,'password not same')
			return redirect('doctorregister')
	else:

		return render(request,'register.html')

def patientregister(request):
	
	if request.method =='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		username = request.POST.get('username')
		email = request.POST.get('email')
		photo = request.POST.get('photo')
		address = request.POST.get('address')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		context = {'fname':fname,'lname':lname,'username':username,'password':password2,'email':email,'photo':photo,'address':address}
		if password == password2:
			print("in if")
			if User.objects.filter(email=email).exists():
				messages.info(request,'Email Already used')
				return redirect('patientregister')
			elif User.objects.filter(username=username).exists():
				messages.info(request,'Username Already used')
				return redirect('patientregister')
			else:
				print("in else")
				user = User.objects.create_user(username =username,email =email,password =password)
				user.save();
				data = Patient.objects.create(fname=fname,lname =lname,username=username,password=password2,email=email,photo=photo,address=address)
				data.save();
				return redirect('login')
		else:
			messages.info(request,'password not same')
			return redirect('patientregister')
	else:

		return render(request,'patientregister.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.info(request,'credientials invalid ')
			return redirect('login')
	else:
		return render(request,'login.html')
def home(request):
	data = Doctor.objects.all()
	print(data)
	stu = {
    "data": data}
	return render(request,'home.html',stu)
def patientdata(request):	
	data = Patient.objects.all()
	print(data)
	stu = {
    "data": data}
	return render(request,'patientdata.html',stu)
def logout(request):
	auth.logout(request)
	return redirect('/')

def patientlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('patientdata')
		else:
			messages.info(request,'credientials invalid ')
			return redirect('patientlogin')
	else:
		return render(request,'patientlogin.html')
