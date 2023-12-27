from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('tretm/', views.Treatmens_mainpage, name='tretm'),
    path('Treatmens/<int:medicines_id>/', views.medicines_index, name='medicines'),
    path('action/', views.action_spisok, name='action_spisok'),
    path('acrion/<int:action_id>/', views.inf_action, name='inf_action'),
    path('partner/<slug:patners_name>/', views.part, name='part'),
    path('client_err_test/', views.err_400),
    path('server_err_test/', views.err_500),
]
