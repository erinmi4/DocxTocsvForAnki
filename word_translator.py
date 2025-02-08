import requests
from bs4 import BeautifulSoup
# ...existing code...

def online_translate(word):
    url = f"https://dictionary.cambridge.org/search/english-chinese-simplified/direct/?q={word}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        trans_elem = soup.find('span', class_='trans')
        if trans_elem:
            return trans_elem.get_text(strip=True)
    except Exception:
        pass
    return "未找到该单词的线上翻译"

def translate_word(word, dictionary):
    # 删除预定义词典逻辑，直接调用线上查询
    return online_translate(word)

# ...existing code...

if __name__ == "__main__":
    # 移除示例词典数据，直接输入单词进行线上查询
    while True:
        word = input("请输入英文单词（输入'q'退出）：")
        if word.lower() == 'q':
            break
        print(f"{word} 的翻译是: {translate_word(word, None)}")
