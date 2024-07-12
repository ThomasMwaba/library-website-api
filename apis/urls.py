from django.urls import path
from . views import BOOKAPIView

urlpatterns = [
    path('',BOOKAPIView.as_view(),name='book_list'),
]