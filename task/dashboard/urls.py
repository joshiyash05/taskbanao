from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name='index'),
	path('doctorregister',views.doctorregister,name='doctorregister'),
	path('patientregister',views.patientregister,name='patientregister'),
	path('login',views.login,name='login'),
	path('home', views.home, name='home'),
	path('patientdata',views.patientdata,name='patientdata'),
	path('logout',views.logout,name='logout'),
	path('patientlogin',views.patientlogin,name='patientlogin')
]
