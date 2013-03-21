from django.shortcuts import render_to_response
from posts.views import profile

def home(request):
	if request.user.is_authenticated():
		return profile(request)
	return render_to_response('base.html')