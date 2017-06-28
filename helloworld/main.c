#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#include "sysheaders/uart.h"
#include "sysheaders/systemregisters.h"

static void putch(char ch){
	uint8_t status;
	do {
		status = uart_status;
	} while(status & UART_TXFULL);		
	uart_fifo = ch;	
}

static void println(char* string){
	while(*string != '\0'){
		putch(*string++);
	}
}

int main(void) {
	systemregisters_dividerbit = 0;
	systemregisters_sysconfig |= SYSTEMREGISTERS_SYSCONFIG_DISABLEBOOTROM;
	uart_clockscaler1 = 1;
	uart_clockscaler2 = 19;

	println("Hello, world!\n");
	while(1){}
	return 0;
}
