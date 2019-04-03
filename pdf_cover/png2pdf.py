#coding:utf-8
import glob
import fitz
import os
import fnmatch


def pic2pdf(file_int):
    file_co = str(file_int)
    base_patch = 'D:/BaiduNetdiskDownload/[銃夢+外傳+Last.Order][木城幸人][天下][C.C][9完+1完+15未]/第一部/[Comic][銃夢][木城ゆきと][天下][C.C]Vol_0'+file_co +'/'
    target_fileName = '铳梦_1_Vol_0'+file_co+'.pdf'
    doc = fitz.open()
    files = fnmatch.filter(os.listdir(base_patch), '*.png')
    for img in files:
        img = base_patch + img
        print(img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    if os.path.exists(base_patch + target_fileName):
        os.remove(base_patch + target_fileName)
    doc.save(base_patch + target_fileName)                   # 保存pdf文件
    doc.close()

def load_all_pages():
    for i in range(1,10):
        pic2pdf(i)
if __name__ == '__main__':
    load_all_pages()
