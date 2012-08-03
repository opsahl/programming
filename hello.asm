section .text
    global_start        ;must be decleared for linker

_start:                 ;tell linker entry point

    mov edx, len ; message length
    mov ecx, msg ; message to write
    mov ebx, 1   ; file descriptor (stdout)
    mov eax, 4   ; system call num (sys_write)
    int 0x80     ; call kernel

    mov eax, 1   ; system call num (sys_exit)
    int 0x80     ; call kernel

section .data

msg db      'Hello World!',0xa    ; our string
len equ     $ - msg               ; length of string
