from urllib import request
import re

#Beautiful Soup  ,Scrapy爬虫框架
#爬虫，反爬虫，反反爬虫
#以下是原生爬虫
class Spider():
    '''
      THIS IS A class 注释放在里面
    '''
    url = "https://www.huya.com/g/lol"
    # \w匹配单词字符包括下划线   \W非单词字符 []里代表的是或者关系 [\w\W]代表取的一个字符，要取无限多次，就要用*
    # *前字符匹配0次或者无限多次 #加？是非贪婪模式 按最小量来匹配
    # .匹配除换行符\n之外的其他所有字符
    # ()组，只取组里内容
    root_patter = '<li class="game-live-item"([\w\W]*?)</li>'
    name_patter = '<i class="nick"([\w\W]*?)</i>'
    #去掉name里的title的具体名字可以一起写，不用像我这样分成两步
    #name_patter = '<i class="nick" title="([\w\W]*?)">[\w\W]*?</i>'
    real_name_pattern = '>(.*)'
    number_patter = '<i class="js-num">([\w\W]*?)</i>'
    #取得html内容
    def __def_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()  # bytes
        htmls = str(htmls, encoding='utf-8')
        return htmls
    #解析，获取名字和数
    def __anlisys_content(self, htmls):
        root_html = re.findall(Spider.root_patter, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_patter, html)  # list
            real_name = re.findall(Spider.real_name_pattern, name[0])
            number = re.findall(Spider.number_patter, html)
            anchor = {'name': real_name, 'number': number}
            anchors.append(anchor)
        # print(anchors[0])
        return anchors
    

    #数据精炼
    def __refine(self,anchors):
        l=lambda anchor:{
           'name':anchor['name'][0], 
           'number':anchor['number'][0]
        }
        return map(l,anchors)

    #排序
    def __sort(self,anchors):
        anchors=sorted(anchors,key=self.__sort__seed,reverse=True)
        return anchors

    def __sort__seed(self,anchor):
        r=re.findall('[1-9]\d*\.?\d*',anchor['number'])
        number=float(r[0])
        if '万' in anchor['number']:
            number*=10000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('rank '+str(rank+1)
            +' :'+anchors[rank]['name']
            +' '+anchors[rank]['number'])


        

    def go(self):
        htmls = self.__def_content()
        anchors = self.__anlisys_content(htmls)
        dictx = self.__refine(anchors)
        anchors=self.__sort(dictx)
        self.__show(anchors)


if __name__ == "__main__":
    spider = Spider()
    spider.go()

