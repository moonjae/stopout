from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Webtoon





def webtoon_list(request):
	webtoons = Webtoon.objects.all()
	context = { 'webtoons': webtoons}
	return render(request, 'list.html', context)


def webtoon_detail(request, pk):
	webtoon = Webtoon(pk = pk)
	episodes = webtoon.episode_set.all()

	context = { 'episodes': episodes}

	return render(request, 'detail.html', context)
