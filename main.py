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