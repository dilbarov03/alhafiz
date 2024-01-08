from django.urls import path


from .views import ApplicationCreateView, NewsListView, NewsDetailView, GalleryView, SlideListView, TarifDetailView, TarifListView


urlpatterns = [
    path("news/", NewsListView.as_view()),
    path("news/<int:pk>/", NewsDetailView.as_view()),
    path("gallery/", GalleryView.as_view()),
    path("tarif/", TarifListView.as_view()),
    path("tarif/<int:pk>/", TarifDetailView.as_view()),
    path("application/", ApplicationCreateView.as_view()),
    path("slides/", SlideListView.as_view()),
]
