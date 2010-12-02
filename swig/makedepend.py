#! /usr/bin/env python

from glob import glob
from string import split
from os.path import splitext
import re

pat1 = re.compile('^%extern')
pat2 = re.compile('^%include')
pat3 = re.compile('^%import')

dependencies = {}

excluded_files = ['typemaps.i']

def print_dependencies():
    print '\n# DO NOT DELETE\n'
    keys = dependencies.keys()
    keys.sort()
    for key in keys:
	print key + ':',
	for dep in dependencies[key].keys():
	    print dep,
	print

def generate_dependencies(filename):
    if not dependencies.has_key(filename):
	dependencies[filename] = {}
    root, ext = splitext(filename)
    if ext == '.i':
	ii_filename = root + '.ii'
	dependencies[filename][ii_filename] = 1
	for line in open(ii_filename, 'r').readlines():
	    if pat1.match(line) or pat2.match(line) or pat3.match(line):
		words = split(line)
		if not words[1] in excluded_files:
		    dependencies[filename][words[1]] = 1

	cpp_filename = '../src/' + root + '.cpp'
	if not dependencies.has_key(cpp_filename):
	    dependencies[cpp_filename] = {}
	    dependencies[cpp_filename][filename] = 1
    else:
	raise NotImplementedError

if __name__ == '__main__':
    for file in glob('*.ii'):
	filename = file[:-1]
	generate_dependencies(filename)

    print_dependencies()
