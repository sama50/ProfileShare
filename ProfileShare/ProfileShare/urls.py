from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.forms import LoginForm
from app.views import home , addprojectdetails , addachimentdetails , uploadurl,shareprofile , profileget , logoutby
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('imgupload/',uploadurl,name='imgupload'),
    path('addproject/',addprojectdetails),
    path('addachiment/',addachimentdetails),
    path('profile/<slug:id>/',shareprofile),
    path('profile/',profileget,name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='./login.html', authentication_form=LoginForm), name='login'),
     path('logout/',logoutby,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
