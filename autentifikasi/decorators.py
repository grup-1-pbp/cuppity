from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Profile

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == role:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You are not authorized to access this page.")
        return _wrapped_view
    return decorator
