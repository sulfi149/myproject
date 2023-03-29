"""myproject URL Configuration

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


from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login_view, name = "login"),
    path('signout/',views.signout,name="signout"),
    path('register/',views.register, name = "signup"),
    path('dashboard/',views.dashboard, name = "dashboard"),
    

    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('forgotPassword/',views.forgotPassword,name="forgotPassword"),
    path('resetPassword_validate/<uidb64>/<token>',views.resetPassword_validate,name="resetPassword_validate"),
    path('reset_password/',views.reset_password,name="reset_password"),
]
