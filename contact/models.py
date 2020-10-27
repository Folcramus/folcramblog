from django.db import models











class Contact(models.Model):
    email = models.EmailField(max_length=260,  unique=True)



    def __str__(self):
       return self.email