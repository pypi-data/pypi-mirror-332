/**
  ******************************************************************************
  * @file    usbd_core.h
  * @author  MCD Application Team
  * @version V2.0.0
  * @date    18-February-2014
  * @brief   Header file for usbd_core.c
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; COPYRIGHT 2014 STMicroelectronics</center></h2>
  *
  * Licensed under MCD-ST Liberty SW License Agreement V2, (the "License");
  * You may not use this file except in compliance with the License.
  * You may obtain a copy of the License at:
  *
  *        http://www.st.com/software_license_agreement_liberty_v2
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  *
  ******************************************************************************
  */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __USBD_CORE_H
#define __USBD_CORE_H

/* Includes ------------------------------------------------------------------*/
#include "usbd_conf.h"
#include "usbd_def.h"
#include "usbd_ioreq.h"
#include "usbd_ctlreq.h"

/** @addtogroup STM32_USB_OTG_DEVICE_LIBRARY
  * @{
  */

/** @defgroup USBD_CORE
  * @brief This file is the Header file for usbd_core.c file
  * @{
  */


/** @defgroup USBD_CORE_Exported_Defines
  * @{
  */

/**
  * @}
  */


/** @defgroup USBD_CORE_Exported_TypesDefinitions
  * @{
  */


/**
  * @}
  */



/** @defgroup USBD_CORE_Exported_Macros
  * @{
  */

/**
  * @}
  */

/** @defgroup USBD_CORE_Exported_Variables
  * @{
  */
#define USBD_SOF          USBD_LL_SOF
/**
  * @}
  */

/** @defgroup USBD_CORE_Exported_FunctionsPrototype
  * @{
  */
USBD_StatusTypeDef USBD_Init(USBD_HandleTypeDef *pdev, USBD_DescriptorsTypeDef *pdesc, uint8_t id);
USBD_StatusTypeDef USBD_DeInit(USBD_HandleTypeDef *pdev);
USBD_StatusTypeDef USBD_Start  (USBD_HandleTypeDef *pdev);
USBD_StatusTypeDef USBD_Stop   (USBD_HandleTypeDef *pdev);
USBD_StatusTypeDef USBD_RegisterClass(USBD_HandleTypeDef *pdev, const USBD_ClassTypeDef *pclass);

USBD_StatusTypeDef USBD_RunTestMode (USBD_HandleTypeDef  *pdev);
USBD_StatusTypeDef USBD_SetClassConfig(USBD_HandleTypeDef  *pdev, uint8_t cfgidx);
USBD_StatusTypeDef USBD_ClrClassConfig(USBD_HandleTypeDef  *pdev, uint8_t cfgidx);

USBD_StatusTypeDef USBD_LL_SetupStage(USBD_HandleTypeDef *pdev, uint8_t *psetup);
USBD_StatusTypeDef USBD_LL_DataOutStage(USBD_HandleTypeDef *pdev , uint8_t epnum, uint8_t *pdata);
USBD_StatusTypeDef USBD_LL_DataInStage(USBD_HandleTypeDef *pdev , uint8_t epnum, uint8_t *pdata);

USBD_StatusTypeDef USBD_LL_Reset(USBD_HandleTypeDef  *pdev);
USBD_StatusTypeDef USBD_LL_SetSpeed(USBD_HandleTypeDef  *pdev, USBD_SpeedTypeDef speed);
USBD_StatusTypeDef USBD_LL_Suspend(USBD_HandleTypeDef  *pdev);
USBD_StatusTypeDef USBD_LL_Resume(USBD_HandleTypeDef  *pdev);

USBD_StatusTypeDef USBD_LL_SOF(USBD_HandleTypeDef  *pdev);
USBD_StatusTypeDef USBD_LL_IsoINIncomplete(USBD_HandleTypeDef  *pdev, uint8_t epnum);
USBD_StatusTypeDef USBD_LL_IsoOUTIncomplete(USBD_HandleTypeDef  *pdev, uint8_t epnum);

USBD_StatusTypeDef USBD_LL_DevConnected(USBD_HandleTypeDef  *pdev);
USBD_StatusTypeDef USBD_LL_DevDisconnected(USBD_HandleTypeDef  *pdev);

/* USBD Low Level Driver */
USBD_StatusTypeDef  USBD_LL_Init (USBD_HandleTypeDef *pdev, int high_speed, const uint8_t *fifo_size);
USBD_StatusTypeDef  USBD_LL_DeInit (USBD_HandleTypeDef *pdev);
USBD_StatusTypeDef  USBD_LL_Start(USBD_HandleTypeDef *pdev);
USBD_StatusTypeDef  USBD_LL_Stop (USBD_HandleTypeDef *pdev);
USBD_StatusTypeDef  USBD_LL_OpenEP  (USBD_HandleTypeDef *pdev,
                                      uint8_t  ep_addr,
                                      uint8_t  ep_type,
                                      uint16_t ep_mps);

USBD_StatusTypeDef  USBD_LL_CloseEP (USBD_HandleTypeDef *pdev, uint8_t ep_addr);
USBD_StatusTypeDef  USBD_LL_FlushEP (USBD_HandleTypeDef *pdev, uint8_t ep_addr);
USBD_StatusTypeDef  USBD_LL_StallEP (USBD_HandleTypeDef *pdev, uint8_t ep_addr);
USBD_StatusTypeDef  USBD_LL_ClearStallEP (USBD_HandleTypeDef *pdev, uint8_t ep_addr);
uint8_t             USBD_LL_IsStallEP (USBD_HandleTypeDef *pdev, uint8_t ep_addr);
USBD_StatusTypeDef  USBD_LL_SetUSBAddress (USBD_HandleTypeDef *pdev, uint8_t dev_addr);
USBD_StatusTypeDef  USBD_LL_Transmit (USBD_HandleTypeDef *pdev,
                                      uint8_t  ep_addr,
                                      uint8_t  *pbuf,
                                      uint16_t  size);

USBD_StatusTypeDef  USBD_LL_PrepareReceive(USBD_HandleTypeDef *pdev,
                                           uint8_t  ep_addr,
                                           uint8_t  *pbuf,
                                           uint16_t  size);

uint32_t USBD_LL_GetRxDataSize  (USBD_HandleTypeDef *pdev, uint8_t  ep_addr);
void  USBD_LL_Delay (uint32_t Delay);

/**
  * @}
  */

#endif /* __USBD_CORE_H */

/**
  * @}
  */

/**
* @}
*/

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/



