#coding=utf-8

from PIL import Image,ImageDraw
import random
import rgb_hsv_exchange
import hsv_semblance

def _loadimage_test():
    # 打开要处理的图像
    img_src = Image.open('she_and_her_cat-004.jpg')

    # 转换图片的模式为RGBA
    img_src = img_src.convert('RGBA')

    # 获得文字图片的每个像素点
    src_strlist = img_src.load()

    #获取随机质心
    random_cores = _kmeans(img_src.width,img_src.height)
    #计算随机质心HSV
    for core in random_cores:
        slity = src_strlist[core[0],core[1]]
        # print(str(slity[0]).zfill(3))
        # print(str(slity[1]).zfill(3))
        # print(str(slity[2]).zfill(3))
        core_hsv = {}
        core_hsv['H'],core_hsv['S'],core_hsv['V'] = rgb_hsv_exchange.rgb2hsv(slity[0],slity[1],slity[2])

        core_new_semblance = 100
        core_new_x = 0
        core_new_y = 0
        for x in range(1,img_src.width):
            for y in range(1,img_src.height):
                point_slity = src_strlist[x,y]
                #计算普通点HSV
                point_hsv = {}
                point_hsv['H'],point_hsv['S'],point_hsv['V'] = rgb_hsv_exchange.rgb2hsv(point_slity[0],point_slity[1],point_slity[2])
                point_semblance = hsv_semblance._semblance(point_hsv,core_hsv)
                if core_new_semblance > point_semblance :
                    core_new_semblance = point_semblance
                    core_new_x = x
                    core_new_y = y






        #print(core_hsv)


    #循环获取所有像素信息
    # for x in range(img_src.width):
    #     for y in range(img_src.height):
    #         print ('%d - %d : %s' % (x,y,src_strlist[x,y]))
    #         slity = src_strlist[x,y]
    #         slity_r = str(slity[0]).zfill(3)
    #         slity_g = str(slity[1]).zfill(3)
    #         slity_b = str(slity[2]).zfill(3)


def _kmeans(width,height):
    #初始化随机质心数组
    random_core= []
    #产生3个随机数
    for i in range(0,3):
        x = random.randint(1,width)
        y = random.randint(1,height)
        x_y = [x,y]
        random_core.append(x_y)
    #print(random_core)
    return random_core



if __name__ == '__main__':
    _loadimage_test()