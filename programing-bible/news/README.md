# 初始化


# 安裝 Django 模組
```shell
    pip install django==3.1.7
```

# 建立 Django 專案語法
```shell
    django-admin startproject news
```

# 執行伺服器
```shell
    cd news
    python manage.py runserver # windows
    python3 manage.py runserver # mac
```

# 建立 Application 應用程式
```shell
    python manage.py startapp newsapp # windows
    python3 manage.py startapp newsapp # mac
```

# 建立 models

# Url 配置檔加入 path

# 建立 templates 資料夾存放模板

# 建立 migration 資料檔
```shell
    # 若有修正 models.py 檔案, 必須 migrate
    python manage.py makemigrations # windows
    python3 manage.py makemigrations # mac
```

# 模型與資料庫同步
```shell
    # 若有修正 models.py 檔案, 必須 migrate
    python manage.py migrate # windows
    python3 manage.py migrate # mac
```

# 建立管理者帳號和密碼
```shell
    python manage.py createsuperuser # windows
    python3 manage.py createsuperuser # mac
    accrount: admin
    password: password
```

# 啟動伺服器
```shell
    python manage.py runserver # windows
    python3 manage.py runserver # mac
```