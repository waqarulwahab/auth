
from django.urls import path
from . import views


urlpatterns = [
    path(''        , views.signin_page  , name='signin_page'),
    path('signup/' , views.signup_page , name='signup_page'),
]
