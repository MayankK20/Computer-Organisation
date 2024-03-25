
instruction_R = {0110011}  #use if else inside the R type function... 

instruction_I = { 0000011 : {010 : 'lw'},  #may not use these values associated with keys. keys is enough.
                 0010011 : {000 : 'addi', 011 : 'sltiu'},
                 1100111 : {000 : 'jalr'} }

instruction_S = { 0100011 : {010 : 'sw'} }

instruction_B = { 1100011 : {000 : 'beq', 001 : 'bne', 100 : 'blt', 101 : 'bge', 110 : 'bltu', 111 : 'bgeu'} }

instruction_U = { 0110111 : 'lui',
                 0010111 : 'auipc' }

instruction_J = { 1101111 : 'jal'}

instruction_BONUS = { }
