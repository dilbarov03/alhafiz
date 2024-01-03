from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.common.serializers import ApplicationSerializer, NewsSerializer, GallerySerializer, TarifDetailSerializer, TarifListSerializer

from .models import Application, News, Gallery, Tarif


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ("title", )


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class GalleryView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = None


class TarifListView(ListAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifListSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ("title", )


class TarifDetailView(RetrieveAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifDetailSerializer


class ApplicationCreateView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
