import os
import pandas as pd
from lxml import etree
from sqlalchemy import create_engine
from unitgroups_resolve import parse_xml_unitgroups

# 文件夹路径
folder_path = 'data/ELCD3.2/ILCD/unitgroups/'

# 设置PostgreSQL数据库连接信息
db_config = {
    'user': 'postgres',
    'password': '1234qwer',
    'host': 'localhost',
    'port': '5432',
    'database': 'ilcd_ref_sys'
}

table_name = 'unitgroups'

# 格式化连接字符串
conn_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# 创建数据库连接引擎
engine = create_engine(conn_string)

# 初始化数据列表
data_list = []

# 遍历文件夹中的所有文件
for idx, filename in enumerate(os.listdir(folder_path)):
    # 检查是否为XML文件
    if filename.endswith('.xml') and len(filename) == 40:
        # 获取文件路径
        xml_file_path = os.path.join(folder_path, filename)

        # 从文件读取XML数据
        with open(xml_file_path, 'rb') as file:
            xml_data = file.read()

        parsed_xml=parse_xml_unitgroups(xml_data)

        # 将数据添加到数据列表中
        data_list.append(parsed_xml)

        # 每处理100个文件后，向数据库发送一次插入
        if (idx + 1) % 100 == 0:
            # 将数据列表转换为Pandas DataFrame
            df = pd.DataFrame(data_list)

            # 将DataFrame数据传输到PostgreSQL数据库
            df.to_sql(table_name, engine, if_exists='append', index=False)

            # 清空数据列表
            data_list = []

# 处理剩余文件
if data_list:
    df = pd.DataFrame(data_list)
    df.to_sql(table_name, engine, if_exists='append', index=False)

# 关闭数据库连接
engine.dispose()