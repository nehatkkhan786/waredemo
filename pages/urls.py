from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [

	path('', views.deshboard, name = 'dashboard'),
	path('login/', views.login, name ='login'),

]