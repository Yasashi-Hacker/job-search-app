"""
URL configuration for job_search_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from users.views import sign_up,user_login,index,user_home
from companies.views import for_employers,co_sign_up,co_login,co_home
from jobs.views import post_a_job,jobs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', sign_up, name = 'sign_up'),
    path('login/', user_login, name = 'login' ),
    path('', index, name = 'index'),
    path('user-home/', user_home, name= 'user_home'),
    path('for-employers/', for_employers, name = 'for_employers'),
    path('co-sign-up/', co_sign_up, name = 'co_sign_up'),
    path('co-login/', co_login, name = 'co_login'),
    path('co-home/', co_home, name= 'co_home'),
    path('post-a-job/', post_a_job, name= 'post_a_job'),
    path('jobs/', jobs, name='jobs')

]
