#coding=utf-8
import fitz
import os
import fnmatch

path = "D:/BaiduNetdiskDownload/gunslinger girl/gunslinger girl/[Comic][gunslingergirl][REX3688]Vol_15"

def pic2pdf(file_name):
    file_co = str(file_name)
    base_patch = path + "/" + file_co
    target_fileName = file_co + '.pdf'
    doc = fitz.open()
    files = fnmatch.filter(os.listdir(base_patch), '*.[jp][pn]g')
    for img in files:
        img = base_patch + '/' + img
        print(img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    if os.path.exists(base_patch + target_fileName):
        os.remove(base_patch + target_fileName)
    doc.save(base_patch + target_fileName)                   # 保存pdf文件
    doc.close()

def listPath():
    for name in os.listdir(path):
        print name
        pic2pdf(name)

if __name__ == '__main__':
    listPath()

