import re

def process_line(line):
    # 使用正则表达式匹配单词、音标和释义
    # 匹配模式: 单词 [音标]词性.释义
    pattern = r'([a-zA-Z\s]+)\s*\[[^\]]+\]([^。\n]+)'
    
    # 处理一行中可能存在的多个词组
    matches = re.finditer(pattern, line)
    processed_parts = []
    
    for match in matches:
        word = match.group(1).strip()
        definition = match.group(2).strip()
        processed_parts.append(f"{word}\t{definition}")
    
    # 如果没有匹配到任何内容，返回原行
    return " ".join(processed_parts) if processed_parts else line.strip()

def process_file(input_file="vo2.txt", output_file="vo3.txt"):
    try:
        with open(input_file, 'r', encoding='utf-8') as fin:
            with open(output_file, 'w', encoding='utf-8') as fout:
                for line in fin:
                    if line.strip():  # 跳过空行
                        processed_line = process_line(line)
                        fout.write(processed_line + '\n')
        print(f"处理完成! 结果已保存到 {output_file}")
    except Exception as e:
        print(f"处理文件时出错: {str(e)}")

if __name__ == "__main__":
    process_file()
