from django.conf.urls import url
from django.urls import path
from .views import login_view,register_view,logout_view
# urlpatterns = [
#     url(r"^login/$", login_view, name = "login"),
# ]



# from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name = 'register'),
    path('logout/$', logout_view, name = "logout"),
]
