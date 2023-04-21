import pandas as pd
from lxml import etree


def parse_xml_units(xml_string):
    # 解析XML字符串
    root = etree.fromstring(xml_string)
    units_elements = root.findall(".//units/unit", root.nsmap)
    unit_data = [parse_xml_unit(
        unit, root.nsmap) for unit in units_elements]
    return pd.DataFrame(unit_data)


def parse_xml_unit(unit, namespaces):
    try:
        dataSetInternalID = unit.get("dataSetInternalID")
    except AttributeError:
        dataSetInternalID = None

    try:
        name = unit.find("name", namespaces).text
    except AttributeError:
        name = None

    try:
        meanValue = unit.find("meanValue", namespaces).text
    except AttributeError:
        meanValue = None

    try:
        generalComment = unit.find("generalComment", namespaces).text
    except AttributeError:
        generalComment = None

    return {
        'dataSetInternalID': dataSetInternalID,
        'name': name,
        'meanValue': meanValue,
        'generalComment': generalComment,
    }
