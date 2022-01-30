from django.shortcuts import render


posts = [
	{
		'author': 'Firdavs Akilov',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': ' January 30, 2022'

	},
	{
		'author': 'Nigina Sadullaeva',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': ' January 31, 2022'

	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
