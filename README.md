# 智联简历自动刷新脚本

### 参考
> [https://x2v3.com/archives/304](https://x2v3.com/archives/304)
> 
> [OS X 添加定时任务](http://codingpub.github.io/2016/10/27/OS-X-%E6%B7%BB%E5%8A%A0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1/)

### 使用
1. 在浏览器上打开[智联](https://www.zhaopin.com/)并登录账号
2. 打开浏览器的开发中工具中的控制台，输入 ```document.cookie``` 并复制打印出来的cookie的字符串，注意不要两头的引号。
3. 新建一个文本文件并将 Cookie 保存在你的文件中
4. 打开终端指定命令 ```python3 ./refresh.py yourCookieFile.txt```



### 使用 **crontab** 定时刷新

1. 编辑 crontab

```
$ crontab -e
```

2. 输入命令

```
$ 0 */2 * * * /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/joe-c/Downloads/ZhiLianRefresh/refresh.py /Users/joe-c/Downloads/ZhiLianRefresh/cookie.txt >>/Users/joe-c/Desktop/log.text
```
> 每两小时执行一次脚本, 并将输出重定向到 log.text 中记录下来

3. 查看定时任务

```
$ crontab -l
```
