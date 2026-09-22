# 🛠️ Git Troubleshooting Log

> 팀 협업 과정에서 수행한 Git 트러블슈팅 실습의 상황, 해결 과정, 결과를 기록한다.
> 모든 기록은 다른 팀원이 동일한 상황에서 재현할 수 있도록 작성한다.

---

## 1. `git commit --amend`

### 참여자

* 담당자: **강소연**
* 실습일: `2026-09-22`
* 브랜치: `feature/sy-`

### 상황

`docs/CONTRIBUTING.md`를 수정하여 커밋하는 과정에서 커밋 메시지에 `-revert`라는 불필요한 내용이 포함되었다.

아직 다른 팀원에게 공유하지 않은 로컬 커밋이었기 때문에 기존 커밋을 삭제하고 다시 생성하는 대신, `git commit --amend`를 사용하여 **가장 최근 커밋의 메시지를 수정하는 상황**을 재현하였다.

* 수정 전 커밋 메시지: `docs: 트러블슈팅 실습 브랜치 예시에서 -revert 젝ㅓ`
* 수정해야 하는 내용: 커밋 메시지의 오타 및 잘못된 표현 수정
* 해당 커밋의 상태: 로컬 커밋
* 수정 대상 파일: `docs/CONTRIBUTING.md`

### 실행 과정

docs/CONTRIBUTING.md 수정 후 커밋하는 과정에서 커밋 메시지에 잘못된 내용이 포함되었다.

아직 다른 팀원에게 공유하지 않은 로컬 커밋이었기 때문에 git commit --amend를 사용하여 최근 커밋의 메시지를 수정하였다.


```bash
PS G:\내 드라이브\Codyssey\02_AI_Tools\B2-2\B2-2> git add docs/CONTRIBUTING.md
PS G:\내 드라이브\Codyssey\02_AI_Tools\B2-2\B2-2> git commit -m "docs: 트러블슈팅 실습 브랜치 예시에서 -revert 젝ㅓ"
[feature/sy-fix-contributing-branch-example 7f3e97a] docs: 트러블슈팅 실습 브랜치 예시에서 -revert 젝ㅓ
 1 file changed, 1 insertion(+), 1 deletion(-)

PS G:\내 드라이브\Codyssey\02_AI_Tools\B2-2\B2-2> git log -1 --oneline
7f3e97a (HEAD -> feature/sy-fix-contributing-branch-example) docs: 트러블슈팅 실습 브랜치 예시에서 -revert 젝ㅓ

PS G:\내 드라이브\Codyssey\02_AI_Tools\B2-2\B2-2> git commit --amend -m "docs: 트러블슈팅 실습 브랜치 예시에서 -revert 제거"
[feature/sy-fix-contributing-branch-example 5cfcaa0] docs: 트러블슈팅 실습 브랜치 예시에서 -revert 제거
 Date: Tue Sep 22 15:52:14 2026 +0900
 1 file changed, 1 insertion(+), 1 deletion(-)

PS G:\내 드라이브\Codyssey\02_AI_Tools\B2-2\B2-2> git log -1 --oneline
5cfcaa0 (HEAD -> feature/sy-fix-contributing-branch-example) docs: 트러블슈팅 실습 브랜치 예시에서 -revert 제거
```


### 결과

* 수정 전 커밋

  * Hash: `7f3e97a`
  * Message: `docs: 트러블슈팅 실습 브랜치 예시에서 -revert 젝ㅓ`

* 수정 후 커밋

  * Hash: `5cfcaa0`
  * Message: `docs: 트러블슈팅 실습 브랜치 예시에서 -revert 제거`

`git commit --amend`를 실행한 후 기존 커밋의 해시가 `7f3e97a`에서 `5cfcaa0`으로 변경되었으며, 가장 최근 커밋의 메시지가 원하는 내용으로 수정된 것을 확인하였다.

### Why

`git commit --amend`는 **가장 최근의 커밋을 수정**할 때 사용하는 명령이다.

이번 실습에서는 아직 다른 팀원에게 공유하지 않은 로컬 커밋의 커밋 메시지에 잘못된 내용이 포함된 상황을 재현하고, 해당 커밋을 새로운 커밋으로 다시 생성하면서 메시지를 수정하기 위해 `git commit --amend`를 사용하였다.

### 주의사항

`git commit --amend`를 사용하면 기존 커밋의 내용이 변경되면서 **커밋 해시도 변경된다.**

따라서 이미 원격 저장소에 push했거나 다른 팀원과 공유한 커밋을 amend하면 기존 커밋과 다른 새로운 이력이 만들어질 수 있으므로 협업 상황에서는 주의해야 한다.

---

## 2. `git reset --soft HEAD~1`

### 참여자

* 담당자: **유영민**
* 실습일: `2026-09-22`
* 브랜치: `feature/Min-troubleshoot`

### 상황

로컬에서 커밋을 완료했지만 파일을 잘못 포함해서 **최근 커밋을 취소하고 변경 사항은 그대로 유지해야 하는 상황**을 재현했다.

