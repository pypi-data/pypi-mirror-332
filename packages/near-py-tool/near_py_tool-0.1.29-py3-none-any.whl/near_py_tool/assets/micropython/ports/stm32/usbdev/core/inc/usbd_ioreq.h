/**
  ******************************************************************************
  * @file    usbd_ioreq.h
  * @author  MCD Application Team
  * @version V2.0.0
  * @date    18-February-2014
  * @brief   header file for the usbd_ioreq.c file
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

#ifndef __USBD_IOREQ_H_
#define __USBD_IOREQ_H_

/* Includes ------------------------------------------------------------------*/
#include  "usbd_def.h"
#include  "usbd_core.h"

/** @addtogroup STM32_USB_OTG_DEVICE_LIBRARY
  * @{
  */

/** @defgroup USBD_IOREQ
  * @brief header file for the usbd_ioreq.c file
  * @{
  */

/** @defgroup USBD_IOREQ_Exported_Defines
  * @{
  */
/**
  * @}
  */


/** @defgroup USBD_IOREQ_Exported_Types
  * @{
  */


/**
  * @}
  */



/** @defgroup USBD_IOREQ_Exported_Macros
  * @{
  */

/**
  * @}
  */

/** @defgroup USBD_IOREQ_Exported_Variables
  * @{
  */

/**
  * @}
  */

/** @defgroup USBD_IOREQ_Exported_FunctionsPrototype
  * @{
  */

USBD_StatusTypeDef  USBD_CtlSendData (USBD_HandleTypeDef  *pdev,
                               uint8_t *buf,
                               uint16_t len);

USBD_StatusTypeDef  USBD_CtlContinueSendData (USBD_HandleTypeDef  *pdev,
                               uint8_t *pbuf,
                               uint16_t len);

USBD_StatusTypeDef USBD_CtlPrepareRx (USBD_HandleTypeDef  *pdev,
                               uint8_t *pbuf,
                               uint16_t len);

USBD_StatusTypeDef  USBD_CtlContinueRx (USBD_HandleTypeDef  *pdev,
                              uint8_t *pbuf,
                              uint16_t len);

USBD_StatusTypeDef  USBD_CtlSendStatus (USBD_HandleTypeDef  *pdev);

USBD_StatusTypeDef  USBD_CtlReceiveStatus (USBD_HandleTypeDef  *pdev);

uint16_t  USBD_GetRxCount (USBD_HandleTypeDef  *pdev ,
                           uint8_t epnum);

/**
  * @}
  */

#endif /* __USBD_IOREQ_H_ */

/**
  * @}
  */

/**
* @}
*/
/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
