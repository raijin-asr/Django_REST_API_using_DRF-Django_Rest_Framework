from django.http import JsonResponse, HttpResponse

def home_page(request):
    return HttpResponse('<h1>Welcome to the home page</h1>')

def home_page_JSON(request):
    data=[
        'test',
        'success'
    ]
    return JsonResponse(data, safe=False)