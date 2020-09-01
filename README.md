## 먼저 해볼 것
- python web_fuzzer.py -h 하면 사용법 나옴

- wfuzz랑 크게 다를거 없이 출력 함
- 입력값 ex) 
    - python web_fuzzer.py -seed seed/sql/common.txt -url http://testphp.vulnweb.com/BOB.php
    - python web_fuzzer.py -seed seed/sql/common.txt -cookie1 login=test%2Ftest -cookie2 aaaa=bbbb -url http://testphp.vulnweb.com/BOB.php
    - python web_fuzzer.py -seed seed/sql/common.txt -post "uname=BOB&pass=test" -url http://testphp.vulnweb.com/userinfo.php
## 현재 가능한 것
- BOB(FUZZ할 곳)을 지정하여 fuzzing 가능(한 군데)
- 옵션으로는 쿠키값 2개 줄 수 있음
- GET, POST 둘 다 가능

## 개선 필요한 것
- BOB(FUZZ할 곳) 2개 이상 못함
- 쿠키값을 2개밖에 못함
- 일단 존나 느려, 개선 필요함
- 옵션 추가 못한게 많음(일단은 필요한것만 해놓음)