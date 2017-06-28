.extern _bss_start
.extern _bss_end
.extern _text_end
.extern _data_start
.extern _data_end

.section .startup

.text

vectors:
	dc.l	0xF00000 + 2048						/* Initial stack pointer */
	dc.l	start							/* Start of program Code */

start:

clearbss:
	#clear bss
	lea.l	_bss_start,%a0	/* Clear bss */
	move.l	#_bss_end,%d0
1:	cmp.l	%d0,%a0
	beq.s	2f
	clr.b	(%a0)+
	bra.s	1b
2:

copydata:
	#copy data
	lea.l	_text_end,%a0	/* data is located after the text */
	lea.l	_data_start,%a1 /* the data's real start address */
	move.l	#_data_end,%d0  /* the data's real end address */
1:	cmp.l	%a1,%d0			/* copy data from where ever a0 points until a1 equals the end of the data */
	beq.s	2f
	move.b	(%a0)+,(%a1)+
	bra.s	1b
2:
	jmp	main
