from django.db import models

from KiwiAdmin.utils import UUIDTools, random_product_no


class Product(models.Model):
    """商品表"""

    SPECIFICATION_CHOICES = [
        (1, '五斤'),
        (2, '十斤'),
    ]

    STATUS_CHOICES = [
        (-1, '已删除'),
        (0, '下架'),
        (1, '上架'),
    ]

    product_id = models.UUIDField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False)
    product_no = models.CharField(max_length=13, unique=True, default=random_product_no)
    name = models.CharField(max_length=100)
    specification = models.SmallIntegerField(choices=SPECIFICATION_CHOICES)
    image = models.ImageField(upload_to="images/product", max_length=200, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
    description = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # app_label = 'product'
        db_table = "product"
        ordering = ['-create_time']
        verbose_name = "product"
        verbose_name_plural = "product"
