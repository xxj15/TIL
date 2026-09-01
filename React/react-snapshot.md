# React - State as a Snapshot

## 범위

React 공식문서 `State as a Snapshot`

- State 변경이 리렌더링을 발생시키는 방식
- 각 렌더링이 자신만의 State 값을 가지는 이유
- `setState` 직후 값이 바로 바뀌지 않는 이유

React에서 State는 일반 변수처럼 현재 값을 직접 바꾸는 방식이 아니라, **다음 렌더링에 사용할 값을 요청하는 방식**으로 동작한다. 각 렌더링은 그 시점의 State 값을 기준으로 JSX와 이벤트 핸들러를 만든다.

## 핵심 개념

### 1. State 변경은 현재 값을 수정하는 것이 아니다

```jsx
const [count, setCount] = useState(0);

function handleClick() {
  setCount(count + 1);
  console.log(count);
}
```

버튼을 처음 클릭했을 때 출력되는 값은:

```text
0
```

`setCount(1)`을 호출해도 현재 실행 중인 렌더링의 `count`는 여전히 `0`이다.

```text
현재 렌더링
count = 0

setCount(1)
↓
다음 렌더링 요청

다음 렌더링
count = 1
```

---

### 2. 각 렌더링은 State의 Snapshot을 가진다

컴포넌트가 렌더링될 때 React는 그 시점의 State 값을 전달한다.

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

첫 번째 렌더링에서는:

```text
count = 0
```

이때 만들어진 이벤트 핸들러도 `count = 0`을 기준으로 동작한다.

State가 변경되면 React가 컴포넌트를 다시 호출하고 새로운 값으로 새로운 렌더링을 만든다.

---

### 3. 같은 이벤트 안에서는 State 값이 고정되어 있다

```jsx
function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <button
      onClick={() => {
        setNumber(number + 1);
        setNumber(number + 1);
        setNumber(number + 1);
      }}
    >
      +3
    </button>
  );
}
```

버튼을 한 번 클릭한 뒤 값은:

```text
1
```

각 코드가 다음처럼 실행되기 때문이다.

```jsx
setNumber(0 + 1);
setNumber(0 + 1);
setNumber(0 + 1);
```

현재 이벤트 핸들러 안에서 `number`는 계속 `0`이라는 Snapshot을 사용한다.

여러 번의 State 업데이트가 필요할 때는 이전 값을 전달받는 **updater function**을 사용할 수 있다.

```jsx
setNumber(n => n + 1);
setNumber(n => n + 1);
setNumber(n => n + 1);
```

이 경우 결과는:

```text
3
```

## 예제 또는 확인할 코드

다음 코드에서 버튼을 클릭하면 `console.log`에는 무엇이 출력될까?

```jsx
function Counter() {
  const [count, setCount] = useState(5);

  function handleClick() {
    setCount(count + 1);
    console.log(count);
  }

  return <button onClick={handleClick}>{count}</button>;
}
```

정답:

```text
5
```

화면은 다음 렌더링에서:

```text
6
```

으로 바뀐다.

---

다음 두 코드의 차이도 확인한다.

```jsx
setCount(count + 1);
```

```jsx
setCount(prev => prev + 1);
```

첫 번째 방식은 **현재 렌더링의 `count` 값**을 사용한다.

두 번째 방식은 React가 관리하는 **이전 State 값을 기준으로 다음 값을 계산한다.**

## 헷갈리기 쉬운 점

### `setCount()`는 즉시 변수 값을 바꾸지 않는다

```jsx
setCount(10);
console.log(count);
```

`console.log`에서 바로 `10`이 나오는 것은 아니다.

`setCount(10)`은 다음 렌더링에서 사용할 State를 요청한다.

### 이벤트 핸들러도 해당 렌더링의 State를 기억한다

```jsx
setTimeout(() => {
  console.log(count);
}, 3000);
```

나중에 실행되는 함수라도 자신이 만들어졌던 렌더링의 State 값을 사용할 수 있다.

## 취준 포인트

### Q. `setState`를 호출했는데 왜 바로 State 값이 바뀌지 않나요?

각 렌더링의 State 값은 고정되어 있기 때문이다. `setState`는 현재 렌더링의 값을 직접 수정하는 것이 아니라 새로운 State를 사용한 다음 렌더링을 요청한다.

### Q. 아래 코드의 결과가 왜 `3`이 아니라 `1`인가요?

```jsx
setCount(count + 1);
setCount(count + 1);
setCount(count + 1);
```

세 코드 모두 현재 렌더링의 동일한 `count` 값을 사용하기 때문이다.

이전 State를 기준으로 연속 업데이트하려면 updater function을 사용한다.

```jsx
setCount(prev => prev + 1);
```

## 오늘의 한 줄 정리

> React의 State는 현재 렌더링에서 바뀌는 변수가 아니라, 각 렌더링이 전달받는 Snapshot이다.