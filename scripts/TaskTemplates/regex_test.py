import re

msg = "HELLO I AM SNOW BOY"

def get_regex_test_list() -> dict:
    return {
        "HELLO I AM" : "test",
        "DERRRRR" : "test1"
    }

for i in [*get_regex_test_list().keys()]:
    retest = re.compile(r'\b('+i+r')\b')
    print(retest)
    if retest.search(msg):
        print(get_regex_test_list()[i])