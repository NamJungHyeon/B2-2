# Interactive Rebase 실습 기록 (보너스 과제 1)

`git rebase -i`로 개인 feature 브랜치의 커밋을 squash / reword하여 정리한 기록이다.
정리 전후 히스토리를 비교하고, 협업에서 rebase를 쓸 때의 안전 수칙을 함께 남긴다.

## 1. 기본 정보

- 실습일: 2026-09-23
- 수행자: 남정현 (`@NamJungHyeon`)
- 실습 브랜치: `feature/Nam-rebase-practice`
- 분기 기준 커밋: `c52b4f1` (Merge pull request #34)
- 대상 파일: `src/string_utils.py`
- 사용한 명령: `git rebase -i HEAD~4` (squash), `git rebase -i HEAD~1` (reword)
- **push 하지 않은 로컬 커밋만 대상으로 했다.** 공유된 브랜치나 `main`에는 적용하지 않았다.

## 2. 실습 상황

팀 커밋 컨벤션(`docs/CONTRIBUTING.md` 5절)은 `<type>: <무엇을 어떻게 변경했는지>` 형식을
요구하고, `add` · `wip` · `fix` · `final` 같이 변경 대상을 알 수 없는 메시지를 금지한다.

실습을 위해 `src/string_utils.py`를 네 단계로 나눠 작성하면서, 일부러 금지된 형식의
커밋 메시지를 남겼다. 기능상으로는 "문자열 유틸 함수 2개 추가"라는 하나의 작업이므로
PR을 올리기 전에 커밋 하나로 합치고 메시지를 규칙에 맞게 고치는 것이 목표다.

---

## 3. squash — 4개 커밋을 1개로 합치기

### 3-1. 정리 전 히스토리

```
$ git log --oneline -4
1ff1f2e final
95f3e88 fix
cefb908 wip
57be229 add
```

네 커밋 모두 팀 컨벤션의 금지 예시에 해당한다. 무엇을 바꿨는지 메시지만 보고 알 수 없다.

### 3-2. 실행

```
$ git rebase -i HEAD~4
```

편집기에 열린 todo 목록 원본:

```
pick 57be229 add
pick cefb908 wip
pick 95f3e88 fix
pick 1ff1f2e final
```

첫 줄은 `pick`으로 남기고 나머지 세 줄을 `squash`로 바꿨다.

```
pick 57be229 add
squash cefb908 wip
squash 95f3e88 fix
squash 1ff1f2e final
```

저장하고 닫으면 합쳐진 커밋의 메시지를 작성하는 편집기가 다시 열린다.
기존 네 메시지가 모두 주석 없이 나열되어 있어, 전부 지우고 다음 메시지로 다시 작성했다.

```
feat: 문자열 유틸 함수 reverse, count_words 추가

팀 소개 문서를 다룰 때 쓰는 간단한 문자열 유틸을 추가한다.
- reverse: 문자열을 뒤집는다
- count_words: 공백으로 나눈 단어 개수를 센다
```

실행 결과:

```
 1 file changed, 11 insertions(+)
 create mode 100644 src/string_utils.py
Successfully rebased and updated refs/heads/feature/Nam-rebase-practice.
```

### 3-3. 정리 후 히스토리

```
$ git log --oneline -2
17de07f feat: 문자열 유틸 함수 reverse, count_words 추가
c52b4f1 Merge pull request #34 from NamJungHyeon/feature/sy-conflict-resolution-doc
```

### 3-4. 비교

| | 정리 전 | 정리 후 |
| --- | --- | --- |
| 커밋 수 | 4개 | 1개 |
| 커밋 해시 | `57be229`, `cefb908`, `95f3e88`, `1ff1f2e` | `17de07f` |
| 메시지 | `add`, `wip`, `fix`, `final` (전부 금지 형식) | `feat: 문자열 유틸 함수 reverse, count_words 추가` |
| 파일 최종 내용 | `src/string_utils.py` | **동일** (변경 없음) |

커밋 해시가 **전부 바뀌었다.** 내용은 같지만 Git 입장에서는 새로 만든 커밋이다.
이것이 rebase의 핵심 성질이고, 뒤의 안전 수칙이 필요한 이유다.

---

## 4. reword — 커밋 메시지만 고치기

### 4-1. 정리 전 히스토리

`src/string_utils.py`의 모듈 docstring에 사용 예시를 추가하고 `fix2`로 커밋했다.

```
$ git log --oneline -2
ee5ce9d fix2
17de07f feat: 문자열 유틸 함수 reverse, count_words 추가
```

### 4-2. 실행

```
$ git rebase -i HEAD~1
```

todo 목록에서 `pick`을 `reword`로 바꿨다.

```
reword ee5ce9d fix2
```

저장하면 메시지 편집기가 열리고, 다음으로 고쳤다.

```
docs: 문자열 유틸 사용 예시를 모듈 docstring에 추가
```

### 4-3. 정리 후 히스토리

```
$ git log --oneline -2
5e70748 docs: 문자열 유틸 사용 예시를 모듈 docstring에 추가
17de07f feat: 문자열 유틸 함수 reverse, count_words 추가
```

### 4-4. 비교

| | 정리 전 | 정리 후 |
| --- | --- | --- |
| 커밋 해시 | `ee5ce9d` | `5e70748` |
| 메시지 | `fix2` | `docs: 문자열 유틸 사용 예시를 모듈 docstring에 추가` |
| 변경 내용 | docstring에 사용 예시 추가 | **동일** |

메시지만 고쳐도 해시는 바뀐다. 커밋 해시는 메시지를 포함한 내용 전체의 결과이기 때문이다.

---

## 5. reflog — rebase 이력 확인

rebase는 이전 커밋을 즉시 지우지 않는다. `git reflog`에 과정이 남아 있어 되돌릴 수 있다.

```
$ git reflog -8
5e70748 HEAD@{0}: rebase (finish): returning to refs/heads/feature/Nam-rebase-practice
5e70748 HEAD@{1}: rebase (reword): docs: 문자열 유틸 사용 예시를 모듈 docstring에 추가
ee5ce9d HEAD@{2}: rebase: fast-forward
17de07f HEAD@{3}: rebase (start): checkout HEAD~1
ee5ce9d HEAD@{4}: commit: fix2
17de07f HEAD@{5}: rebase (finish): returning to refs/heads/feature/Nam-rebase-practice
17de07f HEAD@{6}: rebase (squash): feat: 문자열 유틸 함수 reverse, count_words 추가
2470bf5 HEAD@{7}: rebase (squash): # This is a combination of 3 commits.
```

rebase를 잘못했을 때 되돌리는 방법:

```
git reflog                      # 정리 전 커밋 해시 확인
git reset --hard <그 해시>       # 해당 지점으로 복귀
```

rebase 진행 중에 문제가 생기면 중단할 수 있다.

```
git rebase --abort
```

## 6. 검증

- `git log --oneline`으로 정리 전후 커밋 수와 메시지를 비교했다.
- `src/string_utils.py`의 최종 내용이 rebase 전과 동일한지 확인했다.
- 모든 커밋 메시지가 `<type>: <내용>` 형식을 따르는지 확인했다.
- 작업 트리에 미커밋 변경이 남아 있지 않은지 `git status`로 확인했다.

## 7. 왜 rebase가 히스토리를 깨끗하게 만드는가

- 여러 개의 시행착오 커밋을 **작업 단위 하나**로 합칠 수 있다. 리뷰어가 "무엇을 왜
  바꿨는가"만 보면 되므로 PR 리뷰가 쉬워진다.
- `merge`처럼 병합 커밋을 만들지 않고 커밋을 일렬로 세우므로 `git log`가 단순해진다.
- 잘못 쓴 메시지를 push 전에 규칙에 맞게 고칠 수 있다. 팀 커밋 컨벤션을 지키는 마지막
  안전장치가 된다.

## 8. 왜 협업에서는 위험한가

rebase는 기존 커밋을 고치는 것이 아니라 **같은 내용의 새 커밋을 다시 만든다.**
그래서 커밋 해시가 전부 바뀐다. 이 성질이 공유된 브랜치에서 문제를 만든다.

- 이미 push한 브랜치를 rebase하면 원격과 히스토리가 갈라져 일반 `git push`가 거부된다.
  강제로 밀어넣으려면 `--force`가 필요하다.
- 다른 팀원이 그 브랜치를 받아 작업 중이었다면, 그 팀원의 로컬에는 사라진 옛 커밋이
  남아 있다. 다음 pull에서 같은 변경이 두 번 들어오거나 충돌이 난다.
- 강제 push는 원격의 커밋을 덮어쓴다. 그 사이 다른 사람이 올린 커밋이 있으면 사라진다.
- PR에서 이미 받은 리뷰 코멘트는 특정 커밋·특정 줄에 붙어 있다. 그 커밋이 사라지면
  코멘트가 outdated 처리되어 리뷰 이력 추적이 끊긴다. 이번 미션은 리뷰 기록 자체가
  평가 대상이므로 특히 손해가 크다.
- `main`을 rebase하면 팀 전원의 히스토리가 어긋난다. 복구 비용이 가장 크다.

## 9. 안전 수칙

1. **push하지 않은 로컬 커밋에만 쓴다.** 이번 실습도 push 전에 수행했다.
2. **`main`과 공유 브랜치에는 절대 적용하지 않는다.**
3. 이미 push한 개인 브랜치를 정리해야 한다면 팀에 알리고, 그 브랜치를 쓰는 사람이
   없는지 확인한 뒤에만 한다. (`docs/CONTRIBUTING.md` 12절)
4. 강제 push가 필요하면 `--force` 대신 `--force-with-lease`를 쓴다. 내가 마지막으로 본
   원격 상태와 다르면 push가 거부되므로, 남의 커밋을 덮어쓰는 사고를 막는다.
5. rebase 전 `git log --oneline`을 저장해 둔다. 되돌릴 기준점이 된다.
6. 진행 중 충돌이 나거나 의도와 달라지면 `git rebase --abort`로 원상 복구한다.
7. 실수했으면 `git reflog`로 이전 해시를 찾아 `git reset --hard`로 복귀한다.
8. 이미 공유된 잘못된 커밋 메시지는 rebase로 고치지 않는다. PR 본문에 의도를 보완하고
   `docs/troubleshooting-log.md`에 기록을 남긴다. (`docs/CONTRIBUTING.md` 12절)

## 10. 배운 점

- squash와 reword 모두 **커밋 해시를 바꾼다.** "메시지만 고쳤으니 같은 커밋"이 아니다.
  해시는 메시지를 포함한 내용 전체로 계산되기 때문이다.
- 그래서 "이 커밋이 이미 남에게 갔는가"가 rebase를 쓸 수 있는지 판단하는 유일한 기준이다.
  아직 안 갔으면 마음껏 정리해도 되고, 갔으면 손대지 않는다.
- 이번 미션에서는 `merge` 방식을 유지하는 편이 유리하다. 병합 커밋이 브랜치 흐름을
  히스토리에 남겨 `git log --oneline --graph --all` 증빙에 그대로 드러나기 때문이다.
  rebase는 개인 브랜치를 PR로 올리기 **전에** 정리하는 용도로만 썼다.
- `git reflog`가 있어서 rebase는 되돌릴 수 있는 작업이다. 다만 되돌릴 수 있는 것은
  **내 로컬**뿐이고, 강제 push로 원격에 반영된 뒤 남이 받아간 것은 되돌리기 어렵다.
