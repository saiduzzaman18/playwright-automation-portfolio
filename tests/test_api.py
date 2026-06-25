import pytest
from playwright.sync_api import sync_playwright
def test_api():
    with sync_playwright() as p:
        # Create API request context — no browser needed
        requests = p.request.new_context()
        # Make GET request — like opening a URL but for data
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        # Assert status code is 200 — success
        assert response.status==200
        print(" Passed: Status code is 200")
        print(response)
        # Read response as JSON
        users = response.json()
        #print(users)
        # Assert we got 10 users
        lenght = len(users)
        print(lenght)
        assert lenght ==10
        print("Success lenght = 10")
        # Print first user details
        first_user = users[0]
        #first_user_name = first_user['name']
        print(f"first user name is {first_user['name']}")
        print(f"First user email id is {first_user["email"]}")
        print(f"First user Phone {first_user['phone']}")
def test_get_single_user():
    with sync_playwright() as p:
        requests = p.request.new_context()
        response = response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        assert response.status==200
        print("Passed: Status code is 200 ")
        user = response.json()
        print(user)
        # Assert specific user details
        assert user['id']==1
        print("Passed: user id is correct")
        # name is present
        assert 'name' in user
        print("Passed: user is available")
        # @ available in email
        assert '@' in user['email']
        print(" Passed: Email is available ")
        print("User is found and name is ", user['name'])

        # create new user
def test_create_new_user():
            with sync_playwright() as p:
                requests = p.request.new_context()
                create_user ={
                    'name': "Szaman",
                    'email': "szman@gmail.com",
                    'phone': '9876655544'
                }
                response=requests.post("https://jsonplaceholder.typicode.com/users",
                                       data=create_user
                                       )

                created = response.json()
                print(f"User created and name is {created['name']}")

def test_user_not_found():
    with sync_playwright() as p:
        requests = p.request.new_context()
        response= requests.get("https://jsonplaceholder.typicode.com/users/998")
        assert response.status == 404
        print(" No User found and got 404 error")


