from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View


from app.models import Movie
from app.forms import MovieForm, SampleChoiceForm


from lib.common import is_float




def movie_list(request, order='release_date'):
	#movies = Movie.objects.all().order_by(order)
	movies = Movie.objects.filter(user=request.user)

	print('ユーザー：', request.user)

	return render(request, 
				'app/movie_list.html', 
				{
					'movies': movies,
					'columns': ('映画タイトル', '公開日', '興行収入'),
					'choice': SampleChoiceForm(),
				}
			)


def movie_edit(request, movie_id=None):
	if movie_id:
		movie = get_object_or_404(Movie, pk=movie_id)
	else:
		movie = Movie()
	
	if request.method == 'POST':
		form = MovieForm(request.POST, instance=movie)
		if form.is_valid():
			movie = form.save(commit=False)
			movie.user = request.user
			movie.income_str = str(movie.income) + '億円'
			movie.save()
			return redirect('app:movie_list')
	else:
		form = MovieForm(instance=movie)
		form.income_str = str(movie.income) + '億円'
	

	return render(request, 
				'app/movie_edit.html', 
				{
					'form': form,
					'movie_id': movie_id,
				}
			)

def movie_del(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('app:movie_list')

def delete_all_movie(request):
	movies = Movie.objects.all().delete()
	return redirect('app:movie_list')


def movie_search(request):
	return HttpResponse('映画の検索')


def regist_all_movie(request):
	TARGET_URL = 'https://nendai-ryuukou.com/article/064.html'

	import requests
	from bs4 import BeautifulSoup
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.support import expected_conditions
	from selenium.webdriver.common.by import By
	from selenium.common.exceptions import SessionNotCreatedException
	import chromedriver_binary


	driver = None
	try:
		options = Options()
		options.add_argument('--headless')

		driver = webdriver.Chrome(options=options)
		driver.get(TARGET_URL)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		#data = soup(class_='odd')
		data = soup('tr')
		for d in data:
			movie_data = d('td')
			
			if len(movie_data) == 3 and movie_data[1].a != None:
				movie = Movie()
				movie.title = movie_data[1].a.string
				movie.release_date = movie_data[0].string
				movie.income_str = movie_data[2].string
				s = movie.income_str.replace('億円', '')
				movie.income = float(s) if is_float(s) else float(0)
				movie.save()

				print(movie)

	except SessionNotCreatedException as e:
		print(e)
	finally:
		if driver != None:
			driver.close()
	
	return redirect('app:movie_list')



def movie_sort(request):
	sort_key = 'release_date'

	if request.method == 'POST':
		form = SampleChoiceForm(request.POST)
		if form.is_valid():
			sort_key = form.cleaned_data['select']

	return movie_list(request, order=sort_key)