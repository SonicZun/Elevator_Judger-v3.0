# -*- coding: utf-8 -*-
"""
@author: Sonic

"""
import os
path = os.getcwd()
#print mode available to console
dirs = os.listdir(path + "\\bomber\\mode")
print("\nChoose a bombing mode:\n")
for dir in dirs:
    print(dir + " ", end = "")
print("\n")

#choose a mode
string_mode = input()
output_dir = "output\\"
bullet_dir = "bomber\\mode\\" + string_mode + "\\"

#bullet amount
print("\nInput the bullet amount:\n")
bullet_amount = int(input())

cmd_4_show = "@for /l %i in (0, 1, {}) do @echo bullet %i is running... & @python bomber\\bomber.py {} %i|java -jar testee.jar".format(bullet_amount - 1, string_mode)


#cmd
cmd_1 = "@echo Running: Writing the output to \"output_x.txt\" under output."
cmd_2 = "@echo Writing the exeption information to \"err_x.txt\" under output\\err."
cmd_3 = "@echo This window will close autonomously when the program is finished."
if (string_mode == "show"):
	cmd_4 = cmd_4_show
else:
	cmd_4 = "@for /l %i in (0, 1, {}) do @echo bullet %i is running... & @python bomber\\bomber.py {} %i|java -jar testee.jar > output\\output_%i.txt 2>output\\err\\err_%i.txt".format(bullet_amount - 1, string_mode)
cmd_5 = "python Checker_plus.py {} {}".format(string_mode, bullet_amount)
os.system("(" + cmd_1 + ") & (" + cmd_2 + ") & (" + cmd_3 + ") & (" + cmd_4 + ") & (" + cmd_5 + ")")