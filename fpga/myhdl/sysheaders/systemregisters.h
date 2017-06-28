#include "memorymap.h"
#define systemregisters_leds *(volatile uint8_t*)(MEMORYMAP_SYSTEMREGISTERS_BASE + 0)
#define systemregisters_dividerbit *(volatile uint8_t*)(MEMORYMAP_SYSTEMREGISTERS_BASE + 2)
#define systemregisters_sysconfig *(volatile uint16_t*)(MEMORYMAP_SYSTEMREGISTERS_BASE + 4)
#define systemregisters_systick *(volatile uint32_t*)(MEMORYMAP_SYSTEMREGISTERS_BASE + 8)
#define systemregisters_systickinterval *(volatile uint16_t*)(MEMORYMAP_SYSTEMREGISTERS_BASE + 12)
#define SYSTEMREGISTERS_SYSCONFIG_DISABLEBOOTROM (1 << 0)
