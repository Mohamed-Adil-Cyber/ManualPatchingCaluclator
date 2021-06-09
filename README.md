# ManualPatchingCaluclator
Simple calculator that calculates how relative address changes to actual hex address

First input is the virtual address of the byte you want to find the offset for

Second is the image base found in the data section of the exe

Third is the relative virtual address of the exe file which can be found in the PE header

Fourth is the pointer to the raw data of the exe found in the data section of the PE header
