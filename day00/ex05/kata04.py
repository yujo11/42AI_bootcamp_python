# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/16 14:25:38 by yujo              #+#    #+#              #
#    Updated: 2020/09/16 14:33:03 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

dic = ( 0, 4, 132.42222, 10000, 12345.67)

header = 'day_{:02d}, ex_{:02d} :'.format(dic[0], dic[1])
body = '{:.2f}, {:.2e}, {:.2e}'.format(dic[2], dic[3], dic[4])

print(header, body)

# Expected answer

# day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04