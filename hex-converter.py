import sys 		#sys module for read user inputs

#This function Converts Byte block to Hex
# data type of byte_block parameter is bytes -> b'text_here'
def convert_to_hex(byte_block):
    hex = [f"{x:02x}" for x in byte_block] #Get each byte and convert to hex
    hex_out = []
    for x in range(0, len(hex), 2):
        hex_out.append("".join(hex[x:x+2])) #Converted Hex chars like ['1a12', '23ab',....]
    return(" ".join(hex_out)) #convert hex_out list to string

#This function checks whether the character printable or not
def hex_checker(data):
    str_array = ""
    for x in data:
        if(x > 31 and x != 127): #0-32 characters are allocated as device control characters
            str_array = str_array + chr(x)
        else:
            str_array = str_array + "."
    return (str_array)


#----------------Program Starts from here--------------------------------------------------

try:
    file_name = sys.argv[1] 	#Read the command line arguments
    with open(file_name, "rb") as file:
        count = 0
        data = file.read(16) #Read the file as 16 byte width blocks
        while (data):
            if(len(data) < 16): # Fill the byte block(data) to exactly 16 byte width
                data = data + ((16 -len(data)) * b' ')
            print( f"{(count*16):08x}  {convert_to_hex(data)}  {hex_checker(data)}")
            data = file.read(16)
            count+=1

except IndexError as index_err:
    print("File not Specified!")
except FileNotFoundError as file_not_found:
    print("File not Found!")


