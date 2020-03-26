from django.db import models


class Post(models.Model):
    """发帖的主要信息，不包括回复内容"""
    topic = models.CharField(max_length=100)  # 发帖主题
    counter = models.IntegerField()  # 浏览次数
    author_user_id = models.IntegerField()  # 发贴用户的id
    content = models.TextField()  # 帖子的内容
    date = models.DateField(auto_now=True)  # 发表的时间

    def __str__(self):
        return self.topic


class PostDetail(models.Model):
    """回复的主要信息，不包括回复的回复，相当于在用户帖子下的一个新回复"""
    topic_id = models.IntegerField()  # 主题id, django自动生成的
    post_user_id = models.IntegerField()  # 对应回复用户的id，相当于一个新的回复
    content = models.TextField()  # 回复的内容
    date = models.DateField()  # 回复的时间

    class Meta:
        ordering = ("-date",)  # 按照时间的降序排


class PostReply(models.Model):
    post_id = models.IntegerField(unique=False)  # 归属于一个 PostDetail id
    user_id = models.IntegerField()  # 回复的用户
    reply_user_id = models.IntegerField()  # 给谁回复的
    content = models.TextField()  # 回复的内容
