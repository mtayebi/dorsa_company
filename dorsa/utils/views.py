from django.http import JsonResponse


def error_404(request, exception):
    print('='*100)
    message = {"the URL you entered was wrong, check it and try again."}
    response = JsonResponse(data={'ERROR': message})
    response.status_code = 404
    return response


def error_401(request, exception):
    message = {"the URL you entered was wrong, check it and try again."}
    response = JsonResponse(data={'ERROR': message})
    response.status_code = 401
    return response


def error_400(request, exception):
    message = {"the URL you entered was wrong, check it and try again."}
    return JsonResponse({'ERROR': message})


def error_500(request):
    message = {"oops! we had some issues, if you can't access again warn us"}

    return JsonResponse(data={'ERROR': message})
