# flask_demo
build website with python flask. 

**requirement:**flask, flask_sqlalchemy

## 创建虚拟环境

> 进入项目根目录，要求安装了virtualenv,可以使用pip安装，```$ virtualenv env```创建虚拟环境。
>
> ```$ source env/bin/activate```使用虚拟环境。
>
>  使用pip安装所需的依赖

## 建立数据库

> 在项目根目录下进入python REPL 执行```$ from app import db ``` ```$ db.create_all()```创建数据库  

## 启动服务

> ```$ python app.py``` 默认端口为5000，访问[http://localhost:5000](http://localhost:5000)

