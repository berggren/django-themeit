__author__ = 'jbn'
import re
from models import Theme

class ThemeitMiddleware(object):
    def build_path(self, request):
        path = (request.META['HTTP_HOST'], request.get_full_path())
        return ''.join(path)

    def process_request(self, request):
        try:
            from themes import themepatterns
        except ImportError:
            return None
        request.themeid = 1
        path = self.build_path(request)
        if re.search("site_media|favicon.ico", path):
            return None
        for pattern, themeid in themepatterns.items():
            if re.search(pattern, path):
                theme = Theme.objects.get(pk=themeid)
                request.themeid = theme.id
                request.site = theme.site
                return None
        return None