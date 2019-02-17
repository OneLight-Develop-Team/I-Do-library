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
        Item = Cam_Item()
        num = len(self.Item_Layout.children())
        
        self.Item_Layout.layout().insertWidget(0,Item)
        for i,child in enumerate(self.Item_Layout.children()):
            if i != 0:
                Item.Cam_Num_Label.setText(u"序号%s" % num)

    def Item_Clear_Fn(self):
        for i,child in enumerate(self.Item_Layout.children()):
            if i != 0:
                child.deleteLater()
        
        


UI_PATH = os.path.join(DIR,"ui","Cam_Item.ui") 
form_class , base_class = loadUiType(UI_PATH)

class Cam_Item(form_class,base_class):
    def __init__(self):
        super(Cam_Item,self).__init__()
        self.setupUi(self)
        self.Cam_Del_BTN.clicked.connect(self.Cam_Del_BTN_Fn) 

    def Cam_Del_BTN_Fn(self):
        self.deleteLater()