from django.http import HttpResponse


def groups_required(groups):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_superuser:
                return view_func(request, *args, **kwargs)
            if not user.is_authenticated:
                return HttpResponse("You must be logged in!")
            if not user.groups:
                return HttpResponse("401 Unauthorized")

            user_groups_names = [g.name for g in user.groups.all()]
            result = set(user_groups_names).intersection(groups)
            if groups and not result:
                return HttpResponse(f'401 Unauthorized')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
