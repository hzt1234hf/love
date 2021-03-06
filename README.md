# 一、项目介绍
## 1.1 介绍
- 表白用的灯光控制系统，可以通过web页面控制灯光的开启，主要用的了树莓派zero w、继电器（8个）、稳压模块、各种led灯饰

## 1.2 用途及效果
- 用于表白
- 表白效果良好，已经成功，2021.3.28

# 二、项目所需软硬件环境
- 软件环境：
  - win 10
  - pycharm 2020.3.3
  - webstorm 2020.3.3
- 硬件环境：
  - 树莓派zero w 1个
  - 继电器模块 8个
  - 杜邦线 若干
  - 电平转换模块 1个
  - 5v/3v稳压模块 若干
  - led灯饰若干
    - 心形灯（挂在窗帘上的）
    - 星星灯（过道悬空的）
    - 棉球灯（用于摆放心形）
    - 电子蜡烛120个（用于摆放心形）
    - 彩虹灯（用于门框）
    - ILOVEU灯（墙上）
    - love灯（心形中间的）
    - 照片灯（悬挂于墙上）
    - 投影灯（心形中心位置）
  - 其他
    - 玩偶若干
    - 各色花瓣2000瓣
    - 会飞的蝴蝶20个

# 三、目录介绍
- core目录：树莓派 zero w控制代码
- web目录：网页端控制代码
- photo目录：介绍用图片

# 四、项目架构
## 4.1 用到的知识
- 语言：python、html、css、js
- 框架：flask、jQuery、树莓派官方库
- 技术：nginx、linux、一点电路知识

## 4.2 原理
- 通过python代码编写flask后台，并且使用树莓派官方的库进行GPIO端口的控制，使用静态html配合jQuery的ajax框架进行前后端通信，进而控制继电器的开合，实现灯光的开关效果

## 4.3 难点
- 挺简单的，就是比较耗时间，灯光布置需要精心考虑，代码很容易上手

# 五、项目展望
- 电子蜡烛需要手动摆放，并没有进行灯光控制，有精力的小伙伴可以将所有灯使用电线并联，使用继电器实现总体控制
- 原本计划小爱同学参与到控制中，但由于时间因素没有进行实现，可以使用ESP8266模块配合小爱同学实现一整套自动控制逻辑
- 拍照、摄像完全通过电脑和相机间隔拍照、一直录像实现，没有实现手动控制，可以增加控制功能
- 音乐完全是播放的自己选的网易云音乐中的音乐，没有进行控制，可以增加控制功能
- 本来打算加入投影仪播放视频的，但是由于时间限制，没有弄，可以增加投影仪播放视频的功能

# 六、项目演示

## 6.1灯光效果
![所有灯光打开效果1](./photo/1.JPG)
![所有灯光打开效果2](./photo/2.JPG)
![所有灯光打开效果3](./photo/3.JPG)
![所有灯光打开效果4](./photo/5.jpg)
![所有灯光打开效果5](./photo/6.jpg)

## 6.2控制器和网页端效果
![控制器接线](./photo/4.jpg)
![网页端](./photo/7.jpg)

