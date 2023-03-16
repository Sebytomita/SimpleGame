import tkinter as tk
from PIL import Image, ImageTk
from functools import partial
from tkinter.colorchooser import askcolor

root = tk.Tk()
game_frm = ''
name_label = ''
active_player = ''
lines_table = []
lines_dict = {}
spaces_table = []
players_dict = {}

for i in range(11):
    temp_list = []
    if i % 2 == 0:
        for j in range(5):
            temp_list.append('black')
    else:
        for j in range(6):
            temp_list.append('black')
    lines_table.append(temp_list)

# print(lines_table)


# Checking winner every turn
def check_winner():
    for k in range(5):
        i = k*2
        temp_list1 = lines_table[i]
        temp_list2 = lines_table[i + 1]
        temp_list3 = lines_table[i + 2]
        # print('##################################')
        # print(f'LINE -> {lines_table[i]}')
        # print(f'LINE + 1 -> {lines_table[i + 1]}')
        # print(f'LINE + 2 -> {lines_table[i + 2]}')
        try:
            blacks = 0
            # Algorithm for checking if a square has been completed
            for j in range(5):

                # print(f'{temp_list1[j]}={temp_list2[j]}={temp_list2[j + 1]}={temp_list3[j]}')
                # print('BEFORE IF')
                # In case a square has been completed by a player, changing its color and updating player's score
                if temp_list1[j] == temp_list2[j] and temp_list2[j] == temp_list2[j + 1] and temp_list2[j+1] == temp_list3[j] and temp_list1[j] != 'black':
                    # print(f"{temp_list1[j]} - BOX - {i}-{j}")
                    color = (players_dict[temp_list1[j]])[1]
                    (spaces_table[int(i / 2)])[j].config(bg = color)
                    # Updating player's score
                    score = (players_dict[temp_list1[j]])[0]
                    (players_dict[temp_list1[j]])[0] = score + 1
                    print(players_dict)
                    continue
                else:
                    blacks += 1

            if blacks == 0:
                end_screen()
                # print('AFTER IF')
        except:
            pass


# Method for changing the color of the
# buttons ( lines ) when pressed
def change_line_colour(button):
    global active_player, name_label
    # print(f'ACTIVE PLAYER - {active_player}')
    # Changing player's turn, changing the main list
    # according to what buttons are pressed
    column = int(lines_dict[button][:-2])
    if column == 10:
        line = int(lines_dict[button][3:])
    else:
        line = int(lines_dict[button][2:])
    temp_list = lines_table[column]
        
    # A very uselessly complicated way to change turn
    # and change buttons' background color
    if active_player == (list(players_dict.keys()))[0]:

        # print(f'COLOR - {(players_dict[(list(players_dict.keys()))[0]])[1]}')
        button.config(bg=(players_dict[(list(players_dict.keys()))[0]])[1])
        button['state'] = 'disabled'
        temp_list[line] = active_player
        active_player = (list(players_dict.keys()))[1]
        name_label.config(text=f'{active_player}`s turn')
    elif active_player == (list(players_dict.keys()))[1]:
        button.config(bg=(players_dict[(list(players_dict.keys()))[1]])[1])
        button['state'] = 'disabled'
        temp_list[line] = active_player
        active_player = (list(players_dict.keys()))[0]
        name_label.config(text=f'{active_player}`s turn')

    check_winner()
    # print(f"COLUMN = {column}, LINE = {line}")


