# Create your views here.
from django.shortcuts import render_to_response

from blog.models import posts

def home(request):
	content = posts.objects.all()[:10]
	return render_to_response('index.html', {
		'content' : content 
		})
