# 安裝 Django 模組
```shell
    pip install django==3.1.7
```

# 建立 Django 專案語法
```shell
    django-admin startproject student
```

# 建立 Application 應用程式
```shell
    python  manage.py startapp studentsapp # windows
    python3 manage.py startapp studentsapp # mac
```

# 建立 models

# 建立 migration 資料檔
```shell
    python3 manage.py makemigrations # 若有修正 models.py 檔後, 必須 migrate
```

# 模型與資料庫同步
```shell
    python3 manage.py migrate # 若有修正 models.py 檔後, 必須 migrate 
```

# 建立管理者帳號和密碼
```shell
    account: admin
    password: password
```

# 啟動伺服器
```shell
    python  manage.py runserver # windows
    python3 manage.py runserver # mac
```