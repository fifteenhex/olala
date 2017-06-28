/**********************************************************************/
/*   ____  ____                                                       */
/*  /   /\/   /                                                       */
/* /___/  \  /                                                        */
/* \   \   \/                                                       */
/*  \   \        Copyright (c) 2003-2009 Xilinx, Inc.                */
/*  /   /          All Right Reserved.                                 */
/* /---/   /\                                                         */
/* \   \  /  \                                                      */
/*  \___\/\___\                                                    */
/***********************************************************************/

/* This file is designed for use with ISim build 0xfbc00daa */

#define XSI_HIDE_SYMBOL_SPEC true
#include "xsi.h"
#include <memory.h>
#ifdef __GNUC__
#include <stdlib.h>
#else
#include <malloc.h>
#define alloca _alloca
#endif
static const char *ng0 = "Function stdl ended without a return statement";
extern char *IEEE_P_1242562249;
static const char *ng2 = "Function to_integer ended without a return statement";

char *ieee_p_1242562249_sub_2045698577_1035706684(char *, char *, char *, char *, int );
unsigned char ieee_p_1242562249_sub_3125432260_1035706684(char *, char *, char *, int );
char *ieee_p_1242562249_sub_3481121704_1035706684(char *, char *, char *, char *);
unsigned char ieee_p_1242562249_sub_3823179160_1035706684(char *, char *, char *, int );


unsigned char work_p_1869287427_sub_3605173140_1322656296(char *t1, unsigned char t2)
{
    char t4[8];
    unsigned char t0;
    char *t5;

LAB0:    t5 = (t4 + 4U);
    *((unsigned char *)t5) = t2;
    if (t2 != 0)
        goto LAB2;

LAB4:    t0 = (unsigned char)2;

LAB1:    return t0;
LAB2:    t0 = (unsigned char)3;
    goto LAB1;

LAB3:    xsi_error(ng0);
    t0 = 0;
    goto LAB1;

LAB5:    goto LAB3;

LAB6:    goto LAB3;

}

unsigned char work_p_1869287427_sub_3411271061_1322656296(char *t1, int t2)
{
    char t4[8];
    unsigned char t0;
    char *t5;
    unsigned char t6;

LAB0:    t5 = (t4 + 4U);
    *((int *)t5) = t2;
    t6 = (t2 != 0);
    if (t6 != 0)
        goto LAB2;

LAB4:    t0 = (unsigned char)2;

LAB1:    return t0;
LAB2:    t0 = (unsigned char)3;
    goto LAB1;

LAB3:    xsi_error(ng0);
    t0 = 0;
    goto LAB1;

LAB5:    goto LAB3;

LAB6:    goto LAB3;

}

