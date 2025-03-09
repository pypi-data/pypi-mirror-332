import requests
import urllib3
import pprint
import warnings
from datetime import datetime, timedelta
import json
import random

class api_arsenal():
    """
    Use 'requests' Library in your requests with help our arsenal, then push your responses into the array to derive the statistics.
    
    Done By: Abdullah Al-Shehri
    """
    
    def __init__(self, disable_warnings: bool = True): # in case of testing 
        """Intializes needed variables and disables warnings and deprecation messages by default."""
        
        self.test_username = self.get_test_username()
        self.test_password = self.get_test_password()
        self.all_responses_arr = []

        # stats variables
        self.total_elapsed: timedelta = timedelta() # increase it with each response pushed in the array
        self.non_successful_response_counter = 0
        self.successful_response_counter = 0
        self.min_el: dict
        self.max_el: dict
        self.responses_arr_len: int = 0
        self.avg_elapsed: int = 0
        self.delimeter =  '//###//'
        self.encryption_key = 2
        
        if disable_warnings:
            self.set_up()
        
    def __is_empty(self, arr:list) -> bool:
        """Returns True if the List empty"""
        
        if len(arr) == 0:
            print("-|- The Array Requested is Empty.")
            return True
        else:
            return False
    
    def __calc_stats(self) -> None:
        """Performs the calculation needed"""
        
        arr = self.all_responses_arr
        arr.sort(key=lambda x:x['response'].elapsed)
                
        try:
            self.min_el = arr[0]
            self.max_el = arr[self.responses_arr_len - 1]
            self.avg_elapsed = self.total_elapsed / self.responses_arr_len
        except Exception as e:
            print(f'--- {e}')
    
    def __response_brief_format(self, response:requests.Response) -> None:
        """Prints the format which will be applied to all request."""     

        print(f'Endpoint                : {response['name']}')
        print(f'Status Code             : [{response['response'].status_code}]')
        print(f'Elapsed                 : {response['response'].elapsed}')
    
    def __log_history_header(self, title: str, length: int):
        print(f'{title} History ({length})\nSorted By Date in ASC.')
        print('--------------------------------------------------\n')
    
    def __encoding(self, text: str) -> str:
        new_str = ''
        
        for i in range(len(text)):
            asc_code = ord(text[i])
            new_str += chr((asc_code + self.encryption_key))
            
        return new_str
    
    def __decoding(self, text: str) -> str:
        new_str = ''
        
        for i in range(len(text)):
            asc_code = ord(text[i])
            new_str += chr((asc_code - self.encryption_key))

        return new_str
    
    def set_up(self) -> None:
        urllib3.disable_warnings() # disabling Connection warnings to beautify output.
        warnings.filterwarnings("ignore", category = DeprecationWarning) # disabling DeprecationWarning to beautify output.
    
    def get_random_letter(self, Uppercase:bool=False) -> chr:
        if Uppercase == True:
            ascii_ranges = list(range(65, 91))
        else:
            ascii_ranges =  list(range(97, 123))
            
        ascii_code = random.choice(ascii_ranges)
        
        return chr(ascii_code)
    
    def get_random_letters(self, number_of_letters:int) -> str:
        str = self.get_random_letter(True)
        for x in range(number_of_letters):
            str += self.get_random_letter(False)
        return str

    def get_random_symbol(self) -> str:
        arr = ['@', '#', '$', '*']
        return str(arr[random.randint(0,len(arr) - 1)])

    def get_random_numbers(self, number_of_numbers:int=5) -> str:
        number_str = ''
        for x in range(number_of_numbers):
            number_str += str(random.randrange(0,9))
        return number_str

    def get_test_username(self, username_length=5) -> str:
        return self.get_random_letters(username_length) + str(random.randint(0,9)) + str(random.randint(0,9))

    def get_test_password(self) -> str:
        return (self.get_random_letter(True) + self.get_random_letter(False) + self.get_random_symbol() + self.get_random_numbers())
    
    def reset_credintials(self) -> None:
        """Re-assigns testing credintials (username and password)."""
        self.test_username = self.get_test_username()
        self.test_password = self.get_test_password()

    def log_user_credintials_in_file(self, filename:str='Users_Logs_File_Encoding.txt', comments:str='No Comments') -> None:
        """
        Adds a line contains :
            - Username
            - Password
            - Current date and time
            - Comment (could be your name)
        separated by the delimeter.
        
        Signature   : Username//###//Password//###//Date and Time now//###//Comments
        
        Example     : Uveofj36//###//Mu#85710//###//2024-07-18 13:53:14.822588//###//Abdullah Al-Shehri
        """
        
        joined_str = self.test_username + self.delimeter
        joined_str += self.test_password + self.delimeter
        joined_str += str(datetime.now()) + self.delimeter
        joined_str += comments
        
        joined_str = self.__encoding(joined_str)

        file = open(filename, 'a')
        file.write(joined_str + '\n')
        file.close()

    def log_stats_in_file(self, filename:str='Stats_Logs_File.txt', comments:str='No Comments') -> None:
        """
        Adds a line contains :
            - Total elapsed
            - Number of successful endpoints
            - Number of non-successful endpoints
            - Name, reponse elapsed, and status code of minimum elapsed. 
            - Name, reponse elapsed, and status code of maximum elapsed. 
            - Average elapsed. 
            - Current date and time
            - Comment (could be your name)
        separated by the delimeter.
        
        Signature   : Total elapsed//###//Successful endpoints//###//Non-successful endpoints//###//Min-name|Min-elapsed|Min-status code//###//Max-name|Max-elapsed|Max-status code//###//Average elapsed//###//Date and Time now//###//Comments
        
        Example     : 0:00:02.818194//###//2//###//0//###//Login|0:00:00.688345|200//###//Main Page|0:00:02.129849|200//###//0:00:01.409097//###//2024-07-22 14:55:43.417038//###//Abdullah Al-Shehri
        """

        joined_str = str(self.total_elapsed) + self.delimeter
        joined_str += str(self.successful_response_counter) + self.delimeter
        joined_str += str(self.non_successful_response_counter) + self.delimeter
        joined_str += self.min_el['name'] + "|" + str(self.min_el['response'].elapsed) + "|" + str(self.min_el['response'].status_code) + self.delimeter
        joined_str += self.max_el['name'] + "|" + str(self.max_el['response'].elapsed) + "|" + str(self.max_el['response'].status_code) + self.delimeter
        joined_str += str(self.avg_elapsed) + self.delimeter
        joined_str += str(datetime.now()) + self.delimeter
        joined_str += comments

        file = open(filename, 'a')
        file.write(joined_str + '\n')
        file.close()

    def push_response(self, response:requests.Response, endpoint_name:str) -> None:
        """Pushs response into the responses array."""
        
        obj = {
            'name': endpoint_name,
            'response': response
        }
        
        if self.is_response_successful(response):
            self.successful_response_counter += 1
        else:
            self.non_successful_response_counter += 1
            
        self.all_responses_arr.append(obj) # anyway we have to add it in the all responses
        self.responses_arr_len += 1
        self.total_elapsed += response.elapsed # adding total elapsed 

    def is_response_successful(self, response:requests.Response) -> bool:
        """Retrurn True if response status code begin with 2."""
        
        if (response.status_code / 100 == 2): # Any Success message begins with 2 will satisfy the condition
            return True 
        else:
            return False

    def print_detailed(self, response:requests.Response) -> None:
        """Prints response information with the response body."""
        
        self.__response_brief_format(response)
        print(f'Response                : ')  
        print('\n')
        try:
            pprint.pprint(response['response'].json())
        except json.JSONDecodeError as e:
            print("Request Succeeded, JSON couldn't be parsed.")
        except Exception as e:
            print(e)
        print('\n')
        print('-------------------------------------')

    def print_brief(self, response:requests.Response) -> None:
        """Prints response information without the response body."""

        self.__response_brief_format(response)
        print('-------------------------------------')

    def print_all_detailed(self) -> None:
        """Prints all responses information with the response body."""

        if self.__is_empty(self.all_responses_arr) == True:
            return
        
        for response_object in self.all_responses_arr:
            self.print_detailed(response_object)

    def print_successful_detailed_only(self) -> None:
        """Prints all responses information, only successful responses with response body."""
        
        if self.__is_empty(self.all_responses_arr) == True:
            return
        
        for response_object in self.all_responses_arr:
            if self.is_response_successful(response_object['response']):
                self.print_detailed(response_object)
            else:
                self.print_brief(response_object)

    def print_non_successful_detailed_only(self) -> None:
        """Prints all responses information, only non-successful responses with response body."""
        
        if self.__is_empty(self.all_responses_arr) == True:
            return
        
        for response_object in self.all_responses_arr:
            if self.is_response_successful(response_object['response']):
                self.print_brief(response_object)
            else:
                self.print_detailed(response_object)
                
    def print_all_brief(self) -> None:
        """Prints all responses information without the response body."""
        
        if self.__is_empty(self.all_responses_arr) == True:
            return
        
        for response_object in self.all_responses_arr:
            self.print_brief(response_object)

    def print_stats(self) -> None:
        """Prints statistics derived from the endpoints pushed to the array."""
        
        self.__calc_stats()

        print('-------------------------------------')
        print(f'Total Elapsed               : {self.total_elapsed}')
        print(f'Total Endpoints             : {self.responses_arr_len}')
        print(f'Successful Endpoints        : {self.successful_response_counter}')
        print(f'Non-Successful Endpoints    : {self.non_successful_response_counter}')
        print(f'Max                         : {self.max_el['name']} ({self.max_el['response'].elapsed})')
        print(f'Min                         : {self.min_el['name']} ({self.min_el['response'].elapsed})')
        print(f'Avg                         : {self.avg_elapsed}')

    def print_user_credintials_logs_history(self, filename: str = 'Users_Logs_File_Encoding.txt') -> None:
        file = open(filename, 'r') # read mode
        text = file.read()
        
        text_splitted = text.split('\n')
        
                
        if len(text_splitted) > 1: # in case of only one line
            text_splitted.pop() # removing last array element [''] 
        
        decoded_lines = []
        
        for line in text_splitted:
            decoded_lines.append(self.__decoding(line))            
        
        
        self.__log_history_header('User Credintials', len(decoded_lines))
        
        for line in decoded_lines:
            line_splatted = line.split(self.delimeter)    
            print(f'Username    : {line_splatted[0]}')
            print(f'Password    : {line_splatted[1]}')
            print(f'Datetime    : {line_splatted[2]}')
            print(f'Comments    : {line_splatted[3]}')
            print('---------------------------------')
    
    def print_stats_logs_history(self, filename: str = 'Stats_Logs_File.txt'):         
        file = open(filename, 'r') # read mode
        lines_arr = file.read().split('\n')
        lines_arr.pop() # removing last array element ['']
        
        self.__log_history_header('Stats', len(lines_arr))
                
        for line in lines_arr:
            line_splatted = line.split(self.delimeter)            
            
            min_el = line_splatted[3].split('|')
            max_el = line_splatted[4].split('|')
            
            
            print(f'Total Elapsed                       : {line_splatted[0]}')
            print(f'N. of Successful Endpoints          : {line_splatted[1]}')
            print(f'N. of Non-Successful Endpoints      : {line_splatted[2]}')
            print(f'Minimum Elapsed Data')
            print(f'        Name                        : {min_el[0]}')
            print(f'        Elapsed                     : {min_el[1]}')
            print(f'        Status Code                 : {min_el[2]}')
            print(f'Maximum Elapsed Data')
            print(f'        Name                        : {max_el[0]}')
            print(f'        Elapsed                     : {max_el[1]}')
            print(f'        Status Code                 : {max_el[2]}')
            print(f'Average Elapsed                     : {line_splatted[5]}')
            print(f'Date and Time                       : {line_splatted[6]}')
            print(f'Comments                            : {line_splatted[7]}')
            print('---------------------------------')     
        

# The following line differentiate if this file is a package/module (not intended to run) 
# or an basic file (intended to run) 
if __name__ == '__main__':


    
    my_utility = api_utility()
    my_utility.set_up()