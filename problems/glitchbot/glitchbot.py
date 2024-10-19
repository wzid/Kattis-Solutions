x, y = map(int, input().split())
n = int(input())
cmds = [input() for _ in range(n)]

def run_through(commands):
    curr_pos = (0,0)
    direction = (0, 1)

    for cmd in cmds:
        if cmd == "Forward":
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
        elif cmd == "Right":
            direction = (direction[1], -direction[0])
        elif cmd == "Left":
            direction = (-direction[1], direction[0])
    
    return curr_pos

possible = ['Forward', 'Right', 'Left']
for i in range(n):
    curr_cmd = cmds[i]
    for cmd in possible:
        if cmd != curr_cmd:
            cmds[i] = cmd
            if run_through(cmds) == (x, y):
                print(i+1, cmd)
                quit()
            cmds[i] = curr_cmd