char *work_p_1869287427_sub_4134552588_1322656296(char *t1, char *t2, unsigned char t3, int t4)
{
    char t5[72];
    char t6[16];
    char t15[16];
    char *t0;
    int t7;
    int t8;
    unsigned int t9;
    char *t10;
    char *t11;
    int t12;
    int t13;
    unsigned int t14;
    int t16;
    char *t17;
    char *t18;
    int t19;
    unsigned int t20;
    char *t21;
    char *t22;
    char *t23;
    char *t24;
    char *t25;
    char *t26;
    char *t27;
    char *t28;
    char *t29;
    char *t30;
    int t31;
    char *t32;
    int t33;
    int t34;
    unsigned int t35;
    unsigned int t36;
    char *t37;

LAB0:    t7 = (t4 - 1);
    t8 = (0 - t7);
    t9 = (t8 * -1);
    t9 = (t9 + 1);
    t9 = (t9 * 1U);
    t10 = xsi_get_transient_memory(t9);
    memset(t10, 0, t9);
    t11 = t10;
    memset(t11, (unsigned char)2, t9);
    t12 = (t4 - 1);
    t13 = (0 - t12);
    t14 = (t13 * -1);
    t14 = (t14 + 1);
    t14 = (t14 * 1U);
    t16 = (t4 - 1);
    t17 = (t15 + 0U);
    t18 = (t17 + 0U);
    *((int *)t18) = t16;
    t18 = (t17 + 4U);
    *((int *)t18) = 0;
    t18 = (t17 + 8U);
    *((int *)t18) = -1;
    t19 = (0 - t16);
    t20 = (t19 * -1);
    t20 = (t20 + 1);
    t18 = (t17 + 12U);
    *((unsigned int *)t18) = t20;
    t18 = (t5 + 4U);
    t21 = ((IEEE_P_1242562249) + 1704);
    t22 = (t18 + 52U);
    *((char **)t22) = t21;
    t23 = (char *)alloca(t14);
    t24 = (t18 + 36U);
    *((char **)t24) = t23;
    memcpy(t23, t10, t14);
    t25 = (t18 + 40U);
    *((char **)t25) = t15;
    t26 = (t18 + 48U);
    *((unsigned int *)t26) = t14;
    t27 = (t6 + 4U);
    *((unsigned char *)t27) = t3;
    t28 = (t6 + 5U);
    *((int *)t28) = t4;
    if (t3 != 0)
        goto LAB2;

LAB4:
LAB3:    t10 = (t18 + 36U);
    t11 = *((char **)t10);
    t10 = (t15 + 12U);
    t9 = *((unsigned int *)t10);
    t9 = (t9 * 1U);
    t0 = xsi_get_transient_memory(t9);
    memcpy(t0, t11, t9);
    t17 = (t15 + 0U);
    t7 = *((int *)t17);
    t21 = (t15 + 4U);
    t8 = *((int *)t21);
    t22 = (t15 + 8U);
    t12 = *((int *)t22);
    t24 = (t2 + 0U);
    t25 = (t24 + 0U);
    *((int *)t25) = t7;
    t25 = (t24 + 4U);
    *((int *)t25) = t8;
    t25 = (t24 + 8U);
    *((int *)t25) = t12;
    t13 = (t8 - t7);
    t14 = (t13 * t12);
    t14 = (t14 + 1);
    t25 = (t24 + 12U);
    *((unsigned int *)t25) = t14;

LAB1:    return t0;
LAB2:    t29 = (t18 + 36U);
    t30 = *((char **)t29);
    t29 = (t15 + 0U);
    t31 = *((int *)t29);
    t32 = (t15 + 8U);
    t33 = *((int *)t32);
    t34 = (0 - t31);
    t20 = (t34 * t33);
    t35 = (1U * t20);
    t36 = (0 + t35);
    t37 = (t30 + t36);
    *((unsigned char *)t37) = (unsigned char)3;
    goto LAB3;

LAB5:;
}

