# 长江雨课堂定时签到
## 食用方法
### 推荐：Github Actions
默认设置为 每周一至周五7:00~22:00，每5分钟运行一次检查，若发现新的课程则写入log.json

修改cron表达式,自行学习,注意corn使用0时区时间，应在东八区时间-8

1.按下面教程拿到SESSIONID，或者自己抓APP的包

2.按图中路径，配置名为SESSION的环境变量，值为SESSIONID的值
![图片1](img/Step_1.png)
![图片2](img/Step_2.png)

3.继续在设置中，修改选项(为了写入日志)
![图片3](img/Step_3.png)

3.去Action板块直接Run，测试是否通过
![图片4](img/Step_4.png)

4.查看日志log.json签到内容，如果已经签到过不再写入

### 部署在服务器
1.下载**server-use**文件夹

2.打开config.txt,填写SESSIONID

3.安装依赖
```bash
pip install requests
```
3.定时运行main.py(推荐使用宝塔面板定时任务，具体教程自行搜索)
```python
python main.py
```

4.查看日志log.json签到内容，如果已经签到过不再写入

## 获取SESSIONID方式

访问 https://changjiang.yuketang.cn/ ,登录后，按F12
![图片1](server-use/screenShot/1.png)
![图片2](server-use/screenShot/2.png)
![图片3](server-use/screenShot/3.png)
![图片4](server-use/screenShot/4.png)

复制粘贴得到的id到config.txt，并保存即可