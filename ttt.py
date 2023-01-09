import tkinter as tk

class TicTacToe:
  def __init__(self, root):
    self.root = root
    self.buttons = []
    for i in range(9):
      button = tk.Button(self.root, width=10, height=5, font=('Helvetica', '20'), command=lambda i=i: self.move(i))
      button.grid(row=i // 3, column=i % 3)
      self.buttons.append(button)
    self.current_player = 'X'

  def move(self, index):
    button = self.buttons[index]
    if button['text'] == '':
      button['text'] = self.current_player
      if self.has_won(self.current_player):
        tk.messagebox.showinfo('Game Over', f'{self.current_player} has won!')
        self.reset()
      elif self.is_full():
        tk.messagebox.showinfo('Game Over', 'It is a tie!')
        self.reset()
      else:
        self.current_player = 'O' if self.current_player == 'X' else 'X'

  def has_won(self, player):
    for i in range(3):
      if self.buttons[i]['text'] == player and self.buttons[i+3]['text'] == player and self.buttons[i+6]['text'] == player:
        return True
    for i in range(3):
      if self.buttons[i*3]['text'] == player and self.buttons[i*3+1]['text'] == player and self.buttons[i*3+2]['text'] == player:
        return True
    if self.buttons[0]['text'] == player and self.buttons[4]['text'] == player and self.buttons[8]['text'] == player:
      return True
    if self.buttons[2]['text'] == player and self.buttons[4]['text'] == player and self.buttons[6]['text'] == player:
      return True
    return False

  def is_full(self):
    return all(button['text'] != '' for button in self.buttons)

  def reset(self):
    for button in self.buttons:
      button['text'] = ''
    self.current_player = 'X'

root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()