# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/16 13:51:46 by yujo              #+#    #+#              #
#    Updated: 2020/09/16 20:45:47 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

time = (3, 30, 2019, 9, 25)
model = '{:%m/%d/%Y %H:%M}'

print(model.format(datetime(time[2], time[3], time[4], time[0], time[1])))


# Expected answer

# 09/25/2019 03:30
