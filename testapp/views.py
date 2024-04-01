from django.shortcuts import render

def m_view(request):
    return render(request,'testapp/m.html')

from testapp.models import Movie
def list_movies_view(request):
    movie_list = Movie.objects.all()
    return render(request,'testapp/movies.html',{'movie_list':movie_list})

from testapp.forms import MovieForm
def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return m_view(request)
    return render(request,'testapp/add.html',{'form':form})

