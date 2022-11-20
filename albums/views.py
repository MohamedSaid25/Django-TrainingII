from django.views.generic import FormView
from .forms import CreateAlbum
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album
from .serializers import AlbumSerializer
from django_filters import rest_framework as filters
from rest_framework import generics, pagination, permissions, response


# Create Form to Make albums
class CreateForm(LoginRequiredMixin, FormView):
    form_class = CreateAlbum
    template_name = 'albums/createAlbum.html'
    success_url = 'create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'cost': ['lte', 'gte'],
            'name': ['icontains'],
        }


class AlbumViewApprovedList(generics.ListCreateAPIView):
    queryset = Album.objects.filter(isApproved=True)
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AlbumFilter

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)


# manual Filter at endpoint =>(/ablums/manualFilter)
class AlbumManualFilter(generics.ListCreateAPIView):
    queryset = Album.objects.filter(isApproved=True)
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)

    def list(self, request):
        cost_LTE = request.GET.get('cost__lte', 200)
        cost_GTE = request.GET.get('cost__gte', 200)
        name_filter = request.GET.get('name__icontains', 'A')
        queryset = self.get_queryset()
        queryset = queryset.filter(cost__gte=cost_GTE,
                                   cost__lte=cost_LTE,
                                   name__icontains=name_filter)

        serializer = AlbumSerializer(queryset, many=True)
        data = serializer.data

        return response.Response(data)
