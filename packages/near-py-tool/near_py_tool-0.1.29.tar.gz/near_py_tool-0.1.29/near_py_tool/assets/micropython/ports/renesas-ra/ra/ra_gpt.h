/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2023 Vekatech Ltd.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#ifndef RA_RA_GPT_H_
#define RA_RA_GPT_H_

#include <stdint.h>

void ra_gpt_timer_start(uint32_t ch);
void ra_gpt_timer_stop(uint32_t ch);
void ra_gpt_timer_set_freq(uint32_t ch, float freq);
float ra_gpt_timer_get_freq(uint32_t ch);
float ra_gpt_timer_tick_time(uint32_t ch);
void ra_gpt_timer_set_period(uint32_t ch, uint32_t ns);
uint32_t ra_gpt_timer_get_period(uint32_t ch);
void ra_gpt_timer_set_duty(uint32_t ch, uint8_t id, uint32_t duty);
uint32_t ra_gpt_timer_get_duty(uint32_t ch, uint8_t id);
void ra_gpt_timer_init(uint32_t pwm_pin, uint32_t ch, uint8_t id, uint32_t duty, float freq);
void ra_gpt_timer_deinit(uint32_t pwm_pin, uint32_t ch, uint8_t id);
bool ra_gpt_timer_is_pwm_pin(uint32_t pin);

#endif /* RA_RA_GPT_H_ */
