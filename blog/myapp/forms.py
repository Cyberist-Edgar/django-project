from django import forms


class VirusPro(forms.Form):
    province = forms.CharField(max_length=30, label='省份')
    value = forms.CharField(label='总人数', max_length=20)
    # susNum = forms.CharField(label='疑似人数', max_length=20)
    # deathNum = forms.CharField(label='死亡人数', max_length=20)
    # cureNum = forms.CharField(label='治疗人数', max_length=20)
    # city = forms.CharField(label='城市信息')
