from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    salary = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

