# write a function that returns a string with all the items separated by a comma and a space, with and inserted before the last iten.

def comma_code(input_list):
    if len(input_list)==0: print('Please enter a list');
    else:
        output_str = ''
        for index, name in enumerate(input_list):
            if index == 0: output_str = name;
            elif index == len(input_list)-1:
                output_str = output_str + ', and' + name
            else: output_str = output_str + ', ' + name
        return output_str

spam = ['apples','bananas','tofu','cats']
print( comma_code(spam))
