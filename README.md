# Diango学习记录

## 2023年2月8日

- 项目初始结构创建，可以启动运行
- 切换数据库配置到mysql
- 尝试使用ORM框架
- 增加redis缓存整个网站

# 常用命令记录

- python3 manage.py makemigrations #相当于在该app的migrations目录，记录下该app下modes.py所有表结构类型的改动（普通增删改查不记录）
- python3 manage.py migrate #将刚刚对于表结构的改动作用至数据库
- pip free > .\requirements.txt # 导出项目依赖到文件中