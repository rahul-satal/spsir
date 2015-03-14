from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response




def index(request):
	return render(request,"spsir_website/index.html")    