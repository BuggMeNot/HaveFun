# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:18:19 2017

@author: adminuser
"""


#!/usr/bin/python
import os, re, datetime, xlrd, xlwt


def find_file():
        """
        --查找文件，即遍历文件树将查找到的文件放在文件集合中
        :return:
        """
        
        file_path = 'C:\\FindCode\\tofind\\'
        input_file = "C:\\FindCode\codetype.csv"
    
        filelist = []
        file_p = []
        for root, dirs, files in os.walk(file_path, topdown=True):
            for name in files:
                
                filelist.append(name.split('-')[1])
                
                file_p.append(os.path.join(root,name))
                
                #     print(os.path.join(root, name))
                # for name in dirs:
                #     print(os.path.join(root, name))
        
        return file_p

def search():
    
    print datetime.datetime.now()
   
    file_path = 'C:\\FindCode\\tofind\\'
    input_file = "C:\\FindCode\codetype.csv"
    f = open(input_file, "r")
    old_content = f.read()
    f.close()
    input_files_read = old_content.split('\n')
    count = 0
    
    file_p = find_file()
    col_name = 'Codetype' + '\t' + 'ColName' + '\t' +'TableName'
    for item1 in file_p:
        
        data = xlrd.open_workbook(item1)
        table = data.sheets()[0]
        col1 = table.col_values(0)
        temp_r = []
        temp_r.append(col_name)
        for item2 in input_files_read:
            if item2:
                temp_count = 0
                for content in col1:
                    distance = abs(len(item2)-len(content))
                    item2 = item2.lstrip('"')
                    item2 = item2.rstrip('"')
                    # 从input_files中读到的为'"string"'的形式，需要去掉双引号之后与'string'进行匹配，否则无返回结果
                    searchObj = re.search( item2 + '.*', content, re.M | re.I)
                    # 正则匹配，无视大小写
                    
                    if searchObj and distance<1: 
                    #如不指定字符长度差，则会出现flag匹配出很多结果的情况，这里是为了去除不必要的匹配结果
                        content = str(item2) + '\t' +content
                        temp_r.append(content)
                        
                    else:
                        continue
                        
                input_files_out = temp_r
                temp_count = len(temp_r)-1
        count = count + temp_count
        print count        
            
        try:
            result = ''
            for item3 in input_files_out:
                item3 = str(item3)
                result += item3 + '\t' + item1.split("\\")[-1].split('.')[0] + '\n' 
                # 结果以 查找目标，查找结果，表名的形式展现
                
            f = file("C://FindCode/result_files.txt", "a")
            f.write('\n')
            f.write(result)
            f.close()
        except IOError, msg:
            print "Error:", msg
        else:
            print 'Table'+ '  '+ item1.split("\\")[-1].decode('GBK')+' ' + "is OK"   
    print datetime.datetime.now()

if __name__=="__main__":
    search()
