from playwright.sync_api import expect
class Bookingpage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/automation-practice-form")
    def personalinformation(self,first_name, last_name, email, mobile_number ):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.locator("#lastName").fill(last_name)
        self.page.locator("#userEmail").fill(email)
        self.page.locator("#userNumber").fill(mobile_number)
        self.page.wait_for_timeout(3000)
    def radio(self):
        radio_check_locator = self.page.get_by_role("radio", name="Male").first
        radio_check = radio_check_locator.check()
    def datepicker(self, year):
       self.page.locator("#dateOfBirthInput").click()
       year_select = self.page.locator(".react-datepicker__year-select")
       year_select.select_option(value = year)
       month_select= self.page.locator(".react-datepicker__month-select")
       month_select.select_option(value="1")
       date_select = self.page.locator(".react-datepicker__day--018").click()
    def citystate(self, state, city):
        self.page.locator("#state").click()
        self.page.wait_for_timeout(1000)
        self.page.locator(f"text={state}").click()
        self.page.locator("#city").click()
        self.page.locator(f"text={city}").click()
    def submit(self):
        self.page.get_by_role("button", name="Submit").click()
    def verify(self):
        expect(self.page.locator("#example-modal-sizes-title-lg")).to_be_visible()