import pyttsx3

def says(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    

dict1={'pen':10,'notebook': 20};
says('enter the product name to search')
tar=input('enter product to search their price:')
if tar in dict1:
    print(f'the price of {tar} is: {dict1[tar]}')
    says(f'the price of {tar} is: {dict1[tar]}')
else:
    print('product are not avalible in the list\nwant to update your price\nyes or no')
    says('product are not avalible in the list and want to update your price')
    says('yes or no')
    n=input()
    if n=='yes':
        says('enter your product')
        m=input('enter your product: ')
        if m in dict1:
            says('enter your price')
            s=int(input('enter the price: '))
            dict1[m]=s
            says('price is Updated')
            print(dict1)
        else:
            print('exit-->thanks')
            says('exit-->thanks')
    else:
        says('No updation\nTerminated-->Successfully')
        print('No updation\nTerminated-->Successfully')
