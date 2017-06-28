#include "memorymap.h"
#define uart_fifo *(volatile uint8_t*)(MEMORYMAP_UART_BASE + 0)
#define uart_clockscaler1 *(volatile uint8_t*)(MEMORYMAP_UART_BASE + 2)
#define uart_clockscaler2 *(volatile uint8_t*)(MEMORYMAP_UART_BASE + 4)
#define uart_status *(volatile uint8_t*)(MEMORYMAP_UART_BASE + 6)
#define uart_config *(volatile uint8_t*)(MEMORYMAP_UART_BASE + 8)
#define uart_fill *(volatile uint8_t*)(MEMORYMAP_UART_BASE + 10)
#define UART_TXEMPTY    1
#define UART_TXFULL     (1 << 1)
#define UART_RXEMPTY    (1 << 2)
#define UART_RXFULL     (1 << 3)
