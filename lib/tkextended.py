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


def refreshWindow(root, window):
    """
    Switches Window previous root gets destroyed new window gets started

    :param root: old root that will be destroyed
    :param window: name of the new window to be started expand the if
    :return: none - starts new window
    """

    root.destroy()
    if window == "main":
        # some function to start the new window
        # expl. tableWindow()
        pass


def separateData(paths):
    """
    Separates Data of a tkdnd menu content is saved as {some path...}

    :param paths: paths = tk.dnd event input is a big string divided through "{" and "}"
    :return: returns a clear list of paths
    """

    if "{" in paths:
        pathList = []
        keepWord = ""
        wordStart = False

        for letter in paths:
            if letter == "{":
                wordStart = True
            elif letter == "}":
                pathList.append(keepWord)
                keepWord = ""
                wordStart = False
            elif wordStart:
                keepWord = keepWord + letter
    else:
        pathList = [paths]

    print("\033[32m" "separateData:    DONE" "\033[0m")
    return pathList

# Bastian Lipka
# https://github.com/kirbs-btw
