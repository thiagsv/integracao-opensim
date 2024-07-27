import os
import datetime
import shutil

def processEspData(espDataFile):
    """
    Processes data from the ESP32 device.

    This function processes the raw data from the ESP32 device by applying a Kalman filter 
    and then converting the processed data into a .sto file structure. The resulting data 
    is saved in two locations: a timestamped file in the 'opensimData' directory in the user's 
    home directory and a fixed location 'data/imuData.sto'.

    Args:
    espDataFile (str): Path to the collected data

    Returns:
    None
    """

    processedFile = 'data/imuData.sto'

    with open(processedFile, 'w') as out_f:
        out_f.write('')
    
    createSTOStructure(processedFile)

    try:
        with open(espDataFile, 'r') as f:
            data = f.read()
            dataList = list(map(float, data.split(',')))
            filteredData = applyKalmanFilter(dataList)

            with open(processedFile, 'a') as out_f:
                out_f.write(','.join(map(str, filteredData)) + '\n')
            
            saveFile2User()
    except Exception as e:
        print(f'Error processing file: {e}')
        


def saveFile2User():
    """
    Saves data to a file in a specified location.

    Args:
    None
    
    Returns:
    None
    """

    path = os.path.expanduser('~') + '/opensimData/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    dateTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    path += '/data_' + dateTime + '.sto'

    try:
        shutil.copy('data/imuData.sto', path)
    except Exception as e:
        print(f'Error at saving data: {e}')

def createSTOStructure(espData):
    return espData

def applyKalmanFilter(espData):
    return espData