"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from tasks import views

### IMPORTACIONES PARA EL USERADMIN

from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [
    ##Vistas predetterminadas de Django
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    #path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    #path('signin/', views.signin, name='signin'),

    #Modulos creados que pueden usarse en otro proyecto.
    path('recep/', include('recep.urls')),
    path('tablero/', include('tablero.urls')),

    #Llamada a la API
    path('api/', include('api.urls')),


    ### AUTENTICACION DE USUARIO: EL CODIOG PERTENECIENTE A ESTA RUTA DEBE MANTENERSE EN INGLES PORQUE ES POR DEFECTO DE FRAMEWORK
    path('', include('users.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]

