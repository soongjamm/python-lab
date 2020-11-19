# rest-api basic 
조금 추상적일 수 있다.

GET... html을 return하거나 다른 것들을 리턴.

rest api는 테크니컬한 요소는 없다.

data가 아닌 resources를 응답한다. 그냥 생각의 차이다.



- Resource?

orm과 비슷하게 각 resource는 interact 가능. (pertinent와)

ex. get, post, put, delete가 똑같은  (/item/chair) url? endpoint?를 요청. 똑같은 item resource 이기 때문



- Stateless?

또 다른 특징. 하나의 리퀘스트는 다른 리퀘스트에 의존할 수 없다. 서버는 지금의 리퀘스트만 알고 이 전의 리퀘스트는 기억하지 못한다.

ex) post item/chair 후 잊어버린다. 다음 get 요청이 왔을 때 서버는 데이터가 있다고 대답 못한다. DB를 확인해야 한다.

ex) 서버는 유저가 로그인 했는지 모른다. 웹앱은 데이터를 interact 할 때 마다 서버에 데이터를 보내야 한다.


### - 
javascript와 python은 서로 코드를 모르지만, API를 통해 소통한다. 즉 json을 주고 받으며 소통한다.