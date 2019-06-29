from django.urls import path

from . import views


urlpatterns = [
   
    path('freightrate/', views.freight, name='freight'),
  	path('products/',views.product_view, name = 'product_view'),
    path('users/', views.buyers_view, name = 'buyers_view'),
    path('Deleteusers/<str:pk>/<int:pk2>/', views.delete_user_view, name = 'delete_user_view'),
    path('Deletefrieghtrate/<int:pk>/', views.delete_frieght_view, name = 'delete_frieght_view'),
    path('freights/', views.freight_view, name = 'freight_view'),
    path('orders/', views.order_view, name = 'order_view'),

        
    
    

]