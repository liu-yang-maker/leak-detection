# -*- coding: utf-8 -*-

import numpy as np
import struct

#读取泄漏监测系统bin文件
def readBin(filePath):
    #file_path = unicode(file_path,'utf8')
    #file_path = str(file_path)
    file = open(filePath,'rb')
    
    file.seek(120,0)
    dataStr = file.read()
    file.close()
    
    dataLen = int(len(dataStr)/4)
    
    data = struct.unpack('>'+str(dataLen)+'f',dataStr)
    #data = struct.unpack('>71996f',data_str)

    data = np.array(data)
    #转换成列向量
    data = data.reshape(data.size)
    return data 

#生成读取文件路径，LabView程序生成的bin文件
def createBinPath(path,station_name,signal_type,station_type,year,month,day,hour):
    #file_path = '%s/%s%s/%s/%02年/%02d月/%02d日/%s%s%02d时.bin' % (path,station_name,signal_type,station_type,year,month,day,station_name,station_type,hour)   
    filePath = '%s/%s%s/%s/%d年/%02d月/%02d日/%s%s%02d时.bin' % (path,station_name,signal_type,station_type,year,month,day,station_name,station_type,hour) 
    return filePath