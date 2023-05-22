import re


def get_frequency(string):  # define the function for getting the characters' frequency
    frequency = {}  # define a dictionary that will hold every character with its frequency
    pattern = r'[^\s\n\r\b\t\f\v\a]'  # regex created to avoid cases where a special character is counted
    for char in string:  # loop through the characters of the string
        if re.match(pattern, char):  # check if the character matches the regex
            if char in frequency:  # check if the character is already in the dictionary
                frequency[char] += 1  # if it is, increment its frequency
            else:
                frequency[char] = 1  # if it's not, add the character to the dictionary
    # sort the dictionary by value to create a list that contains every character with its frequency
    frequency_list = sorted(frequency.items(), key=lambda item: item[1],
                            reverse=True)
    result = ''  # define an empty string that will hold the final result
    for char, freq in frequency_list:  # loop through the list's items
        result += char + str(freq)  # add the character and its frequency to the final string
    return result


if __name__ == '__main__':
    input1 = "testinnput"
    input2 = "    \n\r\b\t\f\v\atestinnput"
    output1 = get_frequency(input1)
    output2 = get_frequency(input2)
    print(output1)
    print(output2)
