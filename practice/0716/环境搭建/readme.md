##  Pygame环境搭建

### 一 、安装pip

+++

pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。

get-pip.py 脚本可以帮助安装 pip 工具。

````c
sudo python3 get-pip.py
````

检查是否安装成功

```c
pip3 --version
```



### 二、安装pygame包

---

* **安装pygame依赖库**

  ```
  sudo apt-get install python3.7-dev mercurial
  sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
  sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
  sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
  sudo apt-get install python-numpy
  ```

* **安装pygame**

  ```
  sudo pip3 install pygame
  ```

  

### 三、运行代码

----

python是一种脚本语言,运行起来也特别简单，可以采用解释器加脚本文件的运行方式。可以在shell中执行如下命令

```
python3 plane_main.py
```







