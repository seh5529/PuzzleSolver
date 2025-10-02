
import Node as n
import ReadIn as c


def find_nodes2(puzzle, rows, cols):
    dict_of_nodes = {}
    start = None
    end = None
    rows = rows - 1
    cols = cols - 1
    y = 0

    for row in puzzle:
        x = 0
        for character in row:
            if character != '*':
                if character == '0':
                    start = f'{x},{y}'
                if character == '1':
                    end = f'{x},{y}'
                neighbors = []

                if x + 1 <= cols:
                    if puzzle[y][x+1] == '.' or puzzle[y][x+1] == '1':
                        if f'{x+1},{y}' not in dict_of_nodes:
                            new_node = n.Node(None, '.', x+1, y)
                            dict_of_nodes[f'{x+1},{y}'] = new_node
                            neighbors.append(new_node)
                        else:
                            node = dict_of_nodes[f'{x+1},{y}']
                            neighbors.append(node)
                # south
                if y + 1 <= rows:
                    if puzzle[y+1][x] == '.' or puzzle[y+1][x] == '1':
                        if f'{x},{y+1}' not in dict_of_nodes:
                            new_node = n.Node(None, '.', x, y + 1)
                            dict_of_nodes[f'{x},{y+1}'] = new_node
                            neighbors.append(new_node)
                        else:
                            node = dict_of_nodes[f'{x},{y+1}']
                            neighbors.append(node)
                # west
                if x - 1 >= 0:
                    if puzzle[y][x-1] == '.' or puzzle[y][x-1] == '1':
                        if f'{x-1},{y}' not in dict_of_nodes:
                            new_node = n.Node(None, '.', x - 1, y)
                            dict_of_nodes[f'{x-1},{y}'] = new_node
                            neighbors.append(new_node)
                        else:
                            node = dict_of_nodes[f'{x-1},{y}']
                            neighbors.append(node)
                # north
                if y - 1 >= 0:
                    if puzzle[y-1][x] == '.' or puzzle[y-1][x] == '1':
                        if f'{x},{y-1}' not in dict_of_nodes:
                            new_node = n.Node(None, '.', x, y - 1)
                            dict_of_nodes[f'{x},{y-1}'] = new_node
                            neighbors.append(new_node)
                        else:
                            node = dict_of_nodes[f'{x},{y-1}']
                            neighbors.append(node)


                if f'{x},{y}' not in dict_of_nodes:
                    new_node = n.Node(neighbors, character, x, y)
                    dict_of_nodes[f'{x},{y}'] = new_node
                else:
                    node = dict_of_nodes[f'{x},{y}']
                    node.neigbors = neighbors
            x += 1
        y += 1
    # for key in dict_of_nodes:
    #     print(f'{key}: {dict_of_nodes[key].neigbors}')
    solve_puzzle(dict_of_nodes, start, end)
def read_file(filename):
    with open(filename) as file:
        i = 0
        y = 0
        for line in file:
            if i == 0:
                line = line.split(" ")
                cols = int(line[0])
                rows = int(line[1])
                file_characters = [['.' for i in range(cols)] for j in range(rows)]
                i += 1
            else:
                x = 0
                line = line.split(" ")
                for char in line:
                    file_characters[y][x] = char.strip("\n")
                    x += 1
                y += 1
    find_nodes2(file_characters, rows, cols)

def back_track(path, end, start):
    end_node = path[end]
    solved_path = []
    solved_path.append(end_node)
    while True:
        next_node = path[end_node]
        solved_path.append(next_node)
        if next_node == start:
            break
        end_node = next_node
    print(solved_path)

def solve_puzzle(nodes, start, end):
    visited = []
    visited.append(start)
    queue = [start]
    path = {}
    while len(queue) > 0:
        node_coords = queue.pop(0)
        node = nodes[node_coords]
        x = node.x
        y = node.y
        # if f'{x},{y}' == end:
        #     print(path)
        #     break

        neighbors = node.neigbors
        for neighbor in neighbors:
            if neighbor.to_string() not in visited:
                buh = neighbor.to_string()
                visited.append(buh)
                queue.append(buh)
                path[buh] = node.to_string()
    back_track(path, end, start)


read_file("Puzzle1")