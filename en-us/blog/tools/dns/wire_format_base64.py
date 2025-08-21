import base64
import dns.message
import dns.rdatatype

# Create a DNS query message
query = dns.message.make_query('baidu.com', dns.rdatatype.A)

# Convert the message to Wire Format
wire_format = query.to_wire()

# Convert to base64
wire_format_base64 = base64.b64encode(wire_format).decode('utf-8')

# Print
print(wire_format_base64)