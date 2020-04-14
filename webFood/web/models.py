from django.db import models
from django.utils import timezone

# Create your models here.


class Consumer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=245)
    password = models.CharField(max_length=12)
    phone = models.DecimalField(max_digits=10, decimal_places=10)
    address = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        db_table = 'tb_consumer'
        verbose_name = 'Consumers'


class BillDetail(models.Model):
    create_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    consumer = models.ForeignKey(Consumer, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_bill_detail'
        verbose_name = 'Bill Detail'


class Good(models.Model):
    code = models.CharField(max_length=200, null=True, blank=True )
    name = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    id_bill_detail = models.ForeignKey(BillDetail, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_goods'
        verbose_name = 'Goods'


class Bill(models.Model):
    status_delivery = models.BooleanField(null=True, blank=True, default=False)
    total_money = models.FloatField(null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        db_table = 'tb_bill'
        verbose_name = 'Bill'







