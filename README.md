파이썬

### 아나콘다설치
1. https://www.anaconda.com/download 접속
2. 다운로드 후 파일 실행
3. 옵션 선택
    - Create shortcuts: 시작메뉴 추가
    - Add Anaconda3 to my PATH environment variable: 시스템 환경변수 추가(파이썬이 이미 설치되어있는 경우는 추천X)
    - Register Anaconda3 as my default Python: 아나콘다를 기본 파이썬으로 등록(VSCode에서 자동적으로 감지됨)
    - Clear the package cache upon completion: 설치 완료시 패키지 캐시 삭제(파이썬이 설치되어있는경우)

4. 명령어

| 명령어                                   | 설명       |
| ------------------------------------- | -------- |
| `conda create -n 이름 python=버전`        | 새 환경 만들기 |
| `conda activate 이름`                   | 환경 활성화   |
| `conda deactivate`                    | 비활성화     |
| `conda install 패키지명`                  | 패키지 설치   |
| `conda env export > environment.yml`  | 환경 내보내기  |
| `conda env create -f environment.yml` | 환경 불러오기  |

### VSCode
1. 필수 확장자 설치
    - Python 
    - Jupyter
    - Pylance(선택)

2. 아나콘다 환경과 연결
    - Ctrl + Shift + P
    - Python: Selet Interpreter 검색 후 클릭
    - Python (base: conda) 선택

3. 실행 단축키 설정
    1. 파일(File) → 기본 설정(Preferences) → 키보드 단축키(Keyboard Shortcuts)
    2. run python file 입력 > Python: Run Python File in Terminal 여기서 단축키 설정