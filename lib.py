from activesoup import driver

def getPage():
    d = driver.Driver()
    login_page = d.get('https://paws.tcnj.edu/psp/paws/?cmd=login')
    login_form = login_page.form

    print(login_page)
    print(login_form)

    member_portal = login_form.submit({'username': 'username',
                    'password': 'password'})

    if member_portal.response.status_code not in range(200, 300):
        raise RuntimeError("Couldn't log in")

getPage()
