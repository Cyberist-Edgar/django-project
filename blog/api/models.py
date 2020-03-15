from django.db import models


# Create your models here.
class VerifyCode(models.Model):
    # 用户验证登录的时候
    # - type --> 来确定验证码的类型
    # - email --> 用户的email address
    # - code --> 验证码
    # expired_date --> 验证码过期的时间
    email = models.EmailField()
    type = models.IntegerField()
    code = models.IntegerField()
    expired_date = models.DateTimeField()

    class Meta:
        unique_together = ("email", "type")
