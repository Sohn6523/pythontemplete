#%%

import os
import sys

"""User / Custom Library path 설정 사용  
    sys.path

    https://velog.io/@ybear90/Python-%EB%AC%B8%EB%B2%95%EC%97%90-%EA%B4%80%ED%95%9C-%EB%82%B4%EC%9A%A9-%EC%9D%BC%EB%B6%80-%EC%A0%95%EB%A6%AC-5Python-module-package-%EB%82%B4%EC%9A%A9-%EC%A0%95%EB%A6%AC

"""


def set_path(show=False):
    """Terminal과 interactive에서 바라보는 path 위치가 다름 
    그래서 interactive에서는 바로 실행되는데 terminal에서는 실행 오류가 발생함 
    terminal과 interactive 모두 실행 가능하도록 sub folder 모두 sys.path에 등록이 되어야함 
    reg 편집기에서 설정 가능하지만 귀찮음 --> 난 코딩으로 해결하겠음 

    Mian에서 실행하면 필요 없음 sub folder에서 확인용으로 사용하기 위해서 필요함 
    EDA수준이면 그냥 하면 됨, 배포의 목적이면 유지 보수를 위해 폴더링이 필요함 이때 사용
    """
    paths = []

    if os.path.exists("Src"):
        ## 현 위치에서 Src폴더가 있을 경우, 최상위 폴더
        for (path, dir, file) in os.walk(os.getcwd()):
            sys.path.append(path)
            paths.append(path)

        txt = "path 설정이 완료 되었습니다."

    else:
        ## 현 위치에서 Src폴더가 없을 경우, sub 폴더
        orgPath = os.getcwd()  # 지금 경로 정보
        paths = os.getcwd().split("/")  # 지금 경로 문자열 분리
        order = len(paths) - paths.index("Src") - 1  # "Src 폴더 위치 확인"
        up = ["", "..", "../.."]
        if (order > 0) & (order < 3):  # sub-folder depth가 1~2사이 3이상 허용 안됨
            os.chdir(os.path.join(os.getcwd(), up[order]))  # 상위 패스 설정  및 이동
            for (path, dir, file) in os.walk(os.getcwd()):  # 뭐있나 확인하고 패스 설정하기
                sys.path.append(path)
                paths.append(path)
            txt = f"path 설정이 완료 되었습니다. sub folder의 depth는 {order} 입니다."
        else:
            txt = "Sub-Folder가 너무 깊어요"

        os.chdir(orgPath)

    if show:
        print(txt)
        print(f"설정된 패스 입니다.: {paths}")
    else:
        pass

    return None


# # %%


# %%
