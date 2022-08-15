

def format_data_for_display(people) -> list:
    data = []
    for person in people:
        display_data =f"{person['given_name']} {person['family_name']}: {person['title']}"
        data.append(display_data)
        
    return data

def format_data_for_excel(people) -> str:
    return "test"