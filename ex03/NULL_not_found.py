#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rboudwin <rboudwin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:07:42 by rboudwin          #+#    #+#              #
#    Updated: 2024/06/10 11:07:43 by rboudwin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    o_type = type(object)
    if o_type is None:
        print(f"Nothing: None {o_type}")
    elif o_type is float and object != object:
        print(f"Cheese: nan {o_type}")
    elif o_type is int and object == 0:
        print(f"Zero: 0 {o_type}")
    elif o_type is str and object == '':
        print(f"Empty: {o_type}")
    elif o_type is bool and object == False:
        print(f"Fake: False {o_type}")
    else:
        print("Type not Found")
        return 1
    return 0
    