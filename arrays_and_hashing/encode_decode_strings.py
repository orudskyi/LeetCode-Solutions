"""
Problem 271. Encode and Decode Strings
Category: Arrays and Hashing
Link: https://neetcode.io/problems/string-encode-and-decode/question
Difficulty: Medium
"""


class Solution:
    def encode(self, strs: list[str]) -> str:
        encode_result = ""
        for s in strs:
            encode_result += str(len(s)) + "#" + s
        return encode_result

    def decode(self, s: str) -> list[str]:
        decode_result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decode_result.append(s[i:j])
            i = j
        return decode_result


def test_plus_one():
    s = Solution()
    assert s.encode(["Hello", "World#"]) == "5#Hello6#World#"


if __name__ == "__main__":
    solver = Solution()

    result = solver.encode(["Hello", "World#"])
    result2 = solver.decode("5#Hello6#World#")

    print(f"Result:    {result}")
    print(f"Result2:    {result2}")
