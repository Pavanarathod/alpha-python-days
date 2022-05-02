def format_name(f_name: str, l_name: str):
    """
    Take a first and last and format it 
    to return the title case version of the name
    """
    if f_name == "" or l_name == "":
        return
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"