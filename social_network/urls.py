# social_network/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index/<int:id>', views.index, name='index'),
    path('new_post/<int:id>',views.post,name='post'),
    path('', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)