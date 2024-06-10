#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rboudwin <rboudwin@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:59:03 by rboudwin          #+#    #+#              #
#    Updated: 2024/06/10 11:59:06 by rboudwin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
assert len(sys.argv) < 3, "more than one argument is provided"
try:
    num = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not an integer")
if num % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")
