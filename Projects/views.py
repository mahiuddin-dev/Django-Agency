from django.views.generic import ListView, DetailView
from .models import Project,Category
# Create your views here.

class ProjectView(ListView):
    template_name = 'portfolio-list.html'
    paginate_by = 6
    queryset = Project.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context
    

class ProjectDetail(DetailView):
    template_name = 'portfolio-details.html'
    model = Project
    context_object_name = 'ProjectShow'
