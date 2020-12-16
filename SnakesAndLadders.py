class SnakesAndLadders:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        current_pos = 0
        direction = 1
        portals = {}
        for row in board[::-1]:
            for val in row[::direction]:
                current_pos += 1
                if val > -1:
                    portals[current_pos] = val
            direction *= -1
        if current_pos in portals:
            return -1
        
        queue = []
        visited = []
        # first thing in queue is position of 1 and turns of 0
        queue.append((1,0))
        visited.append(1)
        while queue:
            pos, turns = queue.pop(0)
            for roll in range(1, 7):
                new_pos = pos + roll
                if new_pos not in visited:
                    visited.append(new_pos)
                    
                    # 2nd param return same value if key not in portals
                    new_pos = portals.get(new_pos, new_pos)
                    queue.append((new_pos, turns+1))
                if new_pos == current_pos:
                    return turns + 1
                
        return -1
    
    
