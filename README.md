## 입력값
    python web_fuzzer.py -various_seed seed/sql/injection.txt -area_seed seed/sql/attact_area.txt
    - various_seed 공격 다양화 시드파일 경로
    - area_seed 공격 범위 시드파일 경로


## 시드파일
- @(FUZZ할 곳)을 지정하여 fuzzing 가능(한 군데)
- 옵션으로는 시드파일 2개 줄 수 있음
- GET, POST 둘 다 가능
    - GET과 POST는 '?'로 구분 가능 

## 개선 필요한 것
- 공격이 먹혔는지 안먹혔는지 알 수 없음
- wireshark로 패킷이 잘 날라가는 것은 확인 가능
