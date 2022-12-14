import os
import hashlib

print("-------------------------------------软件加密工具-------------------------------------")
print("关注博主不迷路！！！\nhttps://jiangongfang.blog.csdn.net/\nhttps://blog.51cto.com/u_15449377")
print("使用告知：\n【加密后的文件后缀会多出DATA，是为了方便软件检测，请勿乱改加密后的后缀名】")
print("【保存文件默认路径 为加密文件或解密文件的当前目录，不是软件的当前目录】")
print("【要加密或解密的文件命名不可有“./\”字符，否则会出错】")
print("-------------------------------------软件加密工具-------------------------------------\n")
print("改良；\nhttps://blog.csdn.net/sqxy090123?type=blog")
print("-------------------------------------软件加密工具-------------------------------------\n")
name_1 = input('输入要加密或解密的文件名含后缀：')
# 判断是否存在该文件
if os.path.exists(name_1) == True:
    pass
else:
    print('请检查是否路径错误或不存在该文件！！！！')
    os.system('pause')
    exit()

password = input('请输入要加密或解密的密码：')
data = input('输入要保存文件的路径位置(可不填)：')

name_1 = name_1.replace("\\", "/")  # 替换
data = data.replace("\\", "/")  # 替换

if name_1.split(".")[1][-4:] == 'DATA':
    F = name_1.split(".")[1].replace("DATA", "")
    if os.path.split(data)[0] == '':
        if os.path.split(name_1)[0] == '':
            data = os.path.split(name_1)[-1].split(".")[0] + '.' + F
        else:
            data = os.path.split(name_1)[0] + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + F
    else:
        data = data + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + F
else:
    # 保存路径
    if os.path.split(data)[0] == '':
        if os.path.split(name_1)[0] == '':
            data = name_1.split(".")[1]  # 后缀
            data = os.path.split(name_1)[-1].split(".")[0] + '.' + data + 'DATA'
        else:
            data = name_1.split(".")[1]  # 后缀
            data = os.path.split(name_1)[0] + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + data + 'DATA'
    else:
        name_3 = name_1.split(".")[1]  # 后缀
        data = data + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + name_3 + 'DATA'

a = open(name_1, "rb")  # 读取文件
b = open(data, "wb")  # 写入文件

# 使用MD5进行加密(双层加密）
hl = hashlib.md5()
hl.update(password.encode(encoding='utf-8'))
password_list = hl.hexdigest()

hl.update(password_list.encode(encoding='utf-8'))
password_list2 = hl.hexdigest()
password_data = password_list + password_list2


# 加密及解密
def Encryption_and_decryption():
    count = 0  # 索引
    for now in a:
        for nowByte in now:
            newByte = nowByte ^ ord(password_data[count % len(password_data)])  # 循环遍历出密码的ord值，单个循环
            count += 1
            b.write(bytes([newByte]))  # 转换


Encryption_and_decryption()
a.close()
b.close()

# 删除原文件
os.remove(name_1)
print ("已删除原文件",(name_1))

os.system('pause')
