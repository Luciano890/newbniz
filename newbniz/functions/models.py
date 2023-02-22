"""Models for functions app"""
from django.db import models

class Function(models.Model):
    """Functions model"""
    name = models.CharField(max_length=30)
    function = models.CharField(max_length=30)
    created_at = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return f"Function Name: {self.name}, Function: {self.function}"

class FunctionParameter(models.Model):
    """Function parameters model"""
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    value = models.FloatField()
    created_at = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return f"Function Parameter Name: {self.name}, Value: {self.value}"
