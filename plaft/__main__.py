# -*- coding: utf-8 -*-

import click
import os
import yaml
import pexpect
from pexpect.exceptions import EOF

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

    # Load assigments tests from configure file 
    assignment_tests = yaml.load(config_file.read())

    # Run tests.
    for path in assignment_dirs:
        path_assignment = os.path.abspath(path)
        for assignment_test in assignment_tests:
            run_check(assignment_test,path_assignment)

def run_check(assignment,path):
    for test in assignment['tests']:
        cmd = f'python3 {path}/{assignment["program"]}'
        child = pexpect.spawn(cmd,encoding="utf-8", timeout=5)
        for input_test in test['input']:
            child.sendline(str(input_test))
        child.expect(EOF)
        output = child.before.replace("\r\n", "\n")[:-1].split('\n')
        print(output)

if __name__ == "__main__":
    main()