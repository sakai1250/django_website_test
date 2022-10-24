from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        return ctxt
    
class AboutView(TemplateView):
    template_name = "about.html"

# Create your views here.
