;;Declare external procedure {winapi}

extern ExitProcess
extern AllocConsole 
extern FreeConsole 
extern SetConsoleTitleA 
extern Sleep 
extern GetStdHandle
extern ReadFile
extern WriteFile

import ExitProcess		kernel32.dll
import AllocConsole		kernel32.dll 
import FreeConsole		kernel32.dll 
import SetConsoleTitleA	kernel32.dll 
import Sleep 			kernel32.dll
import GetStdHandle 	kernel32.dll
import ReadFile		kernel32.dll
import WriteFile		kernel32.dll


SEGMENT .DATA use32
Title   	     db "TUGAS MIKROPROSESOR DANIEL",0 

msg0 		db "Daniel Suranta S / 18-424185-PA-18290",0
msg0_len 	     dd $-msg0

msg1 		db 13,10,"TULIS TEXT (Selesai? Enter)         : ",0
msg1_len 	     dd $-msg1

msg2 		db 13,10,"UBAH KE HURUF BESAR : ",0
msg2_len 	     dd $-msg2 

msg3 		db 13,10,"DIBALIK MENJADI : ",0
msg3_len 	     dd $-msg3

msg4 		db 13,10,"JUMLAH CHARACTER : ",0
msg4_len 	     dd $-msg4

msg5 		db 13,10,"JUMLAH KATA : ",0
msg5_len 	     dd $-msg5

msg6 		db 13,10,"TERIMA KASIH",0
msg6_len 	     dd $-msg6

buff		resb 255
buff_len	dd 255

conv      resb 255

SEGMENT .BSS  use32
hStdOut		resd 1 
hStdIn		resd 1 
nBytes		resd 1
iBytes		resd 1

SEGMENT .CODE use32
..start:

call [AllocConsole] 
	
push dword Title 
call [SetConsoleTitleA] 
	
push dword -11 			;; STD_OUTPUT_HANDLE = -11.
call [GetStdHandle] 
mov dword [hStdOut], eax 

push dword -10			;; STD_INPUT_HANDLE = -10 
call [GetStdHandle] 
mov dword [hStdIn], eax 

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [msg0_len] 		;; parameter ke 3 panjang string
push dword msg0			;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 		

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [msg1_len] 		;; parameter ke 3 panjang string
push dword msg1			;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 	

push dword 0 			;; parameter ke 5 dari ReadFile() adalah 0 
push dword iBytes 		;; parameter ke 4 jumlah byte yg sesungguhnya terbaca
push dword [buff_len] 	;; parameter ke 3 panjang buffer yg disediakan
push dword buff 		;; parameter ke 2 buffer untuk menyimpan string yg dibaca 
push dword [hStdIn] 	;; parameter ke 1 handle stdin
call [ReadFile] 			

MOV ECX, [iBytes]		;; iBytes menyimpan panjang string yang dituliskan, termasuk Enter (2 bytes: 13,10)

cmp dword[iBytes], 2
je EXIT

SUB ECX, 2

XOR EAX, EAX
XOR EBX, EBX
MOV EBX, dword buff
MOV EAX, dword conv

TOBACK:
     inc EAX
     cmp EAX, ECX
     jle TOBACK

UPPER:
     cmp byte [EBX], 97
     jl NOTWORD
          cmp byte [EBX], 122
          jg NOTWORD
          sub byte [EBX],32
     NOTWORD:
          inc EBX
          dec EAX
     loop UPPER

ADD EBX,2
MOV byte [EBX],0		;; text yang akan ditampilkan diakhiri dengan 0

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [msg2_len] 	;; parameter ke 3 panjang string
push dword msg2		;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 				

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [iBytes] 	;; parameter ke 3 panjang string
push dword buff		;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 	

CONVERT:

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [msg3_len] 	;; parameter ke 3 panjang string
push dword msg3		;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 				

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [iBytes] 	;; parameter ke 3 panjang string
push dword conv		;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 					

push dword 0 			;; parameter ke 5 dari WriteFile() adalah 0 
push dword nBytes		;; parameter ke 4 jumlah byte yg sesungguhnya tertulis
push dword [msg6_len] 	;; parameter ke 3 panjang string
push dword msg6		;; parameter ke 2 string yang akan ditampilkan
push dword [hStdOut] 	;; parameter ke 1 handle stdout
call [WriteFile] 			
  
jmp ..start  

EXIT:
call [FreeConsole] 
	
push 0
call [ExitProcess]
leave
	
RET