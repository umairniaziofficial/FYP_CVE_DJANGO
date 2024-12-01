from django.urls import path
from .views import index, login, signup, mapping

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('mapping/', mapping, name='mapping'),
]
