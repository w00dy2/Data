#데이터셋 (기상)

#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
    val = line.strip()  # 읽어온 줄의 양쪽 공백 제거 후 val 변수에 저장
    (year, temp, q) = (val[15:19], val[87:92], val[92:93])  # val 문자열에서 특정 위치의 값을 추출하여 year, temp, q 변수에 저장
    # year: val 문자열의 16번째 문자부터 19번째 문자까지 (총 4글자) 추출
    # temp: val 문자열의 88번째 문자부터 92번째 문자까지 (총 5글자) 추출
    # q: val 문자열의 93번째 문자 (1글자) 추출
    if ( temp != "+9999" and re.match("[01459]", q)):  # temp 값이 "+9999"가 아니고, q 값이 정규 표현식 "[01459]"와 일치하는 경우
        # re.match("[01459]", q): q 값이 0, 1, 4, 5, 9 중 하나인지 확인
        print "%s\t%s" % (year, temp)  # year와 temp 값을 탭으로 구분하여 출력