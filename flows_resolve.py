import pandas as pd
from lxml import etree

def parse_xml_flow(xml_string):
    # 解析XML字符串
    root = etree.fromstring(xml_string)

    # 提取字段数据
    # 提取所需信息，处理缺失标签
    try:
        uuid = root.find(".//common:UUID", root.nsmap).text
    except AttributeError:
        uuid = None

    try:
        name = root.find(".//name/baseName", root.nsmap).text
    except AttributeError:
        name = None

    try:
        synonyms = root.find(".//common:synonyms", root.nsmap).text
    except AttributeError:
        synonyms = None

    try:
        formula = root.find(".//common:sumFormula", root.nsmap).text
    except AttributeError:
        formula = None
    
    try:
        cas_number = root.find(".//CASNumber", root.nsmap).text
    except AttributeError:
        cas_number = None

    try:
        category_level_0 = root.find(".//common:elementaryFlowCategorization/common:category[@level='0']", root.nsmap).text
    except AttributeError:
        category_level_0 = None

    try:
        category_level_1 = root.find(".//common:elementaryFlowCategorization/common:category[@level='1']", root.nsmap).text
    except AttributeError:
        category_level_1 = None

    try:
        category_level_2 = root.find(".//common:elementaryFlowCategorization/common:category[@level='2']", root.nsmap).text
    except AttributeError:
        category_level_2 = None
        
    try:
        type_of_dataset = root.find(".//modellingAndValidation/LCIMethod/typeOfDataSet", root.nsmap).text
    except AttributeError:
        type_of_dataset = None

    try:
        general_comment = root.find(".//common:generalComment", root.nsmap).text
    except AttributeError:
        general_comment = None

    try:
        short_description = root.find(".//complianceDeclarations/compliance/common:referenceToComplianceSystem/common:shortDescription", root.nsmap).text
    except AttributeError:
        short_description = None

    try:
        approval_of_overall_compliance = root.find(".//complianceDeclarations/compliance/common:approvalOfOverallCompliance", root.nsmap).text
    except AttributeError:
        approval_of_overall_compliance = None

    try:
        timestamp = root.find(".//dataEntryBy/common:timeStamp", root.nsmap).text
    except AttributeError:
        timestamp = None

    try:
        dataset_format = root.find(".//dataEntryBy/common:referenceToDataSetFormat/common:shortDescription", root.nsmap).text
    except AttributeError:
        dataset_format = None

    try:
        dataset_version = root.find(".//publicationAndOwnership/common:dataSetVersion", root.nsmap).text
    except AttributeError:
        dataset_version = None

    try:
        permanent_dataset_uri = root.find(".//publicationAndOwnership/common:permanentDataSetURI", root.nsmap).text
    except AttributeError:
        permanent_dataset_uri = None

    try:
        referenceToReferenceFlowProperty = root.find(".//referenceToReferenceFlowProperty", root.nsmap).text
    except AttributeError:
        referenceToReferenceFlowProperty = None

    try:
        flow_property_short_description = root.find(f".//flowProperty[@dataSetInternalID='{referenceToReferenceFlowProperty}']/referenceToFlowPropertyDataSet/common:shortDescription", root.nsmap).text
    except AttributeError:
        flow_property_short_description = None
    
    # 将数据添加到数据列表中
    return ({
    'UUID': uuid,
    'Name': name,
    'Synonyms': synonyms,
    'Formula': formula,
    'CAS Number': cas_number,
    'Category Level 0': category_level_0,
    'Category Level 1': category_level_1,
    'Category Level 2': category_level_2,
    'General Comment': general_comment,
    'Type of Dataset': type_of_dataset,
    'Short Description': short_description,
    'Approval of Overall Compliance': approval_of_overall_compliance,
    'Timestamp': timestamp,
    'Dataset Format': dataset_format,
    'Dataset Version': dataset_version,
    'Permanent Dataset URI': permanent_dataset_uri,
    'referenceToReferenceFlowProperty': referenceToReferenceFlowProperty,
    'Flow Property Short Description': flow_property_short_description,
    })
