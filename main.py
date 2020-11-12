import os
import copy
import time
def display(vboard):
  os.system("printf '\033c'")  
  number = [1,2,3]
  print ('  1 2 3')
  iterator = 0
  for row in vboard:
    print(number[iterator], end=' ')
    for col in row:
        print(col, end=' ')
    iterator+=1
    print('')
def someonewon(vboard):
  for row in vboard:
    col0 = row[0]
    col1 = row[1]
    col2 = row[2]
    if col0 == col1 and col1 == col2 and not col1 == " " :
      return True
  row0 = vboard[0][0]
  row1 = vboard[1][0]
  row2 = vboard[2][0]
  if row0 == row1 and row1 == row2 and not row1 == " " :
    return True
  row0 = vboard[0][1]
  row1 = vboard[1][1]
  row2 = vboard[2][1]
  if row0 == row1 and row1 == row2 and not row1 == " " :
    return True
  row0 = vboard[0][2]
  row1 = vboard[1][2]
  row2 = vboard[2][2]
  if row0 == row1 and row1 == row2 and not row1 == " " :
    return True
  if not vboard[1][1] == " ":
    mid = vboard[1][1]
    if mid == vboard[0][0] and mid == vboard[2][2]:
      return True
    if mid == vboard[0][2] and mid == vboard[2][0]:
      return True
def makemove(vboard):
  for row in vboard:
    for col in range(3):
      if row[col] == " ":
        row[col] = "O"
        if someonewon(vboard):
          return
        else:
          row[col] = " "
  for row in vboard:
    for col in range(3):
      if row[col] == " ":
        row[col] = "X"
        if someonewon(vboard):
          row[col] = "O"
          return
        else:
          row[col] = " "
  if vboard[1][1] == " ":
    vboard[1][1] = "O"
    return
  if vboard[1][1] == "O":
    if vboard[1][0] + vboard[1][2] == "  ":
        vboard[1][0] = "O"
        return
    if vboard[0][1] + vboard[2][1] == "  ":
        vboard[0][1] = "O"
        return
  if vboard[1][0] + vboard[2][1] == "XX":
    if vboard [2][0] == " ":
      vboard[2][0] = "O"
      return
  if vboard[1][0] + vboard[0][1] == "XX":
    if vboard[0][0] == " ":
      vboard[0][0] = "O"
      return
  if vboard[0][1] + vboard[1][2] == "XX":
    if vboard[0][2] == " ":
      vboard[0][2] = "O"
      return
  if vboard[1][2] + vboard[2][1] == "XX":
    if vboard[2][2] == " ":
      vboard[2][2] = "O"
      return
  corners = vboard[0][0] + vboard[2][2]
  if corners.strip() == "X":
    if corners.startswith(" "):
      vboard[0][0] = "O"
    else:
      vboard[2][2] = "O"
    return
  corners = vboard[0][2] + vboard[2][0]
  if corners.strip() == "X":
    if corners.startswith(" "):
      vboard[0][2] = "O"
    else:
      vboard[2][0] = "O"
    return
  if vboard[0][2] == " ":
    vboard[0][2] = "O"
    return
  if vboard[2][0] == " ":
    vboard[2][0] = "O"
    return
  if vboard[0][0] == " ":
    vboard[0][0] = "O"
    return
  if vboard[2][2] == " ":
    vboard[2][2] = "O"
    return
  for row in vboard:
    for col in range(3):
      if row[col] == " ":
        row[col] ="O"
        return
def spacesleft(vboard):
  spacesleft = False
  for row in vboard:
    for col in row:
      if col == " ":
        spacesleft = True
  return spacesleft
temp = [" "," "," "]
board = [temp,list(temp),list(temp)]
bhumanone = False
bcomputerwon = False
bend = False
while not bend:
  display(board)
  bvalidinput = False
  while not bvalidinput:
    display(board)
    col = input("What column do you want to play?(1-3)")
    row = input("What row do you want to play?(1-3)")
    bvalidinput = True
    try:
      col = int(col)-1
      row = int(row)-1
      if row < 0 or row > 2:
        print ("The row must be 1-3!")
        bvalidinput = False
        time.sleep(0.5)
      if col < 0 or col > 2:
        print ("The column must be 1-3!")
        bvalidinput = False
        time.sleep(0.5)
      if bvalidinput and not board [row][col] == " ":
        print (" You can't play there!")
        bvalidinput = False
        time.sleep(0.5)
    except:
      bvalidinput = False
      print("That is not a number!")
      time.sleep(0.5)

    
  board [row][col] = "X"
  if someonewon(board):
    print ("You won!!!!")
    bhumanwon = True
    bend = True
  if not bend:
    display(board)
    makemove(board)
    time.sleep(0.5)
    if someonewon(board):
      print ("You lost.")
      bcomputerwon = True
      bend = True
  if not bend and not spacesleft(board):
    print ("Draw!")
    bend = True
display(board)
