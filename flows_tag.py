import xml.etree.ElementTree as ET

def extract_tags(element, tag_path=''):
    result = {}
    if element.text and element.text.strip():
        result[tag_path] = element.text.strip()
    for child in element:
        child_tag_path = f"{tag_path}/{child.tag}" if tag_path else child.tag
        result.update(extract_tags(child, child_tag_path))
    return result

# 以下是 XML 字符串的示例，实际上您可以从文件或其他来源读取 XML
with open('data/ELCD3.2/ILCD/flows/1bf85d1d-0b66-4476-99f9-2d69e0b019b3.xml', 'rb') as file:
    xml_string = file.read()

# 解析 XML 字符串
root = ET.fromstring(xml_string)

# 提取所有标签及其文本
tags_with_text = extract_tags(root)

# 打印结果
for tag, text in tags_with_text.items():
    print(f"{tag}: {text}")
