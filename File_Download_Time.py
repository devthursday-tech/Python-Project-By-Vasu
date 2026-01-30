File_Size_GB = float(input('Enter Size Of File:'))
Internet_Speed = int(input('Enter MB/s Speed Of File Storing :'))

GB_INTO_MB = File_Size_GB * 1000
print('Approximate Download Time(Seconds) is', File_Size_GB/Internet_Speed)