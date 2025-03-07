MCU_SERIES = f7
CMSIS_MCU = STM32F746xx
AF_FILE = boards/stm32f746_af.csv
LD_FILES = boards/stm32f746.ld boards/common_ifs.ld
TEXT0_ADDR = 0x08000000
TEXT1_ADDR = 0x08020000

# MicroPython settings
MICROPY_PY_LWIP = 1
MICROPY_PY_SSL = 1
MICROPY_SSL_MBEDTLS = 1
MICROPY_HW_ENABLE_ISR_UART_FLASH_FUNCS_IN_RAM = 1

FROZEN_MANIFEST = $(BOARD_DIR)/manifest.py
