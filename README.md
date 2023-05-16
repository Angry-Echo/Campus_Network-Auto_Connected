# 校园网自动联网（重连）脚本，断网后自动连接
## 不需要配合win10的什么定时计划程序，什么都不用，只需要运行脚本代码即可
## 开发的起始需求：通宵跑需要联网的软件 或 长期远程控制实验室主机，但校园网凌晨自动断网
----
# What do you need
+ 一个 *python 3* 及以上的解释器
+ 下载 *WebDriver*（一个允许你与 Edge 浏览器交互的小文件）
+ 安装 Selenium
# How to install
+ *python* 无需赘述
+ *WebDriver*
  + 进入 Edge--设置--关于Microsoft Edge (edge://settings/help)
  + 查看 Edge 版本，如：版本 113.0.1774.42 (正式版本) (64 位)
  + 转到 [Microsoft Edge WebDriver](https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/)，下载与你的版本完全匹配的
  + 提取文件夹，并将其中包含的可执行文件(.exe)添加到 PATH 环境变量
  + 上一步中如果不添加，也可以在 Main.py 中第22行代处实例化类时将可执行文件的路径作为参数传递
+ *Selenium*
  + pip/conda install selenium  
----
# How to use
+ 如果你在西安石油大学读书：
  + 在 cmd 中运行 Main.py
  + 输入你需要监控的时间（你如果10点睡觉，校园网12点断网，请设置大于120分钟）
  + 输入你的校园网账号
  + 输入密码
  + 上床睡觉!
  + 操作演示截图：<br>
  ![image](https://github.com/Angry-Echo/Campus_Network-Auto_Connected/assets/80184919/ecfb0452-cbf7-4f34-80a0-cca21bea50d1)
+ 如果你在其他学校读书：
  + 在 Login.py 中修改贵校校园网 Web 页面中的控件位置
  + 在 Main.py 中修改贵校校园网 ip
# 演示视频
https://github.com/Angry-Echo/Campus_Network-Auto_Connected/assets/80184919/c9cc9b77-c572-46a0-8a5f-f9ab43cf2ad2

引用：
> https://learn.microsoft.com/zh-cn/microsoft-edge/webdriver-chromium/?tabs=c-sharp
> https://github.com/KuangenZhang/net_connect
