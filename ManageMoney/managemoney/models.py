from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    is_client = models.BooleanField('Is client', default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    source = models.CharField(max_length=255, blank=True, null=True)
    date_received = models.DateTimeField()

    def __str__(self):
        return f"Income: {self.amount} from {self.source}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=255)
    date_spent = models.DateTimeField()

    def __str__(self):
        return f"Expense: {self.amount} on {self.category}"


class Saving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=255)
    goal_amount = models.FloatField()
    current_amount = models.FloatField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Savings: {self.goal_name} with goal of {self.goal_amount}"


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monthly_budget = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget: {self.monthly_budget} created on {self.date_created}"


class Transaction(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_type = models.CharField(
        max_length=7,
        choices=TRANSACTION_TYPE_CHOICES,
    )
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"Transaction: {self.amount} ({self.transaction_type})"