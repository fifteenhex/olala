LINKERSCRIPT=bootrom.lds

CC=m68k-elf-gcc 
AS=m68k-elf-as
CP=m68k-elf-objcopy

AFLAGS=-ahls -m68000
CFLAGS=-m68000 -ggdb -std=gnu99 -Wall -Os -Wstrict-aliasing -flto
LFLAGS=-m68000 -T$(LINKERSCRIPT) -nostartfiles -Wl,-Map=prog.map,--cref -flto
