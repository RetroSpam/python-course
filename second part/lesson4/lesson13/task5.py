def authenticate(func):
    def wrapper(username, password):
        if username == 'Roman' and password == 'correctpassword':
            return func()
        else:
            return "Access denied!"
    return wrapper

@authenticate
def access_client_data():
    return "Access granted. Data: ..."


print(access_client_data('Roman', 'correctpassword'))
print(access_client_data('Oleg', 'wrongpassword'))