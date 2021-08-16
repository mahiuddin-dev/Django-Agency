from django.views.generic import ListView, DetailView

from .models import Service

# Create your views here.

class ServicesView(ListView):
    template_name = "service-list.html"
    paginate_by = 6
    queryset = Service.objects.all().order_by('-id')


class ServiceListView(DetailView):
    template_name = 'service-details.html'
    model = Service
    context_object_name = 'Service'

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context["service"] = Service.objects.all().order_by('-id')[:4]
        return context
    


    
    



