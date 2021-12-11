import tkinter as tk

def destroyInnerWidgets(frame):
    """ destroys every widget inside the frame, argument needs to be a tk.Canvas()"""
    widgets = frame.winfo_children()
    for widget in widgets:
        widget.destroy()

def scrollBar(table):
    """scrollBar need a frame as argument, adjust frame for scrollbar size"""
    # create a main frame
    mainFrame = tk.Frame(table, bg="#ffffff")
    mainFrame.pack(fill='both', expand=1)
    # canvas
    canvasMainFrame = tk.Canvas(mainFrame)
    canvasMainFrame.pack(side='left', fill='both', expand=1)
    # scrollbar
    canvScroll = ttk.Scrollbar(mainFrame, orient='vertical', command=canvasMainFrame.yview)
    canvScroll.pack(side='right', fill='y')
    # config canvas
    canvas1.configure(yscrollcommand=canvScroll.set)
    canvas1.bind('<Configure>', lambda e: canvasMainFrame.configure(scrollregion=canvasMainFrame.bbox("all")))
    # create another frame in canvas
    frameInCanvas = tk.Frame(canvasMainFrame)
    # add frame to window in canvas
    canvasMainFrame.create_window((0, 0), window=frameInCanvas, anchor="nw")

#Bastian Lipka