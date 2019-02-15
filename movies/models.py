from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.CharField(max_length=4)
  director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True, related_name='movies')

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)

class Director(models.Model):
  name = models.CharField(max_length=50)
  is_arrogant_jerk = models.BooleanField(default=True)

  def __str__(self):
    return self.name
