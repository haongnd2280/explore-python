import configparser


# Ta có thể đọc nhiều file config cùng một lúc
# File config gần đây nhât sẽ có ưu tiên cao nhất 
# => Nếu có conflicting key thì giá trị key đó sẽ được lấy theo file config gần nhất
config_override = configparser.ConfigParser()
config_override["DEFAULT"] = {
    "ServerAlignInterval": "-1"
}
with open("override.ini", "w") as config_file:
    config_override.write(config_file)

# Read multiple config files
configs = configparser.ConfigParser()
configs.read(
    ["example.ini", "override.ini"]
)

# Lúc này, key config["DEFAULT"]["ServerAlignInterval"] 
# của file example.ini đã được ghi đè bởi file "override.ini" 
print(configs.get("DEFAULT", "ServerAlignInterval"))
print(configs["DEFAULT"]["ServerAlignInterval"])     