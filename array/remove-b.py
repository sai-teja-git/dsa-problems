def removeB(color, radius):
    color_len = len(color)
    start = 0
    end = 1
    removed = 0
    last_matched = []
    while (end < color_len):
        # print(start, end)
        if (color[start] == color[end] and radius[start] == radius[end] and start != end):
            removed += 2
            if len(last_matched) == 0:
                start = end+1
                end = start+1
            else:
                start = last_matched.pop()
                end += 1
        else:
            last_matched.append(start)
            start = end
            end += 1
    return max(color_len-removed, 0)


dict_1 = {
    "case-1": {
        "color": [2, 3, 5],
        "radius": [3, 3, 5],
        "solution": 3
    },
    "case-2": {
        "color": [2, 2, 5],
        "radius": [3, 3, 5],
        "solution": 1
    },
    "case-3": {
        "color": [1, 2, 2, 1],
        "radius": [1, 2, 2, 1],
        "solution": 0
    },
    "case-4": {
        "color": [1, 1, 98, 97, 1, 1, 94, 93, 1],
        "radius": [1, 1, 98, 97, 1, 1, 94, 93, 1],
        "solution": 5
    },
    "case-5": {
        "color": [99, 99, 99, 99, 99],
        "radius": [22, 22, 22, 22, 22],
        "solution": 1
    }
}

for key, value in dict_1.items():
    ans = removeB(value["color"], value["radius"])
    print(key+"---> input"+str(value["color"])+str(value["radius"])+" ==> "+str(value["solution"])+"==" +
          str(ans)+" Success = "+str(ans == value["solution"]))
