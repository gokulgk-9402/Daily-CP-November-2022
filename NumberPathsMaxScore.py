class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        max_score = [[0] * n for _ in range(n)]
        max_paths = [[0] * n for _ in range(n)]
        max_paths[-1][-1] = 1
            
        for y in range(n - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                if board[y][x] in 'SX':
                    continue
                
                num = int(board[y][x]) if board[y][x] not in 'SEX' else 0
                
                for y2, x2 in [(y + 1, x), (y, x + 1), (y + 1, x + 1)]:
                    if y2 < n and x2 < n:
                        if board[y2][x2] == 'X' or max_paths[y2][x2] == 0:
                            continue
                            
                        score = (max_score[y2][x2] + num) % MOD
                        
                        if score > max_score[y][x]:
                            max_score[y][x] = score
                            max_paths[y][x] = max_paths[y2][x2]
                        elif score == max_score[y][x]:
                            max_paths[y][x] = (max_paths[y][x] + max_paths[y2][x2]) % MOD
        
        return [max_score[0][0], max_paths[0][0]]