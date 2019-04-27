from django.db import models
from django.contrib.auth.models import User
from product.validators import validate_stars


class AbstractIdNameModel(models.Model):
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        abstract = True


class Color(AbstractIdNameModel):
    pass


class Category(AbstractIdNameModel):
    pass


class AbstractProduct(models.Model):
    # foreign keys
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    colors = models.ForeignKey(Color, on_delete=models.PROTECT)
    # fields
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    in_stock = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if quantity == 0:
            in_stock = False
        super().save()


class Product(AbstractProduct):
    pass


class Review(models.Model):
    # foreign keys
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # fields
    created = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    stars = models.PositiveIntegerField(validators=[validate_stars])
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
