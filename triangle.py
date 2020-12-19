import math
import sys
import unittest

class Triangle:
    def __init__ (self,ax = 0,ay = 0,bx = 0,by = 0,cx = 0,cy = 0):
        self.a = math.sqrt((int(ax)-int(bx))**2 + (int(ay)-int(by))**2)
        self.b = math.sqrt((int(bx)-int(cx))**2 + (int(by)-int(cy))**2)
        self.c = math.sqrt((int(ax)-int(cx))**2 + (int(ay)-int(cy))**2)


    def isTriangle(self):
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return False
        return True


    def isIsoscelesTriangle(self):
        if not(self.isTriangle()):
            return False
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        return False


    def find_area(self):
        if self.isIsoscelesTriangle():
            return(math.sqrt(((self.a + self.b+ self.c)/2) * ((self.a + self.b + self.c)/2 - self.a) * ((self.a + self.b + self.c)/2 - self.b) * ((self.a + self.b + self.c)/2 - self.c)))
        return -1


def makestring(array):
    string = ""
    for element in array:
        string += str(element) + " "
    return string


def find_biggest_area_args(input_filename):
    input_file = open(input_filename, 'r')
    line = input_file.readline()
    args = []
    max_area = -1
    max_args = []
    while line != "":
        args = line.split()
        if len(args) != 6 or not(line.isdigit):
            line = input_file.readline()
            args = []
            continue
        curr_triangle = Triangle(*args)
        curr_area = curr_triangle.find_area()
        if curr_area > max_area:
            max_area = curr_area
            max_args = args
        line = input_file.readline()
        args = []
    input_file.close()
    if len(max_args) != 6:
        print("Подходящий треугольник не найден.")
        return([""])
    return(max_args)


def main():
    if len(sys.argv) != 3:
        print("Некорректный ввод.")
        return -1
    output_file = open(sys.argv[2], 'w')
    output_file.write(makestring(find_biggest_area_args(sys.argv[1])))
    output_file.close()
    print("Треугольник был найден.")


if __name__ == '__main__':
    main()

'''
class TriangleTest(unittest.TestCase):
    def test_is_Triangle(self):
        triang = Triangle(0,0,0,4,5,0)
        self.assertEqual(True, triang.isTriangle())

    def test_is_not_Triangle_line(self):
        triang = Triangle(1,3,3,3,5,3)
        self.assertEqual(False, triang.isTriangle())
    
    def test_is_not_Triangle_dot(self):
        triang = Triangle(1,3,1,3,1,3)
        self.assertEqual(False, triang.isTriangle())

    def test_is_isosceles_triangle(self):
        triang = Triangle(0,0,0,5,5,0)
        self.assertEqual(True, triang.isIsoscelesTriangle())

    def test_is_not_isosceles_triangle(self):
        triang = Triangle(0,0,0,4,5,0)
        self.assertEqual(False, triang.isIsoscelesTriangle())
    
    def test_find_area(self):
        triang = Triangle(0,0,0,4,4,0)
        self.assertEqual(8, round(triang.find_area()))

    def test_find_area_dot(self):
        triang = Triangle(0,0,0,0,0,0)
        self.assertEqual(-1, triang.find_area())

    def test_makestring(self):
        array = [1,4,5]
        self.assertEqual("1 4 5 ", makestring(array))

    def test_makestring_nothing(self):
        array = [""]
        self.assertEqual(" ", makestring(array))


if __name__ == '__main__':
    unittest.main()
'''




