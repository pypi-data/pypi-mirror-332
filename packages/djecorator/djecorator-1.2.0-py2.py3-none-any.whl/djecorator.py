import inspect
from django import urls
from django.contrib.auth.decorators import login_required as login_required_decorator


class Route:
    def __init__(self, url_prefix="", name_prefix=""):
        self.url_prefix = url_prefix.strip("/")
        self.name_prefix = name_prefix
        self.routes = {}

    def __call__(self, path=None, name=None, login_required=False):
        def wrapper(f):
            urlname = self.name_prefix + (name or f.__name__)
            urlpath = path or f.__name__
            urlpath = self.url_prefix + "/" + urlpath.lstrip("/")

            # Check if f is a class with an as_view method
            if inspect.isclass(f) and hasattr(f, "as_view"):
                view = f.as_view()
                if login_required:
                    view = login_required_decorator(view)
                self.routes[urlname] = urlpath, view
            else:
                view = f
                if login_required:
                    view = login_required_decorator(f)
                self.routes[urlname] = urlpath, view
            return f

        if callable(path):
            f = path
            path = None
            return wrapper(f)
        return wrapper

    @property
    def patterns(self):
        return [
            urls.path(path.lstrip("/"), handler, name=name)
            for name, (path, handler) in self.routes.items()
        ]

    @property
    def names(self):
        return {name: "/" + path.lstrip("/") for name, (path, _) in self.routes.items()}
