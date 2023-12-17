import tkinter as tk
from tkinter import ttk
import random
import math


class Player:
    def __init__(self, name):
        self.name = name
        self.late = tk.StringVar(value="0")
        self.dps = tk.BooleanVar(value=False)
        self.hps = tk.BooleanVar(value=False)
        self.boss1 = tk.BooleanVar(value=False)
        self.boss2 = tk.BooleanVar(value=False)
        self.boss3 = tk.BooleanVar(value=False)
        self.boss4 = tk.BooleanVar(value=False)
        self.boss5 = tk.BooleanVar(value=False)
        self.boss6 = tk.BooleanVar(value=False)
        self.boss7 = tk.BooleanVar(value=False)
        self.boss8 = tk.BooleanVar(value=False)
        self.boss9 = tk.BooleanVar(value=False)
        self.boss10 = tk.BooleanVar(value=False)
        self.init_credit = 100
        self.credit = 100
        self.roll = -1


class FamilyCpApp:
    def __init__(self, root):
        self.root = root
        root.title("Family Credit Point Roll")

        self.players = []
        self.create_widgets()

    def create_widgets(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.add_player_frame = ttk.Frame(self.root)
        self.add_player_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.add_player_entry = ttk.Entry(self.add_player_frame)
        self.add_player_entry.pack()
        self.init_credit_entry = ttk.Entry(self.add_player_frame, text="100")
        self.init_credit_entry.pack()
        self.add_player_button = ttk.Button(
            self.add_player_frame, text="Add Player", command=self.add_player)
        self.add_player_button.pack()
        self.roll_button = ttk.Button(
            self.add_player_frame, text="Roll", command=self.roll_all)
        self.roll_button.pack()
        self.clear_button = ttk.Button(
            self.add_player_frame, text="Update Credits", command=self.clear_roll_result)
        self.clear_button.pack()

        self.update_table()

    def roll_all(self):
        self.update_credit_all()
        for player in self.players:
            if random.random() <= player.credit/100:
                player.roll = 1
            else:
                player.roll = 0

        self.update_table()

    def clear_roll_result(self):
        for player in self.players:
            player.roll = -1

        self.update_table()

    def add_player(self):
        player_name = self.add_player_entry.get()
        init_credit = self.init_credit_entry.get()
        if player_name:
            player = Player(player_name)
            player.init_credit = init_credit
            # player.dps.trace_add("write", self.update_table)
            # player.hps.trace_add("write", self.update_table)
            self.players.append(player)

        self.update_table()

    def update_credit_all(self):
        for player in self.players:
            credit = float(player.init_credit)
            if player.dps.get():
                credit += 5

            if player.hps.get():
                credit += 5

            late = float(player.late.get())
            credit -= math.pow(late/15, 3)*15

            if credit < 0:
                credit = 0

            player.credit = credit

    def update_table(self):
        if len(self.players) == 0:
            return

        self.update_credit_all()

        for widget in self.table_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.table_frame, text="Player Name").grid(row=0, column=0)
        ttk.Label(self.table_frame, text="Late Minutes").grid(row=0, column=1)
        ttk.Label(self.table_frame, text="Best DPS").grid(row=0, column=2)
        ttk.Label(self.table_frame, text="Boss 1").grid(row=0, column=3)
        ttk.Label(self.table_frame, text="Boss 2").grid(row=0, column=4)
        ttk.Label(self.table_frame, text="Boss 3").grid(row=0, column=5)
        ttk.Label(self.table_frame, text="Boss 4").grid(row=0, column=6)
        ttk.Label(self.table_frame, text="Boss 5").grid(row=0, column=7)
        ttk.Label(self.table_frame, text="Boss 6").grid(row=0, column=8)
        ttk.Label(self.table_frame, text="Boss 7").grid(row=0, column=9)
        ttk.Label(self.table_frame, text="Boss 8").grid(row=0, column=10)
        ttk.Label(self.table_frame, text="Boss 9").grid(row=0, column=11)
        ttk.Label(self.table_frame, text="Boss 10").grid(row=0, column=12)

        ttk.Label(self.table_frame, text="Credit").grid(row=0, column=13)
        ttk.Label(self.table_frame, text="Roll Result").grid(row=0, column=14)
        for i, player in enumerate(self.players):
            i = i+1
            ttk.Label(self.table_frame, text=player.name).grid(
                row=i, column=0)  # 玩家名
            ttk.Entry(self.table_frame, textvariable=player.late).grid(
                row=i, column=1)  # 迟到时间
            ttk.Checkbutton(self.table_frame, variable=player.dps).grid(
                row=i, column=2)  # DPS贡献
            ttk.Label(self.table_frame, text=str(
                player.credit)).grid(row=i, column=4)  # 信用分
            roll = ""
            if player.roll == 1:
                roll = "√"
            elif player.roll == 0:
                roll = "×"
            elif player.roll == -1:
                roll = "Unknown"
            ttk.Label(self.table_frame, text=roll).grid(
                row=i, column=5)  # Roll


if __name__ == "__main__":
    root = tk.Tk()
    app = FamilyCpApp(root)
    root.mainloop()
