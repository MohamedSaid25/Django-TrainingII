from django.views.generic import FormView
from .forms import CreateAlbum
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album
# Create your views here.


class CreateForm(LoginRequiredMixin, FormView):
    form_class = CreateAlbum
    template_name = 'albums/createAlbum.html'
    success_url = 'create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
