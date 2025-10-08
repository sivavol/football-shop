from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, show_product
# from main.views import register, login_user, logout_user
from main.views import register_user_ajax, login_user_ajax, logout_user_ajax, render_login_page, render_register_page
# from main.views import edit_product, delete_product
from main.views import add_product_entry_ajax, edit_product_entry_ajax, delete_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('login/', render_login_page, name='login'), # URL untuk merender halaman login
    path('register/', render_register_page, name='register'), # URL untuk merender halaman register

    path('login-ajax/', login_user_ajax, name='login_user_ajax'),
    path('register-ajax/', register_user_ajax, name='register_user_ajax'),
    path('logout-ajax/', logout_user_ajax, name='logout_user_ajax'),
    path('add-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_entry_ajax, name='delete_product_entry_ajax'),
]