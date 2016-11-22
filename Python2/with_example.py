from __future__ import with_statement

with file('/etc/hosts') as hosts:
    for line in hosts:
        if line.startswith('#'):
            continue
        print line