# Creating the game frame, with all its elements
def creating_game_window():
    global game_frm, players_dict, name_label
    players = {}

    # Method that creates a 'color chosing dialog window', 
    # which will be accesed by the player to select their color
    def choose_player_color(button):
        color = askcolor()
        button.config(bg=color[1])

    # Method for retrieving player's name and color
    # and initializes the game itself
    def getting_info():
        global active_player
        for i in range(2):
            player_name = (players[i])[0].get()
            player_color = (players[i])[1]['bg']
            players_dict[player_name] = [0, player_color]
        # print(players_dict)
        active_player = (list(players_dict.keys()))[0]
        players_frm.destroy()
        submit_button.destroy()
        game_frm.pack()
        name_label.pack(pady=10, padx=(300,0))
        name_label.config(text=f'{active_player}`s turn')


    game_window = tk.Toplevel(root)
    game_window.config(bg='white')
    # Creating fields for users to add their names and colours
    players_frm = tk.Frame(game_window, bg='white')
    players_frm.columnconfigure([0,1], minsize=200)
    players_frm.rowconfigure(2, minsize=100)
    for i in range(2):
        player_lbl = tk.Label(players_frm, bg='white', fg='black', text=f'Player {i + 1}', font=('Helvetica', 20))
        player_name = tk.Entry(players_frm, bg='white', fg='black', font=('Helvetica', 20))
        colour_picker = tk.Button(players_frm, bg='grey', font=('',20), relief=None, bd=0, highlightthickness=0, highlightbackground=None)
        colour_picker.config(command=partial(choose_player_color, colour_picker))
        player_lbl.grid(row=0, column=i, pady=20, padx=150, sticky='nsew')
        player_name.grid(row=1, column=i, pady=20, padx=50, sticky='nsew')
        colour_picker.grid(row=2, column=i, padx=50, sticky='nsew')
        players[i] = [player_name, colour_picker]

    submit_button = tk.Button(game_window, bg='green', fg='white', text='START', font=('Helvetica', 20), width=15, height=2, relief=None, bd=0, highlightthickness=0, highlightbackground=None, command=getting_info)
    players_frm.pack()
    submit_button.pack(pady=50)

    game_frm = tk.Frame(game_window, bg='white')
    for j in range(11):
        temp_list = []
        if j % 2 == 0:
            for i in range(11):

                # The rows with circles and horizontal lines
                # Adding just the circles
                if i % 2 == 0:
                    img_temp = Image.open('circle.png')
                    img_temp = img_temp.resize((60,60), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img_temp)
                    label1 = tk.Label(game_frm, bg='white', image=img)
                    label1.image = img
                    label1.grid(row=j, column=i)

                # The rows with just vertical lines
                else:
                    line = tk.Button(game_frm, bg='black', height=1, width=20, font=('', 6), relief=None, bd=0, highlightthickness=0, highlightbackground=None)
                    line.config(command=partial(change_line_colour, line))
                    line.grid(row=j, column=i)
                    lines_dict[line] = f'{j}-{int(i / 2)}'
        else:
            # The rows with circles and horizontal lines
            # Adding just the lines, next to the circles ( code above )
            for i in range(11):
                if i % 2 == 0:
                    line = tk.Button(game_frm, bg='black', width=1, height=8, relief=None, bd=0, highlightthickness=0, highlightbackground=None)
                    line.config(command=partial(change_line_colour, line))
                    line.grid(row=j, column=i)
                    lines_dict[line] = f'{j}-{int(i / 2)}'
            
                # Next to the vertical lines, adding empty space to separate lines
                # These spaces will later be colored according to what square is completed by the players
                else:
                    empty = tk.Frame(game_frm, bg='white', width=120, height=120)
                    empty.grid(row=j, column=i)
                    temp_list.append(empty)
            spaces_table.append(temp_list)
    name_label = tk.Label(game_window, bg='white', fg='black', text='Player`s turn', font=('Helvetica', 35))


def end_screen():
    global game_frm
    game_frm.destroy()
    end_screen = tk.Frame(root, bg='white')
    winner = tk.Label(root, bg='white')

def main_menu():
    root.columnconfigure(0, minsize=300)
    root.rowconfigure([0,1,2,3], minsize=120)
    root.config(bg='white')
    buttons = ['Title', 'Play', 'Settings', 'Exit']
    commands = ['', creating_game_window, '', root.destroy]
    for i in range(len(buttons)):
        if buttons[i] == 'Title':
            title = tk.Label(root, font=('Helvetica', 35), text='Lines Game', bg='white', fg='black')
            title.grid(row=0, column=0, padx=10, sticky='nsew')
        else:
            button = tk.Button(root, text=buttons[i], bg='#c4c4c4', fg='black', font=('Helvetica', 20), highlightthickness = 0, bd = 0, relief=None, command=commands[i])
            if buttons[i] == 'Play':
                button.config(bg='#05dffc', fg='white')
            elif buttons[i] == 'Exit':
                button.config(bg='#a82121', fg='white')
            button.grid(row=i, column=0, pady=(0,40), padx=10, sticky='nsew')

# print(lines_dict)
# print(spaces_table)

main_menu()

root.mainloop()