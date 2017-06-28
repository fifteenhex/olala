.extern _bss_start
.extern _bss_end

.section .startup

.text

vectors:
	dc.l	0x100000	/* Initial stack pointer */
	dc.l	start		/* Start of program Code */
        dc.l    unhandledint	/* Bus error */
        dc.l    unhandledint	/* Address error */
        dc.l    unhandledint	/* Illegal instruction */
        dc.l    unhandledint	/* Division by zero */
        dc.l    unhandledint	/* CHK exception */
        dc.l    unhandledint	/* TRAPV exception */
        dc.l    unhandledint	/* Privilage violation */
        dc.l    unhandledint	/* TRACE exception */
        dc.l    unhandledint	/* Line-A emulator */
        dc.l    unhandledint	/* Line-F emulator */
        dc.l    unhandledint	/* Reserved (NOT USED) */
        dc.l    unhandledint	/* Co-processor protocol violation */
        dc.l    unhandledint                                                             /* Format error */
        dc.l    unhandledint                                                             /* Uninitialized Interrupt */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Reserved (NOT USED) */
        dc.l    unhandledint                                                             /* Spurious Interrupt */
        dc.l    unhandledint	/* IRQ Level 1 */
        dc.l    unhandledint	/* IRQ Level 2 */
        dc.l    unhandledint	/* IRQ Level 3 */
        dc.l    unhandledint	/* IRQ Level 4 */
        dc.l    unhandledint	/* IRQ Level 5 */
        dc.l    unhandledint	/* IRQ Level 6 */
        dc.l    unhandledint	/* IRQ Level 7 */
        dc.l    unhandledint                                                             /* TRAP #00 Exception */
        dc.l    unhandledint                                                             /* TRAP #01 Exception */
        dc.l    unhandledint                                                             /* TRAP #02 Exception */
        dc.l    unhandledint                                                             /* TRAP #03 Exception */
        dc.l    unhandledint                                                             /* TRAP #04 Exception */
        dc.l    unhandledint                                                             /* TRAP #05 Exception */
        dc.l    unhandledint                                                             /* TRAP #06 Exception */
        dc.l    unhandledint                                                             /* TRAP #07 Exception */
        dc.l    unhandledint                                                             /* TRAP #08 Exception */
        dc.l    unhandledint                                                             /* TRAP #09 Exception */
        dc.l    unhandledint                                                             /* TRAP #10 Exception */
        dc.l    unhandledint                                                             /* TRAP #11 Exception */
        dc.l    unhandledint                                                             /* TRAP #12 Exception */
        dc.l    unhandledint                                                             /* TRAP #13 Exception */
        dc.l    unhandledint                                                             /* TRAP #14 Exception */
        dc.l    unhandledint                                                             /* TRAP #15 Exception */
        dc.l    unhandledint                                                             /* (FP) Branch or Set on Unordered Condition */
        dc.l    unhandledint                                                             /* (FP) Inexact Result */
        dc.l    unhandledint                                                             /* (FP) Divide by Zero */
        dc.l    unhandledint                                                             /* (FP) Underflow */
        dc.l    unhandledint                                                             /* (FP) Operand Error */
        dc.l    unhandledint                                                             /* (FP) Overflow */
        dc.l    unhandledint                                                             /* (FP) Signaling NAN */
        dc.l    unhandledint	/* (FP) Unimplemented Data Type */
        dc.l    unhandledint	/* MMU Configuration Error */
        dc.l    unhandledint	/* MMU Illegal Operation Error */
        dc.l    unhandledint	/* MMU Access Violation Error */
        dc.l    unhandledint	/* Reserved (NOT USED) */
        dc.l    unhandledint	/* Reserved (NOT USED) */
        dc.l    unhandledint	/* Reserved (NOT USED) */
        dc.l    unhandledint	/* Reserved (NOT USED) */
        dc.l    unhandledint	/* Reserved (NOT USED) */

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

	jmp	main

unhandledint:
	jmp unhandledint
