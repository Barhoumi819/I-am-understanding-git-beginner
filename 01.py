def find_missing_colors(grid):
  Color = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  missing = []

  for box in grid :
    print(f"box is {box}")
    for color in box :
        print(f"color is {color}")
        if Color not in color :
           missing.append(color)
    print(missing)


(find_missing_colors( [["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
  ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
  ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
  ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
  ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
  ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
  ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]))




# Failed 