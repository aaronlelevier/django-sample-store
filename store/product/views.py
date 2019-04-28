import json

from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.generic.edit import CreateView
from rest_framework import viewsets

from product.forms import ProductForm
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFormCreateView(CreateView):
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = '/product_form/'

    def form_valid(self, form):
        response = super().form_valid(form)

        # self.object will now be the created object
        model_data = model_to_dict(self.object)

        print("let's print it to the console")
        print(model_data)

        print("or print it as json")
        print(json.dumps(model_data, indent=2))

        return response
