# coding: utf-8
import os
from pprint import pprint
from wechatarticles import Url2Html

if __name__ == "__main__":
    # 微信文章下载为离线HTML（含图片）
    # 微信文章的url
    url = "https://mp.weixin.qq.com/s?__biz=MzUzNjk1NDIyNg==&mid=2247506248&idx=1&sn=c9a8b4d2e11fd1b6ae924877da3f0ea8&chksm=faeccd55cd9b44432ea81578b1e33db2ae5ce938ed5a90e32847cb0ea88916a16ac47c92e135&scene=132#wechat_redirect"
    url = "http://mp.weixin.qq.com/s?__biz=MzIxNzUxNjgyOQ==&amp;mid=2247488011&amp;idx=1&amp;sn=5c800930c79b0f90c05ff524dfe7a804&amp;chksm=97f9cc79a08e456f2f399190b5d4b9d8beb0e1de2b9310cb2c4b58273fa1a65bee11077cc0f7&amp;scene=27#wechat_redirect"
    uh = Url2Html()
    # 请提前创建一个以公众号为名的文件夹，并且在该文件夹下创建imgs文件夹
    res = uh.run(url, mode=4)
    print(res)
