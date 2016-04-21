# (c) Copyright 2016 forkedbranch (http://forkedbranch.eu/)
# Licensed under the Apache License, Version 2.0

import os
import shutil
import config

INPUT_FOLDER = config.get_input_folder()
FEMM_EXE = config.get_femm_exe()
FEMM_SCRIPT_TEMPLATE = config.get_femm_scr_templ()
FEMM_SCRIPT_LIBRARY = config.get_femm_scr_lib()

femm_script_template_str = None

def prepare_output_folder(output_folder):
    os.makedirs(output_folder, exist_ok=True)
    shutil.copy2(os.path.join(INPUT_FOLDER, FEMM_SCRIPT_LIBRARY), output_folder)

def prepare_femm_template(ycenter, radius, output_base_name, output_folder):
    global femm_script_template_str
    prepare_output_folder(output_folder)

    if femm_script_template_str == None:
        with open(os.path.join(INPUT_FOLDER, FEMM_SCRIPT_TEMPLATE)) as f:
            femm_script_template_str = f.read()
    
    with open(os.path.join(output_folder, FEMM_SCRIPT_TEMPLATE), "w") as f:
        femm_main_script = femm_script_template_str\
            .replace("_YCENTER_", str(ycenter))\
            .replace("_RADIUS_", str(radius))\
            .replace("_OUTNAME_", output_base_name)
        f.write(femm_main_script)

def run_femm(ycenter, radius, output_base_name, output_folder):
    prepare_femm_template(ycenter, radius, output_base_name, output_folder)
    os.chdir(output_folder)
    os.system("%s -lua-script=%s" % (FEMM_EXE, FEMM_SCRIPT_TEMPLATE))
    
    field_values = []
    with open(os.path.join(output_folder, "%s.dat" % output_base_name)) as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                field_values.append(float(line.strip()))
            
    return max(field_values), \
           len(list(filter(lambda x: x==-1, field_values))), \
           os.path.join(output_folder, "%s.bmp" % output_base_name)