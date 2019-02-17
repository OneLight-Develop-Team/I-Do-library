# -*- coding:utf-8 -*-
# Require Header
import os
import json
from functools import partial

# Sys Header
import sys
import traceback
import subprocess

import plugin.Qt as Qt
from Qt.QtCore import *
from Qt.QtGui import *
from Qt.QtWidgets import *

def loadUiType(uiFile):
    import plugin.Qt as Qt
    if Qt.__binding__.startswith('PyQt'):
        from Qt import _uic as uic
        return uic.loadUiType(uiFile)
    elif Qt.__binding__ == 'PySide':
        import pysideuic as uic
    else:
        import pyside2uic as uic
        
    import xml.etree.ElementTree as xml
    from cStringIO import StringIO

    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}

        uic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        # Fetch the base_class and form class based on their type
        # in the xml from designer
        form_class = frame['Ui_%s'%form_class]
        base_class = eval('%s'%widget_class)

    return form_class, base_class

from Qt.QtCompat import wrapInstance

DIR = os.path.dirname(__file__)
UI_PATH = os.path.join(DIR,"ui","Cam_Item_Layout.ui") 
GUI_STATE_PATH = os.path.join(DIR, "json" ,'GUI_STATE.json')
form_class , base_class = loadUiType(UI_PATH)

class Cam_Item_Layout(form_class,base_class):
    def __init__(self):
        super(Cam_Item_Layout,self).__init__()
        self.setupUi(self)
        self.Item_Add_BTN.clicked.connect(self.Item_Add_Fn) 
        self.Item_Clear_BTN.clicked.connect(self.Item_Clear_Fn) 

    def Item_Add_Fn(self):
        Cam_Item(self)
        
    def Item_Clear_Fn(self):
        for i,child in enumerate(self.Item_Layout.children()):
            if i != 0:
                child.deleteLater()
        
        


UI_PATH = os.path.join(DIR,"ui","Cam_Item.ui") 
form_class , base_class = loadUiType(UI_PATH)

class Cam_Item(form_class,base_class):
    def __init__(self,parent):
        super(Cam_Item,self).__init__()
        self.setupUi(self)
        self.Cam_Del_BTN.clicked.connect(self.Cam_Del_BTN_Fn)

        TotalCount = len(parent.Item_Layout.children())
        parent.Item_Layout.layout().insertWidget(TotalCount-1,self)
        self.Cam_LE.setText("Cam_Item_%s" % TotalCount)
        self.Cam_Num_Label.setText(u"镜头%s" % TotalCount)
        self.setObjectName("Cam_Item_%s" % TotalCount)
        self.num = TotalCount


    def Cam_Del_BTN_Fn(self):
        # self.deleteLater()
        
        # TotalCount = len(self.parent().children())
        ChildrenList = self.parent().children()
        print len(ChildrenList)

        for i in range(self.num,len(ChildrenList)):
            ChildrenList[i] = ChildrenList[i+1]
            if i+1 == len(ChildrenList):
                break

        for i,child in enumerate(ChildrenList):

                #     if i != 0:
    #         child.Cam_Num_Label.setText(u"镜头%s" % i)
    #         child.setObjectName("Cam_Item_%s" % i)




        # index = 999999
        # for i,child in enumerate(ChildrenList):
        #     if i != 0:
        #         child.Cam_Num_Label.setText(u"镜头%s" % i)
        #         child.setObjectName("Cam_Item_%s" % i)
        #         if child == self:
        #             index = i
        #         elif i < index:
        #             child.Cam_Num_Label.setText(u"镜头%s" % i)
        #             child.setObjectName("Cam_Item_%s" % i)
