import collections
import os
import datetime

'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------
def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """
    if start_time <= end_time and 0<start_time<=23 and 0<end_time<=23:
        if date in calendar.keys():
            calendar[date].insert(0,{"start": start_time, "end": end_time, "title": title})
            return True
        else:
            calendar[date] = [{"start": start_time, "end": end_time, "title": title}]
        return True
    else:
        return False
def save_calendar(calendar):
    my_Output = ''
    nKeys = list(calendar.keys())
    iterCount = len(nKeys)
    for s in range(iterCount):
        nKey = nKeys[len(nKeys)-s-1]
        nEvent = calendar.get(nKey)
        TiList=[]
        for v in nEvent:
            hh = int(v["start"])
            TiList.insert(0,hh)
        TiList.sort()
        my_Output += nKey + ":"
        for first in TiList:
            for ev in nEvent:
                q = ev.get("start")
                if first == q:
                    if len(str(first))!=2:
                        first = "0" + str(first)
                    my_Output += str(first) + "-"
                    w = ev.get("end")
                    w = str(w)
                    if len(w) !=2:
                        second = "0" + w + " "
                    else:
                        second = str(ev.get("end")) + " "
                    my_Output += second
                    third = ev.get("title")
                    my_Output += third + "\t"
        my_Output =my_Output[:-1] + "\n"
    f = open('calendar.txt','w')
    f.write(my_Output)
    f.close()
    return os.path.exists('calendar.txt')

def command_show(calendar):
    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """

    if calendar:
        str_return = ""
        od = collections.OrderedDict(sorted(calendar.items(), reverse=True))
        for dict_day in od:
            list_tasks = od[dict_day]
            str_return += "\n" + dict_day + " : "
            if len(list_tasks) > 1:
                def my_func(e):
                    return e['start']

                list_tasks.sort(reverse=False, key=my_func)
            for dict_task in list_tasks:
                start = dict_task["start"]
                end = dict_task["end"]
                title = dict_task["title"]
                str_return += "\n    start : " + \
                              datetime.datetime(2018, 6, 1, start).strftime("%H:%M") + \
                              ",\n    end : " + \
                              datetime.datetime(2018, 6, 1, end).strftime("%H:%M") + ",\n" + \
                              "    title : " + title
                if len(list_tasks) > 1 and dict_task != list_tasks[-1]:  # only middle change line appended
                    str_return += "\n"
        return str_return
    else:
        return ""


def command_delete(date, start_time, calendar):
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """

    # YOUR CODE GOES HERE
    save_calendar(calendar)
    if date in calendar:
        list_task = calendar.get(date)
        for dict_task in list_task:
            if start_time == dict_task["start"]:
                list_task.remove(dict_task)
                if len(list_task) == 0:
                    calendar.pop(date)
                save_calendar(calendar)
                return True
        if True:
            return "There is no event with start time of " + str(start_time) + " on date " + date + " in the calendar"
    else:
        return date + " is not a date in the calendar"


# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''

    # YOUR CODE GOES HERE
    f = open("calendar.txt", "r")
    calendar = {}
    if not f.read(1):
        # empty txt
        f.seek(0)
        return calendar
    else:
        f.seek(0)
        days = f.read().strip().split("\n")
        for day in days:
            date = day.split(":")[0]
            str_tasks = day.split(":")[1]
            list_task = str_tasks.split("\t")
            calendar[date] = []
            list_tasks_for_dict = []
            for str_task in list_task:
                list_time_title = str_task.split()
                str_time = list_time_title.pop(0)
                int_start = int(str_time.split("-")[0])
                int_end = int(str_time.split("-")[1])
                str_title = ""
                strspace =0;
                for x in list_time_title:
                    str_title += x +" "
                    strspace=str_title.strip()
                list_tasks_for_dict.append({"start": int_start, "end": int_end, "title":strspace})
            calendar[date] = list_tasks_for_dict
            f.close()
    return calendar



# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''
    input1 = ["add", "delete", "quit", "help", "show"]
    if command in input1:
        return True
    else:
        return False


def is_calendar_date(str0):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    if len(str0) == 10:
        str1 = str0[0] + str0[1] + str0[2] + str0[3]
        str2 = str0[5] + str0[6]
        str3 = str0[8] + str0[9]

        if len(str1) == 4 and len(str2) == 2 and len(str3) == 2 \
                and is_natural_number(str1) \
                and int(str1) >= 1000 and int(str2) >= 1 and int(str2) <= 12 and \
                int(str3) >= 1 and int(str3) <= 31 \
                and is_natural_number(str2) and is_natural_number(str3)  \
                and str0[4] == str0[7] == "-":
            return True
        else:
            return False
    else:
        return False


def is_natural_number(str2):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE
    x = ""
    for letter in range(len(str2)):
        if str2[letter] == "0" or str2[letter] == "1" or str2[letter] == "2" or str2[letter] == "3" or str2[
            letter] == "4" or str2[letter] == "5" or str2[letter] == "6" or str2[letter] == "7" or str2[
            letter] == "8" or str2[letter] == "9":
            x = True
        else:
            x = False
            break

    return x


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', 14]
    >>> parse_command("delete 2015-10-22 14 hello")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE
    if line == "" or line == "help":
        return ['help']
    if line == "quit":
        return ['quit']

    command = str(line.split()[0])
    if not is_command(command):
        return ['help']

    if command == "show":
        try:
            n = line.split()[1]
            return ['error', 'show']
        except:
            return ['show']
    if command == "delete":
        try:
            n = line.split()[1]
        except:
            return ['error', 'delete DATE START_TIME']
        if line.split()[1] == "":
            return ['error', 'delete DATE START_TIME']
        try:
            date = line.split()[1]
            start = line.split()[2]
            if not (is_calendar_date(date)):
                return ['error', 'not a valid calendar date']

            try:
                start = int(start)
            except:
                return ['error', 'not a valid event start time']
            return ['delete', date, int(start)]
        except:
            return ['error', 'delete DATE START_TIME']
    if command == "add":
        try:
            date = line.split()[1]
            start = line.split()[2]
            end = line.split()[3]
            details = ' '.join(line.split()[4:])
        except:
            return ['error', 'add DATE START_TIME END_TIME DETAILS']

        if not (is_calendar_date(date)) :
            return ['error', 'not a valid calendar date']

        try:
            start = int(start)
        except:
            return ['error', 'not a valid event start time']

        try:
            end = int(end)
        except:
            return ['error', 'not a valid event end time']

        return ['add', date, start, end, details]
def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor

            start : 12:30,
			end : 13:00,
			title : lunch with sid

			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car

            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway

            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me




if __name__ == "__main__":
    import doctest

    doctest.testmod()