from django.contrib import admin
from .models import Newsletter

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'date', "user_id")

    fields = ('date', 'email', "user_id")

    list_display = ('email', 'date', "user_id")

    ordering = ('-date',)


admin.site.register(Newsletter, NewsletterAdmin)