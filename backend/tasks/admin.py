from django.contrib import admin

from .models import Attachment, Comment, Tag, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Attachment)
