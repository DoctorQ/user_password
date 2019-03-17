#!/usr/bin/python
# -*- coding: UTF-8 -*-


import random,string
import xlwt

# num:一次性生成账号个数
# length:账号长度
# has_number:是否含有数字,0表示不含有,1表示含有,默认为1
# has_uppercase:是否含有大写字母,0表示不含有,1表示含有,默认为1
# has_lowercase:是否含有小写字母,0表示不含有,1表示含有,默认为1
# suffix:字符串类型,默认为""
# file_name:字符串类型,账号存放的文件名
def user_password(num,length,has_numer=1,has_uppercase=1,has_lowercase=1,suffix="",file_name="users.txt"):
    result = []
    #小写字母
    a = string.ascii_lowercase
    #大写字母
    b = string.ascii_uppercase
    #数字
    c = string.digits
    #a-zA-Z
    d = string.ascii_letters
    count = 0
    while count < num:
        if length > 2:
            #random.choice从序列中随机选取一个元素
            #random.sample从序列中随机选取n个元素
            #random.shuffle将一堆元素随机打乱
            a1 = random.choice(a)
            b1 = random.choice(b)
            c1 = random.choice(c)
            # 标准组
            d1 = []
            # 补充组
            fill_group = []
            if (has_lowercase == 1):
                d1.append(a1)
            if (has_uppercase == 1):
                d1.append(b1)
            if (has_numer == 1):
                d1.append(c1)
            if (has_lowercase == 1) :
                fill_group = random.sample(a,length-len(d1))
            elif (has_numer == 1) :
                fill_group = random.sample(c,length-len(d1))
            elif (has_uppercase == 1) :
                fill_group = random.sample(b,length-len(d1))

            for i in fill_group:
                d1.append(i)
            

            random.shuffle(d1)
            users = ''.join(d1) + suffix +'\n'
            #print(users)
            if users not in result:
                result.append(users)
                count +=1
        else:
            print('请输入大于2的长度')
            break
    #with open(file_name,'w') as fw:
    #    fw.writelines(result)
    work_book = xlwt.Workbook(encoding='utf-8')
    sheet = work_book.add_sheet('account')
    for item in range(len(result)):
        sheet.write(item, 0, result[item])
    work_book.save(file_name)

    return result

#用法示例

#生成10个账号，账号位数是8个，后缀以@结尾qq.com，包含数字，大写字母和小写字母
user_password(num=10,length=8,suffix="@qq.com",file_name="user1.xls")
#生成1个账号，账号位数是10个，只包含数字，无后缀
user_password(num=1,length=10,has_uppercase=0,has_lowercase=0,file_name="user2.xls")
#生成10个账号，账号位数为11个，只包含小写字母，无后缀
user_password(num=10,length=11,has_numer=0,has_uppercase=0,file_name="user3.xls")
#生成10个账号，账号位数为3个，只包含大写字母，无后缀
user_password(num=10,length=3,has_numer=0,has_lowercase=0,file_name="user4.xls")
#生成10个账号，账号位数为15个，包含小写字母和大写字母，无后缀
user_password(num=10,length=3,has_numer=0,file_name="user5.xls")
#生成10个账号，账号位数为10个，包含小写字母和数字，无后缀
user_password(num=10,length=10,has_uppercase=0,file_name="user6.xls")
#生成10个账号，账号位数为10个，包含大写字母和数字，无后缀
user_password(num=10,length=10,has_lowercase=0,file_name="user7.xls")



