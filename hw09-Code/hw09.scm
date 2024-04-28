;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems
(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr)
   (filter
   (lambda(,var) ,filter-expr) ,lst))
)
(define (sub-num1 lst) (map (lambda (x) (- x 1)) lst))
(define (make-change total biggest)
  (cond ((= total 0) (cons nil nil))
    ((= total 1) (cons (cons 1 nil) nil))
    ((= biggest 1) (list-of (append '(1) y) for y in (make-change (- total 1) 1) if #t))
    (else (begin (if (> biggest total)
                   (define biggest total))
                 (append (list-of (append `(,biggest) x) for x in (make-change (- total biggest) biggest) if #t) (make-change total (- biggest 1)))
            )
      )
    )
  )

(define (find n lst)
  (define (finds-nests lsts ans n)
    (if (= (car lsts) n)
      ans
      (finds-nests (cdr lsts) (+ 1 ans) n)))
    (finds-nests lst 0 n)
)


(define (find-nest n sym)
  (define (is-equal lst ans n)
    (cond
      ((null? lst) nil)
      ((number? lst)
      (if (= n lst)
        ans
        nil))
      (else (search lst ans n))))
  (define (search lst ans n)
    (let
      ((first-ele (is-equal (car lst) `(car ,ans) n))
         (rest-ele (is-equal (cdr lst) `(cdr ,ans) n)))
      (if (null? first-ele)
        rest-ele
        first-ele)))
  (search (eval sym) sym n)
)


(define-macro (my/or operands)
  (cond
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)))
         (if t
           t
           (my/or ,(cdr operands))))))
)
(define (remained args indices)
  (cond
    ((null? indices) args)
    ((= 0 (car indices))
      (remained (cdr args) (sub-num1 (cdr indices)))
      )
    (else (cons (car args) (remained (cdr args) (sub-num1 indices))))
    )
  )
(define (substitute args vals indices)
  (cond
    ((null? indices) args)
    ((= 0 (car indices)) (cons (car vals) (substitute (cdr args) (cdr vals) (sub-num1 (cdr indices)))))
    (else (cons (car args) (substitute (cdr args) vals (sub-num1 indices))))
    ))
(define-macro (k-curry fn args vals indices)
  (let ((need-arg (remained args indices))
         (new-arg (substitute args vals indices)))
    `(lambda ,need-arg cons(,fn ,@new-arg)))
)


(define-macro (let* bindings expr)
  (cond ((null? bindings) `(let () ,expr))
    (else `(let ((,(car (car bindings)) ,(car (cdr (car bindings))))) (let* ,(cdr bindings) ,expr))))
)

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)