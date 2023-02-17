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

'''
# 모델을 통한 조회(기초)
>>> qs = Post.objects.all().order_by('-id')
>>> qs
<QuerySet [<Post: 세번째 메시지>, <Post: 두번째 메시지>, <Post: 첫번째 메시지>]>
>>> print(qs.query)
SELECT "instagram_post"."id", "instagram_post"."message", "instagram_post"."photo", "instagram_post"."is_public", "instagram_post"."created_at", "instagram_post"."updated_at" FROM "instagram_post" ORDER BY "instagram_post"."id" DESC
>>> for post in qs:
...     print("id:{id}, mag:{message} ({created_at})".format(**post.__dict__))
...
id:3, mag:세번째 메시지 (2023-02-07 05:28:27.637628+00:00)
id:2, mag:두번째 메시지 (2023-02-07 05:28:22.679304+00:00)
id:1, mag:첫번째 메시지 (2023-02-07 05:28:17.466399+00:00)
>>> qs = Post.objects.all().filter(message='첫번째 메시지')
>>> qs
<QuerySet [<Post: 첫번째 메시지>]>
>>> qs = Post.objects.all().filter(message__startswith='첫번째')
>>> qs
<QuerySet [<Post: 첫번째 메시지>]>
>>> qs = Post.objects.all().filter(message__icontains='첫번째')
>>> qs
<QuerySet [<Post: 첫번째 메시지>]>
>>> qs.none()
<QuerySet []>
>>> qs.first()
<Post: 첫번째 메시지>
>>> qs.last()
<Post: 첫번째 메시지>
>>> qs.none().last()


>>> from django.db.models import Q
>>> qs = Post.objects.all()
>>> qs = qs.exclude(id__gte=2, message__icontains=query)
>>> print(qs.query)
SELECT "instagram_post"."id", "instagram_post"."message", "instagram_post"."photo", "instagram_post"."is_public", "instagram_post"."created_at", "instagram_post"."updated_at" FROM "instagram_post" WHERE NOT ("instagram_post"."id" >= 2 AND "instagram_post"."message" LIKE %첫번째% ESCAPE '\')
>>> qs = Post.objects.all()
>>> qs = qs.exclude(Q(id__gte=2) & Q(message__icontains=query))
>>> print(qs.query)
SELECT "instagram_post"."id", "instagram_post"."message", "instagram_post"."photo", "instagram_post"."is_public", "instagram_post"."created_at", "instagram_post"."updated_at" FROM "instagram_post" WHERE NOT ("instagram_post"."id" >= 2 AND "instagram_post"."message" LIKE %첫번째% ESCAPE '\')
>>> qs = Post.objects.all()
>>> qs = qs.exclude(Q(id__gte=2) |  Q(message__icontains=query))
>>> print(qs.query)
SELECT "instagram_post"."id", "instagram_post"."message", "instagram_post"."photo", "instagram_post"."is_public", "instagram_post"."created_at", "instagram_post"."updated_at" FROM "instagram_post" WHERE NOT (("instagram_post"."id" >= 2 OR "instagram_post"."message" LIKE %첫번째% ESCAPE '\'))
'''