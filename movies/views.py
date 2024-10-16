from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.db.models import Count
# Create your views here.

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def dashboard(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return redirect('dashboard')
    
    genre_stats = Movie.objects.values('genre').annotate(count=Count('genre')).order_by('-count')
    total_movies = Movie.objects.count()
    movies = Movie.objects.all()

    return render(request, 'dashboard.html', {'genre_stats': genre_stats, 'total_movies': total_movies, 'movies': movies,})

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'list_movies.html', {'movies': movies})