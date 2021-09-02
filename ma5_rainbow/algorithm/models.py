
from django.db import models


class Md5Rainbow(models.Model):
    plaintext = models.CharField(max_length=5, verbose_name='明文')
    ciphertext = models.CharField(max_length=40, verbose_name='密文')

    class Meta:
        db_table = "md5_rainbow"
        verbose_name = "md5彩虹表"
        verbose_name_plural = verbose_name