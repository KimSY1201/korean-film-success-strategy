## 모듈 로딩 -----------------------------------------------
from matplotlib import font_manager, rc

##----------------------------------------------------------
## 함수 기능 : 시각화 시 폰트 설정
## 함수 이름 : sethangeulFont
## 매개 변수 : font_path
## 반 환 값 : 없음
##----------------------------------------------------------

def sethangeulFont(font_path):
    
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    #한글 폰트 설정
    rc('font', family=font_name)
    # 확인 출력
    print(f'{font_name} 폰트 설정')