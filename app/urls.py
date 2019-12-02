from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('movie/', views.movie_list, name='movie_list'),
	path('movie/add/', views.movie_edit, name='movie_add'),
	path('movie/edit/<int:movie_id>/', views.movie_edit, name='movie_edit'),
	path('movie/del/<int:movie_id>/', views.movie_del, name='movie_del'),
	path('movie/del/all/', views.delete_all_movie, name='movie_del_all'),
    path('movie/search/', views.movie_search, name='movie_search'),
    path('movie/regist/all/', views.regist_all_movie, name='movie_regist_all'),
    path('movie/sort/', views.movie_sort, name='movie_sort'),
]
