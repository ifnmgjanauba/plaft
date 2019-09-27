# -*- coding: utf-8 -*-

import click
import os
import yaml

@click.command()        
@click.option( '-c','--config-file', type=click.File('rb'), default='tests.yaml',
            help='file configuration test')
@click.option('-a','--assignments', type=click.Path(),
            help='directory with students assignments files') 

def main(config_file,assignments):
    # Load assignments directories.
    assignment_dirs = [os.path.join(assignments, d)
                for d in os.listdir(assignments)]
    assignment_dirs = filter(os.path.isdir, assignment_dirs)

    # Load tests from configure file 
    tests = yaml.load(config_file.read())
    print(tests)

    # Run tests.
    for path in assignment_dirs:
        name = os.path.abspath(path)
        #print(name)      


if __name__ == "__main__":
    main()