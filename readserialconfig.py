import configparser
def read_seript_conf_fun():
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='utf-8')
    list = []
    list = config.sections()# 获取到配置文件中所有分组名称
    if 'config' not in list:# 如果分组config不存在则插入config分组
        config.add_section('config')
        config.set('config', 'serial', 'COM1')# 设置默认串口号为1

    file_config = open('config.ini', 'w')
    config.write(file_config)
    serial_port = config.get('config', 'serial')
    config.read('config.ini', encoding='utf-8')
    file_config.close()#不要忘记关闭
    return serial_port
def write_seript_conf_fun(seript_port):
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    config.set('config', 'serial', seript_port)
    file_config = open('config.ini', 'w')
    config.write(file_config)
    file_config.close()#不要忘记关闭

write_seript_conf_fun('COM6')
print(read_seript_conf_fun())

