import logging
import time

#Create logger
logging.basicConfig(filename = 'problems.log', level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    '''Return the contents of the file at 'path' and measure time required.'''
    start_time = time.time()
    try:
        f = open(path, mode='rb')
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info('Time required for {file} = {time}'.format(file=path,
                                                               time=dt))

data = read_file_timed(r'C:\Users\Dziugas\Downloads\Lena Headey - Aberdeen (English).avi')
# data = read_file_timed(r'C:\Users\Dziugas\Downloads\Software Wasteland - How the Application-Centric Mindset is Hobbling our Enterprises.pdf')