from django.shortcuts import render, redirect
from .models import Movie

# 1) 전체 영화 데이터 조회 및 index.html 렌더링
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


# 2) 장르 데이터 제공 및 new.html 렌더링
def new(request) :
    return render(request, 'movies/new.html')


# 3) 새로운 영화 데이터 저장 및 detail 페이지로 리다이렉트
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('movies:detail', movie.pk)


# 4) 단일 영화 데이터 조회 및 detail.html 렌더링
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


# 5) 수정 대상 영화 데이터 조회 및 edit.html 렌더링
def edit(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)


# 6) 영화 데이터 수정 및 detail 페이지로 리다이렉트
def update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()

    return redirect('movies:detail', movie.pk)


# 7) 단일 영화 데이터 삭제 및 index 페이지로 리다이렉트
def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
    return redirect('movies:index')