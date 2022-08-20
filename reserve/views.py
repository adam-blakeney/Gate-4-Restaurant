from django.shortcuts import render

# Create your views here.

def get_reserve_list(request):
    return render(request, 'reserve/reserve_list.hmtl')


