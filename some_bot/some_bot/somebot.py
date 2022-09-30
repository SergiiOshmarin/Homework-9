import sys
contact_dictionary={"Sergii Oshmarin":"0999552457","Olga Oshmarina":"0934852256"}

def format_phone_number(func):
    def inner(x):
        result = func(x)
        if len(result)<10:
            return sanitize_phone_number(input("Looks like you type wrong number.Please try again.Type only number\n"))
        elif len(result)<12:
            new_result="+38"+result
            return new_result
        elif len(result)<13:
            new_result="+"+result
            return new_result
        elif len(result)>=13:
            return sanitize_phone_number(input("Looks like you type wrong number.Please try again.Type only number\n"))
        else:
            return result      
    return inner

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

def format_name(list):
    if type(list)==str:
        list=list.strip().split()
    new_name=[]
    for i in list:
        if i.isalpha():
            name=i.lower().capitalize()
            new_name.append(name)
        else:
            return format_name(input("Looks like you type wrong name.Please try again.Type only first and second name\n"))
    return " ".join(new_name) 
            


def parser_command(string):
    modified_list1=string.strip().split()
    return modified_list1

def name_search(some_list):
    name_list=list(contact_dictionary.keys())
    if type(some_list)==str:
        some_list=some_list.strip().split()
    result=[]
    if len(some_list)==1:
        if some_list[0].lower()=="cancel":
            return
        for i in name_list:
            if some_list[0].lower().capitalize() in i:
                result.append(i)
            else:
                pass
    elif len(some_list)==2:
        name_list=list(contact_dictionary.keys())
        new_name=" ".join([some_list[0].lower().capitalize(),some_list[1].lower().capitalize()])
        another_name =" ".join([some_list[1].lower().capitalize(),some_list[0].lower().capitalize()])
        if new_name in name_list:
            return contact_dictionary[new_name]
        elif another_name in name_list:
            return contact_dictionary[another_name]
        for i in name_list:
            if some_list[0].lower().capitalize() in i:
                result.append(f"{i}")
            elif some_list[1].lower().capitalize() in i:
                result.append(f"{i}") 
            else:
                pass
    if len(result)>=1:
        return name_search(input(f'{result} These are the best match what I found for you. Type one of this names to see number you need\n'))
    else:
        return name_search(input('No results were found with such name.Try another name or type "cancel"\n'))
    

def handler(string):
    exit_list=['good bye','close','exit']
    while string.lower() not in exit_list:
        x=parser_command(string)
        if len(x)==1:
            if x[0].lower()=="hello":
                x=input("Hello.How can I help you?:\n")
                return handler(x)
            else:
                return handler(input("Looks like you type something wrong.Please try again,don't forget space between words and use correct commands\n"))
        elif len(x)>1:
            if x[0].lower()=="add":
                if len(x)==4:
                    list2=[]
                    list2.extend(x[1:-1])
                    clean_name=format_name(list2)
                    contact_dictionary[clean_name]=sanitize_phone_number(x[-1])
                    print(f'Contact dictionary successfully updated with such contact {clean_name}:{contact_dictionary[clean_name]}')
                    return handler(input("Would you like to do something else?\n"))
                else:
                    return handler(input('Function "add" accept only such sequence: first name,second name and phone number.Please try again\n'))
            elif x[0].lower()=="phone":
                if len(x)<2 or len(x)>4:
                    return handler(input('Function "change" accept only such sequence: first name and second name.Please try again\n'))
                elif len(x) in [2,3]:
                    list2=[]
                    list2.extend(x[1:])
                    phone_number=name_search(list2)
                    if phone_number==None:
                        return handler(input("Would you like to do something else?\n"))
                    else:
                        print(f'Contact has such number:{phone_number}')
                        return handler(input("Would you like to do something else?\n"))
            elif x[0].lower()=="change":
                if len(x)==4:
                    list2=[]
                    list2.extend(x[1:3])
                    clean_name=format_name(list2)
                    clean_name2=format_name(" ".join([list2[1],list2[0]]))
                    if clean_name in contact_dictionary.keys():
                        contact_dictionary[clean_name]=sanitize_phone_number(x[-1])
                        print(f'Contact {clean_name} successfully updated with number:{contact_dictionary[clean_name]}')
                        return handler(input("Would you like to do something else?\n"))
                    elif clean_name2 in contact_dictionary.keys():
                        contact_dictionary[clean_name2]=sanitize_phone_number(x[-1])
                        print(f'Contact {clean_name2} successfully updated with number:{contact_dictionary[clean_name2]}')
                        return handler(input("Would you like to do something else?\n"))
                    else:
                        return handler(input('There are no match for your input. Type "show all" to see all contacts\n'))
                else:
                    return handler(input('Function "change" accept only such sequence: first name,second name and phone number.Please try again\n'))
            elif string.lower() =="show all":
                print(contact_dictionary)
                return handler(input("Would you like to do something else?\n"))
        else:
            return handler(input("Looks like you type something wrong.Please try again,don't forget space between words\n"))
         

def main():
    print('Hello. I am bot which works with your phone book.')
    print('[1] Enter "hello" and receive answer "How can I help you?"')
    print('[2] Enter "add ...". With this command I will save in memory new contact(Only Ukraininan Numbers).')
    print('[3] Enter "change ...". With this command I will change number in existing contact.Excepting first or second name')
    print('[4] Enter "phone ....". With this command I will show number of contact that you enter.')
    print('[5] Enter "show all". With this command I will show all numbers existing in your contact list.')
    print('[6] Enter "good bye","close" or "exit" to quit.')
    y = input('How can I help you today?:\n')
    handler(y)
    print("Good bye!")
if __name__ == '__main__':
    exit(main())