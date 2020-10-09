import pywal
import os

CACHE_DIR = os.path.join(os.environ["HOME"], ".config/wal")

def doit(wallpaper_folder, home_dir, debug=False):
    if debug:
        print("Debug from ch_wal.doit()")
        print("Image Path: "+wallpaper_folder)
        print("Home Path: "+home_dir)

    """Entry Function into changing wallpaper"""
    image = pywal.image.get(str(wallpaper_folder))
    # get image palette
    colors = pywal.colors.get(image)
    # apply the palette to all open terminals
    pywal.sequences.send(colors)
    # export all template files.
    pywal.export.every(colors, CACHE_DIR)
    # export individual template files.
    pywal.export.color(colors, "xresources", home_dir+".Xresources")
    pywal.export.color(colors, "shell", home_dir+".config/wal/colors.sh")
    # reload xrdb, i3, and polybar
    pywal.reload.env()
    ########
    # Reload individual programs.
    pywal.reload.i3()
    pywal.reload.polybar()
    pywal.reload.xrdb()

    # set the wallpaper
    pywal.wallpaper.change(image)
