from tkinter import HORIZONTAL


row_one = ["X", "X", "X"]
row_two = ["X", "X", "X"]
row_three = ["X", "X", "X"]


map = [row_one, row_two, row_three]
print(f"{row_one}\n{row_two}\n{row_three}")
tresure_location = input("Enter the two digits location: ")
horizontal = int(tresure_location[0])
vertical = int(tresure_location[1])

print(f"{horizontal}\n{vertical}")

selected_row = map[vertical - 1]
print(f"{selected_row}")
selected_row[horizontal - 1] = "Y"



print(f"{row_one}\n{row_two}\n{row_three}")


