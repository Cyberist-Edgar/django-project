"""
记录一些功能函数
"""
# from django.contrib.auth.models import User
#
# User.objects.create_user()  # 可以创建新的用户

# -----------------------邮件的发送----------------------------
from django.core.mail import send_mail
from django.conf import settings

from_email = settings.DEFAULT_FROM_EMAIL  # 获取settings.py中的配置信息

# 发送邮件，发送对象可以是很多
send_mail("Reset your password", 'You verification code is: ', from_email, ['201648748@qq.com'])

# 使用send_mass_mail 可以实现发送多封邮件
from django.core.mail import send_mass_mail

message1 = ("Reset your password", 'You verification code is: ', from_email, ['201648748@qq.com'])
message2 = ("Reset your password", 'You verification code is: ', from_email, ['201648748@qq.com'])

send_mass_mail((message1, message2), fail_silently=False)

# 使用EmailMultiAlternatives
from django.core.mail import EmailMultiAlternatives

content = 'Hello world'  # 正文内容
msg = EmailMultiAlternatives("Reset your password", content, from_email, ['201648748@qq.com'])
msg.content_subtype = 'html'  # 将文本格式设置为html格式
msg.attach_alternative("<strong>Hello </strong>", 'text/html')  # 对正文内容进行补充，修改
msg.attach_file("file_path")  # 添加附件
msg.send()  # 发送


# ------------------如何定义自己的用户模型-----------
"""
- 代理模式： 模型继承，无须创建新数据表，一般用于改变现有模型的行为方式
- profile扩展模型User：当储存的信息于模型User相关，而且并不改变模型User原有的认证方法时，
可定义新的模型MyUser，并设置某个字段为OnetoOneField，这样能与模型User形成一对一关联
- AbstractBaseUser扩展模型User：当模型User的内置方法并不符和开发需求时，可使用该方法
对模型User重新自定义设计，该方法对模型User和数据库架构影响很大
- AbstractUser扩展模型User：如果模型User内置的方法符合开发要求，在不改变这些函数方法的情况下，
添加模型User的额外字段，可通过该方式实现，需要在setting中配置 AUTH_USER_MODEL = 'xxx.table_name'
xxx -> app的名字
table_name -> 新定义的模型
"""
