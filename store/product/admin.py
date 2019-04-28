from django.contrib import admin

from product import models as product_models


@admin.register(product_models.Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(product_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(product_models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(product_models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
