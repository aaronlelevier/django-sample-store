"""
Sample Store Django models.py

This is modeled after data in this store:

https://www.oneupcomponents.com/collections/pedals
"""
from django.contrib.auth.models import User
from django.db import models

from product.validators import validate_stars


class AbstractIdNameModel(models.Model):
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.id


class Color(AbstractIdNameModel):
    pass


class Category(AbstractIdNameModel):
    class Meta:
        verbose_name_plural = 'Categories'


class AbstractProduct(models.Model):
    # foreign keys
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    # fields
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text="value is in pennies")
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(AbstractProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.quantity > 0


class Product(AbstractProduct):
    pass


class Review(models.Model):
    # foreign keys
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # fields
    created = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    stars = models.PositiveIntegerField(validators=[validate_stars])

    def __str__(self):
        return f"{self.title} - {' '.join(self.body.split()[:10])}..."
