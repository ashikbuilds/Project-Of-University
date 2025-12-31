from django.shortcuts import render, HttpResponse
from hotel.models import Contact
from django.views.generic import TemplateView
def home(request):
    name=["hasan","sojeeb"]
    context={
        'name': name,
    }
    return render(request,'home.html',context)
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'আমাদের ওয়েবসাইটে আপনাকে স্বাগতম!'
        return context
