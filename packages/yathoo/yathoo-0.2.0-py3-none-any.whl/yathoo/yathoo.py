import os


characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                  "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                  "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]",
                  "|", "\\", ":", ";", "'", '"', "<", ">", ",", ".", "?", "/", "~", "😊", "😍", "👍", "👎", "🌟", "🔥",
                  "💡", "🚀", "🎉", "❤️", "💯", "🙌", "👏", "🤔", "😎", "🤣", "😜", "😇", "👻", "🍕", "🍎", "🌈", "🎈",
                  "📚", "⚽", "🎸", "🎮", "🎃", "🍔", "🌺", "🚗", "🏖️", "🎨", "🎤", "🍦", "🍹", "🚲", "📷", "🌍", "🌞",
                  "🌜", "🚢", "🎳", "🏆", "🍭", " ", "\n"]
if __name__ == '__main__':
    print("Hello! This is yathoo, all-in-one custom module of ADROITNATH")
else:
    letter_sr = 0
    normal_txt = 0
    length_of_string = 0
    encoded_string = 0
    final_index = 0
    no_of_spaces = 0


    def encode(normal_txt):
        try:
            normal_txt = str(normal_txt)
            letter_sr = 0
            length_of_string = len(normal_txt)
            encoded_string = ""

            while letter_sr <= length_of_string - 1:  # length for abcd would be 4 but the index would only be till 3 (0 1 2 3) so after the letter sr is 3 the next time it would try to take index 4 which will give Index error
                current_letter = normal_txt[letter_sr]
                current_encoded_letter = characters.index(current_letter)
                encoded_string = str(encoded_string) + str(current_encoded_letter) + " "
                letter_sr += 1

            encoded_string = str(encoded_string)
            return encoded_string
            # letter_sr = 0 # for decoding purpose(letter_sr always remains 0) maybe this will not work but let it be now
        except:
            return 'invalid entry'


    def decode(encoded_txt_any):
        try:
            no_of_spaces = encoded_txt_any.count(" ") - 1
            # print(no_of_spaces)
            letter_sr = 1
            # print(encoded_txt_any[letter_sr])
            decoded_string = ""
            i = 0
            while i <= no_of_spaces:
                if encoded_txt_any[letter_sr] == " ":
                    decoded_string = decoded_string + characters[int(encoded_txt_any[letter_sr - 1])]
                    letter_sr += 1
                    # print("first condition was true")
                    #  print(decoded_string)
                    i += 1
                elif encoded_txt_any[letter_sr + 1] == " ":
                    decoded_string = str(decoded_string) + str(
                        characters[int(str(encoded_txt_any[letter_sr - 1]) + str(encoded_txt_any[letter_sr]))])
                    # print("second condition string: ", decoded_string)
                    # print("second condition was true")
                    letter_sr += 3
                    i += 1
                else:
                    decoded_string = str(decoded_string) + str(characters[int(str(encoded_txt_any[letter_sr - 1]) + str(
                        encoded_txt_any[letter_sr]) + str(encoded_txt_any[letter_sr + 1]))])
                    letter_sr += 4
                    #  print("third condition was true")
                    #  print("third condition string: ", decoded_string)
                    i += 1
            return decoded_string
        except:
            return 'Invalid entry'


    def init_cloaker():
        if os.path.exists('D:\\Yathoo_Cloaker'):
            if not os.path.exists('D:\\Yathoo_Cloaker\\userdata.txt'):
                file = open('D:\\Yathoo_Cloaker\\userdata.txt', 'w')
                file.write("76 77 ")
                print('created userdata')
                file.close()

        else:
            os.mkdir('D:\\Yathoo_Cloaker')
            file = open('D:\\Yathoo_Cloaker\\userdata.txt', 'w')
            file.write("76 77 ")
            print('created directory and user data')
            file.close()

        print("\nInitialization for Cloaking completed.\n")


    def cloak(txt_file_path):
        file = open(txt_file_path, 'r')
        data = file.read()
        print(data)
        file.close()
        encode(data)
        file = open('D:\\Yathoo_Cloaker\\userdata.txt', 'r')
        userdata = eval(decode(file.read()))
        #print('hi')
        userdata[len(userdata) + 1] = txt_file_path
        file.close()
        file = open('D:\\Yathoo_Cloaker\\{}'.format(
            str(len(userdata)) + ".txt"), 'w')
        file.write(encode(data))
        print(decode(encode(data)))
        file = open('D:\\Yathoo_Cloaker\\userdata.txt', 'w')
        file.write(encode(str(userdata)))
        file.close()
        os.remove(txt_file_path)
        #easygui.msgbox("Your file's ID is {}{}".format(('0' * (9 - len(str(len(userdata))))), len(userdata)), 'Important')  # 9-digit ID (might want to store it in a var rather than directly showing, the user of function may or may not want to)
        print(f"file with id {('0' * (9 - len(str(len(userdata))))) + str(len(userdata))} cloaked successfully.")
        return ('0' * (9 - len(str(len(userdata))))) + str(len(userdata))




    def decloak(sr_cloaked_file_stringonly):
        var = str(sr_cloaked_file_stringonly)
        sr_cloaked_file_stringonly = int(var)
        cloaked_file_path = 'D:\\Yathoo_Cloaker\\{}{}'.format(
            sr_cloaked_file_stringonly, '.txt')
        file = open(cloaked_file_path, 'r')
        encoded_data = file.read()
        file.close()
        os.remove('D:\\Yathoo_Cloaker\\{}{}'.format(
            sr_cloaked_file_stringonly, '.txt'))
        file = open('D:\\Yathoo_Cloaker\\userdata.txt', 'r')
        userdata = eval(decode(file.read()))
        original_path = userdata[sr_cloaked_file_stringonly]
        file.close()
        file = open('D:\\Yathoo_Cloaker\\userdata.txt', 'w')
        del userdata[sr_cloaked_file_stringonly]
        file.write(encode(str(userdata)))
        file.close()
        file = open(original_path, 'w')
        file.write(decode(encoded_data))
        file.close()
        print(f'file with id {sr_cloaked_file_stringonly} decloaked successfully')

    def friends():
        return ['Naitik', 'Pranav', 'Harshal', 'Yash', 'Vighnesh_THE_PRO', 'Sarode']