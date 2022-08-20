from django.shortcuts import render
from .models import Item
# Create your views here.


def get_reserve_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'reserve/reserve_list.hmtl')
