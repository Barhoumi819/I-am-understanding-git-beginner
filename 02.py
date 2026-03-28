def dompier_music(switches):
  position = 1
  lst = []
  sum1 = 0 

  real_lst = []
  for lists in switches:
    for binary in lists[::-1] :
      
      print(f"Positon : {position} Binary : {binary}")

      sum1 = (position*int(binary))
      position = position * 2
  lst.append(sum1)
  print(lst)


    #   for ls1 in real_lst :

    #     if sum(ls1) == 261 :
    #         real_lst.append("C4")

    #     if sum(ls1) == 294 :
    #         real_lst.append("D4")

    #     if sum(ls1) == 329 :
    #         real_lst.append("E4")

    #     if sum(ls1) == 349 :
    #         real_lst.append("F4")

    #     if sum(ls1) == 392 :
    #         real_lst.append("G4")

    #     if sum(ls1) == 440 :
    #         real_lst.append("A4")

    #     if sum(ls1) == 494 :
    #         real_lst.append("B4")

    #     if sum(ls1) == 523 :
    #         real_lst.append("C5")

    #     if sum(ls1) == 0 :
    #         real_lst.append("REST")

      


dompier_music(["0100000101", "0100000101", "0110001000"])

# this one too gg 