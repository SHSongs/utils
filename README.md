# utils

## 주요 기능

1. 현재 경로 기준, 하위 모든 이미지를 가져옵니다.
2. 이미지를 적절한 비율로 만듭니다. 
3. 이미지의 메타데이터(위치, 시간 등)를 삭제합니다.  


## 동기
[github blog](https://shsongs.github.io/) 에 올릴 
1. 이미지의 크기가 중구난방이다.
2. 메타데이터로 인해 개인 정보가 유출된다. 

<br>

이를 방지하기 위해 이 레포를 만들었다. 

1. 이미지의 resize 크기를 설정하지 않고, 알아서 딱 적절하게 줄여주는 기능이 필요하다. 
2. [remove metadata](https://github.com/search?q=remove+metadata) 는 이미 존재하지만, 모든 파일 탐색해 자동으로 메타 데이터를 삭제하는 소스코드는 찾지 못했다. ([nikvoronin/Metanull](https://github.com/nikvoronin/Metanull) 찾았지만, window 전용)   

