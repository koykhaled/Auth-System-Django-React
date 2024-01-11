from django.urls import path , include , re_path
from django.views.generic import TemplateView # for react side

urlpatterns = [
    path('auth/',include('djoser.urls')), # to handle login , register , logout ...etc
    path('auth/',include('djoser.urls.jwt')), # to handle tokens 
    path('account/',include('accounts.urls')),
]


urlpatterns +=[re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]