class Stack():
    def __init__(self, value=[]) -> None:
        self.value = value

    def values(self):
        return self.value

    def isEmpty(self):
        return len(self.value) == 0

    def push(self, x):
        self.value.append(x)

    def pop(self):
        if self.isEmpty():
            print("Error : stack underflow")
        else:
            return self.value.pop()


class Solution():
    def nextLargerElement(self, arr, n):
        """
        ## using array

        The function "nextLargerElement" takes an array of integers and returns a new array where each
        element is replaced with the next larger element in the original array, or -1 if there is no
        larger element.

        :param arr: The input array of integers for which we want to find the next larger element
        :param n: The parameter `n` represents the length of the array `arr`
        :return: the modified array `arr` where each element is replaced with the next larger element in
        the array. If there is no larger element, the element is replaced with -1.
        """
        s = []
        for i in range(n):
            while s and s[-1].get("value") < arr[i]:
                ele = s.pop()
                arr[ele.get("ind")] = arr[i]
            s.append({"value": arr[i], "ind": i})
        while s:
            ele = s.pop()
            arr[ele.get("ind")] = -1
        return arr


dict_1 = {
    "case-1": {
        "arr": [1, 3, 2, 4],
        "solution": [3, 4, 4, -1]
    },
    "case-2": {
        "arr": [6, 8, 0, 1, 3],
        "solution": [8, -1, 1, 3, -1]
    },
    "case-3": {
        "arr": [4, 4, 4, 4],
        "solution": [-1, -1, -1, -1]
    },
    "case-4": {
        "arr": [6, 8, 2, 1, 3],
        "solution": [8, -1, 3, 3, -1]
    }
}

solution = Solution()

for key, value in dict_1.items():
    ans = solution.nextLargerElement(value["arr"], len(value["arr"]))
    print(key+"---> input"+str(value["arr"])+" ==> "+str(value["solution"])+"==" +
          str(ans)+" Success = "+str(ans == value["solution"]))
