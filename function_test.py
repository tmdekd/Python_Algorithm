# -*- coding: utf-8 -*-

def input_radius():
    return float(input("반지름을 입력하세요: "))

def calc_circle_area(r):
    return 3.14 * r * r

def calc_circle_circumference(r):
    return 2 * 3.14 * r

radius = input_radius()
circle_area = calc_circle_area(radius)
circle_circumference = calc_circle_circumference(radius)
print("원의 면적 : {0:0.2f}, 원의 둘레 : {1:0.2f}".format(3.14*5*5, 2*3.14*5))
print("원의 면적 : {0:0.2f}, 원의 둘레 : {1:0.2f}".format(circle_area, circle_circumference))
