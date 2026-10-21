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
    if event in count:
        count[event] += 1
    else:
        count[event] = 1

print(count)