# Xilinx RAM COE Generator

## Overview
This third party python script with no dependency other than native python package is used to generate Xilinx *.coe files for RAM data initializing

Xilinx RAM COE files aka coefficient files is used to initiate the data associated with their addresses inside Block RAM or other types of RAM.

The reference for Xilinx *.coe files can be found here at [COE File Syntax](https://www.xilinx.com/support/documentation/sw_manuals/xilinx11/cgn_r_coe_file_syntax.htm) on Xilinx support website.

## Using it
* Clone or download the repository
* Update the config.ini files
* Write your own input file using the syntax specified at the following section
* run `python xilinx-coe-generator.py`

## Available setting in config.ini

Default setting values is defined in the `[default]` section, user can overwrite the setting in `[user]` section
```ini
; value in USER section overwrite the default config value
[USER]

; The value in DEFAULT section shall be left untouched
[DEFAULT]
; The file name for output coe file
OUTPUT_FILE = output/output.coe

; the maximum range for each bit, 16 for hex
ACCEPT_RADIX = 16
; maximum size of the targetted RAM
MAX_SIZE = 4096
; number of data in each line of coe output, won't affect Xilinx RAM but affect our readability
BLOCK_WIDTH = 4
; number of data between empty line, won't affect Xilinx RAM but affect our readability
BLOCK_LENGTH = 16
; number to offset between words
OFFSET_VALUE=4
```

## Documentation
This python script is developed on python 3.7.1 on Ubuntu 18.04 LTS

## Disclaimer
Although the contributor of this project had made every attempt to ensure the best possible accuracy of this script. However, this python script is provided "as is" without warranty of any kind. The contributor does not take any responsibility or liability for the damage of lost caused by the usage of this script.

By using this script, you are hereby agree to the condition stated in the disclaimer section of this project.