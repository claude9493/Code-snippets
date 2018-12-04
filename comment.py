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
    clipboard: whether to pass the result to clipboard (default False)

---------------------------------- Features ----------------------------------
    1. Length of comment is adjustable.
    2. Optional function: the program could pass the generated comment into
       clipboard.

----------------------------------- Updates -----------------------------------
    ----------------------------- 2018-12-04 -----------------------------
        1. Extend original fuction to a command script, thanks getopt module
        2. To use it in the command, put it in your working directory,
           and comment.py -h -t <title> -l <length> -c
        3. Meaning of these Options are in the usage function, or use
           comment.py -h
        4. Thanks to the module `pypoerclip`, it is possible now to pass the
           comment in several operating systems.

----------------------------------- To-Do -----------------------------------
    [v] 1. Extend the clipboard features to other platforms
    [ ] 2. Make this command script stay in command enviroment

"""

#%%
def comment(title, length = 60, clipboard = False):
    import os
    import sys
#    import win32clipboard
#    import win32con
    import warnings


    title_len = len(title)

    if title_len > length:
        raise ValueError("Title is too long, please pass a larger 'length'.")

    if clipboard:
        try: # Be careful for the nonexistence of pyperclip
            import pyperclip
        except ImportError:
            raise ImportError('The module `pyperclip` is not found, clipboard function not available.')
            clipboard = False

    dash_half_len = int((length - title_len) / 2 - 1)
    comment = '-'*dash_half_len+' '+title+' '+'-'*dash_half_len

    print(comment)
    if clipboard is True:
        pyperclip.copy(comment)

def usage():
    print('''
Usage:
    comment [option] ... [-t title | -l length]
Options and arguments:
    -h        : help
    -t title  : content in the comment
    -l length : length of the comment, which should be larger than title
    -c        : don't pass the comment to clipboard
        ''')


if __name__ == '__main__':

    try: # Be careful for the nonexistence of getopt
        import getopt
    except ImportError:
        raise ImportError('The module `getopt` is not found, it\'s not able to get the command arguments.')

    import sys
    tit = ''
    leng = 60
    cb = False
    whether_comment = False
    # If no title is given, do not call comment function.
    try:
      opts, args = getopt.getopt(sys.argv[1:],"ht:l:c",["help","title=","length=","clipboard="])
    except getopt.GetoptError:
        print('comment.py -h -t <"title"> -l <length> -c')
        sys.exit(2)
    if len(opts) == 0: # Case that no argument is given
        print('comment.py -h -t <"title"> -l <length> -c')
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            usage()
        if opt_name in ('-t', '--title'):
            whether_comment = True
            tit = opt_value
            continue
        if opt_name in ('-l', '--length'):
            leng = int(opt_value)
            continue
        if opt_name in ('-c', '--clipboard'):
            cb = True
    if whether_comment:
        comment(tit, leng, cb)
