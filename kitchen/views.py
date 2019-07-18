from django.shortcuts import render


def fridge_list(request):

   return render(request, 'kitchen/fridge_list.html', {})
