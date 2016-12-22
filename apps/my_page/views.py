from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import AboutMe, PortfolioApp, Skill, SkillCategory, SocialLink

from django.db import connection

# Create your views here.

def index(request):
	if request.method == 'GET':
		context = {
			'about' : AboutMe.objects.all(),
			'categories' : SkillCategory.objects.prefetch_related('skill_set').all(),
			'portfolio' : PortfolioApp.objects.all(),
			'socials' : SocialLink.objects.all()
		}

		context['table_rows'] = range(max(map(lambda cat: len(cat.skill_set.all()), context['categories'])))
		context['odd_apps'] = len(context['portfolio']) % 2 == 1
		
		if not request.user.is_superuser:
			user = authenticate(username='guest', password='adminportal')
			if user is not None:
				login(request, user)



		return render(request, 'my_page/index.html', context)
