from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from app_test.models import Item
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
	""" Submission of a successful order """
	template_name = "app_test/success.html"


class CancelView(TemplateView):
	""" Order cancellation submission """
	template_name = "app_test/cancel.html"


class CreateCheckoutSessionView(View):
	""" Create checkout session view """
	def post(self, request, *args, **kwargs):
		product_id = self.kwargs['pk']
		product = Item.objects.get(id=product_id)
		YOUR_DOMAIN = "http://127.0.0.1:8000"
		checkout_session = stripe.checkout.Session.create(
			payment_method_types=['card'],
			line_items=[
				{
					'price_data': {
						'currency': 'usd',
						'unit_amount': product.price,
						'product_data': {
							'name': product.name
						},
					},
					'quantity': 1,
				},
			],
			metadata={'product_id': product.id},
			mode='payment',
			success_url=YOUR_DOMAIN + '/success/',
			cancel_url=YOUR_DOMAIN + '/cancel/',
		)
		return JsonResponse({'id': checkout_session.id})


class ProductPageView(TemplateView):
	""" Product view """
	template_name = 'app_test/product.html'

	def get_context_data(self, **kwargs):
		context = super(ProductPageView, self).get_context_data(**kwargs)
		product = Item.objects.get(name='Test Product')
		context.update({
			'product': product,
			'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
		})
		return context


