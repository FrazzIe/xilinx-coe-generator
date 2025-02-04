from shutil import copyfile
import configparser

# Loading available config
config = configparser.ConfigParser()
config.read('config.ini')

if 'USER' in config:
    allSetting = config['USER']
    OUTPUT_FILE = allSetting.get('OUTPUT_FILE')

    OFFSET_VALUE = allSetting.getint('OFFSET_VALUE')    
    BLOCK_WIDTH = allSetting.getint('BLOCK_WIDTH')
    BLOCK_LENGTH = allSetting.getint('BLOCK_LENGTH')

    ACCEPT_RADIX = allSetting.get('ACCEPT_RADIX')
    MAX_SIZE = allSetting.getint('MAX_SIZE')
    NUM_DATA_EACH = allSetting.getint('NUM_DATA_EACH')
else: 
    print('Error: Please make sure that config.ini is accessible and both [USER] and [DEFAULT] sections exist in it.. Exiting..')
    exit()

## end of setting

try:
    with open(OUTPUT_FILE) as fp:
        pass
    copyfile(OUTPUT_FILE, '{}.bak'.format(OUTPUT_FILE))
except:
    pass

try:
    fp = open(OUTPUT_FILE, 'w')
except IOError:
    print("Error: Cannot open the OUTPUT_FILE for write.. exiting..")
    exit()

MAX_WORD = 2**32-1
MIN_WORD = MAX_WORD - (MAX_SIZE * OFFSET_VALUE)
print('Creating BRAM addresses from {min:x} to {max:x} (size: {size}KiB)'.format(min = MIN_WORD, max = MAX_WORD, size = (MAX_SIZE * 32 / 8 / 1024) ))

addr = 0
wordArray = [None] * MAX_SIZE
wordArray[addr] = MIN_WORD

while addr < (MAX_SIZE-1):
    wordArray[addr+1] = wordArray[addr] + OFFSET_VALUE
    if (addr+1) % (MAX_SIZE / 16) == 0:
        print("\r[ {progress:.2f}% ] — {addr}:{value:x}".format(progress = (addr+1) / (MAX_SIZE-1) * 100, addr = addr+1, value = wordArray[addr+1]))
    addr += 1

fp.write(
"""; This coe file is generated using third party script 
; maintained at the github repository
; By using this script, you are considered
; as accepted the disclaimer and MIT license specified on
; https://github.com/kooltzh/xilinx-coe-generator
; https://github.com/frazzIe/xilinx-coe-generator

""")
fp.write('memory_initialization_radix={};\n'.format(ACCEPT_RADIX))
fp.write('memory_initialization_vector=\n\n')

for idx, word in enumerate(wordArray):
    if idx == MAX_SIZE - 1:
        fp.write("{word:x}\n".format(word = word))
        break

    if (idx + 1) % BLOCK_WIDTH == 0:
        fp.write("{word:x},\n".format(word = word))
    else: 
        fp.write("{word:x},".format(word = word))

    if ( (idx + 1) / BLOCK_WIDTH ) % BLOCK_LENGTH == 0:
        fp.write("\n")
fp.write(";")
fp.close()