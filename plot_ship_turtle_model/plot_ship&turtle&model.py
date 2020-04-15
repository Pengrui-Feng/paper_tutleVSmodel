#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 15:24:00 2020
plot special data for paper
data from matched_ship_turtle.csv and get_model_temp.py
@author: pengrui
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

path1='/content/drive/My Drive/'
#data is from matched turtle ships file
date1='2012-8-12 12:00:00'#from tu74
t_depth1_1=[2,10,12,14,19,20,22,25,31,49]
t_depth1_2=[2,12,14,18,19,21,29,30,37,54]
t_depth1_3=[2,8,10,13,14,16,18,27,37,59]
t_depth1_4=[2,10,14,16,17,18,22,25,34,54]
t_temp1_1=[25.9500,25.8278,24.9874,21.1521,15.7582,14.3219,12.6411,11.3882,10.8381,10.6700]
t_temp1_2=[26.5600,25.5446,24.2539,20.4160,18.7983,16.6987,11.7078,10.7612,9.4016,9.3500]
t_temp1_3=[26.6500,26.1813,25.4615,21.8456,20.0042,17.5769,15.9364,11.8016,10.1611,9.9100]
t_temp1_4=[25.7700,24.9646,23.3201,21.7428,19.5782,18.7224,12.7991,11.7419,9.8290,8.9900]

date2='2012-6-3 01:00:00' #from tu74
t_depth2_1=[2,6,8,9,11,13,21,24,29,41]
t_depth2_2=[2,5,6,9,11,13,15,22,28,56]

t_temp2_1=[20.0100,19.2642,17.0810,17.0539,15.2708,14.7419,14.3419,13.5961,13.2300,13.4673]
t_temp2_2=[19.7800,19.6122,19.1172,18.3621,17.2462,15.7612,14.6118,11.8766,11.4487,11.3900]
date3='2018-9-15 00:00:00' #from tu98
t_depth3=[2,6,22,26,30,33,36,37,39,40]
t_temp3=[21.170,20.042,19.217,17.533,16.514,14.198,13.541,12.750,12.750,13.575]

