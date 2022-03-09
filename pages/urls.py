from  django.urls import path
from pages import views as pages_view


urlpatterns = [

    #path('', views.blogpage, name='blog-home'),   --function-base biew
    path('', pages_view.home_view, name='home'),
    path('list/', pages_view.PersonListView.as_view(), name='person_changelist'),
    path('add/', pages_view.PersonCreateView.as_view(), name='person_add'),
    path('ajax/load-lgas/', pages_view.load_lgas, name='ajax_load_lgas'),
    path('product', pages_view.product_view, name='product'),

    path('productadd/', pages_view.ProductCreateView.as_view(), name='product-add'),
    path('contact/', pages_view.contact_view, name='contact'),
    path('about/', pages_view.about_view, name='about'),

]
