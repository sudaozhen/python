import configparser
 
#  实例化configParser对象
config = configparser.ConfigParser()
# -read读取ini文件
config.read('config.ini', encoding='utf-8')
list = []
list = config.sections()# 获取到配置文件中所有分组名称
if 'config' not in list:# 如果分组config不存在则插入config分组
    config.add_section('config')
    config.set('config', 'COM', '2')# 给type分组设置值
 
# #config.remove_option('type', 'stuno')# 删除type分组的stuno
# #config.remove_section('tpye')# 删除配置文件中type分组
o = open('config.ini', 'w')
config.write(o)
o.close()#不要忘记关闭


##############################################################
# import configparser
 
#  实例化configParser对象
config = configparser.ConfigParser()
# -read读取ini文件
config.read('config.ini', encoding='utf-8')
# # -sections得到所有的section，并以列表的形式返回
# print('sections:' , ' ' , config.sections())
 
# # -options(section)得到该section的所有option
# print('options:' ,' ' , config.options('config'))
 
# # -items（section）得到该section的所有键值对
# print('items:' ,' ' ,config.items('cmd'))
 
# # -get(section,option)得到section中option的值，返回为string类型
# print('get:' ,' ' , config.get('cmd', 'startserver'))
 
# -getint(section,option)得到section中的option的值，返回为int类型
print('getint:' ,' ' ,config.getint('config', 'COM'))
# print('getfloat:' ,' ' , config.getfloat('cmd', 'weight'))
# print('getboolean:' ,'  ', config.getboolean('cmd', 'isChoice'))
"""
首先得到配置文件的所有分组，然后根据分组逐一展示所有
"""
# for sections in config.sections():
#     for items in config.items(sections):
#         print(items)


#######config 文件########
# #  定义config分组
# [config]
# platformName=Android
# appPackage=com.romwe
# appActivity=com.romwe.SplashActivity
 
# #  定义cmd分组
# [cmd]
# viewPhone=adb devices
# startServer=adb start-server
# stopServer=adb kill-server
# install=adb install aaa.apk
# id=1
# weight=12.1
# isChoice=True
 
# #  定义log分组
# [log]
# log_error=true
