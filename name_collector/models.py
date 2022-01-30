from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'pk: {self.pk} | {self.name}'

    class Meta:
        db_table = 'Names'
