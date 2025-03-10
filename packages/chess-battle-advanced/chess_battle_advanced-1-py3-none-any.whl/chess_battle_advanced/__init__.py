import os, pathlib, tkinter, subprocess

__CBA_DIR = os.path.dirname(__file__)
CBA_VIDEO = os.path.join(__CBA_DIR, 'chessbattleadvanced.mp4')

def cba():
    tk = tkinter.Tk()
    command = ['ffplay', '-autoexit', '-noborder', '-x', f'{tk.winfo_screenwidth()}', '-y', f'{tk.winfo_screenheight()}', '-window_title', 'chess battle advanced', f'{os.path.join(__CBA_DIR, 'chessbattleadvanced.mp4')}']
    try:
        subprocess.check_call(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        raise Exception('this command requires ffmpeg')