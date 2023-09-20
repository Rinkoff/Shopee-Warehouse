from core.const import *
from GUI.pages.main_page import MainPage

import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()

    main_frame = MainPage(root)
    main_frame.pack(fill="both", expand=True)

    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON_PATH)
    root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)



    root.mainloop()
