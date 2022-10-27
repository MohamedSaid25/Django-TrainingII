from django.views.generic import FormView
from .forms import CreateAlbum
from .models import Album
# Create your views here.


class CreateForm(FormView):
    form_class = CreateAlbum
    template_name = 'albums/createAlbum.html'
    success_url = 'create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


"""
def createAlbum(request):

    form = CreateAlbum(request.POST or None)
    if form.is_valid():
        form.save()
        form = createAlbum()
    context = {
        'form': form
    }
    return render(request, 'albums/createAlbum.html', context)

"""
