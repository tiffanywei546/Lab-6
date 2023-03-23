# Tiffany Wei

def menu():
    print(f'Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit')
def encode(password):
    global final
    encode=[]
    list=[int(x) for x in password]
    for num in list:
        num=num+3
        encode.append(num)
    final=''
    for num in encode:
        num=str(num)
        final+=num
    return final

def decoder(final):
    global result
    result = ''
    final = [int(i) - 3 for i in final]
    for j in final:
        result += str(j)
    return result
    pass

def main():
    menu()



if __name__ =='__main__':
    x=1
    while x>0:
        main ()
        option = int(input('Please enter an option:'))
        if option==1:
            password=str(input('Please enter your password to encode:'))
            code=encode(password)
            print('Your password has been encoded and stored!')
        if option == 2:
            decoder(final)
            print(f'The encoded password is {final}, and the original password is {password}.')
        elif option==3:
            break
