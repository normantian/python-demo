# -*- coding: utf-8 -*-
import os
import os.path
import codecs

from xml.etree import ElementTree

def walkRoot(rootdir=None):
    if rootdir is None:
        return
    if os.path.isdir(rootdir): # 文件夹处理
        for parent,dirnames,filenames in os.walk(rootdir):
            for filename in filenames:
                if os.path.splitext(filename)[1] == '.calculationview' and filename[:3]=='CV_':
                    filePath = os.path.join(parent,filename)
                    analysisFile(rootdir,filePath,filename)
    else:
        #单独文件处理
        rootPath = os.path.dirname(rootdir) #文件路径
        filename = os.path.basename(rootdir) #文件名
        if os.path.splitext(filename)[1] == '.calculationview' and filename[:3]=='CV_':
            analysisFile(rootPath,rootdir,filename)

def analysisFile(rootdir,filePath,filename):
    txtFile = rootdir+'\\'+filename[:filename.find('.')]+'.txt'
    if os.path.exists(txtFile):
        os.remove(txtFile)
    f = codecs.open(txtFile,'w','utf-8')
    tree = ElementTree.parse(filePath)
    root = tree.getroot()
    model_name = tree.find('descriptions').attrib['defaultDescription']
    print '=='*10,filePath,model_name,'=='*10
    #print 'text : ',tree.find('localVariables').text
    if len(root.find('localVariables/variable').getchildren()) > 0:
        f.write('=='*10 + model_name + ' input parameter'+ '=='*10 + '\r\n')
        for element in tree.findall('localVariables/variable'):
            element_id = element.attrib['id']
            desc = element.find('descriptions').attrib['defaultDescription']
            datatype = element.find('variableProperties').attrib['datatype']
            if element.find('variableProperties').attrib.has_key('length'):
                length = element.find('variableProperties').attrib['length']
                f.write('%s  \t%s  \t%s(%s)\r\n' %(element_id,desc,datatype,length))
            else:
                f.write('%s  \t%s  \t%s\r\n' %(element_id,desc,datatype))
    #output param
    #print '=='*10,model_name,'output parameter','=='*10
    f.write('=='*10 + model_name + ' output parameter'+ '=='*10 + '\r\n')
    outputDic = {}
    for element in tree.findall('logicalModel/attributes/attribute'):
        element_id = element.attrib['id']
        desc = element.find('descriptions').attrib['defaultDescription']
        outputDic[element_id] = desc
        #element.find('keyMapping').attrib['columnName']
        #print '%s  %s' %(element_id,desc)
    for element in tree.findall('logicalModel/baseMeasures/measure'):
        element_id = element.attrib['id']
        desc = element.find('descriptions').attrib['defaultDescription']
        outputDic[element_id] = desc
    for element in tree.findall('calculationViews/calculationView/viewAttributes/viewAttribute'):
        datatype = element.attrib['datatype']
        element_id = element.attrib['id']
        if element.attrib.has_key('length') and element.attrib.has_key('scale'):
            #print '%s  %s  %s(%s,%s)' %(element_id,outputDic[element_id],datatype,element.attrib['length'],element.attrib['scale'])
            f.write('%s  \t%s  \t%s(%s,%s)\r\n' %(element_id,outputDic[element_id],datatype,element.attrib['length'],element.attrib['scale']))
        elif element.attrib.has_key('length'):
            #print '%s  %s  %s(%s)' %(element_id,outputDic[element_id],datatype,element.attrib['length'])
            f.write('%s  \t%s  \t%s(%s)\r\n' %(element_id,outputDic[element_id],datatype,element.attrib['length']))        
        else:
            #print '%s  %s  %s' %(element_id,outputDic[element_id],datatype)
            f.write('%s  \t%s  \t%s\r\n' %(element_id,outputDic[element_id],datatype))
    f.close()


if __name__=='__main__':
    #文件夹扫描
    #walkRoot('C:/Users/Norman/Desktop/DEV/WD1/HN/YWFX')
    #单个文件
    walkRoot('C:/Users/Norman/Desktop/DEV/WD1/HN/YWFX/SC/calculationviews/CV_SC_GR_MON.calculationview')
    print '=='*10,'well done!!!','=='*10
