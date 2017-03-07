from django.contrib import admin
from webapp.models import headlines
from webapp.models import user_comment


admin.site.register(headlines)
admin.site.register(user_comment)
