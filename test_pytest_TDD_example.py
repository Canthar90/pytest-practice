
import pytest

from format_data import format_data_for_display, format_data_for_excel


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruzi",
            "title": "Senior Software Engeener",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
        
    ]



def test_format_data_for_display(example_people_data):
    
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruzi: Senior Software Engeener",
        "Sayid Khan: Project Manager",
    ]
    
    
def test_format_daa_for_excel(example_people_data):
    
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruzi,Senior Software Engeener
Sayid,Khan,Project Manager"""