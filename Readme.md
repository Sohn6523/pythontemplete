

# Custom User Lib Path 자동 설정

VSCode에서 interactive에서는 실행되는데 Terminal에서는 오류 발생하는 경우가 있음 왜? 

## 데이터 분석은 아나콘다 기반으로 배움 
 * EDA 수준이면 아나콘다 환경이 개꿀이지 
 * 코드가 복잡해지면서 라인이 증가하면? 유지보수는 어쩜?? 
 * IDE 툴이 필요함 (VSCode 아님 Pycharm) 
 * 빌게이츠 형님이 플렉스한 VSCode를 사용하겠음 

## 여기서 문제가 생김 
 * Terminal과 interactive에서 바라보는 path 위치가 다름 
    그래서 interactive에서는 바로 실행되는데 terminal에서는 실행 오류가 발생함 
 * terminal과 interactive 모두 실행 가능하도록 sub folder 모두 sys.path에 등록이 되어야함 
 * reg 편집기에서 설정 가능하지만 귀찮음 --> 난 코딩으로 해결하겠음 