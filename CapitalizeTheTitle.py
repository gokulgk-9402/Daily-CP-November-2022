class Solution:
    def capitalizeTitle(self, title: str) -> str:
        temp = title.split()
        for i in range(len(temp)):
            if len(temp[i]) <= 2:
                temp[i] = temp[i].lower()
            else:
                temp[i] = temp[i][0].upper() + temp[i][1:].lower()

        return " ".join(temp)