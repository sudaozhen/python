


f2 = open('高压板测试_'+'2020-6-16'+'.txt',"a",encoding="utf-8")     #追加模式，在原文件内容最后追加，无原文件则新建
f2.write("-------------\n")
f2.close()


# f = open("file_test.txt","r",encoding = "utf-8")    #打开文件，“读模式”，只能读，得到文件句柄并赋值给一个变量
# print(f.read())                     #读文件所有内容，读完之后文件光标跳到最后,文件大时慎用
# f.close()

# import re
# #查找文件中有多少个hello
 
# fp=open("file_test.txt","r")

# for s in fp.readlines():
#     li=re.findall("hello", s)
#     print(li)
#     if len(li)>0:
#         print('find')
        
# #print("search:",count,">>>hello")
# # fp.close()

# # def fileTest(strVal):
# #         lineNum = 0
# #         msg = "There is no result"
# #         with open(r"f:\a.txt", 'r') as file:
# #             for line in file.readlines():
# #                 lineNum = lineNum + 1
# #                 if strVal in line.strip():
# #                     msg = "'%s' string in line %d" % (strVal, lineNum)
# #                     break
# #         print msg
# #打开IDLE(python)，并新创建一个py文件，编辑内容为：

# '''
# 本示例演示如何在一个txt文件中搜索特定的字符串，并将其行显示
# '''
# '''
# # 1. 打开文件
# # # 2. 读取行信息
# # # 3. 判断是否包含关键词
# # # 4. 不包含则循环操作，包含的话将行显示并退出程序'''
# # # FileName = r"D:\8-Python\str_search_in_file\test.txt"
# # # KeyStr = "charles"
# FileName = input("the object file: ")
# KeyStr = input("the key string: ")
# FoundFlag = False
# # 1. 打开文件
# FileObj = open(FileName)
# # 2. 读取行信息
# LineTemp = FileObj.readline()
# while LineTemp:    
#     # 3. 判断是否包含关键词    
#     # 4. 不包含则循环操作，包含的话将行显示并退出程序    
#     if LineTemp.find(KeyStr) == 0:        
#         FoundFlag = True        
#         print("*************************")        
#         print("the line is: " + LineTemp, end='')        
#         print("*************************")        
#         break    
#     else:        
#         LineTemp = FileObj.readline()
# FileObj.close()
# if FoundFlag == False:    
#     print("Not found the string!")
# input()

# f1 = open('file_test.txt')
# linen = 1
# for line in linen:
#     if not line.find('hello') == -1:
#         print(linen)
#     linen +=1
# f1.close()

#####################################
# f = open('file_test.txt','r')
# lines = f.readlines()
# for lines in lines:
#     if "hello" in lines:
#         print(lines)
####################################
# _*_ coding:utf-8 _*_
# def get_math_line(source, keyword):
#     # re chinese
#     # 源文件编码需要指定
#     source = source.decode('utf-8')
#     pattern = '((\d)*).*' + keyword
#     pattern = pattern.decode('utf-8')
#     import re
#     prog = re.compile(pattern)
#     result = prog.search(source)
#     return result.group(1) if result else None

# with open('source.txt', 'rb') as src_file:
#     with open('dest.txt', 'w') as dst_file:
#         for line in src_file.readlines():
#             val = get_math_line(line, 'hello')
#             if val:
#                 print val
#             else:
#                 dst_file.write(line.strip('\n'))

#################################################
# iplist = 'hello'
 
# def ipfilter(ln):
#     global iplist
#     for ip in iplist:
#         if ip in ln: 
#             return False
#     else:
#         return True
 
# tobewrite = filter(ipfilter, open(r'file_test.txt',"rt"))
 
# open(r"file_test.txt","wt").writelines(tobewrite)