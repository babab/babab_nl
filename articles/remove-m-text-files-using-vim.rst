These are instructions on how to get rid of ^M in text-files with the use of Vim.

In Linux/Unix by pressing::

   :%s/^M//g

Note that ^M is inserted by pressing the keystoke **Ctrl+V Ctrl+M**. This is
because Ctrl+V will give the escaped form of the key pressed after this.
You’ll see that when you press Ctrl+V <RETURN> it is actually the
same. So yes, you can insert return/enter by pressing Ctrl+M in Unix.

In the Windows version of Vim the instruction will not work but you can
accomplish the same by using::

   :%s/\t//g

The substitute command
----------------------

- The ``%`` means that this aplies on all the lines in the file.
- The ``s/old/new/`` is a substitute command where old gets replaced by new.
- The ``g`` on the end means to this mutliple times if found more then once
  in the same line.

For more info, you can use the help function of Vim by entering::

   :help substitute
