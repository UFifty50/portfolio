.section .text
.global main
.arm

// The program starts here in (32-bit) ARM mode.
main:
    mov r0, #1               @ STDOUT
    adr r1, label            @ R1 = address of string
    mov r2, #5               @ R2 = size of string
    mov r7, #4               @ R7 = syscall number for 'write'
    svc #0                   @ invoke syscall
_exit:
    mov r7, #1               @ R7 = syscall number for 'exit'
    svc #0                   @ invoke syscall
label:
.string "fox\n"
