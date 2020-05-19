(princ "Factorial using recursion")
(terpri)

;Factorial using recursion

(princ "Enter Number: ")
(setq num (read))
(setq numb num)
(defun factorial (num)
   (cond ((zerop num) 1)
      (t ( * num (factorial (- num 1))))
   )
)
(format t "~%Factorial ~d is: ~d" numb (factorial num))

