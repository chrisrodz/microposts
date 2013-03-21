from posts.models import Post
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse


def allposts(request):
	posts = Post.objects.all()
	return render_to_response('allposts.html', {'posts': posts})

# @login_required()
def add(request):
	if request.method == 'POST':
		user = request.user
		post = request.POST['message']
		p = Post(post=post,user=user)
		p.save()
		posts = Post.objects.filter(user=request.user)
		return render_to_response('profile.html', {'user': request.user, 'posts': posts})
	else:
		return render_to_response('addpost.html', {'user': request.user}, context_instance=RequestContext(request))