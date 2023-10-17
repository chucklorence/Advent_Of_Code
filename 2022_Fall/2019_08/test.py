line=open("puzzel_input.txt").readline().strip()

layers=[[line[j+i:j+i+25] for i in range(0, 25*6, 25)] for j in range(0,len(line),25*6)]

allPixels=[[[layers[layer][row][col] for layer in range(len(layers)) if layers[layer][row][col]!='2'] for col in range(25)] for row in range(6)]

correctPixels=[[''.join(pixel[0]).replace('0','.').replace('1',' ') for pixel in row] for row in allPixels]

for i in range(6): print("".join(correctPixels[i]))