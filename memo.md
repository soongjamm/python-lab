### 목적 :

- 인스턴스 : 대부분의 목적을 가지고 있다. 데이터를 넣거나 수정, 등 여러가지 액션
    - instance method는 인자를 넣지 않고 호출할 수 없음
- 스태틱 : 메소드를 클래스 안에 넣기 위함이다. 해당 클래스와 관련성이 있다는 것을 보여주기 위해 (개발자를 위한 기능)
    - @staticmethod는 인자로 아무것도 갖지 않는다. (self도) (instance_method는 self를 가졌다)
    - @staticmethod는 보통 function인데, 클래스와 관련이 있어서 묶기위해 클래스 안에 넣지만, 안에 property들과 아무 관련이 없다.
- 클래스메소드 : 팩토리
    - @classmethod 적용 전 보통 instance method에선 ClassTest.instance_method(test) 와 같이 인자로 (클래스)객체를 넣어줘야 한다.
    - 하지만 @classmethod를 적용하면, 파이썬이 알아서 클래스를 파악한다.




