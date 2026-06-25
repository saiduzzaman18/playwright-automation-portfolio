
from pages.booking_page import Bookingpage
def test_form(page):
    booking = Bookingpage(page)
    booking.open()
    booking.personalinformation(
        "szafdg",
        "gdrf",
        "tegfht@gmail.com",
        "9845684567")
    booking.radio()
    booking.citystate("NCR", "Delhi")
    booking.submit()
    booking.verify()