from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden
from .models import Profile

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == role:
                return view_func(request, *args, **kwargs)
            else:
                # Render a custom 403 forbidden page
                return render(request, '403.html', status=403)
        return _wrapped_view
    return decorator
