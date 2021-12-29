from safepi.libs_root import *

import Person

def greet_times(n=10):
    for i in range(n):
        p=Person.Person()
        p.sayHi()

