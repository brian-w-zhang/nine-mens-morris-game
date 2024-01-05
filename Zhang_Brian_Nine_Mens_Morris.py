"""NINE MEN'S MORRIS

This program allows two human players to play the ancient game that dates
all the way back to the Roman Empire, known as Nine Men's Morris.
Below are the basic rules that explain how the game is played.

Nine Men's Morris is played using 9 white pieces, 9 black pieces, and a grid
with 24 intersections (points). The player with white pieces goes first.

The aim of Nine Men's Morris is to make lines of 3-in-a-row, called mills.
In phase 1, players take turns placing one of their 9 pieces on the board.
After all pieces have been placed, phase 2 begins. In phase 2, players
alternate moving one of their pieces to a vacant adjacent point. If a mill is
formed at any time, the player who made the mill removes an opponents piece,
as long as it isn't currently part of a mill (unless no other pieces are
available). If a player only has 3 pieces left, their pieces gain the ability
to jump to any vacant point. A player wins when the opponent is reduced to 2
pieces, or if they are unable to move. 
"""

__author__ = 'Brian Zhang'

from time import sleep

# Horizontal line length constants for board printing.
L_LINE = 24
M_LINE = 14
S_LINE = 4
XS_LINE = 3

# Locations of points that are adjacent to the point with a position
# of its index.
ADJ = [ [1, 9],
        [0, 2, 4],
        [1, 14],
        [4, 10],
        [1, 3, 5, 7],
        [4, 13],
        [7, 11],
        [4, 6, 8],
        [7, 12],
        [0, 10, 21],
        [3, 9, 11, 18],
        [6, 10, 15],
        [8, 13, 17],
        [5, 12, 14, 20],
        [2, 13, 23],
        [11, 16],
        [15, 17, 19],
        [12, 16],
        [10, 19],
        [16, 18, 20, 22],
        [13, 19],
        [9, 22],
        [19, 21, 23],
        [14, 22]
      ]

# Locations of the 3 pieces in a possible vertical mill.
VER = [ [0, 9, 21],
        [1, 4, 7],
        [2, 14, 23],
        [3, 10, 18],
        [5, 13, 20],
        [6, 11, 15],
        [8, 12, 17],
        [16, 19, 22]
      ]

