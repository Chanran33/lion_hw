from django.shortcuts import render

# Create your views here.
def main(requests):
    return render(requests, 'main.html')

def intro(requests):
    return render(requests, 'intro.html')

def photos(requests):
    return render(requests, 'photos.html')

def memo(requests):
    return render(requests, 'memo.html')

"""render이 무슨 함수인가요?
서버사이트에 main이라는 페이지를 보고 싶을 때, main함수가
작동되어 main.html을 render해서 보여줌
"""

