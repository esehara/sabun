            ___   _   ___  _ __ _  __
          ,' _/ .' \ / o.)/// // |/ /
         _\ `. / o // o \/ U // || / 
        /___,'/_n_//___,'\_,'/_/|_/  
              

What is SABUN ?
---------------
"Sabun" is Simple, Easy and Awesome TODO Task Manager. 

Discription
------------
It is most simple way to write TODO LIST in text file, and manage. but, Task managed by Text file for TODO, it is too easy to record task log.

Most people, in text file, writes One Line - One Task(why not?). and When task done, delete line.I think, record text file diff as task log !!

Example
----

I have TODO.txt.

        * buy egg
        * buy spam
        * spam spam spam

this is my task. oh, I buy egg now!! and one line "buy egg" delete.

        *buy spam
        *spam spam spam

when you delete line, sabun find your delete line and record it.

        2013-02-18 11:00:00 * buy egg

but, "spam spam spam" is not my task .. you want not to pick this fix,but "sabun" pick this fix and logging. ok, you can stop temporary and fix it. but using prefix "#" is better than "sabun" stop.

        *buy spam
        #spam spam spam

and save once. and delete.

        *buy spam

ok, "sabun" don't pick this fix.

Requirement
-----------
* Python 2.7 (or more?)

Setup
-----

clone this repository and do "python setup.py install" :)

Command
-------

        sabun WATCH_TODO_TEXT.txt OUTPUT_RECORD.txt

Option
------

* --color : colorize logging :).

License
-------

MIT License