# Locations of the 3 pieces in a possible horizontal mill.
HOR = [ [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [9, 10, 11],
        [12, 13, 14],
        [15, 16, 17],
        [18, 19, 20],
        [21, 22, 23]
      ]


def print_board(spots):
    """Print the game board with different pieces that correspond with the
    items in the list spots, at locations that match the indexes.

    The positions on the board are the numbers 0 to 23, and the items at 
    index n represent the piece at position n.
    The items in the list spots can be one of the following:
    '▓▓▓' (white piece), '░░░' (black piece), ' ● ' (no piece/placeholder)
    """

    print()
    print(spots[0] + '(00)' + '━'*L_LINE + spots[1] + '(01)' + '━'*L_LINE +
          spots[2] + '(02)')
    for i in range(3):
        print(' ' + '┃' + ' '*30 + '┃' + ' '*30 + '┃')
    print(' ' + '┃' + ' '*8 + spots[3] + '(03)' + '━'*M_LINE +
          spots[4] + '(04)' + '━'*14 + spots[5] + '(05)' + ' '*4 + '┃')
    for i in range(3):
        print(' ' + '┃' + ' '*9 + '┃' + ' '*20 + '┃' + ' '*20 + '┃' +
              ' '*9 + '┃')
    print(' ' + '┃' + ' '*9 + '┃' + ' '*8 + spots[6] + '(06)' + '━'*S_LINE +
          spots[7] + '(07)' + '━'*S_LINE + spots[8] + '(08)' + ' '*4 + '┃' +
          ' '*9 + '┃')
    for i in range(3):
        print(' ' + '┃' + ' '*9 + '┃' + ' '*9 + '┃' + ' '*21 + '┃' +
              ' '*9 + '┃' + ' '*9 + '┃')
    print(spots[9] + '(09)' + '━'*XS_LINE + spots[10] + '(10)' +
          '━'*XS_LINE + spots[11] + '(11)' + ' '*15 + spots[12] + '(12)' +
          '━'*XS_LINE + spots[13] + '(13)' + '━'*XS_LINE + spots[14] + '(14)')
    for i in range(3):
        print(' ' + '┃' + ' '*9 + '┃' + ' '*9 + '┃' + ' '*21 + '┃' +
              ' '*9 + '┃' + ' '*9 + '┃')
    print(' ' + '┃' + ' '*9 + '┃' + ' '*8 + spots[15] + '(15)' +
          '━'*S_LINE + spots[16] + '(16)' + '━'*S_LINE + spots[17] +
          '(17)' + ' '*4 + '┃' + ' '*9 + '┃')
    for i in range(3):
        print(' ' + '┃' + ' '*9 + '┃' + ' '*20 + '┃' + ' '*20 + '┃' +
              ' '*9 + '┃')
    print(' ' + '┃' + ' '*8 + spots[18] + '(18)' + '━'*M_LINE + spots[19] +
          '(19)' + '━'*M_LINE + spots[20] + '(20)' + ' '*4 + '┃')
    for i in range(3):
        print(' ' + '┃' + ' '*30 + '┃' + ' '*30 + '┃')
    print(spots[21] + '(21)' + '━'*L_LINE + spots[22] +'(22)' +
          '━'*L_LINE + spots[23] + '(23)')
    print()


def adjacent_points(location: int) -> list:
    """Return the positions of adjacent points to the the piece at
    position location.

    >>> adjacent_points(3)
    [4, 10]
    >>> adjacent_poins(10)
    [3, 9, 11, 18]
    >>> adjacent_points(22)
    [19, 21, 23]
    """
    
    return ADJ[location]


def vertical_mills(location: int) -> list:
    """Return the positions of pieces in the possible vertical mill that
    involves the piece at position location.

    >>> vertical_mills(1)
    [1, 4, 7]
    >>> vertical_mills(17)
    [8, 12, 17]
    """

    for item in VER:
        if location in item:
            possible_mill = item
    return possible_mill


def horizontal_mills(location:int) -> list:
    """Return the positions of pieces in the possible horizontal mill that
    involves the piece at position location.

    >>> horizontal_mills(6)
    [6, 7, 8]
    >>> horizontal_mills(20)
    [18, 19, 20]
    """

    for item in HOR:
        if location in item:
            possible_mill = item
    return possible_mill


def check_location(spots: list, location:int) -> str:
    """Return the symbol of the piece that is on point location, by
    checking what the item at index location is in the list spots."""

    return spots[location]


def vacant_points(spots: list) -> list:
    """Return the indexes of items in spots that equal ' ● '."""

    vacant_points = []
    for i in range(24):
        piece_identity = spots[i]
        if piece_identity == ' ● ':
            vacant_points.append(i)
    return vacant_points
    

def possible_moves(spots: list, location: int, piece_count: int) -> list:
    """Return the possible points a piece at point location can move to."""

    adj_points = adjacent_points(location)
    empty_points = vacant_points(spots)
    candidate_moves = []

    # Pieces can jump to any vacant point if the controllor has 3 left.
    if piece_count == 3:
        candidate_moves = empty_points
    # Normally, pieces can only move to vacant points that are adjacent
    # to the piece's position before it moved
    elif piece_count > 3:
        for point in empty_points:
            if point in adj_points:
                candidate_moves.append(point)
    return candidate_moves


def check_mill(spots: list, location: int, player_piece: str) -> bool:
    """Return True if the piece at position location is in a mill.
    Otherwise, return false.
    """

    # Mills are consecutive lines of 3 pieces of the same colour in a row.
    consecutive_ver = 0
    consecutive_hor = 0
    possible_horizontal = horizontal_mills(location)
    possible_vertical = vertical_mills(location)
    
    for point in possible_vertical:
        
        if check_location(spots, point) == player_piece:
            consecutive_ver += 1
    for point in possible_horizontal:
        if check_location(spots, point) == player_piece:
            consecutive_hor += 1
    if consecutive_ver == 3 or consecutive_hor == 3:
        mill = True
    else:
        mill = False
    return mill


def get_position_basic(spots: list) -> int:
    """Return valid position that a player inputs."""

    while True:
        try:
            position = int(input('Enter a position (0-23): '))
        except ValueError:
            print('The position not an integer! Try again.')
            continue
        if position < 0 or position > 23:
            print('Please input an integer between 0 and 23.')
            continue
        else:
            break
    return position


def get_place_position(spots: list) -> int:
    """Return position that a player wants to place a piece on."""

    while True:
        position = get_position_basic(spots)
        # Pieces cannot be placed onto an occupied point.
        if position not in vacant_points(spots):
            print('That position is occupied! Try again.')
        else:
            break
    return position


def get_move_position(spots: list, player_piece: str, piece_count: int) -> int:
    """Return position of the piece a player wants to move."""

    while True:
        position = get_position_basic(spots)
        candidate_moves = possible_moves(spots, position, piece_count)
        # Players can only move their own pieces.
        if spots[position] != player_piece:
            print('You do not control a piece on that position! Try again.')
            continue
        # A piece chosen to be moved must have possible moves available.
        elif candidate_moves == []:
            print('That piece has no possible moves. Try again.')
            continue
        else:
            break
    return position


def get_remove_position(spots: list, oppo_piece: str) -> list:
    """Return position of opposing piece player wantes to remove."""

    all_mills = True

    while True:
        position = get_position_basic(spots)
        test_indexes = []
        if spots[position] != oppo_piece:
            print('There is no opposing piece at that position. Try again.')
            continue
        
        for i in range(24):
            piece = spots[i]
            if piece == oppo_piece:
                test_indexes.append(i)
        for index in test_indexes:
            if check_mill(spots, index, oppo_piece) == False:
                all_mills = False

        mill = check_mill(spots, position, oppo_piece)
        if all_mills == False and mill == True:
            print('You cannot remove an opposing piece that is a part of ' +
                  'a mill,\nunless no other pieces are available.')
            continue
        else:
            break
    return position

    
def place_piece(spots: list, player_piece: str) -> list:
    """Return the updated spots list that has a value of player_piece
    ('▓▓▓' or '░░░') at index n, where n is a valid unoccupied position
    the player inputs.
    """

    if player_piece == '▓▓▓':
        player = 'White'
    else:
        player = 'Black'

    print('Where would you like to place your piece?')
    place_position = get_place_position(spots)
    spots[place_position] = player_piece
    print('{} places a piece on point {}.'.format(player, place_position))
    sleep(1.5)
    print_board(spots)

    mill = check_mill(spots, place_position, player_piece)
    if player_piece == '▓▓▓':
        oppo_piece = '░░░'
    elif player_piece == '░░░':
        oppo_piece = '▓▓▓'

    if mill == True:
        print('{} formed a mill.'.format(player))
        remove_piece(spots, oppo_piece)
        sleep(1.5)
        print_board(spots)
    else:
        print('No mills have been formed.')
    sleep(1.5)
    return spots


def move_piece(spots: list, player_piece: str, piece_count: int) -> list:
    """Return the updated spots list that has a value of player_piece
    ('▓▓▓' or '░░░') at index n, and the placeholder value (' ● ') at index m,
    where n is the position the player moved their piece to, and m is the
    old position of the piece that just moved.
    """

    if player_piece == '▓▓▓':
        player = 'White'
    else:
        player = 'Black'

    if piece_count == 3:
        print('The {} pieces can jump to any vacant point.'
              .format(player))

    print('Where is the position of the piece you want to move?')
    moving_piece = get_move_position(spots, player_piece, piece_count)
    print('The piece you chose can move to one of the following positions:')
    candidate_moves = possible_moves(spots, moving_piece, piece_count)
    for move in candidate_moves:
        print('> Point {}'.format(move))
    print('Where do you want to move the piece at point {} to?'
          .format(moving_piece))
    
    while True:
        new_position = get_place_position(spots)
        if new_position not in candidate_moves:
            print('Your piece cannot move to that position! Try again.')
            continue
        else:
            break

    spots[moving_piece] = ' ● '
    spots[new_position] = player_piece
    print('{} moves their piece from point {} to point {}.'
          .format(player, moving_piece, new_position))
    sleep(1.5)
    print_board(spots)

    mill = check_mill(spots, new_position, player_piece)
    if player_piece == '▓▓▓':
        oppo_piece = '░░░'
    elif player_piece == '░░░':
        oppo_piece = '▓▓▓'
    if mill == True:
        print('{} formed a mill.'.format(player))
        remove_piece(spots, oppo_piece)
        sleep(1.5)
        print_board(spots)
    else:
        print('No mills have been formed.')
    sleep(1.5)
    return spots


def count_pieces(spots: list, player_piece: str) -> int:
    """Return the number of occurences of player_piece in spots."""

    piece_count = 0
    for piece in spots:
        if piece == player_piece:
            piece_count += 1
    return piece_count


def remove_piece(spots: list, oppo_piece: str) -> list:
    """Return the updated spots list that has a value of oppo_piece
    at index n replaced with the placeholder value, where n is the
    position of the opposing piece the player wishes to remove.
    """

    if oppo_piece == '▓▓▓':
        player = 'Black'
    else:
        player = 'White'

    sleep(1.5)
    print('Where is the location of an opposing piece you want to remove?')
    position = get_remove_position(spots, oppo_piece)
    spots[position] = ' ● '
    print('{} removes the piece on point {}.'.format(player, position))
    return spots
    

def check_trapped(spots: list, player_piece: str, piece_count: int) -> bool:
    """Return True if a player can't move. Otherwise, return False."""

    if piece_count == 3:
        return False
    trapped_pieces = 0
    test_indexes = []
    for i in range(24):
        piece = spots[i]
        if piece == player_piece:
            test_indexes.append(i)

    for index in test_indexes:
        candidate_moves = possible_moves(spots, index, piece_count)
        if candidate_moves == []:
            trapped_pieces += 1
    if piece_count == trapped_pieces:
        all_trapped = True
    else:
        all_trapped = False
    return all_trapped

            
def check_winner(spots: list) -> str:
    """Return the colour ('black' or 'white') of the winning player.
    If there is no winner yet, return 'none'.
    """

    winner = 'none'
    white_count = count_pieces(spots, '▓▓▓')
    black_count = count_pieces(spots, '░░░')
    white_trapped = check_trapped(spots, '▓▓▓', white_count)
    black_trapped = check_trapped(spots, '░░░', black_count)

    if white_count < 3 or white_trapped == True:
        winner = 'Black'
    elif black_count < 3 or black_trapped == True:
        winner = 'White'
    return winner
 

def play_game():
    """Carry out a game of Nine Men's Morris, including both phases."""

    spots = []
    black_placed = 0
    winner = 'none'
    for i in range(24):
        spots.append(' ● ')
    print_board(spots)

    # Phase 1: Placing Pieces
    print('Welcome to the game!')
    print('In phase 1, players take turns placing their pieces.')
    sleep(2.5)
    while black_placed < 9:
        print("\nWHITE'S TURN:")
        print('White has {} piece(s) left to place.'.format(9-black_placed))
        place_piece(spots, '▓▓▓')
        print("\nBLACK'S TURN:")
        print('Black has {} piece(s) left to place.'.format(9-black_placed))
        place_piece(spots, '░░░')
        black_placed += 1

    # Phase 2: Moving Pieces
    print('\nAll 18 pieces have been placed. Phase 2 will now begin.')
    print('In phase 2, players take turns moving their pieces.')
    while True:
        white_count = count_pieces(spots, '▓▓▓')
        black_count = count_pieces(spots, '░░░')
        winner = check_winner(spots)
        if winner != 'none':
            break
        print("\nWHITE'S TURN:")
        move_piece(spots, '▓▓▓', white_count)
        white_count = count_pieces(spots, '▓▓▓')
        black_count = count_pieces(spots, '░░░')
        winner = check_winner(spots)
        if winner != 'none':
            break
        print("\nBLACK'S TURN:")
        move_piece(spots, '░░░', black_count)

    # Find who lost and how they lost
    if 'White' == winner:
        loser = 'Black'
        loser_pieces = black_count
    else:
        loser = 'White'
        loser_pieces = white_count
    if loser_pieces < 3:
        print('{} has less than 3 pieces, and cannot make mills.'.format(loser))
    else:
        print('{} is trapped, and has no legal moves.'.format(loser))
    print('Game over! {} is the winner.'.format(winner))

    input('Press enter to return to the home screen: ')
    menu()


def how_to_play():
    """Print intructions on how to play Nine Men's Morris"""

    print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  _  _              _         ___ _           
 | || |_____ __ __ | |_ ___  | _ \ |__ _ _  _ 
 | __ / _ \ V  V / |  _/ _ \ |  _/ / _` | || |
 |_||_\___/\_/\_/   \__\___/ |_| |_\__,_|\_, |
                                         |__/ 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Nine Men's Morris is played using 9 white pieces, 9 black pieces, and a grid
with 24 intersections (points). The player with white pieces goes first.
Board Example:
'▓▓▓': white piece    '░░░': black piece    ' ● ': no piece/placeholder

    ▓▓▓(00)━━━━━━━━━━━━━━━━━━━━━━━━ ● (01)━━━━━━━━━━━━━━━━━━━━━━━━ ● (02)
     ┃                              ┃                              ┃
     ┃                              ┃                              ┃
     ┃                              ┃                              ┃
     ┃        ░░░(03)━━━━━━━━━━━━━━ ● (04)━━━━━━━━━━━━━━ ● (05)    ┃
     ┃         ┃                    ┃                    ┃         ┃
     ┃         ┃                    ┃                    ┃         ┃
     ┃         ┃                    ┃                    ┃         ┃
     ┃         ┃        ▓▓▓(06)━━━━░░░(07)━━━━ ● (08)    ┃         ┃
     ┃         ┃         ┃                     ┃         ┃         ┃
     ┃         ┃         ┃                     ┃         ┃         ┃
     ┃         ┃         ┃                     ┃         ┃         ┃
    ▓▓▓(09)━━━░░░(10)━━━░░░(11)                ● (12)━━━▓▓▓(13)━━━▓▓▓(14)
     ┃         ┃         ┃                     ┃         ┃         ┃
     ┃         ┃         ┃                     ┃         ┃         ┃
     ┃         ┃         ┃                     ┃         ┃         ┃
     ┃         ┃         ● (15)━━━━▓▓▓(16)━━━━░░░(17)    ┃         ┃
     ┃         ┃                    ┃                    ┃         ┃
     ┃         ┃                    ┃                    ┃         ┃
     ┃         ┃                    ┃                    ┃         ┃
     ┃        ▓▓▓(18)━━━━━━━━━━━━━━ ● (19)━━━━━━━━━━━━━━░░░(20)    ┃
     ┃                              ┃                              ┃
     ┃                              ┃                              ┃
     ┃                              ┃                              ┃
    ░░░(21)━━━━━━━━━━━━━━━━━━━━━━━━░░░(22)━━━━━━━━━━━━━━━━━━━━━━━━░░░(23)
""")

    input('Press enter to read the instructions: ')
    print("""
The aim of Nine Men's Morris is to make lines of 3-in-a-row, called mills.
In phase 1, the board starts without any pieces on it, and players take
turns placing one of their 9 pieces on the board.

After all pieces have been placed, phase 2 begins. In phase 2, players take
turns moving one of their pieces to a vacant adjacent point.

If a mill is formed at any time, the player who made the mill removes an
opponents piece, as long as it isn't currently part of a mill (unless no
other pieces are available).

If a player only has 3 pieces left, their pieces gain the ability to jump
to any vacant point.

A player wins when the opponent is reduced to 2 pieces, or if they are unable
to move. 
""")
    input('Press enter to return to the home screen: ')
    menu()


def menu():
    """Print the game menu."""

    print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    )                   *                     *                      
 ( /(                 (  `         (        (  `                     
 )\())(          (    )\))(    (   )\       )\))(      (   (  (      
((_)\ )\  (     ))\  ((_)()\  ))\ ((_) (   ((_)()\  (  )(  )( )\ (   
 _((_|(_) )\ ) /((_) (_()((_)/((_))\ ) )\  (_()((_) )\(()\(()((_))\  
| \| |(_)_(_/((_))   |  \/  (_)) _(_/(((_) |  \/  |((_)((_)((_|_|(_) 
| .` || | ' \)) -_)  | |\/| / -_) ' \)|_-< | |\/| / _ \ '_| '_| (_-< 
|_|\_||_|_||_|\___|  |_|  |_\___|_||_|/__/ |_|  |_\___/_| |_| |_/__/

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

  _         ___ _              ___                
 / |  ___  | _ \ |__ _ _  _   / __|__ _ _ __  ___ 
 | | |___| |  _/ / _` | || | | (_ / _` | '  \/ -_)
 |_|       |_| |_\__,_|\_, |  \___\__,_|_|_|_\___|
                       |__/                       
  ___         _  _              _         ___ _           
 |_  )  ___  | || |_____ __ __ | |_ ___  | _ \ |__ _ _  _ 
  / /  |___| | __ / _ \ V  V / |  _/ _ \ |  _/ / _` | || |
 /___|       |_||_\___/\_/\_/   \__\___/ |_| |_\__,_|\_, |
                                                     |__/ 
""")

    while True:
        choice = input('Enter 1 to play, or 2 to learn how to play: ')
        if choice != '1' and choice != '2':
            print('The only options are 1 or 2. Try again.')
            continue
        break
    if choice == '1':
        play_game()
    elif choice == '2':
        how_to_play()


def main():    
    menu()


if __name__ == '__main__':
    main()

