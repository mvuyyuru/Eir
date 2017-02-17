import subprocess
import matplotlib.pyplot as plt
import numpy as np

def gen_input(input, params):
    input_file = open('./' + str(input), 'a')
    for i in params:
        input_file.write(i + '\n')

def run_MC(input):
    process = subprocess.Popen(['mcml.exe'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    commands = 'grid.grd',input
    process.communicate(bytes('\n'.join(commands) + '\n', 'UTF-8'))

min_abs = 1.0
max_abs = 2.0

curr_abs = 1.0
count = 0

#generate the input files
while curr_abs < max_abs:
    input_filename = 'input' + str(count) + '.mci'
    input_params = []
    input_params.append('1.0') #file version
    input_params.append('1')  #number of runs
    input_params.append('output' + str(count) + '.mco') #output file name
    input_params.append('1000000') #number of photons
    input_params.append('20E-4 20E-4') #dz, dr
    input_params.append('15 200 300') #No. of dz, dr & da.
    input_params.append('2') #no. of layers
    input_params.append('1.0') #n for medium above
    #the refractive index,  the  absorption coefficient (1/cm), the scattering coefficient  (1/cm), the  anisotropy  factor, and the  thickness  (cm).
    input_params.append('1.3 20 200 0.70 0.01') #layer 1
    input_params.append('1.4 ' + str(curr_abs) + ' 200 0.70 0.02') #layer 2
    input_params.append('1.0') #n for the medium below
    gen_input(input_filename, input_params)

    count += 1
    curr_abs += 0.5

count -= 1

#sequentially run MCML using input files
while count >= 0:
    print('input' + str(count) + '.mci')
    run_MC('input' + str(count) + '.mci')
    count -= 1