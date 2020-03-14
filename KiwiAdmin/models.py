from django.db import models


class Customer(models.Model):
    """客户信息表"""
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, db_index=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # app_label = 'customer'
        db_table = "customer"
        ordering = ['-create_time']
        verbose_name = "customer"
        verbose_name_plural = "customers"


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

    product_id = models.IntegerField(primary_key=True)
    product_no = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    specification = models.SmallIntegerField(choices=SPECIFICATION_CHOICES)
    image = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
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


class Order(models.Model):
    """订单表"""
    STATUS_CHOICES = [
        (-2, '已取消'),
        (-1, '待付款'),
        (0, '待发货'),
        (1, '已发货'),
        (2, '已收货'),
    ]
    DELIVER_TYPE_CHOICES = [
        (0, '送货上门'),
        (1, '自提'),
    ]
    IS_PAY_CHOICES = [
        (0, '未付款'),
        (1, '已支付'),
    ]

    order_id = models.IntegerField(primary_key=True)
    order_no = models.BigIntegerField()
    customer_id = models.ForeignKey(Customer, related_name="customer", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    product_num = models.IntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
    product_amount = models.DecimalField(max_digits=20, decimal_places=2)
    order_amount = models.DecimalField(max_digits=20, decimal_places=2)
    deliver_type = models.SmallIntegerField(null=True, choices=DELIVER_TYPE_CHOICES)
    is_pay = models.SmallIntegerField(choices=IS_PAY_CHOICES)
    express_no = models.CharField(max_length=100, null=True)
    payment_time = models.DateTimeField(null=True)
    send_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.order_no

    class Meta:
        # app_label = 'order'
        db_table = "order"
        ordering = ['-create_time']
        verbose_name = "order"
        verbose_name_plural = "order"

