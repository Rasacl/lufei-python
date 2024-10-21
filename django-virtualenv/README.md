### 先创建一个带虚拟环境的python项目

### 下载指定版本的django

### 根据django命令创建项目
django-admin startproject mysite .  # 加. 表示当前目录，不做目录的嵌套

生成requirements.txt文件 包依赖列表
pip freeze > requirements.txt
根据requirements.txt安装包
pip install -r requirements.txt