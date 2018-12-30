'''
	目的：通过调用python3中的urllib库实现对任意百度贴吧页面的抓取，并存储至本地。
	说明：视频教程采用的是python2中的urllib和urllib2，本程序已调整为python3执行。
	Kewei@homework 20181230
'''

# coding=utf-8
import urllib.request


def tiebaSpider(url, beginPage, endPage, kw):
    """
        作用：负责处理url，分配每个url去发送请求
        url：需要处理的第一个url
        beginPage: 爬虫执行的起始页面
        endPage: 爬虫执行的截止页面
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50

        filename = str(kw) + "-page" + str(page) + ".html"

        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        #print fullurl

        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)

def loadPage(url, filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename: 文件名
    '''
    print("downloading " + filename)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    return response.read()

def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print("now saving " + filename)
    with open(filename, 'wb+') as f:
        f.write(html)
    print("-" * 20)


# 模拟 main 函数
if __name__ == "__main__":

    kw = input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw" : kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage, kw)