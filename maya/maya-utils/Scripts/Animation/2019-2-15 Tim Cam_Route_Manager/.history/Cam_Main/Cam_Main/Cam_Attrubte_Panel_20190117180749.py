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
UI_PATH = os.path.join(DIR,"ui","Cam_Attrubte_Panel.ui") 
GUI_STATE_PATH = os.path.join(DIR, "json" ,'GUI_STATE.json')
form_class , base_class = loadUiType(UI_PATH)

class Cam_Attrubte_Panel(form_class,base_class):
    def __init__(self):
        super(Cam_Attrubte_Panel,self).__init__()
        self.setupUi(self)
        self.Cam_Input_Layout.setEnabled(False)
        self.Cam_Output_Layout.setEnabled(False)

        # Note - 动画切换效果
        self.Cam_Input_Toggle_Anim = QPropertyAnimation(self.Cam_Input_Layout, b"maximumHeight")
        self.Cam_Input_Toggle_Anim.setDuration(300)
        self.Cam_Input_Toggle_Anim.setStartValue(0)
        self.Cam_Input_Toggle_Anim.setEndValue(self.Cam_Input_Layout.sizeHint().height())
        self.Cam_Input_Toggle_Check = False
        self.Cam_Input_Toggle.clicked.connect(self.Cam_Input_Toggle_Fn)

        self.Cam_Output_Toggle_Anim = QPropertyAnimation(self.Cam_Output_Layout, b"maximumHeight")
        self.Cam_Output_Toggle_Anim.setDuration(300)
        self.Cam_Output_Toggle_Anim.setStartValue(0)
        self.Cam_Output_Toggle_Anim.setEndValue(self.Cam_Output_Layout.sizeHint().height())
        self.Cam_Output_Toggle_Check = False
        self.Cam_Output_Toggle.clicked.connect(self.Cam_Output_Toggle_Fn)


    def Cam_Intput_Toggle_Fn(self):
        if self.Cam_Intput_Toggle_Check:
            self.Cam_Intput_Toggle_Check = False
            self.Cam_Intput_Toggle_Anim.setDirection(QAbstractAnimation.Forward)
            self.Cam_Intput_Toggle_Anim.start()
            self.Cam_Intput_Toggle.setText(u"▼输入设置")
            self.Cam_Intput_Toggle.setStyleSheet('font:normal')
        else:
            self.Cam_Intput_Toggle_Check = True
            self.Cam_Intput_Toggle_Anim.setDirection(QAbstractAnimation.Backward)
            self.Cam_Intput_Toggle_Anim.start()
            self.Cam_Intput_Toggle.setText(u"■输入设置")
            self.Cam_Intput_Toggle.setStyleSheet('font:bold')

    def Cam_Output_Toggle_Fn(self):
        if self.Cam_Output_Toggle_Check:
            self.Cam_Output_Toggle_Check = False
            self.Cam_Output_Toggle_Anim.setDirection(QAbstractAnimation.Forward)
            self.Cam_Output_Toggle_Anim.start()
            self.Cam_Output_Toggle.setText(u"▼输出设置")
            self.Cam_Output_Toggle.setStyleSheet('font:normal')
        else:
            self.Cam_Output_Toggle_Check = True
            self.Cam_Output_Toggle_Anim.setDirection(QAbstractAnimation.Backward)
            self.Cam_Output_Toggle_Anim.start()
            self.Cam_Output_Toggle.setText(u"■输出设置")
            self.Cam_Output_Toggle.setStyleSheet('font:bold')