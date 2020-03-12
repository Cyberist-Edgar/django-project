from django.db import models


# Create your models here.
class Virus(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    ename = models.CharField(max_length=30)
    value = models.CharField(max_length=20, blank=True, null=True)
    susnum = models.CharField(db_column='susNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deathnum = models.CharField(db_column='deathNum', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    curenum = models.CharField(db_column='cureNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'virus'

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(primary_key=True, null=False, blank=False, max_length=30)
    password = models.CharField(null=False, blank=False, max_length=30)


class File(models.Model):
    """保存上传文件"""
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=30)
    fileName = models.CharField(max_length=200)
    alia = models.CharField(max_length=200)
    path = models.CharField(max_length=400)
