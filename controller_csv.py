from csv_utils.csv_utils import CsvMetatraderAdapter, CsvInvestingAdapter

class ControllerCSV:
    __analyzer1 = None

    def __init__(self):
        pass
        # self.__analyzer1 = Analyzer1()

    # def get_data(self):
    #     """
    #     UI data format

    #     const data = [
    #         { time: '2022-01-01', open: 50, high: 60, low: 40, close: 55 },
    #         { time: '2022-01-02', open: 55, high: 65, low: 45, close: 60 },
    #         { time: '2022-01-03', open: 60, high: 70, low: 50, close: 65 },
    #         // ...
    #     ];


    #     Data paths
    #     D:\\documents storage\\repositories\\financials\\market-analysis\\server\\data\\EURUSD_M5_2021-10-27_2023-02-27.csv
    #     D:\\documents storage\\repositories\\sandboxes\\markets\\server\\data\\BTC_USD data.csv
    #     """

    #     data = self.get_metatrader_data("D:\\documents storage\\repositories\\financials\\market-analysis\\server\\data\\EURUSD_M5_2021-10-27_2023-02-27.csv")
    #     data = self.analyze_data(data)
    #     markers = self.__analyzer1.open_positions(data)
    #     data = self.convert_to_ui_format(data)
    #     data['markers'] = markers
    #     return data

    def get_metatrader_data(self, path):
        data_adapter = CsvMetatraderAdapter()
        data_adapter.set_path(path)
        data_adapter.read_data()
        return data_adapter.get_data_base_format()
    
    def get_investing_data(self, path):
        data_adapter = CsvInvestingAdapter()
        data_adapter.set_path(path)
        data_adapter.read_data()
        return data_adapter.get