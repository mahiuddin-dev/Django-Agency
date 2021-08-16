from django.views.generic import ListView,DetailView

# Create your views here.
from .models import Blogpost

class BlogView(ListView):
    template_name = "blog-list-full-width.html"
    paginate_by = 6
    queryset = Blogpost.objects.all().order_by('-id')


class BlogDetailView(DetailView):
    template_name = 'blog-details-full-width.html'
    model = Blogpost
    context_object_name = 'BlogDetail'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["BlogList"] = Blogpost.objects.all().order_by('-id')[:4]
        return context