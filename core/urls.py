from django.urls import path

from . import views

urlpatterns = [
    # BAND
    path("bands-list/", views.ListBand.as_view(), name="band-list"),
    path("single-band/<str:id>/", views.RetrieveBand.as_view(), name="single-band"),
    # ALBUM
    path("albums-list/", views.ListAlbum.as_view(), name="albums-list"),
    path("single-album/<str:id>/", views.RetrieveAlbum.as_view(), name="single-album"),
    # MUSICIAN
    path("musicians-list/", views.ListMusician.as_view(), name="musician-list"),
    path(
        "single-musician/<str:id>/",
        views.RetrieveMusician.as_view(),
        name="single-musician",
    ),
    # TRACK
    path("tracks-list/", views.ListTrack.as_view(), name="tracks-list"),
    path("single-track/<str:id>/", views.RetrieveTrack.as_view(), name="single-track"),
]
