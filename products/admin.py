from django.contrib import admin
from .models import Product, Category, Comment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'friendly_name',
            'name',
        )


class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'body', 'product', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('user', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

