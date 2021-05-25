# spyder_stadiumgoods
# 爬取国外一球鞋网站<https://www.stadiumgoods.com>
## 写在前面
>该项目是于2019年于某鱼平台上接单，帮助开发的一个爬取球鞋网站<https://www.stadiumgoods.com>各商品数据的一个脚本  
>
>感兴趣可联系<zidutian@gmail.com>  
>
>我的主页<https://imygirl.github.io/>

## 说明：

0. result.md中记录了colab平台上的运行结果，可参考；

1. 在主程序中添加 url 即可运行 code.py 文件；

2. 运行 code.py 文件生成的csv文件为分页爬取结果；  

3. 可通过其他脚本将分页爬取结果汇总至一个文件中;  

4. 主要通过<kbd>BeautifulSoup</kbd>数据包单线程爬取，分析**url**指向页面，伪装**header**爬取，主体程序架构如下：
```
--># 爬取所有搜索页面的url

  --># 爬取各搜索页中各详情页的url
      for i in 所有搜索页面的url:
      
    --># 进入详情页，爬取各页面的详情参数
        for j in 各搜索页中各详情页的url:
        ...
```
## 爬取结果
>data01.csv  

<img src="https://github.com/iMyGirl/spyder_stadiumgoods/blob/main/data/data01.png" width="100%">
