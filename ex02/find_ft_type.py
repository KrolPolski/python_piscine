
#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rboudwin <rboudwin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:31:51 by rboudwin          #+#    #+#              #
#    Updated: 2024/06/10 10:31:55 by rboudwin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    o_type = type(object)
    if o_type is list:
        print(f"List : {o_type}")
    elif o_type is tuple:
        print(f"Tuple : {o_type}")
    elif o_type is set:
        print(f"Set : {o_type}")
    elif o_type is dict:
        print(f"Dict : {o_type}")
    elif o_type is str:
        print(f"{object} is in the kitchen : {o_type}")
    else:
        print("Type not found")
    return 42

