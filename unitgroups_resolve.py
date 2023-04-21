import pandas as pd
from lxml import etree

def parse_xml_unitgroups(xml_string):
    # 解析XML字符串
    root = etree.fromstring(xml_string)

    # 提取字段数据
    # 提取所需信息，处理缺失标签
    try:
        uuid = root.find(".//common:UUID", root.nsmap).text
    except AttributeError:
        uuid = None

    try:
        name = root.find(".//common:name", root.nsmap).text
    except AttributeError:   
        try:
            name = root.xpath(".//common:name[@xml:lang='en']", namespaces=root.nsmap)[0].text
        except IndexError:
            name = None

    try:
        classification = root.find(".//common:class[@level='0']", root.nsmap).text
    except AttributeError:
        classification = None

    try:
        general_comment = root.find(".//common:generalComment", root.nsmap).text
    except AttributeError:
        general_comment = None

    try:
        reference_to_reference_unit = root.find(".//referenceToReferenceUnit", root.nsmap).text
    except AttributeError:
        reference_to_reference_unit = None

    return {
        'UUID': uuid,
        'Name': name,
        'Classification': classification,
        'General Comment': general_comment,
        'Reference to Reference Unit': reference_to_reference_unit,
    }