from Message import Message
from Report import Report

class Test:
    '''
    This class determines the order in which the checks are executed.
    As a rule, it receives a "parameter" with a list of the checks to be executed and a "check_map"
    indicating where the code for the respective tests is located.
    The test is then applied to the "message".
    '''

    def __init__(self, message: Message, parameter: dict, check_map: dict):
        raise NotImplementedError

    def run(self) -> Report:
        raise NotImplementedError
