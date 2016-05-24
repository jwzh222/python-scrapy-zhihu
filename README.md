声明：
此爬虫脚本目的是方便获取这类「禁止转载」文章，仅供个人备份学习之用，知乎官方声明“除非获得原作者的单独授权，任何第三方不得转载标注了「禁止转载」的内容，否则均视为侵权。” 

使用知乎过程中遇到喜欢的文章习惯性想拷贝下来备份到自己笔记里，却发现作者开启了「禁止转载」，不能复制粘贴。通常我都是截图备份到笔记，但这样不方便编辑。
![image](https://github.com/jwzh222/python-/raw/master/image_folder/Image.png)


使用说明：
1.python login.py(登录知乎网站)
2.python get.py（获取需要的回答文章）
![image](https://github.com/jwzh222/python-/raw/master/image_folder/Image2.png)


代码说明：
1.登录：login.py 登录知乎，利用@egrcc的方式：https://github.com/egrcc/zhihu-python。 request.Session方式，验证码处理采用人工输入的方式
2.获取：执行get.py，根据程序提示按顺序输入问题url和作者ID,程序则自动将此回答爬下来写到本地txt文件。

待完成：
对于有图片的文章，目前还未完成把图片一并下载，与文字排版输出到本地文件
