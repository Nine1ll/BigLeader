def check_coordinate(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

def update_coordinate(x,y,command):
    if command == "U":
        nx, ny = x, y+1
    elif command == "D":
        nx, ny = x, y-1
    elif command == "R":
        nx, ny = x+1, y
    elif command == "L":
        nx, ny = x-1, y

    return nx,ny

def solution(dirs):
    x, y = 5, 5
    ans = set()
    for dir in dirs:
        nx, ny = update_coordinate(x,y,dir)
        if not check_coordinate(nx,ny):
            continue
    
        ans.add((x,y,nx,ny))
        ans.add((nx,ny,x,y))
        x,y = nx,ny

    return len(ans)/2
