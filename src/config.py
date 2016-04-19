import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_input_folder():
    return config['DEFAULT']['InputFolder']
    
def get_output_folder():
    return config['DEFAULT']['OutputForlder']

def get_femm_exe():
    return config['DEFAULT']['FemmExe']

def get_ffmpeg_exe():
    return config['DEFAULT']['FfmpegExe']
    
def get_femm_scr_templ():
    return config['DEFAULT']['FemmScrTempl']

def get_femm_scr_lib():
    return config['DEFAULT']['FemmScrLib']