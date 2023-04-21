import pandas as pd
from lxml import etree


def parse_xml_flowproperties(xml_string):
    # 解析XML字符串
    root = etree.fromstring(xml_string)
    flow_flowproperties_elements = root.findall(".//flowProperties/flowProperty", root.nsmap)
    flow_flowproperties_data = [parse_xml_flowproperty(
        flow_flowproperties, root.nsmap) for flow_flowproperties in flow_flowproperties_elements]
    return pd.DataFrame(flow_flowproperties_data)


def parse_xml_flowproperty(flow_property, namespaces):
    try:
        dataSetInternalID = flow_property.get("dataSetInternalID")
    except AttributeError:
        dataSetInternalID = None

    try:
        refObjectId = flow_property.find(".//referenceToFlowPropertyDataSet", namespaces).get("refObjectId")
    except AttributeError:
        refObjectId = None

    try:
        shortDescription = flow_property.find(".//common:shortDescription", namespaces).text
    except AttributeError:   
        try:
            shortDescription = flow_property.xpath(".//common:name[@xml:lang='en']", namespaces=namespaces.nsmap)[0].text
        except IndexError:
            shortDescription = None

    try:
        meanValue = flow_property.find("meanValue", namespaces).text
    except AttributeError:
        meanValue = None

    return {
        'dataSetInternalID': dataSetInternalID,
        'refObjectId': refObjectId,
        'shortDescription': shortDescription,
        'meanValue': meanValue,
    }
