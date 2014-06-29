defunct
=======

A interpreted functional programming language, highly inspired (if not shamelessly plagiarised) by LISP


Example
-------
It's a WIP I'm playing with in my spare time, so it does not aim to be a complete programming language.

So far, it can run simple programs like


```
(do 
    (define sum_1 (lambda (x) 
        (+ 1 x)
     )) 

     %env 

     (sum_1 100)
)
```