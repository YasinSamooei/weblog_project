

from django.shortcuts import redirect


class LoginRequire:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("acount_app:login")
        return super().dispatch(request, *args, **kwargs)

