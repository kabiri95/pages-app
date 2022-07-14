from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


############################################################
class HomePageView(TemplateView):
    template_name = 'home.html'

# def HomePage(request):
#     return render(request, 'home.html')



############################################################
class AboutPageView(TemplateView):
    template_name = 'about.html'

def AboutPage(request):
    return render(request, 'home.html')