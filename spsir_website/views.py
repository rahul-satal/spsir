from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
#from spsir_website.models import profilePic
from django.shortcuts import render_to_response
from spsir_website.models import MyTeacher

def home(request):
	return render(request,"spsir_website/index.html")
def index(request):
	return render(request, 'spsir_website/index.html')
def profile(request):
	return render(request, 'spsir_website/profile.html')
def cv(request):
	return render(request, 'spsir_website/cv.html')


def teaching(request):
	return render(request, 'spsir_website/teaching.html')	
def dc_iips(request):
	return render(request,"spsir_website/dc_iips.html")
def ada(request):
	return render(request,"spsir_website/teaching/ada.html")
def cg(request):
	return render(request,"spsir_website/teaching/cg.html")
def dco(request):
	return render(request,"spsir_website/teaching/dco.html")
def dna(request):
	return render(request,"spsir_website/teaching/dna.html")
def project(request):
	return render(request,"spsir_website/teaching/project.html")
def sem_project(request):
	return render(request,"spsir_website/teaching/sem_project.html")
def r_in_c(request):
	return render(request,"spsir_website/teaching/r_in_c.html")

def my_teachers(request):
	return render(request, 'spsir_website/my_teachers.html')
def recommendations(request):
	return render(request, 'spsir_website/recommendations.html')
def books(request):
	return render(request, 'spsir_website/recommendations/books.html')
def ecc(request):
	return render(request, 'spsir_website/recommendations/ecc.html')	
	
def dc_iips(request):
	return render(request, 'spsir_website/dc_iips.html')				
	
						

def contactMe(request):
	return render(request, 'spsir_website/contactMe.html')		

def Miscellaneous(request):
	return render(request, 'spsir_website/Miscellaneous.html')	
def my_students(request):
	return render(request,"spsir_website/miscellaneous/my_students.html")
def spritual_gurus(request):
	return render(request,"spsir_website/miscellaneous/spritual_gurus.html")
def workshop(request):
	return render(request,"spsir_website/miscellaneous/workshop.html")
def my_friends(request):
	return render(request,"spsir_website/miscellaneous/my_friends.html")	





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
						    