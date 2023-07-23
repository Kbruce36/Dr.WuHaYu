from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('index/', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    #path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = 'logout'),
    path('about/', views.home, name = 'aboutdr.wuhayu'),
    #this path is for the buy_item button
    path('home/<int:product_id>', views.product_details, name='product_detail'),
    path('issue_item/<str:pk>', views.issue_item, name = 'issue_item'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name= 'add_to_stock'),
    path('receipt/', views.receipt, name='receipt'),
    #handling all sales requested from the web browser
    path('all_sales/', views.all_sales, name = 'all_sales'),
    path('receipt/<int:receipt_id>', views.receipt_detail, name = 'receipt_detail'),
    #for deleting the items
    path('delete_detail/<int:product_id>', views.delete_detail, name = 'delete_detail'),
    path('add_to_cart/<str:pk>', views.add_to_cart, name= 'add_to_cart'),
    path('appointment/', views.appointment , name='appointment'),
    path('appointment_page', views.appointment_page, name='appointment_page'),
]