char *work_p_1869287427_sub_2713497013_1322656296(char *t1, char *t2, unsigned char t3, int t4)
{
    char t5[72];
    char t6[16];
    char t15[16];
    char *t0;
    int t7;
    int t8;
    unsigned int t9;
    char *t10;
    char *t11;
    int t12;
    int t13;
    unsigned int t14;
    int t16;
    char *t17;
    char *t18;
    int t19;
    unsigned int t20;
    char *t21;
    char *t22;
    char *t23;
    char *t24;
    char *t25;
    char *t26;
    char *t27;
    char *t28;
    char *t29;
    char *t30;
    int t31;
    char *t32;
    int t33;
    int t34;
    unsigned int t35;
    unsigned int t36;
    char *t37;

LAB0:    t7 = (t4 - 1);
    t8 = (0 - t7);
    t9 = (t8 * -1);
    t9 = (t9 + 1);
    t9 = (t9 * 1U);
    t10 = xsi_get_transient_memory(t9);
    memset(t10, 0, t9);
    t11 = t10;
    memset(t11, (unsigned char)2, t9);
    t12 = (t4 - 1);
    t13 = (0 - t12);
    t14 = (t13 * -1);
    t14 = (t14 + 1);
    t14 = (t14 * 1U);
    t16 = (t4 - 1);
    t17 = (t15 + 0U);
    t18 = (t17 + 0U);
    *((int *)t18) = t16;
    t18 = (t17 + 4U);
    *((int *)t18) = 0;
    t18 = (t17 + 8U);
    *((int *)t18) = -1;
    t19 = (0 - t16);
    t20 = (t19 * -1);
    t20 = (t20 + 1);
    t18 = (t17 + 12U);
    *((unsigned int *)t18) = t20;
    t18 = (t5 + 4U);
    t21 = ((IEEE_P_1242562249) + 1764);
    t22 = (t18 + 52U);
    *((char **)t22) = t21;
    t23 = (char *)alloca(t14);
    t24 = (t18 + 36U);
    *((char **)t24) = t23;
    memcpy(t23, t10, t14);
    t25 = (t18 + 40U);
    *((char **)t25) = t15;
    t26 = (t18 + 48U);
    *((unsigned int *)t26) = t14;
    t27 = (t6 + 4U);
    *((unsigned char *)t27) = t3;
    t28 = (t6 + 5U);
    *((int *)t28) = t4;
    if (t3 != 0)
        goto LAB2;

LAB4:
LAB3:    t10 = (t18 + 36U);
    t11 = *((char **)t10);
    t10 = (t15 + 12U);
    t9 = *((unsigned int *)t10);
    t9 = (t9 * 1U);
    t0 = xsi_get_transient_memory(t9);
    memcpy(t0, t11, t9);
    t17 = (t15 + 0U);
    t7 = *((int *)t17);
    t21 = (t15 + 4U);
    t8 = *((int *)t21);
    t22 = (t15 + 8U);
    t12 = *((int *)t22);
    t24 = (t2 + 0U);
    t25 = (t24 + 0U);
    *((int *)t25) = t7;
    t25 = (t24 + 4U);
    *((int *)t25) = t8;
    t25 = (t24 + 8U);
    *((int *)t25) = t12;
    t13 = (t8 - t7);
    t14 = (t13 * t12);
    t14 = (t14 + 1);
    t25 = (t24 + 12U);
    *((unsigned int *)t25) = t14;

LAB1:    return t0;
LAB2:    t29 = (t18 + 36U);
    t30 = *((char **)t29);
    t29 = (t15 + 0U);
    t31 = *((int *)t29);
    t32 = (t15 + 8U);
    t33 = *((int *)t32);
    t34 = (0 - t31);
    t20 = (t34 * t33);
    t35 = (1U * t20);
    t36 = (0 + t35);
    t37 = (t30 + t36);
    *((unsigned char *)t37) = (unsigned char)3;
    goto LAB3;

LAB5:;
}

int work_p_1869287427_sub_2465831651_1322656296(char *t1, unsigned char t2)
{
    char t4[8];
    int t0;
    char *t5;

LAB0:    t5 = (t4 + 4U);
    *((unsigned char *)t5) = t2;
    if (t2 != 0)
        goto LAB2;

LAB4:    t0 = 0;

LAB1:    return t0;
LAB2:    t0 = 1;
    goto LAB1;

LAB3:    xsi_error(ng2);
    t0 = 0;
    goto LAB1;

LAB5:    goto LAB3;

LAB6:    goto LAB3;

}

int work_p_1869287427_sub_2365366537_1322656296(char *t1, unsigned char t2)
{
    char t4[8];
    int t0;
    char *t5;
    unsigned char t6;

LAB0:    t5 = (t4 + 4U);
    *((unsigned char *)t5) = t2;
    t6 = (t2 == (unsigned char)3);
    if (t6 != 0)
        goto LAB2;

LAB4:    t0 = 0;

LAB1:    return t0;
LAB2:    t0 = 1;
    goto LAB1;

LAB3:    xsi_error(ng2);
    t0 = 0;
    goto LAB1;

LAB5:    goto LAB3;

LAB6:    goto LAB3;

}

