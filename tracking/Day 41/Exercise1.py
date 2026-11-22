# program nhận 1 dict, mỗi key trong dict đó - ticker chứa 1 list giá
# kết quả cần trả ra: key biến thành 1 dict mới, trong đó có các key: start, latest, change, trend chứa các value tương ứng



def filter(data): # có những potential error gì? ticker dài hơn 3 ký tự cover được việc có dấu cách ở đầu, giữa, cuối, giá không có, giá âm

    for key, values in data.items():
        if len(key) != 3 or " " in key:
            raise ValueError("Ticker invalid, ticker must have exactly 3 character")

        if values is None or len(values) <= 1:
            raise ValueError("There are no price here")

        for value in values:
            if value is None or type(value) not in (int, float) or float(value) <= 0:
                raise ValueError("Price Invalid, Price must positive, int/float type and not None")

    return data

# tiếp theo cần làm gì?
def key2dict(data):
    output = {}

    for key, values in data.items():
        output[key] = {}

    return output

def program(data):
    market = filter(data)
    skeleton = key2dict(data)

    for key, value in market.items():
        skeleton[key]["start"] = value[0]

        skeleton[key]["latest"] = value[-1]

        skeleton[key]["change"] = value[-1] - value[0]

        if skeleton[key]["change"] > 0:
            skeleton[key]["trend"] = "UP"
        elif skeleton[key]["change"] == 0:
            skeleton[key]["trend"] = "FLAT"
        else:
            skeleton[key]["trend"] = "DOWN"

    return skeleton


print(program(
    {"VCB": [90, {}]}
))

    