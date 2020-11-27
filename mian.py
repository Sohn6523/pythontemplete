#%%
# --------------------------------------------------------------------------------
# 모든 실행 파일에 필수 적으로 사용할 것
import sys, os

# 부모 디텍터리의 파일을 호출 가능 설정
try:
    # python interactive 보모 폴더 사용하도록 설정
    # python interactive 에서는 파일의 현제 위치가 os.path가 되기 때문에 상위 폴더 추가만으로 해결
    # pathconfig파일을 불러와서 모든 폴더 경로 등록
    # python interactive 에서는 pathconfig 실행없이 사용가능,
    # --> import 구문에 부모 폴더명이 필요함
    sys.path.append(os.pardir)
    from Config import pathconfig

    pathconfig.set_path()
except:
    # Terminal 보모, 자식 폴더 사용하돌고 설정
    # Terminal에서는 Pjt Root 폴더를 보고 있고 절대 경로 등록이 필요함
    # 코드 폴더인 Src를 절대 경로로 우서 추가하고 Config의
    # pathconfig파일을 호출하여 모든 폴더 경로 등록
    sys.path.append(os.path.join(os.getcwd(), "Src"))
    from Config import pathconfig

    pathconfig.set_path()

# --------------------------------------------------------------------------------
# Library Call
# --------------------------------------------------------------------------------
# Public Lib
import pandas as pd

# Custom Lib
# from 폴더이름 import 파일명 대신 import 파일명 사용 가능
# 명시적으로 폴더 위치 표현하는 from 폴더이름 import 파일명 방법이 좋을 듯
from Param import parms
from DataIO import dataread
from Figure import makefigure
from Model import prediction


# --------------------------------------------------------------------------------
# user code

if __name__ == "__main__":
    oParam = parms.PARAM()  # Param 객체 생성
    data = dataread.DATAREAD(oParam).read()  # 데이터 읽어오기

    print(data)

    makefigure.make_bar()
    prediction.best_model()


# %%


# %%
