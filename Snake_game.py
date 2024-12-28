# SNAKE GAME

import tkinter as tk
import random
from tkinter import messagebox

class SnakeGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = tk.Canvas(self, width=600, height=600, bg='white')
        self.canvas.pack()

        for i in range(0, 600, 10):
            for j in range(0, 600, 10):
                self.canvas.create_rectangle(i, j, i+10, j+10, fill='light gray')

        self.canvas.create_rectangle(150, 150, 450, 300, fill='light blue')
        self.canvas.create_text(300, 225, text='SNAKE GAME', fill='black', font=('Arial', 30))

        self.snake = [(300, 300)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.score = 0

        self.bind('<KeyPress>', self.change_direction)

        self.move_snake()

    def create_food(self):
        x = random.randint(0, 59) * 10
        y = random.randint(0, 59) * 10
        self.canvas.create_rectangle(x, y, x+10, y+10, fill='red', tag='food')
        return x, y

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Right':
            head_x += 10
        elif self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        self.canvas.delete('snake')
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x+10, y+10, fill='dark green', tag='snake')

        if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 600 or \
                len(self.snake) != len(set(self.snake)):
            self.game_over()
            return

        if head_x == self.food[0] and head_y == self.food[1]:
            self.score += 1
            self.canvas.delete('food')
            self.food = self.create_food()
        else:
            self.snake.pop()

        self.after(150, self.move_snake)

    def change_direction(self, event):
        if event.keysym in ['Left', 'Right', 'Up', 'Down']:
            if (event.keysym == 'Left' and self.direction != 'Right') or \
                    (event.keysym == 'Right' and self.direction != 'Left') or \
                    (event.keysym == 'Up' and self.direction != 'Down') or \
                    (event.keysym == 'Down' and self.direction != 'Up'):
                self.direction = event.keysym

    def game_over(self):
        
        messagebox.showinfo('Game Over', f'Game Over\nScore: {self.score}')

        choice = messagebox.askyesno('New Game or Quit', 'Do you want to start a new game?')
        if choice:
            self.canvas.delete('all')
            self.__init__()  
        else:
            self.quit() 

if __name__ == "__main__":
    root = SnakeGame()
    root.title('Snake Game')
    root.mainloop()
