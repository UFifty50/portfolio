CC := arm-linux-gnueabi-gcc-10

SOURCES = $(wildcard out/*.s)
EXECS = $(SOURCES:%.s=%)
V2 = $(shell cp src/*.s out/)

all: one two three

one:
	cp src/*.s out/

two: $(EXECS)

three:
	rm -rf out/*.s

run:
	read -p "Enter File Name: " file; \
	qemu-arm out/$$file

clean:
	rm -f out/*

.PHONY: all one two three clean