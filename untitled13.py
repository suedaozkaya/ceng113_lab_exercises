text = input("Text: ")

width = int(input("Width: "))

height = int(input("Height: "))

border_character = input("Border character: ")

print(border_character*width + "\n" + 
      ("*" + " "*(width-2) + "*" +"\n")*((height-2)//2) +
      ("*" + " "*(width-2-len(text)//2) + text + " "*(width-2-len(text)-(width-2-len(text)//2)) +
      ("*" + " "*(width-2) + "*" +"\n")*(height-2-(height-2//2))) + 
      border_character*width)
