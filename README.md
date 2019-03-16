# user_password


# 用法示例

```
#生成10个账号，账号位数是8个，后缀以@结尾qq.com，包含数字，大写字母和小写字母
user_password(num=10,length=8,suffix="@qq.com",file_name="user1.txt")
#生成1个账号，账号位数是10个，只包含数字，无后缀
user_password(num=1,length=10,has_uppercase=0,has_lowercase=0,file_name="user2.txt")
#生成10个账号，账号位数为11个，只包含小写字母，无后缀
user_password(num=10,length=11,has_numer=0,has_uppercase=0,file_name="user3.txt")
#生成10个账号，账号位数为3个，只包含大写字母，无后缀
user_password(num=10,length=3,has_numer=0,has_lowercase=0,file_name="user4.txt")
#生成10个账号，账号位数为15个，包含小写字母和大写字母，无后缀
user_password(num=10,length=3,has_numer=0,file_name="user5.txt")
#生成10个账号，账号位数为10个，包含小写字母和数字，无后缀
user_password(num=10,length=10,has_uppercase=0,file_name="user6.txt")
#生成10个账号，账号位数为10个，包含大写字母和数字，无后缀
user_password(num=10,length=10,has_lowercase=0,file_name="user7.txt")


```


# 执行

```
python main.py
```


