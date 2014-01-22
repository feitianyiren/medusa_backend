from django.contrib import admin

# Register your models here.
from soplog.models import *

admin.site.register(Group)
admin.site.register(User)

admin.site.register(List)
admin.site.register(ListNotify)
admin.site.register(ListStep)
admin.site.register(StepType)