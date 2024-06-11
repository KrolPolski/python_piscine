#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rboudwin <rboudwin@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:57:19 by rboudwin          #+#    #+#              #
#    Updated: 2024/06/10 11:57:23 by rboudwin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time as ti
import datetime as dt
current_time = ti.time()
s_time = ti.gmtime(current_time)
d_time = dt.datetime.now()
print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")
print(d_time.strftime("%B")  + " " + str(s_time.tm_mday) + " " + str(s_time.tm_year))