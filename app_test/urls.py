from django.urls.conf import path
from app_test.views import CreateCheckoutSessionView, SuccessView, CancelView, ProductPageView

urlpatterns = [
	path('item/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
	path('success/', SuccessView.as_view(), name='success'),
	path('cancel/', CancelView.as_view(), name='cancel'),
	path('', ProductPageView.as_view(), name='product'),
]