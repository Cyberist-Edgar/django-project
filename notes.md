#### 装饰器
- `from django.contrib.auth.decorators import ...`
    - `login_required(redirect_field_name='next', login_url=None)`  
        - 如果用户没有登录，重定向到settings.LOGIN_URL,并传递绝对路径到查询字符串中
        - 如果用户已经登录，则执行正确的视图
        - login_url 指定用户登录的网页
        - redirect_field_name 指定跳转路径的参数名称，默认为next
       
    