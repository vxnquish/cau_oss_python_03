#%%

"""
figure 모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈이다.
line class를 이용하여 선의 길이를 설정/참조를 수행하며
area_rectangle, area_ellipse, area_right_triangle 함수로
각각 직사각형, 타원, 직각삼각형의 넓이를 반환한다.
"""

import math

class line:
    """
    line class는 선의 길이에 대해 저장하고 있는 클래스이다.
    변수로는 외부에서 접근 불가능한 __width 와 __height 가 있다.
    해당 변수를 접근하고 수정하기 위해서는:
    get_length, set_length 메소드를 제공한다.
    """
    __width  = 0
    __height = 0
    
    def __init__(self, width, height):
        """
        생성자 초기 length 값을 받는다.
        width  (int or float): 초기 선의 가로 길이 값.
        height (int or float): 초기 선의 세로 길이 값.
        """
        self.__width  = width
        self.__height = height

    def set_length(self, width, height):
        """
        선의 길이를 수정한다.
        width  (int or float): 가로 선의 길이를 수정한다.
        height (int or float): 세로 선의 길이를 수정한다.
        """
        self.__width  = width
        self.__height = height

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이를 반환한다.
        returns: int or float: 저장하고 있는 선의 길이입니다.
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    """"
    길이를 입력받아 직사각형의 넓이를 구하는 함수.
    width  (int or float): 밑변의 길이
    height (int or float): 높이의 길이
    returns: int or float: 직사각형의 넓이를 반환한다. 
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height
    
def area_ellipse(width, height):
    """"
    길이를 입력받아 타원의 넓이를 구하는 함수.
    width  (int or float): 긴  반지름의 길이
    height (int or float): 짧은 반지름의 길이
    returns: int or float: 타원의 넓이를 반환한다. 
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi
        
def area_right_triangle(width, height):
    """"
    길이를 입력받아 직각삼각형의 넓이를 구하는 함수.
    width  (int or float): 밑변의 길이
    height (int or float): 높이의 길이
    returns: int or float: 직각삼각형의 넓이를 반환한다. 
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2

# %%
