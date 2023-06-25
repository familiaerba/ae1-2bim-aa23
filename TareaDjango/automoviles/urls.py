from django.urls import path

from automoviles import views


urlpatterns = [
        path('', views.listarInformacion, name='listarInformacion'),
 ]