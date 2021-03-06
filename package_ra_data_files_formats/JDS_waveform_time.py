'''
'''
import numpy as np
from package_ra_data_files_formats.file_header_JDS import FileHeaderReaderJDS

def JDS_waveform_time(wf_data, clock_frequency, data_block_size):
    '''
    '''

    # The frequency meter of the receiver measures frequency roughly, and the clock
    # frequency comes from precision clock generator, so we round the measured frequency to
    # exact 66 or 33 MHz
    clock_frequency = int(clock_frequency/10**6) * 10**6

    second_of_day = np.uint32(wf_data[data_block_size - 2, :]) + np.power(2, 16) * np.uint32(wf_data[data_block_size - 1, :])
    phase_of_second = (np.uint32(wf_data[data_block_size - 4, :]) + np.power(2, 16) * np.uint32(wf_data[data_block_size - 3, :]))

    hour = np.floor(second_of_day[:] / 3600)
    minutes = np.floor(((second_of_day[:] / 3600) % 1) * 60)
    seconds = np.zeros(len(hour))
    for i in range (len(hour)):
        seconds[i] = second_of_day[i] - (hour[i] * 3600) - (minutes[i] * 60) + (np.float(phase_of_second[i]) / clock_frequency)

    timeline_block_str = ['' for x in range(len(hour))]
    for i in range (len(hour)):
        timeline_block_str[i] = ''.join("{:02.0f}".format(hour[i])) + ':' + ''.join("{:02.0f}".format(minutes[i])) + ':' + ''.join("{:02.6f}".format(seconds[i]))
    #for i in range (len(hour)):
    #    print(timeline_block_str[i], '    ', phase_of_second[i])

    return timeline_block_str





if __name__ == '__main__':

    fname = 'DATA/E251015_050029 - wf.jds'

    print('\n\n Parameters of the file: ')

    # *** Data file header read ***
    [df_filename, df_filesize, df_system_name, df_obs_place, df_description,
        CLCfrq, df_creation_timeUTC, Channel, ReceiverMode, Mode, Navr, TimeRes, fmin, fmax,
        df, frequency, FreqPointsNum, data_block_size] = FileHeaderReaderJDS(fname, 0, 1)

    #*******************************************************************************
    #                          R E A D I N G   D A T A                             *
    #*******************************************************************************
    no_of_spectra_to_average = 64

    print ('\n  *** Reading data from file *** \n')

    with open(fname, 'rb') as file:
        file.seek(1024)  # Jumping to 1024 byte from file beginning #+ (sizeOfChunk+8) * chunkSkip
        for av_sp in range (1):

            # Reading and reshaping all data with readers
            wf_data = np.fromfile(file, dtype='i2', count = no_of_spectra_to_average * data_block_size)
            wf_data = np.reshape(wf_data, [data_block_size, no_of_spectra_to_average], order='F')

            JDS_WF_time(wf_data, CLCfrq, data_block_size)
