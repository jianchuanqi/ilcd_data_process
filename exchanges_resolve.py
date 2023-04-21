import pandas as pd
from lxml import etree


def parse_xml_exchanges(xml_string):
    # 解析XML字符串
    root = etree.fromstring(xml_string)

    exchange_elements = root.findall(".//exchanges/exchange", root.nsmap)
    exchange_data = [parse_xml_exchange(
        exchange, root.nsmap) for exchange in exchange_elements]
    return pd.DataFrame(exchange_data)


def parse_xml_exchange(exchange, namespaces):
    try:
        ref_flow_data_set = exchange.find(".//referenceToFlowDataSet", namespaces)
        short_description = ref_flow_data_set.find(".//common:shortDescription", namespaces).text
        ref_object_id = ref_flow_data_set.get('refObjectId')
    except AttributeError:
        short_description = None
        ref_object_id = None

    try:
        exchange_direction = exchange.find(
            ".//exchangeDirection", namespaces).text
    except AttributeError:
        exchange_direction = None

    try:
        mean_amount = exchange.find(".//meanAmount", namespaces).text
    except (AttributeError, TypeError):
        mean_amount = None

    try:
        resulting_amount = exchange.find(
            ".//resultingAmount", namespaces).text
    except (AttributeError, TypeError):
        resulting_amount = None

    try:
        data_source_type = exchange.find(".//dataSourceType", namespaces).text
    except AttributeError:
        data_source_type = None

    try:
        data_derivation_type_status = exchange.find(
            ".//dataDerivationTypeStatus", namespaces).text
    except AttributeError:
        data_derivation_type_status = None

    return {
        'ref_object_id': ref_object_id,
        'Short Description': short_description,
        'Exchange Direction': exchange_direction,
        'Mean Amount': mean_amount,
        'Resulting Amount': resulting_amount,
        'Data Source Type': data_source_type,
        'Data Derivation Type Status': data_derivation_type_status,
    }
