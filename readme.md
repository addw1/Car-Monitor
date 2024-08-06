# 上位机软件开发文档

## 1. 软件整体架构

**PART1** QT软件开发

**PART2** 服务器环境搭建

**PART3** 在ROS中建立发送和接收节点



## 2.QT软件开发

### 2.1 Qt 前端界面设计

#### 	2.1.1 Qt界面设计介绍

所有界面UI内容由Qt Designer完成，文件存储在 *qtUiFile* 文件夹中。通过转换工具可将 ui 文件转换成 py 文件，转换工具在pycharm中的配置方法为：https://blog.csdn.net/wang_hugh/article/details/88775868。转换后的文件全部存储在 Ui 文件夹中。相关图片资源在qtQrc中，同样通过转换工具完成转换。

如果需要对界面进行修改，步骤如下：1. 进入qtUiFile中，找到相关的Ui文件。通过Qt Designer将它们打开，打开修改完成后保存。接下来在Pycharm中，右键通过external tool进行转换，转换完成后得到相关python文件。最后移动到Ui文件夹即可。

#### 								2.1.2加载QT界面

首先下列代码加载Ui文件，之后 ui 成员变量中会有所有界面组件。

```python
     # 加载UI文件
        self.ui = MainWindowUi()
        self.ui.setupUi(self)
```

接下来初始化各个成组件，既在类中为各个组件设置变量。python中两个变量赋值，不会新开辟一片地址，而是指向同一个地址。例如

```python
b = 66
a = b
```

<img src="https://pic4.zhimg.com/80/v2-fe64212de94f9d1d5ce73c3cc7497793_1440w.webp" alt="img" style="zoom:50%;" />

最后为各个组件添加界面逻辑即可。这里采用Qt独有的`信号-槽机制`。

#### 	2.1.3 主界面设计



主界面代码位于mainWindow.py文件（Gui文件夹）。其主要作用为接收后端线程消息，用户输入指令，并将内容更新到界面上，如下图所示。



主界面主要包含两个容器，为`mainContainer`和`bottomContainer`。mainContainer为上方纯白色区域，bottomContainer为下方灰色区域。mainContainer容器用于存储主页面**MainPage**。bottomContainer容器用于储存6个按钮。



**按钮的逻辑添加**

按钮的作用是切换界面。

通过`btn_init()`连接按钮与`change_moudle()`函数，将按钮与change_module函数进行连接，既按钮每点击一次会触发一次change_module函数。change_module根据传入的参数进行页面切换。

**添加主页面mainPgae**

先为**mainContainer**设置layout（布局)，之后初始化主页面。

```python
self.layout = QStackedLayout()
self.mainContainer.setLayout(self.layout)
self.mainPage = MainPage()
self.layout.addWidget(self.mainPage)
```



**初始化后端线程并启动**

网上大部分教程使用qt线程的方式为：

```python
class Thread(QThread):
    def __init__(self):
        super(Thread,self).__init__()
    def run(self):
        #业务逻辑代码

#创建一个新的线程
thread = Thread()
thread.start()
```

这样的做法能够线程正常运行，但是Qt官方并不推荐这种做法。

推荐的做法是先自己定义一个线程类，这个类要继承**QObject**，**在里面实现线程的相关业务逻辑**，同时在主界面里**实例化这个线程类**，然后用**moveToThread**方法移动到**QThread**管理。

```python
# PyQt线程科学用法
self.thread = QThread()
#实例外线程对象 workThread是自己写的线程类
self.work_thread = workThread()
# 把实例化的线程用moveToThread移到QThread管理
self.work_thread.moveToThread(self.thread)
```

```python
class workThread(QObject):
    def __init__(self):
        super(workThread, self).__init__()
    def work(self):
				# 你的业务逻辑代码
```

本项目共包含三个线程，在后面会依依介绍。

**远程控制功能**

通过Qt提供的keyPressEvent读取键盘命令，如果开启远程控制，则将命令传输出去。是否开启远程控制由按钮控制，按钮显示`远程控制`时表示**开启**，显示`监测`时表示**关闭**。

命令由publisher线程接收。



#### 	2.1.4 主页面设计

mainPage.ui为主界面的ui设计图。



在mainPage.py中，首先为这些将这些组件初始化。其中中间灰色部分为centerFrame组件。为该组件添加堆栈stack布局。QStackedLayout主要用于Qt界面中的布局切换。通过Api `setCurrentIndex`可以切换显示的界面。在mainPage通过设立`set_center_content`接口完成通过点击按钮切换界面，具体原理如下：







其他几个API口（设置速度、位置、图像信息）的建立过程和上述过程基本相同，在此不再进行介绍。

----

### 2.2 QT后端设计

#### 2.2.1 位置/速度接收线程

在mainWindow中启动线程后，该线程会进入wrok()函数。work()函数是一个死循环，它会一直等待mqtt服务器相关信息的发布，每接收到一次信息调用一次回调。



#### 2.2.2 控制命令发布线程

控制命令由键盘进行输入，控制方式为：

```text
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
```



#### 2.2.3 图像接收线程

图像信息通过UDP传输，使用时需要修改IP地址。



-----

### 2.3 云服务器搭载

相关视频链接https://www.bilibili.com/video/BV1wM411t7CH/?spm_id_from=333.337.search-card.all.click&vd_source=f71d184c112ea6517078404a8fb1dab0

EMQX 官方文档https://www.emqx.io/docs/zh/v5/getting-started.html#%E7%89%88%E6%9C%AC%E9%80%89%E6%8B%A9

-----

### 2.4 在ROS中搭建信息采集程序

在Test文件夹中是采集程序，为模拟在ros中的情况，实际过程需要按需更改。
