states_in_india = ["Andra Pradesh", "Goa", "Bihar", "Rajstan","Karanataka", "Tamil nadu", "Gujurath", "Kashmir", "Odisa"]

for states in states_in_india:
    if "Karanataka" in states:
        print("Found Karanataka in states")
        break
    else:
        print("Karanataka not found in states")
        continue