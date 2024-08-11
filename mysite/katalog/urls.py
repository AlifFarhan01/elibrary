from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name="katalog"
urlpatterns = [
    path('create/', login_required(views.create), name='create'),
    path('detail/<int:id>/', login_required(views.detail), name='detail'),
    path('delete/<int:id>/', login_required(views.delete), name='delete'),
    path('update/<int:id>/', login_required(views.update), name='update'),
    path('katalog/', login_required(views.index), name='index')
]