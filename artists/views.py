from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateArtist
from .models import Artist
# Create your views here.


class ArtistForm(LoginRequiredMixin, FormView):
    form_class = CreateArtist
    template_name = 'artists/addArtist.html'
    success_url = 'create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArtistList(ListView):
    model: Artist
    context_object_name = 'Artists'
    template_name = 'artists/info.html'
    queryset = Artist.objects.all()
