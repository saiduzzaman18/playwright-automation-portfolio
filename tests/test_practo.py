import pytest
from pages.practo_page import practoPage
@pytest.mark.parametrize ("city, speciality", [
    ('kolkata', 'Dentist'),
    ('Delhi', 'Cardiology'),
    ('Bengaluru', 'Dermatology')])

def test_practo(page,speciality, city):
    practo = practoPage(page)
    practo.open()
    practo.search_doctor(city, speciality)
    practo.doctor_click()
    name = practo.doctor_profile()
    practo.verify_doctor_name(name)