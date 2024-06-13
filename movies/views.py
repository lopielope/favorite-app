from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'things': ['Bother my dad when he is busy', 'Meow until I get what I want', 'Eat', 'Basking in the sun']

    }

    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {} )

#There is a template structure Django uses
#app/templates/app/index.html
#movies/templates/movies/index.html