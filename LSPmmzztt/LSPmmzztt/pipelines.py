# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time

import requests
import os
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import execjs


class LspmmzzttPipeline:

    def process_item(self, item, spider):
        num = item['num']
        url = item['url']
        directory = 'images' + url[-9:]
        try:
            os.makedirs(directory)
            print(f"目录 {directory} 创建成功")
        except OSError as e:
            print(f"创建目录 {directory} 失败: {e}")
        data = item['data']
        js_code = """
        var CryptoJS = require('crypto-js');
        function _0x90fx(_0x36f56e, _0x12e44e) {
          var _0x4ed349 = '',
              _0x1f3833 = CryptoJS;

          for (i = 2; i < 18; i++) {
            _0x4ed349 += (_0x36f56e % (i + 1) % 9)['toString']();
          }

          var _0x811f47 = _0x1f3833['MD5'](_0x36f56e + "LrlC00Fk")['toString'](),
              _0x3410d6 = _0x1f3833['MD5'](_0x4ed349 + _0x811f47)['toString']()['substr'](8, 16),
              _0x29f672 = _0x12e44e["split"](_0x811f47)[1],
              _0x45b1da = _0x1f3833['enc']["Hex"]["parse"](_0x29f672),
              _0x445741 = _0x1f3833["enc"]['Base64']['stringify'](_0x45b1da),
              _0x3410d6 = _0x1f3833['enc']["Utf8"]["parse"](_0x3410d6),
              _0x3517e4 = _0x1f3833['AES']['decrypt'](_0x445741, _0x3410d6, {
            "iv": _0x1f3833['enc']["Utf8"]['parse'](_0x4ed349),
            "mode": _0x1f3833["mode"]['CBC'],
            "padding": _0x1f3833["pad"]['Pkcs7']
          });

          return JSON["parse"](_0x3517e4["toString"](_0x1f3833['enc']['Utf8']));
        }
        """
        context = execjs.compile(js_code)

        # 调用JavaScript函数并获取结果
        result = context.call("_0x90fx", num, data)
        # print(result)

        item['image_urls'] = [url + item for item in result]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
            'Referer': 'https://mmzztt.com/'
        }
        for url in item['image_urls']:
            reponse = requests.get(url, headers=headers)

            print(url, reponse.status_code)
            print(1)
            time.sleep(1)
            with open(directory + url.split('/')[-1], "wb") as f:
                f.write(reponse.content)
                reponse.close()

        return item
