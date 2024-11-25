calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

print(string_info('BanNaNA'))

print(string_info('hArMOny'))

print(is_contains('Friday', ['mOnDAY', 'SuNdAy']))  # Urban ~ urBAN

print(is_contains('society', ['tEam', 'claSS', 'soCiEty']))  # No matches

print(string_info('PeAcH'))
print(calls)