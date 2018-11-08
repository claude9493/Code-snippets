# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:38:27 2018

@author: Claude
"""

"""
--------------------------------- Background ---------------------------------
When I'm coding, comments are always needed. And elegent comments are what
we like. Especially such kind of (sub)title is always used:
   # ------------------- Some Words -------------------
But how to make it symmetric and all titles have same length?
I decided to write a script to  generate such kind of title...
    
----------------------------------- Input -----------------------------------
    title:     what is put in the center of dash line
    length:    total length of this line, (defalut 60)
    clipboard: whether to pass the result to clipboard (default true)
    
---------------------------------- Features ----------------------------------
    1. Length of comment is adjustable.
    2. Optional function: the program could pass the generated comment into
       clipboard. (Howerer, till now, it's only support windows system)

----------------------------------- To-Do -----------------------------------
    1. Extend the clipboard features to other platforms
    
"""

#%%
def comment(title, length = 60, clipboard = True):
    import os
    import win32clipboard
    import win32con
    import warnings

    title_len = len(title)
    
    if title_len > length:
        raise ValueError("Title is too long, please pass a larger 'length'.")
    if os.name is not 'nt' and clipboard is True:
        warnings.warn("The function of passing the results to the clipboard is \
                      only available on Windows system till now")
        clipboard = False
        
    dash_half_len = int((length - title_len) / 2 - 1)
    comment = '-'*dash_half_len+' '+title+' '+'-'*dash_half_len
    print(comment)
    if clipboard is True:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, str(comment))
        win32clipboard.CloseClipboard()
    


    
