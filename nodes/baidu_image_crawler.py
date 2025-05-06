import requests
from bs4 import BeautifulSoup
import os
import re

class BaiduImageCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def search_images(self, keyword, max_num=30):
        """
        搜索百度图片并返回图片URL列表
        :param keyword: 搜索关键词
        :param max_num: 最大图片数量
        :return: 图片URL列表
        """
        url = f'https://image.baidu.com/search/flip?tn=baiduimage&word={keyword}'
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            # 解析HTML获取图片URL
            soup = BeautifulSoup(response.text, 'html.parser')
            img_urls = []
            
            # 从JavaScript数据中提取图片URL
            script_text = soup.find_all('script')
            for script in script_text:
                if 'flip.setData' in script.text:
                    pattern = re.compile(r'"objURL":"(.*?)"')
                    img_urls = pattern.findall(script.text)
                    break
            
            return img_urls[:max_num]
        except Exception as e:
            print(f"搜索图片出错: {e}")
            return []
    
    def download_images(self, img_urls, save_dir='./downloads'):
        """
        下载图片到指定目录
        :param img_urls: 图片URL列表
        :param save_dir: 保存目录
        """
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        for i, url in enumerate(img_urls):
            try:
                response = requests.get(url, headers=self.headers, stream=True)
                response.raise_for_status()
                
                # 获取文件扩展名
                ext = os.path.splitext(url)[1]
                if not ext:
                    ext = '.jpg'
                
                save_path = os.path.join(save_dir, f'image_{i}{ext}')
                
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                print(f"已下载: {save_path}")
            except Exception as e:
                print(f"下载图片 {url} 出错: {e}")