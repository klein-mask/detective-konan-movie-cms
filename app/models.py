from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
	"""映画"""
	id = models.AutoField(primary_key=True)
	title = models.CharField('映画タイトル', max_length=255)
	release_date = models.CharField('公開日', max_length=11, default='----年--月--日')
	income = models.FloatField('興行収入', default=0)
	income_str = models.CharField(max_length=255, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title
