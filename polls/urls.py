from django.urls import include, path

from . import views

app_name = 'polls'
urlpatterns = [
    path(r'^$', views.IndexView.as_view(), name='index'),
    path(r'^<int:pk>/$', views.DetailView.as_view(), name='detail'),
    path(r'^<int:pk>/results/$', views.ResultsView.as_view(), name='results'),
    path(r'^<int:pk>/vote/$', views.vote, name='vote'),
]