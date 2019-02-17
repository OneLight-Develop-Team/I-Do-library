# -*- coding:utf-8 -*-

# Require Header
import os
import json
from functools import partial

# Sys Header
import sys
import traceback
import subprocess

# Maya Header
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui


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
UI_PATH = os.path.join(DIR,"ui","Cam_Main.ui") 
GUI_STATE_PATH = os.path.join(DIR, "json" ,'GUI_STATE.json')
form_class , base_class = loadUiType(UI_PATH)

import Cam_Item_Layout
import Cam_Attrubte_Panel
reload(Cam_Item_Layout)
reload(Cam_Attrubte_Panel)
from Cam_Item_Layout import Cam_Item_Layout
from Cam_Attrubte_Panel import Cam_Attrubte_Panel

class Cam_Main(form_class,base_class):
    def __init__(self):
        super(Cam_Main,self).__init__()
        self.setupUi(self)
        
        self.Cam_Item_Widget = Cam_Item_Layout()
        self.Cam_Attrubte_Widget = Cam_Attrubte_Panel()
        splitter = QSplitter()
        splitter.setHandleWidth(5)
        splitter.addWidget(self.Cam_Item_Widget)
        splitter.addWidget(self.Cam_Attrubte_Widget)
        self.Main_Layout.layout().addWidget(splitter)

        self.Cam_Item_Widget.mousePressEvent = self.Cam_Item_Pressing_Event

        self.Default_Attr_Setting()
       
    
    def Default_Attr_Setting(self):
        self.Cam_Attrubte_Widget.Cam_Name_Label.setText(u"<center> - 请选择镜头 - </center>")
        self.Cam_Attrubte_Widget.Cam_Input_Toggle.setVisible(False)
        self.Cam_Attrubte_Widget.Cam_Input_Layout.setVisible(False)
        self.Cam_Attrubte_Widget.Cam_Output_Toggle.setVisible(False)
        self.Cam_Attrubte_Widget.Cam_Output_Layout.setVisible(False)




    
    def Cam_Item_Pressing_Event(self,e):
        """
        mousePressEvent 
        # Note 点击事件触发
        """
        ##   Note 清空所有颜色轮廓
        for i,child in enumerate(self.Cam_Item_Widget.Item_Layout.children()):
            if i != 0:
                if child.Cam_Item.styleSheet() != "":
                    child.Cam_Item.setStyleSheet("")

        for i,child in enumerate(self.Cam_Item_Widget.Item_Layout.children()):
            if i != 0:
                ##   Note 如果坐标匹配则载入相关数据
                if child.geometry().contains(e.pos().x(),e.pos().y()-60):
                    child.Cam_Item.setStyleSheet("#Cam_Item{border:3px solid red}" )

                    camName = child.Cam_LE.text()
                    self.Cam_Attrubte_Widget.Cam_Name_Label.setText(u"<center> - %s - </center>" % camName)
                    self.Cam_Attrubte_Widget.Cam_Input_Toggle.setVisible(True)
                    self.Cam_Attrubte_Widget.Cam_Input_Layout.setVisible(True)
                    self.Cam_Attrubte_Widget.Cam_Output_Toggle.setVisible(True)
                    self.Cam_Attrubte_Widget.Cam_Output_Layout.setVisible(True)
                    break
        else:
            ##   Note 遍历全部对象说民没有匹配
            self.Default_Attr_Setting()

         

