from django.contrib import admin

from .models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...


class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(model_or_iterable=Category,
                    admin_class=CategoryAdmin)
admin.site.register(model_or_iterable=Recipe,
                    admin_class=RecipeAdmin)
