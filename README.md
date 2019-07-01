# Django 에서 Redis이용해 Caching 

## Requriements
```
python (3.6)
pipenv 
Django(2.x) ----> pipenv install 
django-redis ---->pipenv install 
redis-tools------> sudo apt-get install 
redis-server-----> sudo apt-get install
loadtest --------> sudo npm install -g loadtest 
```

1. post object 10000개추가     
  ./manage.py addpost 10000  

2. 서버 실행시킨다.  
./manage.py runserver  

3. views.py  line8~10 wn주석 해제, 그아래 주석처리   

4. caching 없이 메인페이지에 요청 100개 보내는것  얼마나 걸리는지 테스트   
  loadtest -n 100 http://localhost:8000  

5. views.py line8~10 주석처리, 그아래 주석 해제   

6. 요청 한번 보내서 redis서버에 key값과 대응되는 데이터(postobject100000개)저장시킴    
  curl http://localhost:8000  

7. 키,value redis서버에 잘 들어갔는지 확인    
 redis-cli -h 127.0.0.1 -p 6379       
SELECT 1   
KEY *  

8. 다시 loadtest해본다.  



