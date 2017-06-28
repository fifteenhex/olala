include common.mk

all: prog.srec

prog.srec: prog.elf
	$(CP) -S -O srec prog.elf prog.srec
	
prog.elf: crt.o main.o $(LINKERSCRIPT)
	$(CC) $(LFLAGS) -o prog.elf crt.o main.o

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

crt.o: crt.s
	$(AS) $(AFLAGS) crt.s -o crt.o > crt.lst

clean:
	rm -f *.o
	rm -f *.bin
	rm -f *.srec
	rm -f *.map
	rm -f *.elf
	rm -f *.lst
