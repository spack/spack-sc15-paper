#!/usr/bin/env spack-python
import time
import numpy as np
import spack
from external import yaml
from spack.spec import Spec

# prime the timer
s = Spec('qt')
s.concretize()

reps = 10
timings = []

for name in spack.db.all_package_names():
    print name
    specs = [Spec(s) for s in [name] * reps]
    times = []

    for s in specs:
        start = time.clock()
        s.concretize()
        end = time.clock()
        times.append(end - start)

    record = (name, len([s for s in s.traverse()]), times)
    print record
    timings.append(record)


with open('timings.yaml', 'w') as stream:
    yaml.dump(stream)
