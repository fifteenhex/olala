#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#include "sysheaders/uart.h"
#include "sysheaders/systemregisters.h"

static volatile uint32_t* extram = (uint32_t*) MEMORYMAP_EXTRAM_BASE;

static void putch(char ch){
	uint8_t status;
	do {
		status = uart_status;
	} while(status & UART_TXFULL);		
	uart_fifo = ch;	
}

static int getch_noblock(){
	if(!(uart_status & UART_RXEMPTY))
		return uart_fifo;
	else
		return -1;
}

static uint8_t getch(){
        while(uart_status & UART_RXEMPTY){
	}
	return uart_fifo;
}

static void println(char* string){
	while(*string != '\0'){
		putch(*string++);
	}
}

static void delay(void){
	for(int i = 0; i < 1024; i++){
		for(int j = 0; j < 1024; j++){
			asm volatile (
                        "nop\n\t"
                        :
                        :
                        : );
		}
	}
}


static int parsenibble(uint8_t nibble){
	if(nibble >= 0x30 && nibble <= 0x39)
	  return nibble - 0x30;
	else if(nibble >= 0x61 && nibble <= 0x66)
	  return nibble - (0x61 - 0xa);
	else if(nibble >= 0x41 && nibble <= 0x46)
	  return nibble - (0x41 - 0xa);
	else
	  return -1;
}

static int parsebyte(uint8_t msc, uint8_t lsc){
      return (parsenibble(msc) << 4) | parsenibble(lsc);
}

static void printnibble(uint8_t nibble){
	if(nibble <= 9)
		putch(nibble + 0x30);
	else
		putch((nibble - 0xa) + 0x61);
}

static void printbyte(uint8_t byte){
	printnibble((byte >> 4) & 0xf);
	printnibble(byte & 0xf);
}

static void printword(uint16_t word){
	printbyte((word >> 8) & 0xff);
	printbyte(word & 0xff);
}

static void printdoubleword(uint32_t doubleword){
	printword((doubleword >> 16) & 0xffff);
	printword(doubleword & 0xffff);
}

static void extramtest(void){
	unsigned onemegindoublewords = (1024 * 1024) / 4;
	bool pass = true;
	println("detecting ext ram\n");
	unsigned extramsz = 0;
	unsigned lastoffset = 0;
	for(int i = 1; i < 5; i *= 2){
		int offset = (i * onemegindoublewords) - 1;
		extram[offset] = 0xAAAA5555;
		
		// this should overwrite the value just written if the memory has started to mirror
		if(lastoffset != 0)	
			extram[lastoffset] = 0;
		
		if(extram[offset] == 0xAAAA5555){
			lastoffset = offset;
			extramsz++;
			break;
		}
	}

	switch(extramsz){
		case 1:
			println("1MB");
			break;
		case 2:
			println("2MB");
			break;
		case 4:
			println("4MB");
			break;
	}

	if(extramsz > 0){
		println(" ext ram detected\n");

		for(uint32_t i = 0; i < (onemegindoublewords * extramsz); i++){
			extram[i] = (~i & 0xffffffff);
		}

		for(uint32_t i = 0; i < (onemegindoublewords * extramsz); i++){
			if(extram[i] != (~i & 0xffffffff)){
				pass = false;
				println("e: ");
				printword(i);
				println(" g: ");
				printword(extram[i]);
				putch('\n');
				break;
			}
		}

		if(!pass){
			println("extram test failed\n");
			while(1){
				extram[0] = 0xffff;
				systemregisters_leds = ~systemregisters_leds;
				delay();
			}
		}
	}
	else
		println("no ext ram\n");
}

enum srecstate { START, COUNT, ADDRESS, DATA, CHECKSUM, DONE };
typedef enum srecstate srecstate_t;

static int rectypetoaddresslen(int rectype){
  switch(rectype){
    case 1:
    case 9:
      return 2;
    case 2:
    case 8:
      return 6;
    case 3:
    case 7:
      return 8;
    default:
      return 0;
  }
}

static void dosrecorddownload(){
  srecstate_t srecstate = START;
  int rectype;
  int count;
  uint32_t address;
  uint8_t datasum;
  bool failed = false;
  
  println("send srecords now\n");
	while(srecstate != DONE){
		//printnibble(srecstate);
		//putch('\n');
		switch(srecstate){
		  case START:{
		    uint8_t ch = getch();
		    if(ch == 'S'){
		      address = 0;
		      uint8_t type = getch();
		      rectype = parsenibble(type);
		      srecstate = COUNT;
		    }
		  }
		  break;
		  case COUNT:{
		    uint8_t msc = getch();
		    uint8_t lsc = getch();
		    count = parsebyte(msc, lsc);
		    datasum = count;
		    srecstate = ADDRESS;
		  }
		  break;
		  case ADDRESS:{
		      int addressrem = rectypetoaddresslen(rectype);
		      while(addressrem > 0){
			uint8_t addrnibblemsc = getch();
			uint8_t addrnibblelsc = getch();
			uint8_t addrbyte = parsebyte(addrnibblemsc, addrnibblelsc);
			address = (address << 8) | addrbyte;
			datasum += addrbyte;
			addressrem--;
		     }
		    srecstate = DATA;
		  }
		      break;
		  case DATA:{
		    volatile uint8_t* dest = (uint8_t*) address; 
		    while(count > (1 + rectypetoaddresslen(rectype))){
		      uint8_t datamsc = getch();
		      uint8_t datalsc = getch();
		      uint8_t databyte = parsebyte(datamsc, datalsc); 
		      if(rectype == 1 || rectype == 2 || rectype == 3)
			*dest++ = databyte;
		      datasum += databyte;
		      count--;
		    }
		     srecstate = CHECKSUM;
		  }
		    break;
		  case CHECKSUM:{
		    uint8_t checksummsc = getch();
		    uint8_t checksumlsc = getch();
		    uint8_t checksum = parsebyte(checksummsc, checksumlsc);
		    datasum = ~datasum;
		    //printbyte(checksum);
		    //printbyte(datasum);
		    if(checksum == datasum)
		      putch('.');
		    else {
		      failed = true;
		      putch('x');
		    }
		    
		    if(rectype == 7 || rectype == 8 || rectype == 9)
		      srecstate = DONE;
		    else
		      srecstate = START;
		    
		  }
		    break;
		}
	}
	
	putch('\n');
	if(failed)
	  println("Failed\n");
	else
	   println("Done\n");
}

int main(void) {
	systemregisters_dividerbit = 0;
	systemregisters_sysconfig |= SYSTEMREGISTERS_SYSCONFIG_DISABLEBOOTROM;
	uart_clockscaler1 = 1;
	uart_clockscaler2 = 19;

	println("OLALA bootrom\n");

	extramtest();

	while(1){
	  println("send ! to start upload\n");
	  while (1) {
		systemregisters_leds = (systemregisters_systick >> 9) & 0xff;
		int ch = getch_noblock();
		if(ch > 0){
		  switch(ch){
		  case '!':
		  dosrecorddownload();
		  break;
		}
	      }
	  }	
	}
	
	return 0;
}
