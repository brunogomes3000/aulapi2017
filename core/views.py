from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def cursos(request):
	return render(request, 'cursos.html')