char *work_p_1869287427_sub_4249709490_1322656296(char *t1, char *t2, unsigned char t3, int t4)
{
    char t5[72];
    char t6[16];
    char t15[16];
    char *t0;
    int t7;
    int t8;
    unsigned int t9;
    char *t10;
    char *t11;
    int t12;
    int t13;
    unsigned int t14;
    int t16;
    char *t17;
    char *t18;
    int t19;
    unsigned int t20;
    char *t21;
    char *t22;
    char *t23;
    char *t24;
    char *t25;
    char *t26;
    char *t27;
    char *t28;
    char *t29;
    char *t30;
    int t31;
    char *t32;
    int t33;
    int t34;
    unsigned int t35;
    unsigned int t36;
    char *t37;

LAB0:    t7 = (t4 - 1);
    t8 = (0 - t7);
    t9 = (t8 * -1);
    t9 = (t9 + 1);
    t9 = (t9 * 1U);
    t10 = xsi_get_transient_memory(t9);
    memset(t10, 0, t9);
    t11 = t10;
    memset(t11, (unsigned char)2, t9);
    t12 = (t4 - 1);
    t13 = (0 - t12);
    t14 = (t13 * -1);
    t14 = (t14 + 1);
    t14 = (t14 * 1U);
    t16 = (t4 - 1);
    t17 = (t15 + 0U);
    t18 = (t17 + 0U);
    *((int *)t18) = t16;
    t18 = (t17 + 4U);
    *((int *)t18) = 0;
    t18 = (t17 + 8U);
    *((int *)t18) = -1;
    t19 = (0 - t16);
    t20 = (t19 * -1);
    t20 = (t20 + 1);
    t18 = (t17 + 12U);
    *((unsigned int *)t18) = t20;
    t18 = (t5 + 4U);
    t21 = ((IEEE_P_1242562249) + 1704);
    t22 = (t18 + 52U);
    *((char **)t22) = t21;
    t23 = (char *)alloca(t14);
    t24 = (t18 + 36U);
    *((char **)t24) = t23;
    memcpy(t23, t10, t14);
    t25 = (t18 + 40U);
    *((char **)t25) = t15;
    t26 = (t18 + 48U);
    *((unsigned int *)t26) = t14;
    t27 = (t6 + 4U);
    *((unsigned char *)t27) = t3;
    t28 = (t6 + 5U);
    *((int *)t28) = t4;
    t29 = (t18 + 36U);
    t30 = *((char **)t29);
    t29 = (t15 + 0U);
    t31 = *((int *)t29);
    t32 = (t15 + 8U);
    t33 = *((int *)t32);
    t34 = (0 - t31);
    t20 = (t34 * t33);
    t35 = (1U * t20);
    t36 = (0 + t35);
    t37 = (t30 + t36);
    *((unsigned char *)t37) = t3;
    t10 = (t18 + 36U);
    t11 = *((char **)t10);
    t10 = (t15 + 12U);
    t9 = *((unsigned int *)t10);
    t9 = (t9 * 1U);
    t0 = xsi_get_transient_memory(t9);
    memcpy(t0, t11, t9);
    t17 = (t15 + 0U);
    t7 = *((int *)t17);
    t21 = (t15 + 4U);
    t8 = *((int *)t21);
    t22 = (t15 + 8U);
    t12 = *((int *)t22);
    t24 = (t2 + 0U);
    t25 = (t24 + 0U);
    *((int *)t25) = t7;
    t25 = (t24 + 4U);
    *((int *)t25) = t8;
    t25 = (t24 + 8U);
    *((int *)t25) = t12;
    t13 = (t8 - t7);
    t14 = (t13 * t12);
    t14 = (t14 + 1);
    t25 = (t24 + 12U);
    *((unsigned int *)t25) = t14;

LAB1:    return t0;
LAB2:;
}

