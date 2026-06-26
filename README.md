![Playwright Tests](https://github.com/saiduzzaman18/playwright-automation-portfolio/actions/workflows/playwright.yml/badge.svg)
# Playwright Automation Portfolio

Automation test suite built with Playwright + Python + pytest

## About Me
12 years manual testing experience. Building Playwright automation skills.

## Tech Stack
- Python 3.12
- Playwright
- pytest
- Page Object Model

## Project Structure
my_automation/
├── conftest.py
├── pages/
│   ├── flipkart_page.py
│   ├── booking_page.py
│   └── practo_page.py
└── tests/
    ├── test_search.py
    ├── test_booking.py
    ├── test_practo.py
    └── test_api.py

## What is Automated

### 1. Flipkart E-commerce
- Search for products
- Verify search results
- Click product and read name and price from new tab

### 2. DemoQA Booking Form
- Fill complete registration form
- Select dropdown for state and city
- Upload file
- Submit and verify success message

### 3. Practo Doctor Booking (Data Driven)
- Search doctors by city and speciality
- Parametrized with 3 cities: Kolkata, Delhi, Bengaluru
- Verify doctor profile page and name

### 4. API Testing
- GET all users and verify count
- GET single user and verify fields
- POST create new user and verify response
- Negative test: verify 404 for missing user

## How to Run

Install dependencies:
pip install playwright pytest-playwright pytest-html
playwright install

Run all tests:
pytest tests/ -v -s

Run specific test:
pytest tests/test_practo.py -v -s

Generate HTML report:
pytest tests/ -v -s --html=report.html