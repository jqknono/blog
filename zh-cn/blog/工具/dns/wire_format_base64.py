import base64
import dns.message
import dns.rdatatype

# 创建一个DNS查询消息
query = dns.message.make_query('baidu.com', dns.rdatatype.A)

# 将消息转换为Wire Format
wire_format = query.to_wire()

# 转为base64
wire_format_base64 = base64.b64encode(wire_format).decode('utf-8')

# 打印
print(wire_format_base64)