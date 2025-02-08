import requests
from bs4 import BeautifulSoup
import re

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

def is_english(word):
    return re.fullmatch(r"[A-Za-z]+", word) is not None

def update_vocab_file(input_file="vocab.txt", output_file="vocab_updated.txt"):
    updated_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            # 保留空行或仅中文行不处理
            if not stripped or re.search(r'[\u4e00-\u9fff]', stripped):
                updated_lines.append(line)
                continue

            tokens = stripped.split(maxsplit=1)
            # 如果只有一个 token 且为纯英文，则调用线上查询
            if len(tokens) == 1 and is_english(tokens[0]):
                print(f"正在查询单词: {tokens[0]}...", flush=True)
                definition = online_translate(tokens[0])
                new_line = f"{tokens[0]} {definition}\n"
                updated_lines.append(new_line)
            else:
                updated_lines.append(line)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    print(f"更新完成，结果保存到 {output_file}")

if __name__ == "__main__":
    update_vocab_file()
