from selenium import webdriver
import requests
import json
import os


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)




target_url = "https://interactivemeta.cmc.zju.edu.cn/courseapi/v3/web-socket/search-trans-result?sub_id=1490238&format=json"

try:
    login_url = 'https://classroom.zju.edu.cn/'  
    driver.get(login_url)
    
    print("浏览器已打开，请手动登录...")
    
    input("按 Enter 键继续，确认登录完成并准备获取 Cookies...")
    
    cookies = driver.get_cookies()
    
    cookie_string = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

    print(cookie_string)
    
finally:
    driver.quit()

header = {
    "Host": "interactivemeta.cmc.zju.edu.cn",
    "Method": "GET",
    "Path": "/courseapi/v3/web-socket/search-trans-result?sub_id=1490239&format=json",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Cookie": f"{cookie_string}",
    "Priority": "u=0, i",
    "Sec-CH-UA": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

response = requests.get(target_url, headers=header)

json_text = response.text

data = json.loads(json_text)

all_texts = []

if 'list' in data:
    for item in data['list']:
        if 'all_content' in item:
            for content in item['all_content']:
                if 'Text' in content:
                    all_texts.append(content['Text'])

combined_text = " ".join(all_texts)


os.system("touch ./text.txt")

os.system(f"echo {combined_text} > ./text.txt")
