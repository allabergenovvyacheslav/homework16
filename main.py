calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    a = (len(string), string.upper(), string.lower())
    count_calls()
    return a
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [x.upper() for x in list_to_search]
    if string.upper() in list_to_search:
        return (True)
    else:
        return (False)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
