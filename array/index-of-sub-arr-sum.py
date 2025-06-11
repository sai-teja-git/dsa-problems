class Solution:
    def subarraySum(self, arr, target):
        start = 0
        end = 1
        sum = arr[0]
        length = len(arr)
        while (end < length and start < end):
            if (sum == target):
                return [start+1, end]
            sum += arr[end]
            if (sum > target):
                while (start < end and sum > target):
                    sum -= arr[start]
                    start += 1
            end += 1
        if (sum == target):
            return [start+1, end]
        return [-1]


case_arr = [
    {
        "arr": [1, 2, 3, 7, 5],
        "target": 12,
        "solution": [2, 4]
    },
    {
        "arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "target": 15,
        "solution": [1, 5]
    },
    {
        "arr": [5, 3, 4],
        "target": 2,
        "solution": [-1]
    },
    {
        "arr": [12, 18, 5, 11, 30, 5],
        "target": 69,
        "solution": [2, 6]
    },
]

solution = Solution()

pos = 1
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
RESET = "\033[0m"
TEXT_WHITE = "\033[97m"
for value in case_arr:
    ans = solution.subarraySum(value["arr"], value["target"])
    color = BG_GREEN if ans == value["solution"] else BG_RED
    print(
        f"{color}{TEXT_WHITE}Case-{pos}---> input = {value['arr']} ==> {value['solution']} == {ans} Success = {ans == value['solution']}{RESET}"
    )
    pos += 1
