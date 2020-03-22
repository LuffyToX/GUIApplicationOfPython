# PyQt5

PyQt5 官网：www.riverbankcomputing.co.uk

PyQt5 模块介绍的官网：http://pyqt.sourceforge.net/Docs/PyQt5/introduction.html

PyQt 是 Python 下的一套图形用户界面库，可以在 Python 中调用 Qt 的图形库和控件

PyQt 可以运行在所有主流的操作系统上

PyQt 采用双许可证：GPL 版（GNU General Public License）、商业版

Qt 和 PyQt 的设计都是完全面向对象的，Qt 使用一种称为 **信号/槽** 的机制在窗口控件之间传递事件和消息

PyQt5 官方默认只提供对 Python3 的支持，不再向下兼容 PyQt4



## PyQt5 整体结构

**PyQt5 的主要模块：**

+ QtCore：

  包含了核心的非 GUI 功能，用于处理程序中涉及的时间、文件、目录、数据类型、文本流、链接、QMimeData、线程或进程等对象

  

+ QtGui：

  包含了多种基本图形功能的类，包括：窗口集、事件处理、2D图形、基本的图像和界面、字体和文本类

  

+ QtWidgets：

  包含了一整套 UI 元素控件，用于建立符合系统风格的基础界面

  

+ QtMultimedia：

  包含了一套类库，用于处理多媒体事件，通过调用 API 接口访问摄像头、语音设备、收发消息等

  

+ QtBluetooth：

  包含了处理蓝牙活动的类库，其功能包括：扫描设备、连接、交互等行为

  

+ QtNetwork：

  包含了用于进行网络编程的类库

  

+ QtPositioning：

  用于获取位置信息，包括但不限于：卫星、无线网等，此模块一般用在网络地图定位系统中

  

+ Enginio：

  用于构建客户端的应用程序库，在运行时访问 Qt Cloud 服务器托管的应用程序

  

+ QtWebSockets：

  包含了一组类程序，用于实现 WebSocket 协议

  

+ QtWebKit：

  包含了用于实现基于 WebKit2 的网络浏览器的类库

  

+ QtWebKitWidgets：

  提供了一组类库，用于实现一种由 Widgets 包构建的、基于 WebKit 的网络浏览器

  

+ QtXml：

  包含了用于处理 XML 的类库，此模块为 SAX 和 DOM API 的实现提供了函数

  

+ QtSvg：

  通过一组类库，为显示矢量图形文件的内容提供了函数

  

+ QtSql：

  提供了数据库对象的接口

  

+ QtTest：

  包含了通过单元测试，调试 PyQt5 应用程序的功能

  

+ QtHelp：

  包含了用于创建和查看可查找的文档的类

  

+ QtOpenGL：

  使用 OpenGL 库来渲染 3D 和 2D 图形，该模块使得 Qt GUI 库和 OpenGL 库无缝集成

  

+ QtXmlPatterns：

  所包含的类实现了对 XML 和自定义数据模型的 Xquery 与 XPath 的支持

  

+ QtDesigner：

  所包含的类允许使用 PyQt 扩展 Qt Designer

  

+ Qt：

  将上面模块中的类综合到一个单一的模块中

  

+ uic：

  所包含的类用来处理 .ui 文件，将其编译为 .py 文件





**PyQt5 的主要类：**

PyQt5 API 拥有 620 多个类和 6000 个函数，它是一个跨平台的工具包，可以运行在所有主流的操作系统上

+ QObject：

  顶部类（Top Class），它是所有 PyQt 对象的基类

  

+ QPaintDevice：

  所有可绘制的对象的基类

  

+ QApplication：

  用于管理图形用户界面应用程序的控制流和主要设置。它包含主事件循环，对来自窗口系统和其他资源的所有事件进行处理和调度；它也对应用程序的初始化和结束进行处理，并且提供对话管理；还对绝大多数系统范围和应用程序范围的设置进行处理

  

+ QWidget：

  所有用户界面对象的基类，QDialog 类和 QFrame 类继承自 QWidget 类，这两个类有自己的子类系统

  

+ QFrame：

  有框架的窗口控件的基类，它也被用来直接创建没有任何内容的简单框架

  

