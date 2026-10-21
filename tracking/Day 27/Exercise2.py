events = [
    "LOGIN",
    "LOGOUT",
    "LOGIN",
    "ERROR",
    "LOGIN",
    "TIMEOUT",
    "ERROR",
    "LOGOUT",
    "TIMEOUT"
]
count = {}

for event in events:
    count[event] = count.get(event, 0) + 1

print(count)