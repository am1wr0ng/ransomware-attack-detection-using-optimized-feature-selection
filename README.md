# ransomware-attack-detection-using-optimized-feature-selection

##### colab basis

1. GFS 모델 실험
    - [x]  a. 전체라벨링 파일로 원핫인코딩
    - [x]  b. a 파일로 Feture Selection 모델 돌리기 (첨부한 사이트 참고)
    - [x]  c. a 파일에서 선별된 Feature 를 제외한 컬럼을 모두 삭제하기
        - 전체라벨링 코드 수정 -> utf-8로 저장 -> 원핫인코딩 코드 돌린 파일 -> utf-8로 재저장
    - [x]  d. c 파일을 KNN 모델로 실험
    - [x]  e. 정확도와 속도 기록

1. OFS 모델 실험 
    - [x]  a. 전체라벨링 파일로 원핫인코딩
    - [x]  b. a 파일에서 PSRansomeware의 특성을 고려하여 Feature 직접 선별
        - basename, remote_address.ip, st_mtime, st_atime, st_ctime
    - [x]  c. b의 피처를 기반으로 제외한 컬럼을 모두 삭제하기
    - [x]  d. c 파일을 KNN 모델로 실험
    - [x]  e. 정확도와 속도 기록
