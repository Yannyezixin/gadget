# coding:utf-8
# !/usr/bin/python2.7

from PIL import Image
import os


def zoomImg(img, size):
    """缩放图像大小函数"""
    disposedIm = os.path.splitext(img)[0] + '-dis.png'
    im = Image.open(os.path.join(os.getcwd(), 'img', img))
    size = disposeSize(im.size, size)
    newIm = im.resize(size)
    newIm.save(disposedIm)


def disposeSize(oldSize, size):
    rate = min(float(size[0]) / oldSize[0], float(size[1]) / oldSize[1])

    return (int(oldSize[0] * rate), int(oldSize[1] * rate))


if __name__ == '__main__':
    # 获取图片列表
    imglist = os.listdir(os.path.join(os.getcwd(), 'img'))
    iphone5sSize = (1136, 640)

    for i in range(len(imglist)):
        zoomImg(imglist[i], iphone5sSize)
