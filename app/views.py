from django.shortcuts import render
from .models import Post
#from .models import Post

# Create your views here.
def index(request):
    return render(request, 'app/index.html')
