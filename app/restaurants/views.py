# from django.shortcuts import render
from django.http import JsonResponse


def demo_view(request):

    context = {
        'data':
            {
                'a': 1,
                'b': 2,
                'c': 3
            }
    }

    return JsonResponse(context)
