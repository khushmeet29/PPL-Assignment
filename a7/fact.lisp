(princ "Factorial without using recursion")
(terpri)

;Factorial without using recursion
(princ "Enter Number: ")
(setq no (read))
(setq fact 1)
(defun facto(n)
    ( loop for x from 2 to n
           do(setq fact (* x fact))
           )

    )
(facto no)
(format t "~%Factorial ~d is: ~d" no fact)
  

