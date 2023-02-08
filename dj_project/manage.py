#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

'''
#shell에서 django 소스내에 접근하듯이 쓰고 싶다면
    >>> os.environ['DJANGO_SETTINGS_MODULE']
    'dj_project.settings'
    >>> import django
    >>> django.setup()   
    >>>
    >>> from instagram.models import Post
    >>> Post.objects.all()
    <QuerySet [<Post: 첫번째 메시지>, <Post: 두번째 메시지>, <Post: 세번째 메시지>]>
'''