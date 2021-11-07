from django.db import models

# Create your models here.

TYPE_CHOICES = {
    ('Mr. ', 'Mr. '),
    ('Ms. ', 'Ms. '),
    ('Mrs. ', 'Mrs. '),
}

class Profiles(models.Model):
    Prefix = models.CharField (max_length=60, default="", choices=TYPE_CHOICES)
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.TextField(max_length=300, default="", blank=True, null=False)
    Username = models.TextField(max_length=300, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name
