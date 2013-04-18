from posts.models import Post, Follower
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Display all posts
def allposts(request):
	posts = Post.objects.all()
	return render_to_response('allposts.html', {'posts': posts})


# Profile view for users
@login_required()
def profile(request):
	# Posts by the current user
	posts = Post.objects.filter(user=request.user)
	# Users being followed
	follows = Follower.objects.get(follower=request.user).following.all()
	# Posts by followees
	fposts = Post.objects.filter(user__in=follows)
	return render_to_response('profile.html', {'user': request.user, 'posts': posts, 'fposts': fposts})

# View for registering users
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			follower = Follower(follower=new_user).save()
			return HttpResponseRedirect('/')
	else:
		return render_to_response('register.html',{'form': UserCreationForm}, context_instance=RequestContext(request))

# View for adding posts
@login_required()
def add(request):
	if request.method == 'POST':
		user = Follower.objects.get(follower=request.user)
		post = request.POST['message']
		p = Post(post=post,user=user)
		p.save()
		return profile(request)
	else:
		return render_to_response('addpost.html', {'user': request.user}, context_instance=RequestContext(request))

#View for adding followers
@login_required()
def follow(request):
	if request.method == 'POST':
		if request.POST['newguys[]']:
			current = Follower.objects.get(follower=request.user)
			newguys = Follower.objects.filter(follower__username__in=request.POST.getlist('newguys[]'))
			for guy in newguys:
				current.following.add(guy)
			return profile(request)
	else:
		# Select current user from Follower model
		current = Follower.objects.get(follower=request.user)
		# Select users not currently following, excluding the current user
		users = Follower.objects.exclude(follower__in=current.following.all()).exclude(follower=current.follower)
		return render_to_response('follow.html', {'users': users}, context_instance=RequestContext(request))
		