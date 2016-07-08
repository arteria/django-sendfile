import os
import stat
import re
try:
    from email.utils import parsedate_tz, mktime_tz
except ImportError:
    from email.Utils import parsedate_tz, mktime_tz

# https://docs.djangoproject.com/en/dev/ref/request-response/#fileresponse-objects 
from django.http import FileResponse

from django.http import HttpResponse, HttpResponseNotModified
from django.utils.http import http_date


def sendfile(request, filename, **kwargs):
    response = FileResponse(open(filename, 'rb'))
    return response





def was_modified_since(header=None, mtime=0, size=0):
    """
    Was something modified since the user last downloaded it?

    header
      This is the value of the If-Modified-Since header.  If this is None,
      I'll just return True.

    mtime
      This is the modification time of the item we're talking about.

    size
      This is the size of the item we're talking about.
    """
    try:
        if header is None:
            raise ValueError
        matches = re.match(r"^([^;]+)(; length=([0-9]+))?$", header,
                           re.IGNORECASE)
        header_date = parsedate_tz(matches.group(1))
        if header_date is None:
            raise ValueError
        header_mtime = mktime_tz(header_date)
        header_len = matches.group(3)
        if header_len and int(header_len) != size:
            raise ValueError
        if mtime > header_mtime:
            raise ValueError
    except (AttributeError, ValueError, OverflowError):
        return True
    return False
