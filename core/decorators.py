from django.shortcuts import render

def admin_login_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated() \
                and request.user.groups.filter(name='admin').exists():
            return function(request, *args, **kwargs)
        else:
            context = {
                'title': _('403 Forbidden'),
                'message': _('You are not allowed to access this page!')
            }
            # you can also return redirect to another page here.
            return render(request, 'path/to/error_page.html', context)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap