"""
Definition of models.
"""

from django.db import models

# Create your models here.
import ast
class ListField(models.TextField):
	description = "Stores a python list"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def from_db_value(self, value, expression, connection):
		if value is None:
			return value
		if isinstance(value, str):
			return value.split(',')

	def to_python(self, value):
		if not value:
			value = []
		if isinstance(value, list):
			return value
		if isinstance(value, str):
			return ast.literal_eval(value)

	def get_prep_value(self, value):
		if value is None:
			return value
		if value is not None and isinstance(value, str):
			return value
		if isinstance(value, list):
			return ','.join(value)

	def value_to_string(self, obj):
		value = self.value_from_object(obj)
		return self.get_prep_value(value)

class Question(models.Model):
    name = models.CharField(max_length=255)
    question = models.CharField(max_length=1000)
    answer =  ListField()



class Chat(models.Model):
    name = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now_add=True)