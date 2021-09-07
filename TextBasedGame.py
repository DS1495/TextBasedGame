#DanielSchroedl
rooms = {
    'Start Cell': {'East': 'Block 1'},
    'Block 1': {'East': 'Cell 1', 'South': 'Block 2'},
    'Cell 1': {'West': 'Block 1'},
    'Block 2': {'West': 'Cell 2', 'East': 'Cell 3', 'South': 'Block 3'},
    'Cell 2': {'East': 'Block 2'},
    'Cell 3': {'West': 'Block 2'},
    'Block 3': {'East': 'Cell 4', 'West': 'Guard Room'},
    'Cell 4': {'West': 'Block 3'},
    'Guard Room': {'East': 'Block 3'}
}
items = {
    'Start Cell': 'Map',
    'Block 1': 'Cleaver',
    'Cell 1': 'Igor',
    'Block 2': 'Razor',
    'Cell 2': 'Sergei',
    'Cell 3': 'Dmitri',
    'Block 3': 'Brick',
    'Cell 4': 'Nikolai',
    'Guard Room': 'Prison Guard'

}
print("-----------------------------------------------------------")
print("Gulag Escape Text Adventure Game")
print("Collect 7 items to overthrow guards, or be sent back to the Gulag.")
print("Move commands: South, North, East, West")
print("Add to Inventory: get 'item name'")
print("-----------------------------------------------------------")

state = 'Start Cell'
inventory = []


def get_new_state(state, direction):
    new_state = state
    for i in rooms:
        if i == state:
            if direction in rooms[i]:
                new_state = rooms[i][direction]

    return new_state


while 1:
    print('You are in the ', state)
    if state == 'Guard Room':
        print('Battling with Prison Guard', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) > 7:
            print('Congratulations Comrade - You Won!')
        else:
            print('Nyet, back to your cell - you need more items')
        break

    print('Available to you in this room is', items[state])
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go OR exit to give up: ')
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    direction = direction.capitalize()
    if direction == 'Exit':
        exit(0)
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':
        new_state = get_new_state(state, direction)
        if new_state == state:
            print('You cannot enter!')
        else:
            state = new_state
    else:
        print('Invalid direction!!')