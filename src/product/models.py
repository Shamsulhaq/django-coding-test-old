from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True  # define this table/model is abstract.


class Variant(BaseModel):
    title = models.CharField(
        max_length=40
    )
    description = models.TextField()
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

    def get_unique_values(self):
        return self.productvariant_set.values('variant_title').distinct()


class Product(BaseModel):
    title = models.CharField(
        max_length=255
    )
    sku = models.SlugField(
        max_length=255
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    file_path = models.URLField()

    def __str__(self):
        return self.product


class ProductVariant(BaseModel):
    variant_title = models.CharField(
        max_length=255
    )
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )

    def __str__(self):
        return f'{self.product}-{self.variant_title}'


class ProductVariantPrice(BaseModel):
    product_variant_one = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='product_variant_one'
    )
    product_variant_two = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='product_variant_two'
    )
    product_variant_three = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='product_variant_three'
    )
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variant_prices'
    )

    def __str__(self):
        return self.product
