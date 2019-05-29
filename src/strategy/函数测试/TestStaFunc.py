import talib


def initialize(context): 
    SetBarInterval('SHFE|F|CU|1907', 'M',1, 100)


def handle_data(context):
    close = Close()
    ret, sma = SMA(close, 12, 2)
    LogInfo("len:%d, sma:%f, cl:%f\n" %(len(close), sma, close[-1]))
