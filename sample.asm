section .data
	a dd 10,20,   3,4
	b dq 3, 5, 10
	msg db "hello there",10,0
section .bss
	n resd 1
    c resq 2
    d resb 1
section .text
    global main

main:
    mov eax, 10
    mov ebx, 25
    add eax, ebx
	mov eax, ebx
	mov eax, eax
	sub eax, ecx
	add eax, 10
	add ebx, 10
	sub ebx, 10
	sub edi, 20
	sub eax, 30
	mov eax, a
	mov ecx, a
	mov ebx, a
	add eax, ecx
