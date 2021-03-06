#%%
# --------------------------------------------------------------------------------
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
import prediction

# --------------------------------------------------------------------------------
# user code


def make_bar():
    return print("BAR Chart")


prediction.best_model()
# %%
