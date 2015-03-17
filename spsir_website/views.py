from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
#from spsir_website.models import profilePic
from django.shortcuts import render_to_response

def home(request):
	return render(request,"spsir_website/index.html")

def index(request):
	return render(request, 'spsir_website/index.html')
def profile(request):
	return render(request, 'spsir_website/profile.html')
def cv(request):
	return render(request, 'spsir_website/cv.html')


def dc_iips(request):
	return render(request,"spsir_website/dc_iips.html")
def home(request):
	return render(request,"spsir_website/index.html")
def home(request):
	return render(request,"spsir_website/index.html")
def home(request):
	return render(request,"spsir_website/index.html")
def home(request):
	return render(request,"spsir_website/index.html")
						

def contactMe(request):
	return render(request, 'spsir_website/contactMe.html')		

def Miscellaneous(request):
	return render(request, 'spsir_website/Miscellaneous.html')	

def teaching(request):
	return render(request, 'spsir_website/teaching.html')	

def education(request):
	return render(request, 'spsir_website/education.html')	

def research(request):
	return render(request, 'spsir_website/research.html')			

def header(request):
	return render(request, 'spsir_website/header.html')

def footer(request):
	return render(request, 'spsir_website/footer.html')	

def publications(request):
	return render(request, 'spsir_website/publications.html')

def subjectsThought(request):
	return render(request, 'spsir_website/subjectsThought.html')	

def InternationalConferences(request):
	return render(request, 'spsir_website/InternationalConferences.html')	

def nationalConferences(request):
	return render(request, 'spsir_website/nationalConferences.html')	
	
def journalPublications(request):
	return render(request, 'spsir_website/journalPublications.html')	
						    