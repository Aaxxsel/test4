
from django.urls import path, include

from blog.views import *

urlpatterns = [
    path('', index, name='index'),
]
