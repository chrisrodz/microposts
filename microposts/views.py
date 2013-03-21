from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from posts.models import Post

def home(request):
	return render_to_response('base.html')

@login_required()
def profile(request):
	posts = Post.objects.filter(user=request.user)
	return render_to_response('profile.html', {'user': request.user, 'posts': posts})