* 취소 대상 커밋: `e2f4bf8 (HEAD -> feature/Min-troubleshoot) docs: 트러블슈팅 로그 문서 추가`
* 취소 사유: `truoubleshoot_example.md 파일이 잘못 포함됨.`
* 해당 커밋의 상태: `로컬`

### 실행 과정

```bash
PS C:\Users\dudals\Downloads\B2-2> git add .
PS C:\Users\dudals\Downloads\B2-2> git commit -m "docs: 트러블슈팅 로그 문서 추가"  
[feature/Min-troubleshoot e2f4bf8] docs: 트러블슈팅 로그 문서 추가
 2 files changed, 289 insertions(+)
 create mode 100644 docs/troubleshooting-log.md
 create mode 100644 docs/truoubleshoot_example.md

PS C:\Users\dudals\Downloads\B2-2> git log -1 --oneline
e2f4bf8 (HEAD -> feature/Min-troubleshoot) docs: 트러블슈팅 로그 문서 추가
PS C:\Users\dudals\Downloads\B2-2> git reset --soft HEAD~1
PS C:\Users\dudals\Downloads\B2-2> git status
On branch feature/Min-troubleshoot
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   docs/troubleshooting-log.md
        new file:   docs/truoubleshoot_example.md

PS C:\Users\dudals\Downloads\B2-2> git log -1 --oneline
6886022 (HEAD -> feature/Min-troubleshoot, origin/feature/Min-profile, feature/Min-profile) docs: 유영민 팀원 소개 문서 수정2
```

### 결과

* 최근 커밋이 히스토리에서 취소되었다.
* 작업 파일의 변경 내용은 유지되었다.
* 변경 내용이 `staged` 상태로 유지되는 것을 확인했다.


### Why

`--soft` 옵션은 **HEAD만 이전 커밋으로 이동시키고 작업 내용과 staging 상태는 유지**한다.

따라서 이미 작업한 내용을 잃지 않고 커밋만 다시 작성해야 하는 이번 상황에 적합했다.

### 주의사항

`reset`은 커밋 히스토리를 변경할 수 있으므로 이미 원격에 공유된 커밋에 대해서는 팀 합의 없이 사용하지 않는다.

---

## 3. `git revert`

### 참여자

* 담당자: **유영민**
* 실습일: `2026-09-22`
* 브랜치: `feature/Min-troubleshoot`

### 상황

`feature/Min-troubleshoot` 브랜치에서 `truoubleshoot_example.md`라는 더미 파일을 생성하여 테스트용 커밋을 만들었다.

이후 해당 커밋의 변경 내용을 취소하는 상황을 재현하였다. 단순히 커밋 이력을 삭제하는 것이 아니라, **기존 커밋은 그대로 남기면서 해당 커밋에서 추가된 변경 내용만 되돌리기 위해 `git revert`를 사용하였다.**

* 취소 대상 커밋: `truoubleshoot_example.md` 추가 커밋
* 문제 내용: 테스트를 위해 추가한 더미 파일의 변경 내용을 취소할 필요가 있었음
* 해당 커밋의 상태: `feature/Min-troubleshoot` 브랜치에 커밋 완료

### 실행 과정

먼저 `truoubleshoot_example.md` 더미 파일을 생성하고 커밋하였고 이후 커밋 해시를 확인한 뒤 해당 커밋을 `git revert`로 되돌렸다. 마지막으로 `git log`와 `git status`를 통해 결과를 확인하였다.

```bash
PS C:\Users\dudals\Downloads\B2-2> git add docs/truoubleshoot_example.md

PS C:\Users\dudals\Downloads\B2-2> git commit -m "docs: revert 실습용 더미 파일 추가"
[feature/Min-troubleshoot 75a01ce] docs: revert 실습용 더미 파일 추가
 1 file changed, 1 insertion(+)
 create mode 100644 docs/truoubleshoot_example.md

PS C:\Users\dudals\Downloads\B2-2> git log -1 --oneline
75a01ce (HEAD -> feature/Min-troubleshoot) docs: revert 실습용 더미 파일 추가

PS C:\Users\dudals\Downloads\B2-2> git revert 75a01ce
[feature/Min-troubleshoot 1c3960f] Revert "docs: revert 실습용 더미 파일 추가"
 1 file changed, 1 deletion(-)
 delete mode 100644 docs/truoubleshoot_example.md

PS C:\Users\dudals\Downloads\B2-2> git log --oneline -3
1c3960f (HEAD -> feature/Min-troubleshoot) Revert "docs: revert 실습용 더미 파일 추가"
75a01ce docs: revert 실습용 더미 파일 추가
6886022 (origin/feature/Min-profile, feature/Min-profile) docs: 유영민 팀원 소개 문서 수정2

PS C:\Users\dudals\Downloads\B2-2> git status
On branch feature/Min-troubleshoot
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        docs/troubleshooting-log.md

nothing added to commit but untracked files present (use "git add" to track)

PS C:\Users\dudals\Downloads\B2-2>
```

