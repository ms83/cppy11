"""
    Render README.md based on code samples in current directory
"""

import os
import sys
from slugify import slugify

def _slug(s):
    return slugify(unicode(s)).lower()

def _code(filename):
    try:
        return open(filename).read().strip()
    except IOError:
        return ''

def _title(s):
    return s.replace('-', ' ').title()

def _lctitle(s):
    return s.replace('-', ' ').title().lower()

# key - section
# val - topics
topics = {}

# Iterate over directories
for d in os.walk('.'):
    # ('./lambda', [], ['create-function.cpp', 'create-function.py'])
    # ('./queue', [], ['insert-to-queue.cpp', 'insert-to-queue.py'])
    for f in d[2]:
        topic_file = os.path.join(d[0], f)
        if topic_file.endswith(('.cpp', 'py')) and f != sys.argv[0]:
            dir_name = _title(''.join([ch for ch in d[0] if ch.isalnum() or ch == '-']))
            topic = f.split('.')[0]
            topics.setdefault(dir_name, set())
            topics[dir_name].add(topic)

print('''
# C++ for Python Programmers
''')

# Header
print(' &nbsp; '.join(['[{}](#{})'.format(section, _slug(section)) for section in sorted(topics)]))

# Sections
for section in sorted(topics):
    print('\n\n\n## {}'.format(section))
    for topic in sorted(topics[section]):
        print('\n[{}](#{})'.format(_lctitle(topic), _slug(topic)))

    for topic in topics[section]:
        print('\n### {}'.format(_lctitle(topic)))
        py_code = _code(os.path.join(_slug(section), topic) + '.py')
        cpp_code = _code(os.path.join(_slug(section), topic) + '.cpp')
        print('```python\n{}\n```'.format(py_code))
        print('```cpp\n{}\n```'.format(cpp_code))

    print('\n[&uarr;top](#c-for-python-programmers)')

