#%%

"""
figure 모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈이다.
line class를 이용하여 선의 길이를 설정/참조를 수행하며
area_square, area_circle, area_regular_triangle 함수로
각각 정사각형, 원, 정삼각형의 넓이를 반환한다.
"""

import math

class line:
    """
    line class는 선의 길이에 대해 저장하고 있는 클래스이다.
    변수로는 외부에서 접근 불가능한 __length가 있다.
    해당 변수를 접근하고 수정하기 위해서는:
    get_lenght, set_length 메소드를 제공한다.
    """
    __length = 0
    def __init__(self, length):
        """
        생성자 초기 length 값을 받는다.
        length (int or float): 초기 선의 길이 값.
        """
        self.__length = length

    def set_length(self, length):
        """
        선의 길이를 수정한다.
        length (int or float): 선의 길이를 수정한다.
        """
        self.__length = length

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이를 반환한다.
        returns: int or float: 수정하고자 하는 선의 길이입니다.
        """
        return self.__length

def area_square(length):
    """"
    길이를 입력받아 정사각형의 넓이를 구하는 함수.
    length (int or float): 한 변의 길이
    returns: int or float: 정사각형의 넓이를 반환한다. 
    """
    return math.pow(length, 2)
    
def area_circle(length):
    """"
    길이를 입력받아 원의 넓이를 구하는 함수.
    length (int or float): 반지름의 길이
    returns: int or float: 원의 넓이를 반환한다. 
    """
    return math.pow(length, 2) * math.pi
        
def area_regular_triangle(length):
    """"
    길이를 입력받아 정삼각형의 넓이를 구하는 함수.
    length (int or float): 한 변의 길이
    returns: int or float: 정삼각형의 넓이를 반환한다. 
    """
    return math.sqrt(3) / 4 * math.pow(length, 2)

# %%
