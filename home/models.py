from django.db import models

# Create your models here.
#makemigrations- creates changes and store in a file
# migrate - apply pending changes created by makemigrations
class contact(models.Model):
  name = models.CharField(max_length=122)
  phone = models.CharField(max_length=12)
  email = models.EmailField(max_length=122)
  desc = models.TextField()
  date = models.DateField()

  def __str__(self):
    return f"{self.name} - {self.email}"