from pG_regression import *

def where_shot(inp1, inp2):
    if inp1 == 'R':
        X1 = 2
    elif inp1 == 'L':
        X1 = 0
    elif inp1 == 'C':
        X1 = 1
    else:
        print("Please choose between three diffirent letters: R for right, L for left and C for center ")
    X2 = int(inp2)
    return X1, X2

def random_gen():
    #df = load_ds()
    rand = create_random_train(1000)
    score_rand = train_model(rand.loc[:, ['Input Side', 'Input Height']],
                             rand.loc[:, ['Scored']])
    #score_player = train_model(df.loc[:, ['Predicted Side', 'Predicted Height']],
    #                           df.loc[:, ['Scored']])
    jump = out_(score_rand)
    print(len(rand))
    return jump
def grid_to_word(coor1, coor2):
    grid = {'0, 3': 'left bottom corner',
            '0, 6': 'left middle',
            '0, 9': 'left upper corner',
            '1, 3': 'middle bottom corner',
            '1, 6': 'middle',
            '1, 9': 'middle upper corner',
            '2, 3': 'right bottom corner',
            '2, 6': 'right middle',
            '2, 9': 'right upper corner', }
    k = f'{str(coor1)}, {str(coor2)}'
    return grid[k]
def outcome(X1, X2, X11, X21):
    you = grid_to_word(X1, X2)
    gk = grid_to_word(X11, X21)
    print(f'You shoot in the {you}')
    if (X1 == X11) and (X2 == X21):
        print(f'Keeper jumps in {gk} and takes the ball')
        scored = 0
    else:
        print(f"You scored, as keeper jumped in {gk}")
        scored = 1
    return scored
