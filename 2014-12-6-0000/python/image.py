# coding:utf-8
# !/usr/bin/python2.7

from PIL import Image, ImageDraw, ImageFont
import os


class avatorRemind():

    @property
    def avator(self):
        return self._avator

    @avator.setter
    def avator(self, value):
        self._avator = value

    def __init__(self, avator):
        """初始化，传入要处理的图像"""
        self.avator = avator

    def generate(self):
        num = "3"
        nXsize, nYsize = 50, 50

        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-generate-num.jpg"
        xsize, ysize = im.size
        dr = ImageDraw.Draw(im)
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 50)
        dr.text((xsize - nXsize, 0), num, font=font, fill="#ff0000")
        im.save(outfile)

    """
    生成提醒数字: 此方法生成的数字有背景颜色。
    FIX:??
    def generate(self):
        num = "3"
        nXsize, nYsize = 50, 50
        imNum = Image.new("RGBA", (nXsize, nYsize), (255, 255, 255, 0))
        dr = ImageDraw.Draw(imNum)
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 40)
        dr.text((5, 5), num, font=font, fill="#ff0000")
        imNum.save("num.png")

        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-generate-num.jpg"
        xsize, ysize = im.size
        im.paste(imNum, (xsize - nXsize, 0, xsize, nYsize))
        im.save(outfile)
    """

    def convertToJPEG(self):
        """将图片转化为JPEG"""
        outfile = os.path.splitext(self.avator)[0] + ".jpg"
        if self.avator != outfile:
            try:
                Image.open(self.avator).save(outfile, "JPEG", quality=80)
                return outfile
            except IOError:
                print("Cannot convert to jpeg", self.avator)

    def cropAvator(self):
        """剪切图片另保存"""
        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-crop.png"
        box = (100, 100, 200, 200)
        im.crop(box).save(outfile)

    def transpose(self):
        """旋转图片"""
        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-transpose.png"
        box = im.size
        # im = im.rotate(45)
        im = im.transpose(Image.ROTATE_180)
        im.paste(im, box)
        im.save(outfile)

    def transposeCover(self):
        """旋转覆盖图片"""
        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-transpose-cover.png"
        box = (100, 100, 200, 200)
        region = im.crop(box)
        region = region.transpose(Image.ROTATE_180)
        im.paste(region, box)
        im.save(outfile)

    def roll(self):
        """卷动图片"""
        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-roll.png"
        xsize, ysize = im.size
        delta = 240
        delta = delta % xsize
        if delta == 0:
            return self.avator

        part1 = im.crop((0, 0, delta, ysize))
        part2 = im.crop((delta, 0, xsize, ysize))
        im.paste(part2, (0, 0, xsize-delta, ysize))
        im.paste(part1, (xsize-delta, 0, xsize, ysize))
        im.save(outfile)

    def splittingAndMergingBands(self):
        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-split-merge-band.png"
        r, g, b = im.split()
        im = Image.merge("RGB", (r, r, r)).save(outfile)

    def pointTransforms(self):
        im = Image.open(self.avator)
        outfile = os.path.splitext(self.avator)[0] + "-point-transform.png"
        source = im.split()

        R, G, B = 0, 1, 2
        # 选择红色值小于100的区域
        mask = source[R].point(lambda i: i < 100 and 255)
        # 处理绿色区域
        out = source[G].point(lambda i: i * 0.7)

        source[G].paste(out, None, mask)
        im = Image.merge(im.mode, source)
        im.save(outfile)

if __name__ == '__main__':
    avator = "avator.png"
    avatorRemind = avatorRemind(avator)
    avatorRemind.generate()

    """
    avatorToJPEG = avatorRemind.convertToJPEG()
    avatorRemind.cropAvator()
    avatorRemind.transpose()
    avatorRemind.transposeCover()
    avatorRemind.roll()
    avatorRemind.splittingAndMergingBands()
    avatorRemind.pointTransforms()
    """
    # print(modedAvator.format, modedAvator.size, modedAvator.mode)