### 결과

* `truoubleshoot_example.md`를 추가했던 기존 커밋은 Git 히스토리에 그대로 남았다.
* 기존 커밋의 변경 내용을 반대로 적용하는 새로운 `revert` 커밋이 생성되었다.
* `truoubleshoot_example.md` 파일이 제거되어 기존 변경 사항이 취소된 것을 확인하였다.
* `git log`를 통해 기존 커밋과 `revert` 커밋이 모두 존재하는 것을 확인하였다.
* 취소 대상 커밋: `75a01ce`
* 생성된 revert 커밋: `1c3960f`

### Why

이번 실습에서는 커밋 자체를 삭제하는 것이 아니라, **특정 커밋에서 발생한 변경 사항을 되돌리면서 해당 작업 이력은 그대로 남기는 것**을 확인하기 위해 `git revert`를 사용하였다.

`git revert`는 기존 커밋을 삭제하거나 히스토리를 변경하는 대신, 기존 커밋의 변경 내용을 반대로 적용하는 새로운 커밋을 생성한다.

따라서 기존 커밋과 변경 사항을 되돌린 기록을 모두 확인할 수 있다는 점에서 `reset`과 차이가 있다.

### `reset`과의 차이

이번 실습에서는 다음과 같은 차이를 확인하였다.

```text
git reset

→ 브랜치의 HEAD를 이전 커밋으로 이동시켜 커밋 이력을 되돌릴 수 있음

git revert

→ 기존 커밋은 유지
→ 변경 내용을 취소하는 새로운 커밋 생성
```

이번 상황에서는 `truoubleshoot_example.md`를 추가했던 커밋의 이력을 삭제하지 않고, 해당 변경을 취소한 사실까지 커밋 기록으로 남기기 위해 `revert`를 사용하였다.

### 주의사항

`git revert`는 되돌리고 싶은 커밋의 변경 내용을 반대로 적용하기 때문에, 실행 전에 `git log --oneline`을 통해 **정확한 커밋 해시를 확인해야 한다.**

또한 되돌리려는 커밋 이후에 다른 변경 사항이 추가되어 있다면 충돌이 발생할 수 있으므로, 실행 후 `git status`를 통해 작업 상태를 확인하는 것이 필요하다.


---

## 4. `git stash / git stash pop`

### 참여자

* 담당자: **남정현**
* 실습일: `2026-09-22`
* 작업 브랜치: `feature/`
* 전환 대상 브랜치: `feature/`

### 상황

작업 중인 변경 사항을 아직 커밋하고 싶지 않은 상태에서 **다른 브랜치의 작업을 확인하거나 처리해야 하는 상황**을 재현했다.

* 작업 중인 파일:
* 작업 내용:
* 브랜치를 전환해야 했던 이유:

### 실행 과정

```bash

```

### 결과

* 커밋하지 않은 작업 내용을 stash에 임시 저장했다.
* 작업 트리가 깨끗해진 상태에서 다른 브랜치로 이동했다.
* 원래 브랜치로 돌아온 후 `git stash pop`을 실행했다.
* 기존 작업 내용이 정상적으로 복구되었음을 확인했다.

### Why

아직 완료되지 않은 작업을 임시 커밋으로 남기지 않고 다른 브랜치로 이동해야 했기 때문에 `git stash`를 사용했다.

작업을 다시 이어가기 위해 `git stash pop`으로 보관된 변경 사항을 복구했다.

### 주의사항

* `git stash`는 기본적으로 추적되지 않은 파일까지 모두 보관하지 않는다.
* 필요한 경우 `git stash -u`를 사용한다.
* `git stash pop`은 적용 후 stash 항목을 제거한다.
* stash는 로컬에 저장되므로 원격 저장소에 자동으로 공유되지 않는다.

---

# 👥 팀원별 참여 현황

> 과제 조건: **모든 팀원은 최소 1개 이상의 시나리오에 참여해야 한다.**

| 팀원   | amend | reset | revert | stash | 담당 시나리오  |
| ------ | :---: | :---: | :----: | :---: | -------------- |
| 강소연 |   ✅   |       |        |       | amend          |
| 유영민 |       |   ✅   |   ✅    |       | reset / revert |
| 남정현 |       |       |        |   ✅   | stash          |



---

# ✅ 제출 전 체크리스트

### 필수 시나리오

* [ ] `git commit --amend` 수행 및 기록
* [ ] `git reset --soft HEAD~1` 수행 및 기록
* [ ] `git revert` 수행 및 기록
* [ ] `git stash / git stash pop` 수행 및 기록

### 팀원 참여

* [ ] 모든 팀원이 최소 1개 시나리오에 참여
* [ ] 각 기록에 참여자의 이름과 실행과정 작성
* [ ] 실행 명령 및 결과 기록

### 기록 품질

* [ ] 문제 상황을 구체적으로 작성
* [ ] 실제 실행한 명령을 기록
* [ ] 해결 결과를 명확하게 작성
* [ ] 해당 명령을 선택한 이유(Why) 작성