char *work_p_1869287427_sub_2828653915_1322656296(char *t1, char *t2, unsigned char t3, int t4)
{
    char t5[72];
    char t6[16];
    char t15[16];
    char *t0;
    int t7;
    int t8;
    unsigned int t9;
    char *t10;
    char *t11;
    int t12;
    int t13;
    unsigned int t14;
    int t16;
    char *t17;
    char *t18;
    int t19;
    unsigned int t20;
    char *t21;
    char *t22;
    char *t23;
    char *t24;
    char *t25;
    char *t26;
    char *t27;
    char *t28;
    char *t29;
    char *t30;
    int t31;
    char *t32;
    int t33;
    int t34;
    unsigned int t35;
    unsigned int t36;
    char *t37;

LAB0:    t7 = (t4 - 1);
    t8 = (0 - t7);
    t9 = (t8 * -1);
    t9 = (t9 + 1);
    t9 = (t9 * 1U);
    t10 = xsi_get_transient_memory(t9);
    memset(t10, 0, t9);
    t11 = t10;
    memset(t11, (unsigned char)2, t9);
    t12 = (t4 - 1);
    t13 = (0 - t12);
    t14 = (t13 * -1);
    t14 = (t14 + 1);
    t14 = (t14 * 1U);
    t16 = (t4 - 1);
    t17 = (t15 + 0U);
    t18 = (t17 + 0U);
    *((int *)t18) = t16;
    t18 = (t17 + 4U);
    *((int *)t18) = 0;
    t18 = (t17 + 8U);
    *((int *)t18) = -1;
    t19 = (0 - t16);
    t20 = (t19 * -1);
    t20 = (t20 + 1);
    t18 = (t17 + 12U);
    *((unsigned int *)t18) = t20;
    t18 = (t5 + 4U);
    t21 = ((IEEE_P_1242562249) + 1764);
    t22 = (t18 + 52U);
    *((char **)t22) = t21;
    t23 = (char *)alloca(t14);
    t24 = (t18 + 36U);
    *((char **)t24) = t23;
    memcpy(t23, t10, t14);
    t25 = (t18 + 40U);
    *((char **)t25) = t15;
    t26 = (t18 + 48U);
    *((unsigned int *)t26) = t14;
    t27 = (t6 + 4U);
    *((unsigned char *)t27) = t3;
    t28 = (t6 + 5U);
    *((int *)t28) = t4;
    t29 = (t18 + 36U);
    t30 = *((char **)t29);
    t29 = (t15 + 0U);
    t31 = *((int *)t29);
    t32 = (t15 + 8U);
    t33 = *((int *)t32);
    t34 = (0 - t31);
    t20 = (t34 * t33);
    t35 = (1U * t20);
    t36 = (0 + t35);
    t37 = (t30 + t36);
    *((unsigned char *)t37) = t3;
    t10 = (t18 + 36U);
    t11 = *((char **)t10);
    t10 = (t15 + 12U);
    t9 = *((unsigned int *)t10);
    t9 = (t9 * 1U);
    t0 = xsi_get_transient_memory(t9);
    memcpy(t0, t11, t9);
    t17 = (t15 + 0U);
    t7 = *((int *)t17);
    t21 = (t15 + 4U);
    t8 = *((int *)t21);
    t22 = (t15 + 8U);
    t12 = *((int *)t22);
    t24 = (t2 + 0U);
    t25 = (t24 + 0U);
    *((int *)t25) = t7;
    t25 = (t24 + 4U);
    *((int *)t25) = t8;
    t25 = (t24 + 8U);
    *((int *)t25) = t12;
    t13 = (t8 - t7);
    t14 = (t13 * t12);
    t14 = (t14 + 1);
    t25 = (t24 + 12U);
    *((unsigned int *)t25) = t14;

LAB1:    return t0;
LAB2:;
}

unsigned char work_p_1869287427_sub_1404342903_1322656296(char *t1, unsigned char t2)
{
    char t4[8];
    unsigned char t0;
    char *t5;
    unsigned char t6;

LAB0:    t5 = (t4 + 4U);
    *((unsigned char *)t5) = t2;
    t6 = (t2 == (unsigned char)3);
    t0 = t6;

LAB1:    return t0;
LAB2:;
}

unsigned char work_p_1869287427_sub_1403861144_1322656296(char *t1, char *t2, char *t3)
{
    char t5[16];
    unsigned char t0;
    char *t6;
    unsigned char t7;
    char *t8;
    unsigned char t9;

LAB0:    t6 = (t5 + 4U);
    t7 = (t2 != 0);
    if (t7 == 1)
        goto LAB3;

LAB2:    t8 = (t5 + 8U);
    *((char **)t8) = t3;
    t9 = ieee_p_1242562249_sub_3125432260_1035706684(IEEE_P_1242562249, t2, t3, 0);
    t0 = t9;

LAB1:    return t0;
LAB3:    *((char **)t6) = t2;
    goto LAB2;

LAB4:;
}

