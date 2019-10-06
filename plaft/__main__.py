# -*- coding: utf-8 -*-

import click
import os
import yaml
import pexpect
from pexpect.exceptions import EOF
from re import match

@click.command()        
@click.option( '-c','--config-file', type=click.File('rb'), default='tests.yaml',
            help='file configuration test')
@click.option('-a','--assignments', type=click.Path(),
            help='directory with students assignments files') 

def main(config_file,assignments):
    # Load assignments directories.
    assignment_dirs = [os.path.join(assignments, d) for d in os.listdir(assignments)]
    assignment_dirs = [dirs for dirs in assignment_dirs if os.path.isdir(dirs)]

    # Load assigments tests from configure file 
    assignment_tests = yaml.load(config_file.read(), Loader=yaml.FullLoader)

    # Run tests.
    for path in assignment_dirs:
        path_assignment = os.path.abspath(path)
        print(os.path.basename(path))
        for assignment_test in assignment_tests:
            run_check(assignment_test,path_assignment)

def run_check(assignment,path):
    print(f"\t {assignment['title']}: ", end='\t')
    for test in assignment['tests']:
        cmd = f'python3 {path}/{assignment["program"]}'
        child = pexpect.spawn(cmd,encoding="utf-8", timeout=5)
        for input_test in test['input']:
            child.sendline(str(input_test))
        child.expect(EOF)
        output = child.before.replace("\r\n", "\n")[:-1].split('\n')
        if match(test['output'], output[-1]):
            print('P', end = ' ')
        else:
            print('E', end = ' ')
    print('\n')

if __name__ == "__main__":
    main()