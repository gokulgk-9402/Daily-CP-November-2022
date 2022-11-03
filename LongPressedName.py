class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        len_n = len(name)
        len_t = len(typed)

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len_n and ptr2 < len_t:
            curr = name[ptr1]

            if curr != typed[ptr2]:
                return False

            if (ptr1==len_n-1) or (ptr1 != len_n -1 and curr != name[ptr1+1]):
                while ptr2 < len_t-1 and typed[ptr2+1] == curr:
                    ptr2 += 1

            ptr1 += 1
            ptr2 += 1

        if ptr2 < len_t or ptr1 < len_n:
            return False

        return True