# (c) Copyright 2016 forkedbranch (http://forkedbranch.eu/)
# Licensed under the Apache License, Version 2.0

def write_evallog(file, evaluations):
    with open(file, "w") as f:
        f.write('{:<10s} {:>10s} {:>10s} {:>10s} {:>10s}\n'.format 
                        ('eval_no', 'yc', 'r', 'objective', 'failed'))
        
    with open(file, "a") as f:
        for e in evaluations:
            f.write('{:10d} {:10.6f} {:10.6f} {:10.6f} {:10d}\n'.format 
                        (e['evaluation_number'],
                         e['center'],
                         e['radius'],
                         e['objective'],
                         e['failed']))
