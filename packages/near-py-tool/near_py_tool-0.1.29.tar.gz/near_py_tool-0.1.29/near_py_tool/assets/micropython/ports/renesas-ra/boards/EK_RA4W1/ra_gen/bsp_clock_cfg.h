/* generated configuration header file - do not edit */
#ifndef BSP_CLOCK_CFG_H_
#define BSP_CLOCK_CFG_H_
#define BSP_CFG_CLOCKS_SECURE (0)
#define BSP_CFG_CLOCKS_OVERRIDE (0)
#define BSP_CFG_XTAL_HZ (8000000) /* XTAL 8000000Hz */
#define BSP_CFG_PLL_SOURCE (BSP_CLOCKS_SOURCE_CLOCK_MAIN_OSC) /* PLL Src: XTAL */
#define BSP_CFG_HOCO_FREQUENCY (4) /* HOCO 48MHz */
#define BSP_CFG_PLL_DIV (BSP_CLOCKS_PLL_DIV_2) /* PLL Div /2 */
#define BSP_CFG_PLL_MUL (BSP_CLOCKS_PLL_MUL(12U, 0U)) /* PLL Mul x12 */
#define BSP_CFG_CLOCK_SOURCE (BSP_CLOCKS_SOURCE_CLOCK_HOCO) /* Clock Src: HOCO */
#define BSP_CFG_ICLK_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_1) /* ICLK Div /1 */
#define BSP_CFG_PCLKA_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_1) /* PCLKA Div /1 */
#define BSP_CFG_PCLKB_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_2) /* PCLKB Div /2 */
#define BSP_CFG_PCLKC_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_1) /* PCLKC Div /1 */
#define BSP_CFG_PCLKD_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_1) /* PCLKD Div /1 */
#define BSP_CFG_FCLK_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_2) /* FCLK Div /2 */
#define BSP_CFG_CLKOUT_SOURCE (BSP_CLOCKS_CLOCK_DISABLED) /* CLKOUT Disabled */
#define BSP_CFG_CLKOUT_DIV (BSP_CLOCKS_SYS_CLOCK_DIV_1) /* CLKOUT Div /1 */
#define BSP_CFG_UCK_SOURCE (BSP_CLOCKS_SOURCE_CLOCK_HOCO) /* UCLK Src: HOCO */
#endif /* BSP_CLOCK_CFG_H_ */
