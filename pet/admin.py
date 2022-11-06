from django.contrib import admin
from .models import PetCategory, Pet


@admin.register(PetCategory)
class PetCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'age',
        'color',
        'owner_name',
        'owner_contact',
        'category',
    )
    list_filter = ('category',)
    search_fields = ('name',)
