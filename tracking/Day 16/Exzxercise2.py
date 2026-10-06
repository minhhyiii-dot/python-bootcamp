Starting_string = "   ERROR_disk_error   "
message = Starting_string
message = message.strip()
message = message.lower()
message = message.replace("_", " ")

print(message)
print(message.count("error"))
print(message.startswith("error"))
print(message.find("disk"))