# 一个python爬虫小程序

## 起因
深夜忽然想下载一点电子书来扩充一下kindle，就想起来python学得太浅，什么“装饰器”啊、“多线程”啊都没有学到。

想到廖雪峰大神的python教程很经典、很著名。就想找找有木有pdf版的下载，结果居然没找到！！CSDN有个不完整的还骗走了我一个积分！！尼玛！！

怒了，准备写个程序直接去爬廖雪峰的教程，然后再html转成电子书。


## 过程

过程很有趣呢，用浅薄的python知识，写python程序，去爬python教程，来学习python。想想有点小激动……

果然python很是方便，50行左右就OK了。直接贴代码：

    # coding:utf-8
    import urllib
    
    domain = 'http://www.liaoxuefeng.com'           #廖雪峰的域名
    path = r'C:\Users\cyhhao2013\Desktop\temp\\'    #html要保存的路径
    
    # 一个html的头文件
    input = open(r'C:\Users\cyhhao2013\Desktop\0.html', 'r')
    head = input.read()
    
    # 打开python教程主界面
    f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
    home = f.read()
    f.close()
    
    # 替换所有空格回车（这样容易好获取url）
    geturl = home.replace("\n", "")
    geturl = geturl.replace(" ", "")
    
    # 得到包含url的字符串
    list = geturl.split(r'em;"><ahref="')[1:]
    
    # 强迫症犯了，一定要把第一个页面也加进去才完美
    list.insert(0, '/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')
    
    # 开始遍历url List
    for li in list:
        url = li.split(r'">')[0]
        url = domain + url              #拼凑url
        print url
        f = urllib.urlopen(url)
        html = f.read()
    
        # 获得title为了写文件名
        title = html.split("<title>")[1]
        title = title.split(" - 廖雪峰的官方网站</title>")[0]
    
        # 要转一下码，不然加到路径里就悲剧了
        title = title.decode('utf-8').replace("/", " ")
    
        # 截取正文
        html = html.split(r'<!-- block main -->')[1]
        html = html.split(r'<h4>您的支持是作者写作最大的动力！</h4>')[0]
        html = html.replace(r'src="', 'src="' + domain)
    
        # 加上头和尾组成完整的html
        html = head + html+"</body></html>"
    
        # 输出文件
        output = open(path + "%d" % list.index(li) + title + '.html', 'w')
        output.write(html)
        output.close()

简直，人生苦短我用python啊！

# 最后

附上HTML转epub电子书格式在线链接：[html.toepub.com][2]

以及廖雪峰的教程：[链接][1]
廖雪峰的Git教程也非常非常的不错哦~




顺便扩充一下自己的→_→[GitHub][3]（爬下来的html也在github上哦~）


  [1]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
  [2]: http://html.toepub.com/
  [3]: https://github.com/cyhhao/PythonCrawler1