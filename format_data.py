

def format_data_for_display(people) -> list:
    data = []
    for person in people:
        display_data =f"{person['given_name']} {person['family_name']}: {person['title']}"
        data.append(display_data)
        
    return data

def format_data_for_excel(people) -> str:
    final_format = "given,family,title"
    for person in people:
        final_format += f"\n{person['given_name']},{person['family_name']},{person['title']}"
    return final_format