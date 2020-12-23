class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class HexNumber:
    def __init__(self, string):
        self.head = None
        self.lenght = len(string)

        if not (isUpper(string)):
            print("Буквы в строке должны быть в верхнем регистре.")
            return

        for element in string:
            if isnumber(element):
                self.head = Node(element, self.head)
            else:
                return

    def __str__(self):
        string = ''
        subhead = self.head
        while subhead:
            string += subhead.val
            subhead = subhead.next
        return string[::-1]

    def add(self, secNumber):
        if not (secNumber is HexNumber):
            print("Сложение невозможно. Второе слагаемое не является числом.")
            return

        if self.lenght > secNumber.lenght:
            len = self.lenght
        else:
            len = secNumber.lenght
        if_rem = False

        for i in range(len):
            if self.head != None and secNumber.head != None:
                num = makenumber(self.head.val) + makenumber(secNumber.head.val)
                self.head = self.head.next
                secNumber.head = secNumber.head.next

            else:
                if self.head != None and secNumber.head == None:
                    num = makenumber(self.head.val)
                    self.head = self.head.next

                if self.head == None and secNumber.head != None:
                    num = makenumber(secNumber.head.val)
                    secNumber.head = secNumber.head.next

            if if_rem:
                num += 1
                if_rem = False

            if num > 15:
                num = num - 16
                if_rem = True

            if i == 0:
                resNumber = HexNumber(makechar(num))
                real_head = resNumber.head
            else:
                resNumber.head.next = Node(makechar(num))
                resNumber.head = resNumber.head.next

        if if_rem:
            resNumber.head.next = Node(makechar(1))
        resNumber.head = real_head
        return resNumber


def isnumber(char):
    if char.isdigit():
        number = ord(char) - 48
    else:
        number = ord(char) - 55
    if number > 15 or number < 0:
        print("Не все введённые символы соответствуют обозначениям шестнадцатеричной системы счисления (012345ABCDEF)")
        return False
    else:
        return True


def makenumber(char):
    return ord(char) - ord('A') + 10 if char >= 'A' and char <= 'F' else ord(char) - ord('0') 

def makechar(num):
    return chr(ord('A') + num - 10) if num > 9 else chr(ord('0') + num)


def isUpper(string):
    if string == string.upper():
        return True
    else:
        return False
