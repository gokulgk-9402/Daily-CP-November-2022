class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        positions = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                positions[board[i][j]] = (i,j)

        ans = ""
        curry, currx = 0, 0

        for char in target:
            reqy, reqx = positions[char]

            if char == "z":
                if reqx > currx:
                    ans += "R"*(reqx-currx)
                    currx = reqx
                elif reqx < currx:
                    ans += "L"*(currx-reqx)
                    currx = reqx

                if reqy > curry:
                    ans += "D"*(reqy-curry)
                    curry = reqy
                elif reqy < curry:
                    ans += "U"*(curry-reqy)
                    curry = reqy
            else:
                if reqy > curry:
                    ans += "D"*(reqy-curry)
                    curry = reqy
                elif reqy < curry:
                    ans += "U"*(curry-reqy)
                    curry = reqy

                if reqx > currx:
                    ans += "R"*(reqx-currx)
                    currx = reqx
                elif reqx < currx:
                    ans += "L"*(currx-reqx)
                    currx = reqx

            ans += "!"

        return ans