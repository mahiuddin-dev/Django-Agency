from django.views.generic import TemplateView

from .models import TeamMember
from Client.models import ClientFeedback, ClientLogo

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_member = TeamMember.objects.all()
        clientLogo = ClientLogo.objects.all()
        clientfeadback = ClientFeedback.objects.all()

        context["team_member"] = team_member
        context['clientLogo'] = clientLogo
        context['clientfeadback'] = clientfeadback

        return context


class FaqView(TemplateView):
    template_name = 'faq.html'
    
