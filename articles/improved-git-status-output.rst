The output of git status is pretty great. It shows if you are in sync
with the current tracked remote branch and the staged files for your
next commit. It's also is a big help if you are new to Git, since it
practically tells you what to do next and how to do it.

Here is an example of the output of git status in my dotfiles repository:

.. code-block:: console

   $ git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

      modified:   bin/ctb

   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)
     (commit or discard the untracked or modified content in submodules)

      modified:   .gitignore_global
      modified:   .vim/bundle/VimOrganizer (untracked content)
      modified:   .vim/bundle/conque-term (untracked content)
      modified:   .vim/bundle/utl (untracked content)
      modified:   .vim/bundle/vim-MagicKey (new commits)
      modified:   .xinitrc
      modified:   bin/ctb


If you get used to working with git you want something a little less
verbose, so you try out ``git status --short`` and maybe even set it as
a git or shell command alias. The output is indeed short and also does a
better job in indicating if you have both staged and unstaged lines in a
single file.

For the same dotfiles repository, it will look like this:

.. code-block:: console

   $ git status --short
    M .gitignore_global
    M .vim/bundle/VimOrganizer
    M .vim/bundle/conque-term
    M .vim/bundle/utl
    M .vim/bundle/vim-MagicKey
    M .xinitrc
   MM bin/ctb

The only thing that is missing from this output is the tracked remote
branch status. I wanna have both, so I decided to create this very
simple function:

.. code-block:: shell

   kk () {
       git status | head -2 | tail -1
       git status --short
   }

Now, the output will show the tracked remote branch and still be short:

.. code-block:: console

   $ kk
   Your branch is up-to-date with 'origin/master'.
    M .gitignore_global
    M .vim/bundle/VimOrganizer
    M .vim/bundle/conque-term
    M .vim/bundle/utl
    M .vim/bundle/vim-MagicKey
    M .xinitrc
   MM bin/ctb


