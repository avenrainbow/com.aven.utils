#coding:utf-8
# pigpio远程控制pi gpio口
import pigpio

pi_gpio_host = "127.0.0.1"
pi_gpio_port = "8888";

pi_gpio_pin = 0

# 初始化pi gpio 连接
#pi = pigpio.pi(pi_gpio_host, pi_gpio_port)

# 检测连接
#if not pi.connected:
   #exit()

# 0x00 获取pigpio连接配置
# 0x10 连接测试
# 0x10 设置pigpio远程连接配置
# 0x10 返回上一级

# 0x10 GPIO口控制
# 0x11 输出指定GPIO口的状态
# 0x11 设置指定GPIO口的状态
# 0x14 返回上一级

def show_pigpio_connect():
    global pi_gpio_host
    global pi_gpio_port
    print("host:%s" % (pi_gpio_host))
    print("port:%s" % (pi_gpio_port))

def pigpio_connect_test():
    global pi_gpio_host
    global pi_gpio_port
    pi = pigpio.pi(pi_gpio_host, pi_gpio_port)

    if not pi.connected:
        exit()
    else:
        print("connect to %s:%s success" % (pi_gpio_host,pi_gpio_port))

def pigpio_connect_config():
    global pi_gpio_host
    global pi_gpio_port

    host_tmp = raw_input("请输入目标pigpio host: ")
    if(host_tmp != ""):
        pi_gpio_host = host_tmp

    port_tmp = raw_input("请输入目标pigpio port: ")
    if(port_tmp != ""):
        pi_gpio_port = port_tmp

def show_pigpio_pin_state():
    global pi_gpio_pin
    pi_gpio_pin =int(raw_input("PIN："))

    global pi_gpio_host
    global pi_gpio_port
    pi = pigpio.pi(pi_gpio_host, pi_gpio_port)

    print("GPIO %s 状态：%s" %(pi_gpio_pin,pi.get_mode(pi_gpio_pin)))

def set_pigpio_pin_state():
    global pi_gpio_pin
    pi_gpio_pin = int(raw_input("PIN："))
    state = int(raw_input("state："))
    dutycycle = int(raw_input("dutycycle（空占比）："))
    frequency = float(raw_input("frequency（频率）："))

    global pi_gpio_host
    global pi_gpio_port
    pi = pigpio.pi(pi_gpio_host, pi_gpio_port)
    pi.set_mode(pi_gpio_pin, state)
    pi.set_PWM_dutycycle(pi_gpio_pin, dutycycle)
    pi.set_PWM_frequency(pi_gpio_pin, frequency)


if __name__ == '__main__':
    reload_gate = True
    while(reload_gate):
        print("1.获取当前连接信息")
        print("2.配置连接信息")
        print("3.测试连接")
        print("4.获取GPIO信息")
        print("5.配置GPIO信息")
        print("6.退出")
        action_num = raw_input("请输入操作: ")
        if(action_num == "1"):
            show_pigpio_connect()
            action_num = raw_input("输入回车继续")
        elif(action_num == "6"):
            reload_gate = False
        elif(action_num == "5"):
            set_pigpio_pin_state()
            action_num = raw_input("输入回车继续")
        elif(action_num == "2"):
            pigpio_connect_config()
            action_num = raw_input("输入回车继续")
        elif(action_num == "4"):
            show_pigpio_pin_state()
            action_num = raw_input("输入回车继续")
        elif(action_num == "3"):
            pigpio_connect_test()
            action_num = raw_input("输入回车继续")






