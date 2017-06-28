MEMORY 
{
	rom (R)	: ORIGIN = 0xE00000,    LENGTH = 4K    /* ROM */
	ram	: ORIGIN = 0xF00000, 	LENGTH = 2K    /* RAM */
}

SECTIONS 
{
	. = 0;

	.startup : 
	{ 
		*(.text)
		. = ALIGN(2);
	} >rom

	.text :                                                          
    	{
 		*(.text*)                                                
		*(.rodata*)
		*(.eh_frame)
		. = ALIGN(4);
		_text_end = .;
	} >rom                                                      
	
	.data :     
	{
		_data_start = .;                                         
		*(.data*)                                              
		. = ALIGN(4);
		_data_end = .;                           
	} >ram AT >rom
	
	.bss :                                                         
	{
		_bss_start = .;
		*(.bss*)                                                
		. = ALIGN(4);                                           
		_bss_end = . ;                                          
		_end = .;                                                       
		end = .;
	} >ram                                                          	
}

