def relationship_status(from_member, to_member, social_graph):
    from_mem_dic = social_graph[from_member]['following']
    to_mem_dic = social_graph[to_member]['following']

    if from_member in to_mem_dic and to_member in from_mem_dic:
        return('friends')
    elif from_member in to_mem_dic:
        return('followed by')
    elif to_member in from_mem_dic:
        return('follower')
    else:
        return('no relationship')
    
def tic_tac_toe(board):
    size = len(board)

    for horizontal in board:
        if horizontal[0] != "" and all(cell == horizontal[0] for cell in horizontal):
            return horizontal[0]

    for vertical in range(size):
        if board[0][vertical] != "" and all(board[horizontal][vertical] == board[0][vertical] for horizontal in range(size)):
            return board[0][vertical]

    if board[0][0] != "" and all(board[i][i] == board[0][0] for i in range(size)):
        return board[0][0]

    if board[0][size - 1] != "" and all(board[i][size - 1 - i] == board[0][size - 1] for i in range(size)):
        return board[0][size - 1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    runtime = 0

    while first_stop != second_stop:
        for stretch in route_map:
            if stretch[0] == first_stop:
                runtime += route_map[stretch]['travel_time_mins']
                first_stop = stretch[1]
                break
    return runtime