unsigned char work_p_1869287427_sub_1335278590_1322656296(char *t1, char *t2, char *t3)
{
    char t5[16];
    unsigned char t0;
    char *t6;
    unsigned char t7;
    char *t8;
    unsigned char t9;

LAB0:    t6 = (t5 + 4U);
    t7 = (t2 != 0);
    if (t7 == 1)
        goto LAB3;

LAB2:    t8 = (t5 + 8U);
    *((char **)t8) = t3;
    t9 = ieee_p_1242562249_sub_3823179160_1035706684(IEEE_P_1242562249, t2, t3, 0);
    t0 = t9;

LAB1:    return t0;
LAB3:    *((char **)t6) = t2;
    goto LAB2;

LAB4:;
}

unsigned char work_p_1869287427_sub_1310905938_1322656296(char *t1, int t2)
{
    char t4[8];
    unsigned char t0;
    char *t5;
    unsigned char t6;

LAB0:    t5 = (t4 + 4U);
    *((int *)t5) = t2;
    t6 = (t2 != 0);
    t0 = t6;

LAB1:    return t0;
LAB2:;
}

char *work_p_1869287427_sub_2785686743_1322656296(char *t1, char *t2, char *t3, char *t4)
{
    char t6[16];
    char t10[16];
    char t11[16];
    char *t0;
    char *t7;
    unsigned char t8;
    char *t9;
    char *t12;
    unsigned int t13;
    int t14;
    char *t15;
    char *t16;
    char *t17;
    unsigned int t18;
    unsigned int t19;
    char *t20;
    int t21;
    char *t22;
    int t23;
    char *t24;
    int t25;
    char *t26;
    char *t27;
    int t28;
    unsigned int t29;

LAB0:    t7 = (t6 + 4U);
    t8 = (t3 != 0);
    if (t8 == 1)
        goto LAB3;

LAB2:    t9 = (t6 + 8U);
    *((char **)t9) = t4;
    t12 = (t4 + 12U);
    t13 = *((unsigned int *)t12);
    t14 = (t13 + 1);
    t15 = ieee_p_1242562249_sub_2045698577_1035706684(IEEE_P_1242562249, t11, t3, t4, t14);
    t16 = ieee_p_1242562249_sub_3481121704_1035706684(IEEE_P_1242562249, t10, t15, t11);
    t17 = (t10 + 12U);
    t18 = *((unsigned int *)t17);
    t19 = (1U * t18);
    t0 = xsi_get_transient_memory(t19);
    memcpy(t0, t16, t19);
    t20 = (t10 + 0U);
    t21 = *((int *)t20);
    t22 = (t10 + 4U);
    t23 = *((int *)t22);
    t24 = (t10 + 8U);
    t25 = *((int *)t24);
    t26 = (t2 + 0U);
    t27 = (t26 + 0U);
    *((int *)t27) = t21;
    t27 = (t26 + 4U);
    *((int *)t27) = t23;
    t27 = (t26 + 8U);
    *((int *)t27) = t25;
    t28 = (t23 - t21);
    t29 = (t28 * t25);
    t29 = (t29 + 1);
    t27 = (t26 + 12U);
    *((unsigned int *)t27) = t29;

LAB1:    return t0;
LAB3:    *((char **)t7) = t3;
    goto LAB2;

LAB4:;
}


extern void work_p_1869287427_init()
{
	static char *se[] = {(void *)work_p_1869287427_sub_3605173140_1322656296,(void *)work_p_1869287427_sub_3411271061_1322656296,(void *)work_p_1869287427_sub_4134552588_1322656296,(void *)work_p_1869287427_sub_2713497013_1322656296,(void *)work_p_1869287427_sub_2465831651_1322656296,(void *)work_p_1869287427_sub_2365366537_1322656296,(void *)work_p_1869287427_sub_4249709490_1322656296,(void *)work_p_1869287427_sub_2828653915_1322656296,(void *)work_p_1869287427_sub_1404342903_1322656296,(void *)work_p_1869287427_sub_1403861144_1322656296,(void *)work_p_1869287427_sub_1335278590_1322656296,(void *)work_p_1869287427_sub_1310905938_1322656296,(void *)work_p_1869287427_sub_2785686743_1322656296};
	xsi_register_didat("work_p_1869287427", "isim/tb_Top_isim_beh.exe.sim/work/p_1869287427.didat");
	xsi_register_subprogram_executes(se);
}