+ QDialog：

  最普通的顶级窗口（顶级窗口是有框架和标题栏的窗口，如果一个窗口控件没有被嵌入到父窗口中，那么该窗口控件就被称为顶级窗口）。在 Qt 中，QMainWindow 和 QDialog 及其子类是最普通的顶级窗口
  
  

+ QMainWindow：

  提供一个有菜单栏、锚接窗口（如工具栏）和状态栏的主应用程序窗口





**主要类间的继承关系：**

![1](https://img-blog.csdnimg.cn/20200229152614301.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



![2](https://img-blog.csdnimg.cn/2020022915262835.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



![3](https://img-blog.csdnimg.cn/20200229152639605.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



![4](https://img-blog.csdnimg.cn/20200229152651126.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



![5](https://img-blog.csdnimg.cn/20200229152703131.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



**PyQt5 的主要控件：**

QWidget 是所有用户界面类的基类，它能接收所有的鼠标、键盘和其他系统窗口事件

QWidget 的构造函数可以接收两个参数，第一个参数是该窗口的父窗口；第二个参数是该窗口的 Flag

> 根据是否指定父窗口来决定 QWidget 是嵌入到父窗口中还是被当作一个独立的窗口来调用
>
> 根据 Flag，也就是 Qt.WindowFlags，来设置 QWidget 窗口的一些属性

QMainWindow 一般是应用程序的框架，在主窗口中可以添加所需要的 QWidget，如：菜单栏、工具栏、状态栏

+ QLabel：

  用来显示文本或图像

  

+ QLineEdit：

  提供了一个单页面的单行文本编辑器

  

+ QTextEdit：

  提供了一个单页面的多行文本编辑器

  

+ QPushButton：

  提供了一个命令按钮

  

+ QRadioButton：

  提供了一个单选钮和一个文本或像素映射标签

  

+ QCheckBox：

  提供了一个带文本标签的复选框

  

+ QSpinBox：

  允许用户选择一个值，要么通过按 上/下 键 增加/减少 当前显示值，要么直接将值输入到输入框中

  

+ QScrollBar：

  提供了一个水平的或垂直的滚动条

  

+ QSlider：

  提供了一个垂直的或水平的滑动条

  

+ QComboBox：

  一个组合按钮，用于弹出列表

  

+ QMenuBar：

  提供了一个横向菜单栏

  

+ QStatusBar：

  提供了一个适合呈现状态信息的水平条，通常放在 QMainWindow 的底部

  

+ QToolBar：

  提供了一个工具栏，可以包含多个命令按钮，通常放在 QMainWindow 的顶部

  

+ QListView：

  可以显示和控制可选的多选列表，可以设置 ListMode / IconMode

  

+ QPixmap：

  可以在绘图设备上显示图像，通常放在 QLabel / QPushButton 类中

  

+ QDialog：

  对话框窗口的基类



**QApplication 类：**

QApplication 类用于管理图形用户界面应用程序的控制流和主要设置，可以说 QApplication 是 PyQt 的整个后台管理的命脉，任何一个使用 PyQt 开发的图形用户界面应用程序，都存在一个 QApplication 对象。

在 PyQt 中，可以通过如下代码载入必需的模块，获得 QApplication 类：

​                                                     `from PyQt5.QtWidgets import QApplication`

QApplication类的初始化可以参考以下脚本引用：

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 对象做了很多初始化，故它必须在创建窗口之前被创建
                                  # QApplication 类初始化时，需要引入参数 sys.argv
    win = QWidget()
    win.show()
    sys.exit(app.exec_())         # sys.exit() 函数可以结束一个应用程序，使应用程序在主循环中退出
```

QApplication 采用事件循环机制，当 QApplication 初始化后，就进入应用程序的主循环（Main Loop），开始进行事件处理，主循环从窗口系统接收事件，并将这些事件分配到应用程序的控件中。当调用 sys.exit() 函数时，主循环就会结束。PyQt5 的应用程序是事件驱动的，比如键盘事件、鼠标事件等。在没有任何事件的情况下，应用程序处于睡眠状态。主循环控制应用程序什么时候进入睡眠状态，什么时候被唤醒

 



## PyQt5 环境的搭建

Windows 下使用豆瓣镜像

**PyQt5 的安装**：`pip install PyQt5 -i "https://pypi.douban.com/simple"` 

**常用 Qt 工具的安装**：`pip install PyQt5-tools -i "https://pypi.douban.com/simple"`

为让系统能够正确识别 PyQt5-tools 的常用命令，还需要将 PyQt5-tools 的安装目录添加到系统环境变量 path 中





## Qt Designer 的汉化

将汉化包放入路径  `...\Anaconda3\Lib\site-packages\pyqt5_tools\Qt\bin\translations\` 下





## Pycharm 添加 Qt Designer

File  ==>  Settings  ==>  Tools  ==>  External Tools   进入外部工具添加界面

![图1](https://img-blog.csdnimg.cn/20200212153827668.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



Name  ==>  Qt Designer
Tool Settings  ==>  Program  ==>  Qt Designer 安装路径

> `...\Anaconda3\Lib\site-packages\pyqt5_tools\Qt\bin\designer.exe`

Tool Settings  ==>  Working directory  ==>  `$FileDir$` （表示当前文件所在目录）

![图2](https://img-blog.csdnimg.cn/20200212154845672.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



添加完成后，可以在  Tools  ==>  External Tools  中查看与打开

![图3](https://img-blog.csdnimg.cn/20200212155229616.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)





## Pycharm 添加 PyUic

File  ==>  Settings  ==>  Tools  ==>  External Tools   进入外部工具添加界面

![图1](https://img-blog.csdnimg.cn/20200212153827668.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



Name  ==>  PyUic
Tool Settings  ==>  Program  ==>  Python 安装路径

> ...\Anaconda3\python.exe

Tool Settings  ==>  Arguments  ==>  执行参数

> `-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py`
>
> (`$FileNameWithoutAllExtensions$` / `FileNameWithoutExtension`)

Tool Settings  ==>  Working directory  ==>  `$FileDir$`  （表示当前文件所在目录）

![图4](https://img-blog.csdnimg.cn/20200213111533491.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



添加完成后只需选中 .ui 文件，然后：Tools  ==>  External Tools  ==>  PyUic





## Pycharm 添加 Pyrcc

File  ==>  Settings  ==>  Tools  ==>  External Tools   进入外部工具添加界面

![图1](https://img-blog.csdnimg.cn/20200212153827668.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



Name  ==>  Pyrcc
Tool Settings  ==>  Program  ==>  Pyrcc 安装路径

> ...\Anaconda3\Scripts\pyrcc5.exe

Tool Settings  ==>  Arguments  ==>  执行参数

> `$FileName$ -o $FileNameWithoutAllExtensions$.py`
>
> (`$FileNameWithoutAllExtensions$` / `FileNameWithoutExtension`)

Tool Settings  ==>  Working directory  ==>  `$FileDir$`  （表示当前文件所在目录）

![图5](https://img-blog.csdnimg.cn/20200217233732325.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjY0Nzc3,size_16,color_FFFFFF,t_70)



添加完成后只需选中 .qrc 文件，然后：Tools  ==>  External Tools  ==>  Pyrcc





## 将 .ui 文件转换为 .py 文件

**命令行**

Windows 下切换盘符（如：切换到 D 盘）>> D: 

Windows 下切换目录（如：切换到 C 盘根目录下的 new 文件夹）>> cd new

cmd 进入项目目录  ==>  `pyuic5 -o somefile.py somefile.ui`



**Pychram**

Pycharm 打开项目目录，选中 .ui 文件，然后： Tools  ==>  External Tools  ==>  PyUic





## 将 .qrc 文件转换为 .py 文件

**命令行**

cmd 进入项目目录  ==>  `pyrcc5 somefile.qrc -o somefile_rc.py`

> 转换后的 .py 文件之所以要加 _rc，是因为 Qt Designer 导入资源文件时是默认加 _rc 的



**Pycharm**

Pycharm 打开项目目录，选中 .ui 文件，然后： Tools  ==>  External Tools  ==>  Pyrcc

> 如果 Pyrcc 工具转换出来的 .py 文件不带后缀 `_rc` ，要修改为带后缀 `_rc` 的 .py 文件





## Pycharm 中 import 自定义的 .py 文件

项目根目录：右键  ==>  Mark Directory as  ==>  Sources Root



## 运行界面问题

Pycharm：实际运行界面与 Qt Designer 预览界面不一致的解决方案

```python
if __name__ == "__main__":
    # 在测试中添加下述代码
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
```



