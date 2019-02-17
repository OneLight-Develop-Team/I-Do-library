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

from maya import cmds

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

class Cam_Attribute_Panel(form_class,base_class):
    def __init__(self):
        super(Cam_Attribute_Panel,self).__init__()
        self.setupUi(self)

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

        # Note - 选择功能函数
        self.Add_Crv_Get.setVisible(False)
        self.Add_Crv_Pick.clicked.connect(self.Add_Crv_Pick_Fun)

        self.Add_Loc_Get.setVisible(False)
        self.Add_Loc_Pick.clicked.connect(self.Add_Loc_Pick_Fun)

    def Add_Crv_Pick_Fun(self):
        if len(cmds.ls(sl=True)) > 0:
            self.Add_Crv_LE.setText(cmds.ls(sl=True)[0])
            try :
                self.Add_Crv_Get.clicked.disconnect()
            except:
                pass
            self.Add_Crv_Get.clicked.connect(partial(self.Select_OBJ_Fun,cmds.ls(sl=True)[0]))
        else :
            self.Add_Crv_LE.setText("")
        
        if self.Add_Crv_LE.text() != "":
            self.Add_Crv_Label.setVisible(False)
            self.Add_Crv_Get.setVisible(True)
        else:
            self.Add_Crv_Label.setVisible(True)
            self.Add_Crv_Get.setVisible(False)

    def Add_Loc_Pick_Fun(self):
        if len(cmds.ls(sl=True)) > 0 :
            Selection = cmds.ls(sl=True)[0] 
            SelectionShape = cmds.listRelatives(Selection)[0]
            SelectionType = cmds.nodeType( SelectionShape )
            if SelectionType == "locator":
                self.Add_Loc_LE.setText(Selection)
                try :
                    self.Add_Loc_Get.clicked.disconnect()
                except:
                    pass
                self.Add_Loc_Get.clicked.connect(partial(self.Select_OBJ_Fun,Selection))
        else :
            self.Add_Loc_LE.setText("")
        
        if self.Add_Loc_LE.text() != "":
            self.Add_Loc_Label.setVisible(False)
            self.Add_Loc_Get.setVisible(True)
        else:
            self.Add_Loc_Label.setVisible(True)
            self.Add_Loc_Get.setVisible(False)

    def Cam_Input_Toggle_Fn(self):
        if self.Cam_Input_Toggle_Check:
            self.Cam_Input_Toggle_Check = False
            self.Cam_Input_Toggle_Anim.setDirection(QAbstractAnimation.Forward)
            self.Cam_Input_Toggle_Anim.start()
            self.Cam_Input_Toggle.setText(u"▼输入设置")
            self.Cam_Input_Toggle.setStyleSheet('font:normal')
        else:
            self.Cam_Input_Toggle_Check = True
            self.Cam_Input_Toggle_Anim.setDirection(QAbstractAnimation.Backward)
            self.Cam_Input_Toggle_Anim.start()
            self.Cam_Input_Toggle.setText(u"■输入设置")
            self.Cam_Input_Toggle.setStyleSheet('font:bold')

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

    def Select_OBJ_Fun(self,selectTarget):
        if selectTarget != "":
            cmds.select(selectTarget)