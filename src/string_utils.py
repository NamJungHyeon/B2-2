"""팀 소개 문서를 다룰 때 쓰는 간단한 문자열 유틸."""


def reverse(text):
    """문자열을 뒤집는다."""
    return text[::-1]


def count_words(text):
    """공백으로 나눈 단어 개수를 센다."""
    return len(text.split())
