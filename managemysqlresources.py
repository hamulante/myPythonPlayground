# pip install azure-mgmt-rdbms done
# pip install azure-identity done

from azure.identity import ClientSecretCredential
from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient

# 0. 权限 - 创建好app已经在IAM给了权限

# 1. 认证
tenant_id = ''
client_id= ''
client_secret = ''
subscription_id = ''

cred = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

# 2. 初始化 MySQL 管理客户端
mysql_client = MySQLManagementClient(cred, subscription_id)

# # 3. 列出订阅下所有 MySQL 服务器
for server in mysql_client.servers.list():
    print(f"Server name: {server.name}, Location: {server.location}, SKU: {server.sku.name}")
