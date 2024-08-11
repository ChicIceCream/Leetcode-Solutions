class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int: #type:ignore
        answer = 0
        for command in commands:
            if command == "UP":
                answer -= n
            elif command == "DOWN":
                answer += n
            elif command == "RIGHT":
                answer += 1
            elif command == "LEFT":
                answer -= 1
        
        return answer