s_depth1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]
s_depth2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
s_depth3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
s_temp1=[25.13,25.14,25.12,25.1,25.07,25.06,25.06,25.04,25.04,24.82,25.11,21.02,19.63,18.19,16.85,15.38,14.63,13.74,13.07,12.79,12.45,12.2,12.04,11.93,11.89,11.87,11.84,11.77,11.65,11.53,11.46,11.38,11.24,11.09,10.95,10.89,10.72,10.55,10.46,10.4,10.34,10.31]
s_temp2=[20.08,20.07,20.06,20.02,19.89,19.76,19.57,18.99,17.3,16.08,15.24,14.9,14.97,14.92,14.89,14.9,14.88,14.79,14.56,14.35,14.11,13.82,13.7,13.28,12.6,12.72,12.73,12.69,12.33,11.94,11.98,12.01,11.94,11.93,12.05,12.11,12.03,11.98,11.91,11.86,11.78]
s_temp3=[21.01, 21.01, 21.02, 21.02, 21.02, 21.02, 21.01, 21.01, 21.02, 21.02, 21.01, 21.00, 20.97, 20.92, 20.91, 20.90, 20.87, 20.84, 20.84, 20.82, 20.77, 20.68, 20.55, 20.56, 20.32, 19.03, 16.79, 15.36, 14.86, 14.39, 14.06, 14.00, 13.55, 12.80, 12.37, 12.06, 11.98]
f_temp1=[24.705944 , 24.708637 , 24.712175 , 24.715204 , 24.716368 , 24.706427 , 24.592749 , 24.406502 , 24.185843 , 23.728449 , 23.446835 , 23.079977 , 22.634212 , 22.149902 , 21.669231 , 21.21399 , 20.787502 , 20.390606 , 20.023874 , 19.686193 , 19.374086 , 19.083277 , 18.80985 , 18.550915 , 18.304525 , 18.069435 , 17.844826 , 17.630182 , 17.226254 , 17.02752 , 16.819345 , 16.601057 , 16.380346 , 16.11083 , 15.865639 , 15.825584 , 15.808668 , 15.794301 , 15.7848215, 15.776224 , 15.769808 , 15.7656975]
f_temp2=[21.172533 , 21.193596 , 21.193596 , 20.975986 , 20.597488 , 20.168682 , 19.7136 , 19.251392 , 19.251392 , 18.796787 , 18.366684 , 17.973389 , 17.61382 , 17.278465 , 17.278465 , 16.962843 , 16.667868 , 16.39472 , 16.14166 , 15.905948 , 15.905948 , 15.6851845, 15.478137 , 15.284044 , 15.102217 , 14.93211 , 14.93211 , 14.773233 , 14.624748 , 14.485431 , 14.353896 , 14.228884 , 14.228884 , 14.109545 , 13.995211 , 13.8852 , 13.778708 , 13.675345 , 13.675345 , 13.575182 , 13.479743]        
f_temp3=[21.587494, 21.423058, 21.17381 , 21.131859, 21.090631, 21.010502,20.898376, 20.818554, 20.769005, 20.737549, 20.714483, 20.667164,20.62965 , 20.57254 , 20.488874, 20.374586, 20.229563, 20.058056,19.867111, 19.664352, 19.456295, 19.24787 , 19.042212, 18.8416  ,18.647459, 18.460808, 18.282352, 18.112669, 17.952177, 17.800804,17.657442, 17.519415, 17.382017, 17.09171 , 16.948814, 16.845587,16.806799]
e_temp1=[26.654821, 26.657522, 26.660162, 26.662344, 26.664312,26.6662,26.668089, 26.668089, 26.670036, 26.672089, 26.674294, 26.67672 ,26.679565, 26.683397, 26.683397, 26.689205, 26.697075, 26.660381,26.263456, 24.990711, 23.088285, 23.088285, 21.096235, 19.259314,17.952461, 16.995447, 16.16636 , 15.425723, 15.425723, 14.7432  ,14.124955, 13.618519, 13.257369, 13.027269, 12.870188, 12.744915,12.744915, 12.643401, 12.545684, 12.501514, 12.489237, 12.489237]
e_temp2=[20.127386, 20.129395, 20.131294, 20.132654, 20.132654, 20.133438,20.133917, 20.135044, 20.138426, 20.138426, 20.14029 , 20.14272 ,20.139006, 20.082647, 20.082647, 19.89413 , 19.538996, 18.992233,18.041784, 18.041784, 16.306719, 14.857296, 13.842644, 13.234353,13.234353, 12.701059, 11.960268, 11.415138, 11.2023  , 11.2023  ,11.078178, 11.010829, 10.989429, 10.984299, 10.984299, 10.982707,10.98205 , 10.981639, 10.981126, 10.981126, 10.980346]
e_temp3=[20.72312355, 20.72551346, 20.72945404, 20.73393059, 20.73963928,20.74833298, 20.75952339, 20.77222252, 20.7814579 , 20.777565  ,20.75458527, 20.72031975, 20.67634964, 20.61469841, 20.52495003,20.40594292, 20.28597832, 20.21046638, 20.15382767, 19.99875832,19.64816284, 19.15328979, 18.52985191, 17.81350708, 17.06133461,16.32853127, 15.65642548, 15.06072807, 14.54843903, 14.13346767,13.8238287 , 13.62373352, 13.51422596, 13.46639156, 13.45132828,13.43920898, 13.40376663]
#e_temp3 is from doppio model
fig=plt.figure()
plt.plot(np.array(t_temp3),t_depth3,linestyle='-',color='black',linewidth=1,label='turtle')
#plt.plot(np.array(t_temp1_2),t_depth2_2,linestyle='-',color='black',linewidth=1)
#plt.plot(np.array(t_temp1_3),t_depth1_3,linestyle='-',color='black',linewidth=1)
#plt.plot(np.array(t_temp1_4),t_depth1_4,linestyle='-',color='black',linewidth=1)
plt.plot(np.array(s_temp3),s_depth3,linestyle='-',color='red',linewidth=3,label='ship')
plt.plot(np.array(f_temp3),s_depth3,linestyle=':',color='blue',linewidth=3,label='FVCOM')
plt.plot(np.array(e_temp3),s_depth3,linestyle='--',color='green',linewidth=3,label='doppio')
plt.ylim([38,-1])
plt.xlabel('Temperature(℃)',fontsize=14)
plt.title('Turtle vs Ship vs Model Profiles (2018-09-15)',fontsize=14) 
plt.ylabel('Depth(m)',fontsize=14)
plt.legend()
plt.savefig(path1+'18-9-15_compare_profile.png',dpi=200)
plt.show()
