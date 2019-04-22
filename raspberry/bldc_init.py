#coding:utf-8
'''
无刷直流电机 电调 初始化
'''

import pigpio
import time

pi_gpio_port = "8888";
# 输入地址
pi_gpio_host = "127.0.0.1"

pi = None

def connecter_init():

    global pi_gpio_port
    global pi_gpio_host
    global pi
    # 输入地址
    pi_gpio_host = raw_input("请输入目标pigpio host: ")

    # 创建连接
    pi = pigpio.pi(pi_gpio_host, pi_gpio_port)
    raw_input("创建连接成功，回车继续 ")

def bldc_init():
    global pi
    if(pi == None):
        raw_input("请先初始化连接，回车继续 ")
        return 0

    # 输入PIN脚
    pi_gpio_pin = int(raw_input("PIN："))

    # 设置PIN脚OUTPUT
    pi.set_mode(pi_gpio_pin, pigpio.OUTPUT)
    raw_input("设置PIN脚OUTPUT成功，回车继续 ")

    # 输入频率 400
    pi_gpio_frequency = float(raw_input("frequency（频率）："))

    #设置频率
    pi.set_PWM_frequency(pi_gpio_pin, pi_gpio_frequency)
    raw_input("设置频率成功，回车继续 ")

    # 输入最大油门 200
    pi_gpio_dutycycle_max = int(raw_input("最大油门："))

    # 输入最低油门 100
    pi_gpio_dutycycle_min = int(raw_input("最小油门："))

    # 设置最大油门
    raw_input("准备设置行程，回车确认")
    pi.set_PWM_dutycycle(pi_gpio_pin, pi_gpio_dutycycle_max)
    raw_input("设置最大油门成功，准备接电 ")
    time.sleep(3);
    # 电调接电，等待两秒
    #raw_input("电调接电，等待两秒，回车继续 ")

    # 等待油门最高点确认音：bi-bi-
    #raw_input("等待油门最高点确认音：bi-bi-，回车继续 ")

    # 设置最低油门，等待一秒
    #raw_input("准备设置最小油门，回车确认")
    pi.set_PWM_dutycycle(pi_gpio_pin, pi_gpio_dutycycle_min)
    #raw_input("最低油门设置成功，等待一秒，回车继续")

    # N声短鸣音标识锂电节数
    #raw_input("N声短鸣音标识锂电节数，回车继续")

    # 等待油门最低点确认音：bi-
    #raw_input("油门最低点确认音：bi-，回车继续")
    time.sleep(6);
    # 系统就绪
    raw_input("系统就绪，回车继续")


def bldc_resize():
    # 输入PIN脚
    pi_gpio_pin = int(raw_input("PIN："))

    # 输入最大油门
    pi_gpio_dutycycle_resize = int(raw_input("最大油门："))

    #设置油门
    pi.set_PWM_dutycycle(pi_gpio_pin, pi_gpio_dutycycle_resize)
    raw_input("油门设置完成，回车继续")



if __name__ == '__main__':
    reload_gate = True
    while(reload_gate):
        print("1.创建连接")
        print("2.电调初始化")
        print("3.调整油门")
        print("4.安全停机")
        print("5.退出程序")
        actNum = raw_input("请输入操作：")

        if(actNum == "1"):
            connecter_init()
        elif(actNum == "2"):
            bldc_init()
        elif(actNum == "3"):
            bldc_resize()
        elif(actNum == "5"):
            reload_gate = False
