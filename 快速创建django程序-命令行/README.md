1. cd 指定仓库目录
2. django-admin startproject 项目名

- manage.py  项目管理工具
   - dome
     - __init__.py  
     - settings.py  配置文件 配置不全 只有一部分配置 先读取django的配置 在读取自己的配置
     - urls.py  主路由 
     - wsgi.py  同步模式
     - asgi.py  异步模式

编写代码 urls.py

运行命令
```python
#  python manage.py runserver
```

3 app 创建--命令行

```python
#  python manage.py startapp app名
`