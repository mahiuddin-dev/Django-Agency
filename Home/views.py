
from django.views.generic import TemplateView


from Client.models import ClientFeedback, ClientLogo
from Services.models import Service
from Blog.models import Blogpost
from Projects.models import Project
# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clientLogo = ClientLogo.objects.all()
        clientfeadback = ClientFeedback.objects.all()
        service = Service.objects.all().order_by('-id')[:6]
        BlogList = Blogpost.objects.all().order_by('-id')[:6]
        project = Project.objects.all().order_by('-id')[:5]
        
        context['clientLogo'] = clientLogo
        context['clientfeadback'] = clientfeadback
        context['service'] = service
        context["BlogList"] = BlogList
        context["project"] = project
    

        return context
    


   

