# check the excecute which one used in jal ??
# fix assembler errors
# NEW ERROR TYPE: x0 register CANNOT be changed!!
# Bonus instruction - halt: Possilbe simulation: PC += len(simulator)

#Assumption : all syntactical errors have been handled by assembler. So each line in the input file is a valid 32 bit instruction


#################################################################################################################

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

################################################################################################################

def bin_to_dec ( number ) :
  # number is a STRING
  # length is atleast 1
  
  dec = 0
  pow = 0

  length = len(number)
  if length == 0:
    return 0
    
  for i in range( length - 1, 0, -1 ):
    dec += (int(number[i]) * (2**pow) )
    pow += 1

  dec -= (int(number[0]) * (2**(length-1)) )

  return dec

####################################################################################################################

register = 
  { '00000': 0, '00001': 0, '00010': 0, '00011': 0, 
   '00100': 0, '00101': 0, '00110': 0, '00111': 0, 
   '01000': 0, '01001': 0, '01010': 0, '01011': 0, 
   '01100': 0, '01101': 0, '01110': 0, '01111': 0, 
   '10000': 0, '10001': 0, '10010': 0, '10011': 0, 
   '10100': 0, '10101': 0, '10110': 0, '10111': 0, 
   '11000': 0, '11001': 0, '11010': 0, '11011': 0, 
   '11100': 0, '11101': 0, '11110': 0, '11111': 0 }
  
 # to get value stored in register from its binary. value is in DECIMAL

register_name = { } # to decode the register name from its binary

memory = { } # to get content of memory from its binary

        
  


      
      
        
