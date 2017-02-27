import re
def fuzzyfinder(user_input,collection):
    suggestions = []
    pattern = '.*'.join(user_input) #convert djm to d.*j.*m
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append(item)

    return suggestions

def fuzzyfinder_v2(user_input,collection):
    suggestions = []
    pattern = '.*'.join(user_input) #convert djm to d.*j.*m
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()),match.start(),item))

    return [x for _,_,x in sorted(suggestions)]

def fuzzyfinder_v3(user_input,collection):
    suggestions = []
    pattern = '.*?'.join(user_input) #convert djm to d.*j.*m
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()),match.start(),item))

    return [x for _,_,x in sorted(suggestions)]

if __name__ == '__main__':
    collection = ['django_migrations.py',
                  'django_admin_log.py',
                  'main_generator.py',
                  'migrations.py',
                  'api_user.py',
                  'user_group.doc',
                  'accounts.txt']
    print fuzzyfinder_v2('djm',collection)
    print fuzzyfinder_v2('mig',collection)
    print fuzzyfinder_v2('user',collection)
