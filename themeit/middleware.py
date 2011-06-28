__author__ = 'jbn'
import re
from themes import themepatterns

class ThemeitMiddleware(object):
    def build_path(self, request):
        path = (request.META['HTTP_HOST'], request.get_full_path())
        return ''.join(path)

    def process_request(self, request):
        request.themeid = 1
        path = self.build_path(request)
        if re.search("site_media|favicon.ico", path):
            return None
        for pattern, themeid in themepatterns.items():
            if re.search(pattern, path):
                request.themeid = themeid
                return None
        return None

