from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('--.<str:msg>', views.index, name='index'),
    path('list', views.list, name='list'),
    path('details/<str:cid>', views.details, name='details'),
    path('create-client', views.create_client, name='create_client'),
    path('update-client/<str:cid>', views.update_client, name='update_client'),
    path('delete-client/<str:cid>', views.delete_client, name='delete_client'),
    path('update-wallet/<str:cid>', views.update_wallet, name='update_wallet'),
    path('api/test-api', views.test_API, name='test_api'),
    path('api/get/<str:cid>', views.API_single_client, name='API_single_client'),
    path('client-websocket/<str:cid>', views.client_websocket, name='client_websocket')

]