#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rboudwin <rboudwin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 09:53:40 by rboudwin          #+#    #+#              #
#    Updated: 2024/06/10 09:53:40 by rboudwin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import time
import datetime
current_time = time.time()
s_time = time.gmtime(current_time)
d_time = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")
print(d_time.strftime("%B")  + " " + str(s_time.tm_mday) + " " + str(s_time.tm_year))