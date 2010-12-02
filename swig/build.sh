#!/bin/sh

python makedepend.py > dependencies
make
