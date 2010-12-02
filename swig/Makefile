#
#  Makefile for Python/FOX wrappers. Assumes that SWIG and
#  Python are both available on the build system.
#

.SUFFIXES: .cpp .i .ii

# Name of swig executable
SWIG = swig

# SWIG settings here
#DEFINES = -D__WIN32__ -DWIN32
DEFINES =
CFLAGS = $(DEFINES) -c++ -dnone -python -shadow -keyword

# SWIG Interface Files
INTERFACES =	fox.i fxdefs.i fox3d.i controls.i windows.i structs.i \
		graphics.i mdi.i containers.i menus.i dialogs.i misc.i \
		table.i treelist.i dirlist.i iconlist.i text.i

# SWIG-generated wrapper files
WRAPPERS =	../src/mdi.cpp ../src/fox.cpp ../src/fox3d.cpp ../src/mdi.cpp\
		../src/controls.cpp ../src/menus.cpp ../src/dialogs.cpp\
		../src/windows.cpp ../src/containers.cpp ../src/misc.cpp\
		../src/graphics.cpp ../src/table.cpp ../src/treelist.cpp\
		../src/dirlist.cpp ../src/iconlist.cpp ../src/text.cpp

# SWIG-generated shadow class modules
MODULES =	../src/mdi.py ../src/fox.py ../src/fox3d.py ../src/mdi.py\
		../src/controls.py ../src/menus.py ../src/dialogs.py\
		../src/windows.py ../src/containers.py ../src/misc.py\
		../src/graphics.py ../src/table.py ../src/treelist.py\
		../src/dirlist.py ../src/iconlist.py ../src/text.py

# Make a SWIG interface file from its template
%.i: %.ii
	python prep.py $< > $@
	@python crlf.py $@

# Make a wrapper file from its interface file
%.cpp:
	$(SWIG) $(CFLAGS) -c -o $*.cpp $<
	@python crlf.py $*.cpp $*.py

# Make all wrappers & shadow class files
all: $(WRAPPERS)
	@cd ../src; python make_virtuals.py; python overloads.py; python ../swig/crlf.py *.py

include dependencies

# Common Dialogs (needs special rule for SWIG bug workaround)
../src/dialogs.cpp: dialogs.i
	$(SWIG) $(CFLAGS) -c -o $*.cpp $<
	@sed -e "s/FXchar \*\* _arg1/const FXchar \*\* _arg1/g" ../src/dialogs.cpp > junk
	@mv junk ../src/dialogs.cpp
	@python crlf.py $*.cpp $*.py

# Miscellaneous (same SWIG bug workaround)
../src/misc.cpp: misc.i
	$(SWIG) $(CFLAGS) -c -o $*.cpp $<
	@sed -e "s/FXchar \*\*/const FXchar \*\*/g" ../src/misc.cpp > junk
	@mv junk ../src/misc.cpp
	@python crlf.py $*.cpp $*.py

clean:
	@rm -rf $(WRAPPERS) $(MODULES) $(INTERFACES)
