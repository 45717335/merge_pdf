# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
def merge_pdf(infnList, outfn):
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        #print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))
'''
    遍历某个根文件夹,找到子文件夹名字相似于特定名字的时候,将其下面的PDF,合并为一个文件夹同名的pdf
    这里是: 01_OPERATING_INSTRUCTIONS 和 02_MAINTENANCE_INSTRUCTIONS
'''
def merge_pdf_folder(a_rootfd,b_tpfd):
    '''将指定根文件夹下的,特定子文件夹里面的pdf合并并保存再同一文件夹下'''
    for root, dirs, files in os.walk(a_rootfd):
        latdirs1=root.split("\\")[-1]
        if b_tpfd==latdirs1:
            spdfs=[]
            for file in files:
                if file[-4:]=='.pdf':
                    src_file = os.path.join(root, file)
                    spdfs.append(src_file)
            to_file=os.path.join(root,b_tpfd + ".pdf")
            if (not os.path.exists(to_file)) and len(spdfs)>0:
                merge_pdf(spdfs,to_file)
                print("new merge:{0}({1}pdf)".format(to_file,len(spdfs)))
            elif len(spdfs)>0:
                print("already exist:{0}({1}pdf)".format(to_file,len(spdfs)))
            else:
                print("no pdf:{0}".format(root))
print("说明:\n\t用于合并PDF\n输入:\n\t1.输入一个根目录.\n\t2.输入需要合并PDF的子目录(单独一个子目录名称)\n输出:\n\t根目录下的全部指定子目录如果包含.pdf则合并为该目录名的.pdf存放于该子目录下")
str1=input("\n请输入目标文件夹:")
str2=input("\n请输入需要合并的子文件夹名称:")
merge_pdf_folder(str1,str2)
input("Press any key to end!")
