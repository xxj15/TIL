# React - State

## 오늘 할 것

**React 공식문서:** `State: A Component's Memory`


- 일반 변수와 State의 차이
- `useState`가 반환하는 값
- State 변경과 리렌더링의 관계
- Hook을 컴포넌트 최상위에서 호출하는 이유


---

## 핵심 개념

### 1. 왜 일반 변수 대신 State를 사용할까?

```jsx
let index = 0;

function handleClick() {
  index = index + 1;
}
```

이렇게 일반 변수를 변경하는 것만으로는 화면이 바뀌지 않는다.

React에서 화면에 표시되는 값이 바뀌려면 두 가지가 필요하다.

1. **렌더링이 다시 일어나도 값을 기억해야 한다.**
2. **값이 바뀌었다는 사실을 React에 알려 리렌더링해야 한다.**

일반 변수는 이 두 가지를 해주지 못한다.

State는 **렌더링 사이에서 값을 기억하고, 값 변경 시 React에 리렌더링을 요청한다.**

---

### 2. `useState`

```jsx
const [index, setIndex] = useState(0);
```

`useState(0)`은 두 값을 반환한다.

```text
index     → 현재 State 값
setIndex  → State를 변경하는 함수
```

`0`은 최초 렌더링에서 사용할 **초기값**이다.

즉,

```jsx
setIndex(index + 1);
```

을 실행하면 React에게

> 다음 렌더링에서는 index를 새로운 값으로 사용해줘.

라고 요청하는 것과 비슷하다.

---

### 3. State가 변경되면 다시 렌더링된다

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

처음 렌더링:

```text
count = 0
```

버튼 클릭:

```jsx
setCount(1);
```

React가 새로운 State를 기억하고 컴포넌트를 다시 렌더링한다.

```text
count = 1
```

결과적으로 화면에도 `1`이 표시된다.

---

### 4. Hook은 컴포넌트 최상위에서 호출한다

```jsx
const [count, setCount] = useState(0);
```

`useState`, `useEffect`처럼 `use`로 시작하는 함수를 **Hook**이라고 한다.

다음처럼 조건문 안에서 호출하면 안 된다.

```jsx
if (isLogin) {
  const [name, setName] = useState("");
}
```

React는 Hook이 호출되는 **순서**를 기준으로 각 State를 관리하기 때문에 매 렌더링마다 호출 순서가 동일해야 한다.

따라서 Hook은 컴포넌트의 **최상위 레벨**에서 호출한다.

---

## 예제 또는 확인할 코드

### 코드 읽기

아래 코드에서 버튼을 한 번 클릭하면 화면의 숫자는 어떻게 될까?

```jsx
function Counter() {
  const [count, setCount] = useState(3);

  return (
    <button onClick={() => setCount(count + 2)}>
      {count}
    </button>
  );
}
```

<details>
<summary>정답</summary>

```text
3 → 5
```

`useState(3)`으로 초기 State가 `3`이고,

```jsx
setCount(count + 2);
```

가 실행되면서 다음 렌더링의 State가 `5`가 된다.

</details>

---

### 일반 변수라면?

```jsx
function Counter() {
  let count = 0;

  function handleClick() {
    count += 1;
  }

  return <button onClick={handleClick}>{count}</button>;
}
```

`count` 값 자체는 이벤트 핸들러에서 변경될 수 있지만 React에게 **다시 렌더링하라고 요청하지 않는다.**

따라서 화면 업데이트가 필요한 데이터라면 State를 사용해야 한다.

---

## 헷갈리기 쉬운 점

### `setCount`가 변수에 직접 값을 넣는 것은 아니다

```jsx
setCount(count + 1);
```

를

```jsx
count = count + 1;
```

과 동일하게 생각하면 안 된다.

`setCount`는 **다음 렌더링에서 사용할 State 변경을 React에 요청하는 함수**다.

---

### 모든 변수를 State로 만들 필요는 없다

화면에 영향을 주지 않거나 렌더링 사이에 기억할 필요가 없는 값까지 State로 만들 필요는 없다.

예를 들어:

```jsx
const fullName = firstName + lastName;
```

기존 값으로 계산할 수 있는 값이라면 별도의 State가 필요하지 않을 수 있다.

---

## 취준 포인트

### Q. React에서 일반 변수와 State의 차이는?

**일반 변수는 렌더링 사이에서 값이 유지되지 않고 값이 변경되어도 리렌더링을 발생시키지 않는다. State는 렌더링 사이에서 값을 유지하고 setter를 통해 변경하면 React가 새로운 값을 반영하기 위해 다시 렌더링한다.**

### Q. `useState`는 무엇을 반환하는가?

```jsx
const [state, setState] = useState(initialValue);
```

두 개의 값을 가진 배열을 반환한다.

1. 현재 State
2. State를 변경하는 setter 함수

---

## 오늘의 한 줄 정리

> **State는 컴포넌트가 렌더링 사이에서 값을 기억하고, 값의 변화를 화면에 반영할 수 있게 해주는 React의 상태 관리 방식이다.**