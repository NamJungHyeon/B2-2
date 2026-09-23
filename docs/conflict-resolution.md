# Conflict Resolution Log

B2-2 팀이 수행한 충돌 실습 기록이다. 각 기록은 당시 상태를 재현할 수 있도록
브랜치 이름뿐 아니라 충돌 직전 양쪽 커밋 해시를 함께 남긴다.
브랜치는 이후 작업으로 다른 커밋을 가리킬 수 있기 때문이다.

---

## 충돌 기록 #1: README 프로젝트 소개 문장 병합

### 1. 기본 정보

- 발생 날짜: 2026-09-22
- 충돌 파일: `README.md`
- 충돌 발생 브랜치: `feature/sy-conflict-1-retry`
- 먼저 병합된 브랜치: `feature/Nam-conflict-1-retry`
- PR 대상 브랜치: `main`
- 충돌 해결자: 강소연 (`@soy7yos`)
- 관련 팀원: 남정현 (`@NamJungHyeon`, 선병합 PR 작성자)
- 해결 환경: GitHub 웹 충돌 해결 편집기 (남정현 PC에서 함께 합의해 사용, 커밋 author `Nam Jung Hyun`, committer `GitHub` 자동 서명)
- 관련 Issue: [#15](https://github.com/NamJungHyeon/B2-2/issues/15) (선병합, 남정현), [#17](https://github.com/NamJungHyeon/B2-2/issues/17) (충돌유발, 강소연)
- 관련 PR: [PR #16](https://github.com/NamJungHyeon/B2-2/pull/16) (선병합), [PR #18](https://github.com/NamJungHyeon/B2-2/pull/18) (충돌 해결)

충돌 전후 커밋:

| 구분 | 커밋 |
| --- | --- |
| 공통 기준 커밋 | `2e1deec` (Merge pull request #14) |
| 충돌 브랜치 커밋 (HEAD) | `7e28eb1` |
| 병합해 온 main | `8b58cf2` (PR #16 병합 커밋) |
| main → feature 병합(충돌 해결) 커밋 | `9c66e85` |
| PR #18의 main 최종 병합 커밋 | `8885aca` |

### 2. 충돌 상황

두 브랜치 모두 공통 기준 커밋 `2e1deec`에서 분기해 `README.md`의 **3~4번째 줄**
(제목 `# B2-2 github-workflow-practice` 바로 아래 소개 문장 2줄)을 서로 다르게 고쳤다.

기준 커밋의 원문:

```
GitHub Flow 기반 협업 워크플로우를 연습하는 팀 저장소입니다.
이 저장소는 Issue와 Pull Request를 활용한 Git 협업 실습 과정을 기록합니다.
```

- 남정현(`feature/Nam-conflict-1-retry`): 팀원 이름과 실습 항목이 드러나도록 수정
- 강소연(`feature/sy-conflict-1-retry`): 저장소의 목적과 정리 방식이 드러나도록 수정

남정현의 PR #16이 먼저 `main`에 병합된 뒤 강소연이 최신 `main`을 병합하자,
같은 파일의 같은 hunk를 양쪽이 다르게 수정했으므로 Git이 어느 쪽을 남길지
판단하지 못해 충돌이 발생했다.

### 3. 재현 명령

```
git fetch origin
git switch feature/sy-conflict-1-retry
git merge origin/main
```

실행 결과:

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

`git status --short` 출력:

```
UU README.md
```

재현 기준:

- 기준 파일: `README.md`
- 비교할 상태: 충돌 브랜치 `7e28eb1`, 병합해 온 main `8b58cf2`
- 충돌 원인: 두 브랜치가 `2e1deec`에서 분기해 README 3~4행을 서로 다르게 수정

해결 이후의 최신 브랜치끼리 병합하면 같은 충돌이 발생하지 않는다.
재현할 때는 위 두 커밋 해시를 사용해야 한다.

### 4. 실제 충돌 내용

```
# B2-2 github-workflow-practice

<<<<<<< HEAD
B2-2 팀이 GitHub Flow 기반 협업 워크플로우를 익히기 위해 만든 저장소입니다.
브랜치 전략, PR 리뷰, 충돌 해결, 트러블슈팅 과정을 팀원별로 정리합니다.
=======
강소연, 남정현, 유영민 세 명이 GitHub Flow로 협업하는 연습 저장소입니다.
Issue, PR, 코드 리뷰, 충돌 해결, Git 복구 실습의 전 과정을 기록으로 남깁니다.
>>>>>>> 8b58cf2

## 팀원 소개
```

- `<<<<<<< HEAD` 아래: 현재 체크아웃한 브랜치(`feature/sy-conflict-1-retry`)의 내용
- `=======`: 두 변경 영역의 경계
- `>>>>>>> 8b58cf2` 위: 병합해 오는 쪽(최신 `main`, PR #16)의 내용

### 5. 비자명 충돌로 판단한 이유

같은 파일의 같은 hunk를 양쪽 브랜치가 각각 수정했고, 두 변경이 같은 자리를
차지하려 했다. 어느 한쪽을 기계적으로 고를 수 없고 문장의 의미를 비교해야 했다.

- HEAD만 유지하면 팀원 이름이 README 첫 문단에서 사라진다.
- Incoming만 유지하면 "팀원별로 정리한다"는 저장소 구조 설명이 사라진다.
- 네 줄을 단순히 이어 붙이면 같은 내용을 두 번 말하는 중복 문단이 된다.

### 6. 해결 전략

PR #18 코멘트에서 두 문장의 의도를 비교한 뒤 **`choose one` (Incoming 채택)** 으로 합의했다.

선택 근거:

- 두 문장 모두 "GitHub Flow 협업 실습 저장소"라는 같은 사실을 다른 표현으로 말하고 있어
  합치면 중복이 된다. 이 경우 `keep both`는 문서 품질을 떨어뜨린다.
- Incoming(남정현) 1행에는 팀원 세 명의 이름이 들어 있어, 바로 아래 "팀원 소개" 절과
  자연스럽게 이어진다.
- Incoming 2행의 "Issue, PR, 코드 리뷰, 충돌 해결, Git 복구"는 이번 미션에서 실제로
  수행하는 항목을 그대로 나열하고 있어, 저장소를 처음 보는 사람에게 더 구체적이다.
- HEAD(강소연)의 "팀원별로 정리합니다"는 README 아래쪽 "폴더 구조" 절에서 이미
  설명하고 있으므로 첫 문단에서 빠져도 정보가 사라지지 않는다.

충돌 마커 3줄과 HEAD 쪽 2줄을 삭제하고 Incoming 2줄만 남겼다.

### 7. 검증 결과

```
grep -n '<<<<<<<\|=======\|>>>>>>>' README.md
```

출력 없음. 그 밖에 다음을 확인했다.

- 해결 후 README 3~4행이 PR #16의 문장과 일치한다.
- 팀원 소개 링크 3개(`team/soyeon.md`, `team/junghyun.md`, `team/min.md`)가 정상 동작한다.
- 폴더 구조 코드 블록과 표가 깨지지 않았다.
- PR #18에서 충돌 표시가 사라지고 병합 가능 상태가 됐다.
- 해결 커밋 `9c66e85`가 `7e28eb1`과 `8b58cf2` 두 개를 부모로 갖는 merge commit이다.

### 8. 결과

- 충돌 해결 커밋: [`9c66e85`](https://github.com/NamJungHyeon/B2-2/commit/9c66e85)
- 최종 병합 커밋: [`8885aca`](https://github.com/NamJungHyeon/B2-2/commit/8885aca)
- 결과: README 첫 문단이 팀원 이름과 실습 항목을 드러내는 2줄로 정리됐다.

### 9. 실패한 1차 시도와 원인

이번 실습은 **두 번째 시도**다. 1차 시도([Issue #9](https://github.com/NamJungHyeon/B2-2/issues/9),
[Issue #13](https://github.com/NamJungHyeon/B2-2/issues/13), [PR #10](https://github.com/NamJungHyeon/B2-2/pull/10),
[PR #14](https://github.com/NamJungHyeon/B2-2/pull/14))에서는 충돌이 전혀 발생하지 않았다.

원인은 **분기 시점**이었다.

| | 계획 | 1차 시도 실제 |
| --- | --- | --- |
| 강소연 브랜치의 분기점 | `0808a22` (남정현 PR 병합 **전**) | `c7c6599` (남정현 PR #10 병합 **후**) |
| 두 브랜치의 merge-base | `0808a22` | `c788b02` |

강소연이 PR #10 병합 후의 최신 `main`에서 브랜치를 만들었기 때문에,
강소연 브랜치에는 남정현의 변경이 **이미 포함**되어 있었다. Git 입장에서는
두 사람이 같은 곳을 다르게 고친 것이 아니라 강소연이 남정현의 결과물 위에
한 줄을 더 고친 것이어서, 갈라진 역사가 없으니 충돌이 날 수 없었다.

2차 시도에서는 기준 커밋을 `2e1deec`로 고정하고, **남정현 PR #16을 병합하기 전에**
강소연이 브랜치를 만들어 push하는 순서를 지켜 충돌을 재현했다.

분기점 확인 명령:

```
git merge-base origin/main origin/feature/sy-conflict-1-retry
```

### 10. 배운 점

- 충돌은 "같은 파일을 고쳤는지"가 아니라 **"두 브랜치의 merge-base 이후 같은 hunk를
  각각 고쳤는지"** 로 결정된다. 상대 PR이 병합된 뒤에 브랜치를 만들면 아무리 같은 줄을
  고쳐도 충돌이 나지 않는다.
- 브랜치를 만들기 전에 `git log --oneline -1`로 기준 커밋을 확인하고, 두 사람이 같은
  해시를 보고 있는지 Issue에 적어 두면 이번 같은 실패를 막을 수 있다.
- `keep both`가 항상 정답은 아니다. 두 변경이 같은 사실을 다르게 서술한 경우에는
  합치면 중복이 되므로, 한쪽을 선택하고 그 이유를 기록하는 편이 문서 품질에 낫다.

---

## 충돌 기록 #2: `team/min.md` 삭제와 내용 수정 충돌 (modify/delete)

### 1. 기본 정보

- 발생 날짜: 2026-09-22
- 충돌 파일: `team/min.md`
- 충돌 발생 브랜치: `feature/sy-conflict-2-retry`
- 먼저 병합된 브랜치: `feature/Min-conflict-2-retry`
- PR 대상 브랜치: `main`
- 충돌 해결자: 강소연 (`@soy7yos`)
- 관련 팀원: 유영민 (`@imyoman99`, 선병합 PR 작성자)
- 해결 환경: 로컬 `git merge`
- 관련 Issue: [#25](https://github.com/NamJungHyeon/B2-2/issues/25) (선병합, 유영민), [#26](https://github.com/NamJungHyeon/B2-2/issues/26) (충돌유발, 강소연)
- 관련 PR: [PR #27](https://github.com/NamJungHyeon/B2-2/pull/27) (선병합), [PR #28](https://github.com/NamJungHyeon/B2-2/pull/28) (충돌 해결)

충돌 전후 커밋:

| 구분 | 커밋 |
| --- | --- |
| 공통 기준 커밋 | `730d2c8` (Merge pull request #24) |
| 충돌 브랜치 커밋 (HEAD) | `f97554a` |
| 병합해 온 main | `5ce9c85` (PR #27 병합 커밋) |
| main → feature 병합(충돌 해결) 커밋 | `646730a` |
| PR #28의 main 최종 병합 커밋 | `4e7dda6` |

### 2. 충돌 상황

미션 요구사항의 비자명 충돌 두 유형 중 **"한쪽은 파일 삭제, 다른 한쪽은 내용 수정"**
유형을 재현했다. 두 브랜치 모두 `730d2c8`에서 분기했다.

- 유영민(`feature/Min-conflict-2-retry`, 커밋 `50c6c9d`): `team/min.md`를 **삭제**했다.
  앞선 PR #23에서 같은 내용을 `docs/youngmin.md`로 복사해 두었기 때문에,
  원본을 지워 파일 이동을 완성하려는 변경이었다. 같은 커밋에서
  `docs/SUBMISSION.md`와 `docs/troubleshooting-log.md`도 추가했다.
- 강소연(`feature/sy-conflict-2-retry`, 커밋 `f97554a`): `team/min.md`의 **내용을 수정**했다.
  `국내힙합` → `국내 힙합` 띄어쓰기 교정, 마지막 줄 `미션 화이팅입니다!!! 👋` →
  `**"미션 화이팅입니다!!!"** 👋` 강조 표기 통일.

유영민의 PR #27이 먼저 병합된 뒤 강소연이 최신 `main`을 병합하자,
한쪽이 지운 파일을 다른 쪽이 수정한 상태여서 Git이 "삭제를 따를지, 수정을 살릴지"를
스스로 판단하지 못해 `modify/delete` 충돌이 발생했다.

### 3. 재현 명령

```
git fetch origin
git switch feature/sy-conflict-2-retry
git merge origin/main
```

실행 결과:

```
CONFLICT (modify/delete): team/min.md deleted in 5ce9c85 and modified in HEAD.  Version HEAD of team/min.md left in tree.
Automatic merge failed; fix conflicts and then commit the result.
```

`git status --short` 출력:

```
A  docs/SUBMISSION.md
A  docs/troubleshooting-log.md
UD team/min.md
```

`git ls-files -u` 출력:

```
100644 2fadcccb7099d3e345731623080989c9c02d880a 1	team/min.md
100644 80aed1fc3429d8b7fef8c5dbf841e5ca2798ef40 2	team/min.md
```

### 4. 실제 충돌 내용

내용 충돌(#1)과 달리 **파일 안에 충돌 마커가 생기지 않는다.** 한쪽에는 파일이
아예 없으므로 줄 단위로 비교할 대상이 없기 때문이다. 대신 Git은

- 작업 트리에 HEAD 버전(`team/min.md`, 강소연이 수정한 내용)을 그대로 남기고,
- 인덱스에는 **stage 1(공통 조상)과 stage 2(HEAD)만** 등록한다.
  삭제된 쪽인 stage 3(병합해 오는 쪽)은 존재하지 않는다.

`git status --short`의 `UD`는 `U`(unmerged, 우리 쪽 수정) + `D`(상대 쪽 삭제)를 뜻한다.

양쪽 버전:

- incoming (병합해 온 main, 유영민 `50c6c9d`): 파일 자체가 삭제됨 — 비교할 내용 없음
- HEAD (강소연 `f97554a`, 작업 트리에 남는 버전):

  ```diff
  - 🎵 좋아하는 음악: 국내힙합
  + 🎵 좋아하는 음악: 국내 힙합
  ...
  - 미션 화이팅입니다!!! 👋
  + **"미션 화이팅입니다!!!"** 👋
  ```

해결하려면 마커를 지우는 대신 **둘 중 하나를 명령으로 선언**해야 한다.

```
git add team/min.md      # 파일을 살린다 (수정 채택)
git rm team/min.md       # 파일을 지운다 (삭제 채택)
```

### 5. 비자명 충돌로 판단한 이유

- 미션 요구사항이 정한 비자명 충돌 두 유형 중 "한쪽은 파일 이동/이름 변경(또는 삭제),
  다른 한쪽은 내용 수정" 유형에 해당한다.
- 삭제를 따르면 강소연의 띄어쓰기·표기 수정이 사라진다.
- 수정을 살리면 `docs/youngmin.md`와 `team/min.md`가 동시에 존재해
  유영민의 소개 파일이 두 벌이 된다.
- 어느 쪽도 자동으로 옳지 않고, "유영민의 소개 파일을 어느 경로에 둘 것인가"라는
  저장소 구조 결정을 내려야 해결되는 충돌이었다.

### 6. 해결 전략

강소연과 유영민이 협의해 **`team/min.md`를 살리는 쪽(수정 채택)** 으로 합의했다.

선택 근거:

- `README.md`의 팀원 소개 목록이 `team/min.md`를 가리키고 있어, 파일을 지우면
  README 링크가 깨진다.
- 미션 요구사항 10-(B)는 "`team/`에 팀원별 소개 파일"을 요구하므로,
  소개 파일의 정본은 `team/` 아래에 있어야 한다.
- 강소연의 수정(띄어쓰기, 강조 표기 통일)은 다른 팀원 소개 파일과 표기를 맞추는
  변경이라 버릴 이유가 없다.

수행한 명령:

```
git add team/min.md
git commit -m "docs: main 병합 충돌 해결 - team/min.md 유지 및 내용 반영"
git push origin feature/sy-conflict-2-retry
```

같은 병합에 포함된 `docs/SUBMISSION.md`, `docs/troubleshooting-log.md`는
충돌 대상이 아니므로 그대로 받아들였다.

### 7. 검증 결과

- `git ls-files -u` 출력 없음 (unmerged 항목 제거됨).
- 해결 후 `team/min.md` 내용이 `f97554a`의 내용과 일치한다.
- `README.md`의 `team/min.md` 링크가 정상 동작한다.
- 해결 커밋 `646730a`가 `f97554a`와 `5ce9c85`를 부모로 갖는 merge commit이다.
- PR #28에서 충돌 표시가 사라지고 병합 가능 상태가 됐다.
- force push 없이 일반 merge와 일반 push로 해결했다.

### 8. 결과

- 충돌 해결 커밋: [`646730a`](https://github.com/NamJungHyeon/B2-2/commit/646730a)
- 최종 병합 커밋: [`4e7dda6`](https://github.com/NamJungHyeon/B2-2/commit/4e7dda6)
- 결과: `team/min.md`가 강소연의 수정 내용을 담은 채 유지됐다.

### 9. 남은 문제 (후속 조치 필요)

이번 해결로 `team/min.md`와 `docs/youngmin.md`에 유영민의 소개가 **두 벌** 남았고,
두 파일의 내용이 서로 다르다(`docs/youngmin.md`에는 강소연의 수정이 반영되지 않음).

- `team/min.md`: 정본. README가 링크하고 있다.
- `docs/youngmin.md`: PR #23에서 복사만 하고 지우지 않은 사본.

후속 PR에서 `docs/youngmin.md`를 삭제해 정리해야 한다.
`docs/`는 협업 규칙과 실습 기록을 두는 폴더이고 팀원 소개는 `team/` 담당이므로,
사본 쪽을 지우는 것이 저장소 구조에 맞다.

별개로, 같은 병합(PR #28)에 딸려 온 `docs/SUBMISSION.md`·`docs/troubleshooting-log.md`(미완성 템플릿)는
PR #27 작업 중 실수로 함께 커밋된 것으로 드러나, 다음날 유영민이 PR #30
([`c287b92`](https://github.com/NamJungHyeon/B2-2/commit/c287b92))으로 삭제해 원복했다.
`troubleshooting-log.md`는 이후 PR #32에서 실제 내용으로 다시 추가됐고,
`SUBMISSION.md`는 재작성 예정이다.

### 10. 실패한 1차 시도와 원인

충돌 실습 2도 **두 번째 시도**이다. 1차 시도([PR #23](https://github.com/NamJungHyeon/B2-2/pull/23),
[PR #24](https://github.com/NamJungHyeon/B2-2/pull/24))에서는 충돌이 발생하지 않았다.

원인은 **"이동"을 실제로 하지 않았기 때문**이다. PR #23의 커밋 `363a62b`는
제목이 "`team/youngmin.md`를 `docs/`로 이동"이었지만, 실제 변경은
`docs/youngmin.md` 45줄 **추가** 하나뿐이었다. `team/min.md`는 그대로 남아 있었다.

```
$ git show 363a62b --stat
 docs/youngmin.md | 45 +++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 45 insertions(+)
```

Git 입장에서는 "새 파일 추가"와 "다른 파일 수정"이라는 서로 무관한 두 변경이므로
자동 병합됐다(`730d2c8`). 2차 시도에서 유영민이 `team/min.md`를 실제로 삭제(`50c6c9d`)하자
비로소 `modify/delete` 충돌이 발생했다.

### 11. 배운 점

- 파일 이동 충돌을 만들려면 **복사가 아니라 이동**이어야 한다. 원본을 지우지 않으면
  Git은 이동으로 인식하지 않고 단순 추가로 처리한다. 커밋 제목이 "이동"이어도
  `git show --stat`에 삭제(`-`)가 없으면 이동이 아니다.
- `modify/delete` 충돌에는 **충돌 마커가 없다.** 마커만 찾다 보면 "충돌이 안 났다"고
  오해하기 쉽다. `git status --short`의 `UD`와 `git ls-files -u`로 확인해야 한다.
- 이 유형의 해결은 마커 정리가 아니라 `git add`(살리기) / `git rm`(지우기) 중
  하나를 **선언**하는 일이다.
- 파일을 옮길 때는 옮긴 뒤 그 파일을 가리키는 링크(README 등)를 같은 PR에서
  함께 고쳐야 한다. 이번처럼 사본이 남으면 어느 쪽이 정본인지 알 수 없게 된다.
