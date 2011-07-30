from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from projects.forms import ProjectForm
from errors.models import Error


class IndexView(TemplateView):
    template_name = 'panel/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['errors'] = Error.objects.all()
        return context


def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            return

    else:
        form = ProjectForm()

    return TemplateResponse(request, 'panel/project_form.html', {'form': form})
