#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rboudwin <rboudwin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 09:53:59 by rboudwin          #+#    #+#              #
#    Updated: 2024/06/10 09:53:59 by rboudwin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World"
ft_change_tuple = list(ft_tuple)
ft_change_tuple[1] = "Finland"
ft_tuple = tuple(ft_change_tuple)
ft_set.remove("tutu!")
ft_set.add("Helsinki")
ft_dict["Hello"] = "Hive"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)