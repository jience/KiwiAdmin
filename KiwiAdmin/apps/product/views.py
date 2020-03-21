from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import ProductForm


def product_list(request):
    return render(request, 'product/product_list.html')


@require_POST
def product_add(request):
    # Binding uploaded files to a form
    # https://docs.djangoproject.com/en/2.2/ref/forms/api/#binding-uploaded-files
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('products:product_list'))
    else:
        return HttpResponse("1")
