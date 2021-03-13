from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SimpleProductToSell


# Create your views here.
def health(request):
    return HttpResponse("Tá de boas!")


def index(request):
    available_products = SimpleProductToSell.objects.order_by('id')
    template = loader.get_template('menu/ui-tables.html')
    for a in available_products:
        print(a.name)

    context = {
        'product_list': available_products,
    }
    # return HttpResponse(available_products)
    # return render(request, 'menu/index.html')
    return HttpResponse(template.render(context, request))
