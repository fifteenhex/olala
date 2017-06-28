MEMORY 
{
	ram	: ORIGIN = 0x0, 	LENGTH = 1M    /* RAM */
}

SECTIONS 
{
	. = 0;

	.startup : 
	{ 
		*(.text)
		. = ALIGN(2);
	} >ram

	.text :                                                          
    	{
 		*(.text*)                                                
		*(.rodata*)
		*(.eh_frame)
		. = ALIGN(4);
		_text_end = .;
	} >ram                 
	
	.data :     
	{
		_data_start = .;                                         
		*(.data*)                                              
		. = ALIGN(4);
		_data_end = .;                           
	} >ram
	
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
