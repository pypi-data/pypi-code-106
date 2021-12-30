from django.urls import path

from .views import SubmitView, ThanksView

app_name = 'contact'

urlpatterns = [
    path('', SubmitView.as_view(), name='form'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]
