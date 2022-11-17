from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from django.db.models.fields import FloatField

# Create your models here.


class Person(models.Model):
    person_id = models.AutoField(db_column="person_id", primary_key=True, null=False)
    person_name = models.CharField(db_column="person_name", max_length=100, default="", null=False)
    person_email = models.EmailField(db_column="person_email", max_length=250, default="", null=False)
    person_balance = models.FloatField(db_column="person_balance", null=False)
    person_account_number = models.BigIntegerField(null=False, unique=True)

    def __str__(self):
        return str(self.person_name)

    class Meta:
        db_table = "person_table"


class Transaction(models.Model):
    transaction_id = models.AutoField(db_column="transaction_id", primary_key=True)
    receiver_id = models.ForeignKey(Person, db_column="receiver_id", on_delete=models.CASCADE, related_name="receiver_id")
    sender_id = models.ForeignKey(Person, db_column="sender_id", on_delete=models.CASCADE, related_name="sender_id")
    receiver_amount = FloatField("receiver_amount", null=False)

    class Meta:
        db_table = "transaction_table"
