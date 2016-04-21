# (c) Copyright 2016 forkedbranch (http://forkedbranch.eu/)
# Licensed under the Apache License, Version 2.0

from PIL import Image, ImageColor, ImageFont, ImageDraw
from os import path, system, chdir
from shutil import copy2
import config

INPUT_FOLDER = config.get_input_folder()
FFMPEG_EXE = config.get_ffmpeg_exe()

def compose_images(output_directory, 
                   exp1_name, exp2_name, obj_name, 
                   exp1_results, exp2_results):
    
    len_exp1 = len(exp1_results)
    len_exp2 = len(exp2_results)
    
    for i in range(0, len_exp2):
        composite = Image.new('RGBA', (1280, 720), color=ImageColor.getcolor('white', 'RGBA'))
        
        dl_image = Image.open('{}/{}_{:03d}.bmp'
                              .format(output_directory, exp2_name, i+1))
        dl_search = Image.open('{}/{}_searchpath_{:03d}.png'
                               .format(output_directory, exp2_name, i+1))
    
        k = i if i < len_exp1-1 else len_exp1-1
        nl_search = Image.open('{}/{}_searchpath_{:03d}.png'
                               .format(output_directory, exp1_name, k+1))
        nl_image = Image.open('{}/{}_{:03d}.bmp'
                              .format(output_directory, exp1_name, k+1))
        
        objective = Image.open('{}/{}_{:03d}.png'
                               .format(output_directory, obj_name, i+1))
        
        nl_image = nl_image.crop((0, 0, 310, 616))
        dl_image = dl_image.crop((0, 0, 310, 616))
        
        composite.paste(nl_image, (20, 80))
        composite.paste(dl_image, (360, 80))
        composite.paste(nl_search, (700, 420))
        composite.paste(dl_search, (990, 420))
        composite.paste(objective, (700, 80))
        
        font = ImageFont.truetype(path.join(INPUT_FOLDER, "SourceCodePro-Light.ttf"), 20)
        draw = ImageDraw.Draw(composite)
        draw.text((20, 20), 'LOCAL SEARCH', font=font, fill='black')
        draw.text((20, 45), 'Nelder-Mead', font=font, fill='black')
        draw.text((360, 20), 'GLOBAL SEARCH', font=font, fill='black')
        draw.text((360, 45), 'Direct-L', font=font, fill='black')
        draw.text((700, 60), 'OBJECTIVE FUNCTION VALUE', font=font, fill='black')
        draw.text((700, 400), 'SEARCH PATH', font=font, fill='black')
        draw.text((890, 400), 'local', font=font, fill='black')
        draw.text((1170, 400), 'global', font=font, fill='black')

        draw.text((230, 80), 'eval #{:2d}'.format(k+1), font=font, fill='black')
        draw.text((570, 80), 'eval #{:2d}'.format(i+1), font=font, fill='black')
        
        font = ImageFont.truetype(path.join(INPUT_FOLDER, "SourceCodePro-Light.ttf"), 18)
        
        if i<len_exp1-1:
            draw.text((220, 620), 'current', font=font, fill='black')
            item = exp1_results[i]
        else:
            draw.text((220, 620), 'BEST', font=font, fill='black')
            item = min(exp1_results, key=lambda x:x['objective'])
        
        draw.text((220, 638), 'yc = {:+4.2f}'.format(item['center']), font=font, fill='black')
        draw.text((220, 656), 'r  = {:4.3f}'.format(item['radius']), font=font, fill='black')
        draw.text((220, 674), 'E  = {:4.1f}'.format(item['objective']), font=font, fill='black')
            
        if i<len_exp2-1:
            draw.text((560, 620), 'current', font=font, fill='black')
            item = exp2_results[i]
        else:
            draw.text((560, 620), 'BEST', font=font, fill='black')
            item = min(exp2_results, key=lambda x:x['objective'])
            
        draw.text((560, 638), 'yc = {:+4.2f}'.format(item['center']), font=font, fill='black')
        draw.text((560, 656), 'r  = {:4.3f}'.format(item['radius']), font=font, fill='black')
        draw.text((560, 674), 'E  = {:4.1f}'.format(item['objective']), font=font, fill='black')
        
        composite.save('{}/Composite_{:03d}.png'.format(output_directory, i+1))
        
    for i in range(len_exp2, len_exp2+10):
        copy2('{}/Composite_{:03d}.png'.format(output_directory, len_exp2),
              '{}/Composite_{:03d}.png'.format(output_directory, i+1))        

def make_movie(output_directory, 
                   exp1_name, exp2_name, obj_name, 
                   exp1_results, exp2_results, movie_name):
    
    compose_images(output_directory, 
                   exp1_name, exp2_name, obj_name, 
                   exp1_results, exp2_results)
    chdir(output_directory)
    system('{} {} {}.mp4'.format(FFMPEG_EXE,
                             "-framerate 2 -i Composite_%03d.png -c:v libx264 -pix_fmt yuv420p", 
                             movie_name))
