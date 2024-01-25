import sys



def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  ##all the details about exception or error have store in exc_tb : line,error, so on
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message= "Error occur in python script name [{0}] line number [{1}] and error message is [{2}] ".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message
        
class CustomException(Exception):                           #inheriting the parent exception
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        # error details will track by sys


    def __str__(self):    
        return self.error_message
    '''
    whenever we raise the custom exception it will return the error message
    '''
        