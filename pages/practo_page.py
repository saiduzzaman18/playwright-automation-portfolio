import re

from playwright.sync_api import sync_playwright, expect
class practoPage:
    def __init__(self, page):
        self.page = page
    def open(self):
        self.page.goto("https://www.practo.com/")
        self.page.wait_for_load_state("networkidle")
    def search_doctor(self, city, speciality):
        search_city_locator = self.page.get_by_placeholder("Search location")
        search_city_locator.fill(city)
        self.page.locator(".c-omni-suggestion-item__content__sub_text").first.click()
        search_speciality_locator= self.page.get_by_placeholder("Search doctors, clinics, hospitals, etc")
        search_speciality_locator.fill(speciality)
        self.page.locator(".c-omni-suggestion-item__content__title").first.click()
        expect(self.page).to_have_url(re.compile(speciality, re.IGNORECASE))


    def doctor_click(self):
         self.page.get_by_text(re.compile("Dr.")).first.click()
         self.page.wait_for_timeout(5000)

    def doctor_profile(self):
        all_pages = self.page.context.pages
        doctor_page= all_pages[-1]
        print("Last page", doctor_page)
        name = doctor_page.get_by_text(re.compile("Dr.")).first.inner_text()
        return name
    def verify_doctor_name(self,name):
        assert "Dr" in name, f"Expected Dr in name but got: {name}"
        print("PASSED - Doctor name verified:", name)
