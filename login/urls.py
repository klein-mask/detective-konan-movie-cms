from django.urls import path
from login import views

app_name = 'login'
urlpatterns = [
    path('index/', views.index, name='login_index'),
    path('create/', views.create_account, name='create_user'),
    path('user/', views.login_account, name='login_user'),
	path('logout/', views.logout_request, name='logout'),
]