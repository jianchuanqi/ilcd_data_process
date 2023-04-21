import pandas as pd
from lxml import etree

def parse_xml_flowproperties(xml_string):
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
        name = None

    try:
        synonyms = root.find(".//common:synonyms", root.nsmap).text
    except AttributeError:
        synonyms = None

    try:
        classification = root.find(".//common:class[@level='0']", root.nsmap).text
    except AttributeError:
        classification = None

    try:
        general_comment = root.find(".//common:generalComment", root.nsmap).text
    except AttributeError:
        general_comment = None

    try:
        ref_unit_group_id = root.find(".//referenceToReferenceUnitGroup", root.nsmap).get('refObjectId')
    except AttributeError:
        ref_unit_group_id = None

    return {
        'UUID': uuid,
        'Name': name,
        'Synonyms': synonyms,
        'Classification': classification,
        'General Comment': general_comment,
        'Ref Unit Group ID': ref_unit_group_id,
    }
