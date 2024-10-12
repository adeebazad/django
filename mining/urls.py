from django.urls import path
from .views import FetchOrderView
from .views import predict_order_prices



urlpatterns = [
               path('fetch-order/',FetchOrderView.as_view(),name='fetch_order'),
               path('predict-order-prices/', predict_order_prices.as_view(), name='predict_order_prices'),

               ]