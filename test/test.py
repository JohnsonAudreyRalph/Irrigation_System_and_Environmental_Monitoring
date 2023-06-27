import requests
import json

url = "http://solar-ctd.ddns.net/data/line"

# Gửi yêu cầu HTTP để lấy dữ liệu từ URL
response = requests.get(url)
data = response.json()

# Truy cập vào các giá trị trong dữ liệu JSON
status = data["status"]
line1_power = data["data"]["line1"]["power"]
line1_volt = data["data"]["line1"]['volt']
line1_perform = data["data"]["line1"]["perform"]
line1_ampe = data["data"]["line1"]["ampe"]


line2_power = data["data"]["line2"]["power"]
line2_volt = data["data"]["line2"]['volt']
line2_perform = data["data"]["line2"]["perform"]
line2_ampe = data["data"]["line2"]["ampe"]

# In ra các giá trị đã truy cập
print("Trạng thái lấy dữ liệu:", status)

print("Line 1 Power:", line1_power)
print("Line 1 Volt: ", line1_volt)
print("Line 1 Perform: ", line1_perform)
print("Line 1 Ampe: ", line1_ampe)


print("Line 2 Power:", line2_power)
print("Line 2 Volt: ", line2_volt)
print("Line 2 Perform: ", line2_perform)
print("Line 2 Ampe: ", line2_ampe)