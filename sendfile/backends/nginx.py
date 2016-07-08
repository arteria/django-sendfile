from __future__ import absolute_import
from django.http import HttpResponse
from ._internalredirect import _convert_file_to_url
import mimetypes
import os

def sendfile(request, filename, **kwargs):
    f = open("/tmp/sendfile.log", "a")
    response = HttpResponse()
    url = _convert_file_to_url(filename)
    statobj = os.stat(filename)
    mimetype, encoding = mimetypes.guess_type(filename)
    mimetype = mimetype or 'application/octet-stream'
    response['Content-Type'] = mimetype
    response['X-Accel-Redirect'] = url.encode('utf-8')
    response['Content-Length'] = statobj.st_size
    f.write("filename: %s url: %s\n" %(str(filename), str(url)))
    return response
"""

def _handle_nginx(request, instance, field_name):
    field_file  = getattr(instance, field_name)
    basename = os.path.basename(field_file.path)
    mimetype, encoding = mimetypes.guess_type(field_file.path)
    mimetype = mimetype or 'application/octet-stream'
    statobj = os.stat(field_file.path)
    response = HttpResponse()
    response['Content-Type'] = mimetype
    if field_file.attachment:
        response['Content-Disposition'] = 'attachment; filename=%s'%basename
    response["X-Accel-Redirect"] = "/%s"%unicode(field_file)
    response['Content-Length'] = statobj.st_size
    return response

    """
