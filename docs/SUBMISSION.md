# Submission Index

## Team

- 팀명: codyssey B2-2
- 저장소: https://github.com/NamJungHyeon/B2-2
- 기본 브랜치: `main`
- 선택한 결과물: (B) 팀 소개 — `team/` 팀원별 소개 파일 + README 목록

| 팀원   | GitHub                                           | 정리 책임                                                                      | Git 실습 담당                                       |
| ------ | ------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------- |
| 남정현 | [@NamJungHyeon](https://github.com/NamJungHyeon) | 저장소·권한·main 보호, `CONTRIBUTING.md`, `.github/` 템플릿·CODEOWNERS, README | `git stash` / `git stash pop`, `rebase -i` (보너스) |
| 강소연 | [@soy7yos](https://github.com/soy7yos)           | 충돌 실습 일정, `conflict-resolution.md`                                       | `git commit --amend`                                |
| 유영민 | [@imyoman99](https://github.com/imyoman99)       | `troubleshooting-log.md`, 제출 인덱스                                          | `git reset --soft`, `git revert`                    |

### 개인별 기준 충족 현황

| 기준                          | 남정현      | 강소연                | 유영민              |
| ----------------------------- | ----------- | --------------------- | ------------------- |
| 병합된 본인 PR 2개 이상       | 5개         | 7개                   | 5개                 |
| 타인 PR 실질 리뷰 2개 이상    | 2개         | 2개                   | 3개                 |
| 본인 PR 리뷰 반영 1회 이상    | 2회         | 1회 (**답글 미작성**) | 2회                 |
| 소개 파일 기여 커밋 1개 이상  | 2개         | 2개                   | 3개                 |
| 트러블슈팅 기록 참여 1개 이상 | 1개 (stash) | 1개 (amend)           | 2개 (reset, revert) |

---

## 남정현 (`@NamJungHyeon`)

### Issues

| #                                                     | 제목                                                       | 상태            |
| ----------------------------------------------------- | ---------------------------------------------------------- | --------------- |
| [#1](https://github.com/NamJungHyeon/B2-2/issues/1)   | [Docs] 남정현 팀원 소개 문서 작성                          | Closed (PR #4)  |
| [#7](https://github.com/NamJungHyeon/B2-2/issues/7)   | [Chore] 협업 규칙 문서 작성 및 PR·Issue 템플릿 추가        | Closed (PR #8)  |
| [#9](https://github.com/NamJungHyeon/B2-2/issues/9)   | [Conflict] 충돌 실습 1: README 작성 및 동일 영역 충돌 재현 | Closed (PR #10) |
| [#15](https://github.com/NamJungHyeon/B2-2/issues/15) | [Conflict] 충돌 실습 1 재시도 (선병합)                     | Closed (PR #16) |
| [#21](https://github.com/NamJungHyeon/B2-2/issues/21) | [Chore] CODEOWNERS로 파일별 책임 리뷰어 지정               | Closed (PR #22) |
| [#35](https://github.com/NamJungHyeon/B2-2/issues/35) | [Chore] 보너스 과제 1: interactive rebase 히스토리 정리    | Open (PR #36)   |

### Pull Requests

**[PR #4](https://github.com/NamJungHyeon/B2-2/pull/4) — docs: 남정현 팀원 소개 문서 추가** · Merged `69d5b54` · Closes #1
- 변경: `team/junghyun.md` 신규 (+46)
- 커밋: `6cd2300` 소개 문서 추가 → `d06883b` 리뷰 반영(백틱 제거, 역할·학습 목표 추가)
- 리뷰: 강소연 `[P2] Recommend` → 반영 → Approve

**[PR #8](https://github.com/NamJungHyeon/B2-2/pull/8) — chore: 협업 규칙 문서 작성 및 PR·Issue 템플릿 추가** · Merged `0808a22` · Closes #7
- 변경: `docs/CONTRIBUTING.md`, `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/task.md`, `.github/ISSUE_TEMPLATE/config.yml` (+424)
- 커밋: `d2686a7` 규칙·템플릿 작성 → `a5d3e3b` 리뷰 반영(실습용 Issue 템플릿 2종 삭제)
- 리뷰: 강소연 `[P1] Must Fix` → Changes requested → 반영 → Approve, 유영민 Approve

**[PR #10](https://github.com/NamJungHyeon/B2-2/pull/10) — docs: README에 팀원 소개 링크, 폴더 구조, 작업 흐름 추가** · Merged `c7c6599` · Closes #9
- 변경: `README.md` (+61/-2) — 2줄짜리 README를 팀원 소개 링크, 문서 목차, 폴더 구조 트리, 작업 흐름으로 확장
- 커밋: `c788b02` · 리뷰: 강소연 Approve

**[PR #16](https://github.com/NamJungHyeon/B2-2/pull/16) — docs: README 소개 문장을 팀원 이름과 실습 항목 중심으로 수정** · Merged `8b58cf2` · Closes #15
- 변경: `README.md` 3~4행 (+2/-2) · 커밋: `932f550`
- 역할: **충돌 실습 1의 선병합 브랜치.** 기준 커밋 `2e1deec`에서 분기
- 리뷰: 강소연 Approve

**[PR #22](https://github.com/NamJungHyeon/B2-2/pull/22) — chore: CODEOWNERS로 파일별 책임 리뷰어 지정 및 순환 리뷰 규칙 정정** · Merged `9e753cb` · Closes #21
- 변경: `.github/CODEOWNERS` 신규, `docs/CONTRIBUTING.md` 1·7·8절 (+45/-5)
- 커밋: `13f8ed6` · 리뷰: 강소연 Approve
- **보너스 과제 2 (리뷰어 자동화)**

**[PR #36](https://github.com/NamJungHyeon/B2-2/pull/36) — docs: interactive rebase squash·reword 실습 기록 추가** · Open · Closes #35
- 변경: `docs/rebase-practice.md` 신규(239줄), `src/string_utils.py` 신규, `README.md` 링크 추가 (+263/-2)
- 커밋: `17de07f`(squash 결과) → `5e70748`(reword 결과) → `e1e2fc3` 문서 → `8adc050` README
- 리뷰어: 강소연
- **보너스 과제 1 (히스토리 정리)**

### Code Reviews

| 대상 PR                                                                                                                                                       | 작성자         | 내용                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------- |
| [#6](https://github.com/NamJungHyeon/B2-2/pull/6)                                                                                                             | 유영민         | **실질 리뷰** — `[P2] Recommend : 영어를 제외해서 수정하시는걸 추천드립니다.`         |
| [#32](https://github.com/NamJungHyeon/B2-2/pull/32)                                                                                                           | 유영민         | **실질 리뷰** — `[P2] Recommend : 제목에 이모지를 지우는 방향의 수정을 추천드립니다.` |
| [#14](https://github.com/NamJungHyeon/B2-2/pull/14), [#18](https://github.com/NamJungHyeon/B2-2/pull/18), [#30](https://github.com/NamJungHyeon/B2-2/pull/30) | 강소연, 유영민 | 승인                                                                                  |

실질 리뷰 **2개** — 기준 충족.

### Review 반영

| PR                                                | 받은 리뷰                                                            | 반영 커밋 | 답글                                                                                                                              |
| ------------------------------------------------- | -------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [#4](https://github.com/NamJungHyeon/B2-2/pull/4) | `[P2]` 다른 팀원 문서와 표기 통일을 위해 백틱 제거 (강소연)          | `d06883b` | "반영했습니다. d06883b 커밋에서 문서 전체의 백틱을 제거했습니다."                                                                 |
| [#8](https://github.com/NamJungHyeon/B2-2/pull/8) | `[P1] Must Fix` 기록 문서와 중복될 실습용 Issue 템플릿 삭제 (강소연) | `a5d3e3b` | "반영했습니다. a5d3e3b 커밋에서 conflict-practice.md, troubleshooting-practice.md를 삭제했고 CONTRIBUTING.md 6절도 수정했습니다." |

### 결과물 기여 커밋

- `6cd2300` — `team/junghyun.md` 신규 작성
- `d06883b` — 이번 미션 역할과 학습 목표 추가

### 실습 참여

- `git stash` / `git stash pop` (담당) — 브랜치 `feature/Nam-troubleshoot-stash`, [troubleshooting-log.md](docs/troubleshooting-log.md) 4절
- `git rebase -i` squash·reword (보너스) — 브랜치 `feature/Nam-rebase-practice`, [rebase-practice.md](docs/rebase-practice.md)
- 충돌 실습 1 선병합 담당

---

## 강소연 (`@soy7yos`)

### Issues

| #                                                     | 제목                                                | 상태            |
| ----------------------------------------------------- | --------------------------------------------------- | --------------- |
| [#2](https://github.com/NamJungHyeon/B2-2/issues/2)   | [Docs] 강소연 팀원 소개 문서 작성                   | Closed (PR #5)  |
| [#11](https://github.com/NamJungHyeon/B2-2/issues/11) | [Docs] 트러블슈팅 실습 브랜치 예시에서 -revert 제거 | Closed (PR #12) |
| [#13](https://github.com/NamJungHyeon/B2-2/issues/13) | [Conflict] 충돌 실습 1 (충돌유발)                   | Closed (PR #14) |
| [#17](https://github.com/NamJungHyeon/B2-2/issues/17) | [Conflict] 충돌 실습 1 재시도 (충돌유발)            | Closed (PR #18) |
| [#19](https://github.com/NamJungHyeon/B2-2/issues/19) | [Conflict] 충돌 실습 2 (충돌유발)                   | Closed (PR #24) |
| [#26](https://github.com/NamJungHyeon/B2-2/issues/26) | [Conflict] 충돌 실습 2 재시도 (충돌유발)            | Closed (PR #28) |
| [#33](https://github.com/NamJungHyeon/B2-2/issues/33) | [Docs] 충돌 해결 기록 문서 작성                     | Closed (PR #34) |

### Pull Requests

**[PR #5](https://github.com/NamJungHyeon/B2-2/pull/5) — docs: 강소연 팀원 소개 문서 추가** · Merged `04c2a28` · Closes #2
- 변경: `team/soyeon.md` 신규 (+46)
- 커밋: `de3c7fc` 소개 문서 추가 → `3235718` 최애 음료를 `라떼` → `아인슈페너 라떼`로 구체화
- 리뷰: 유영민 `[P2] Recommend` → 반영 → Approve

**[PR #14](https://github.com/NamJungHyeon/B2-2/pull/14) — docs: README 소개 문구 수정** · Merged `2e1deec` · Closes #13
- 변경: `README.md` (+1/-1) — `병합합니다` → `merge합니다` · 커밋: `fd99451`
- 역할: 충돌 실습 1의 **1차 시도**. 분기 시점 문제로 충돌 미발생
- 리뷰: 남정현 Approve

**[PR #18](https://github.com/NamJungHyeon/B2-2/pull/18) — docs: README 소개 문장 수정 및 충돌 해결** · Merged `8885aca` · Closes #17
- 커밋: `7e28eb1` 소개 문장 수정 → `9c66e85` main 병합 충돌 해결(merge commit)
- 역할: **충돌 실습 1의 충돌 발생·해결 브랜치**
- 리뷰: 남정현 Approve

**[PR #24](https://github.com/NamJungHyeon/B2-2/pull/24) — docs: team/min.md 내용 수정** · Merged `730d2c8` · Closes #19
- 변경: `team/min.md` (+2/-2) — `브레이킹배드(Breaking bad)` → `Breaking Bad` 등 표기 정리 · 커밋: `bbb5f01`
- 역할: 충돌 실습 2의 **1차 시도**. 상대가 복사만 하고 원본을 지우지 않아 충돌 미발생
- 리뷰: 유영민 `[P3] FYI` 코멘트 + Approve

**[PR #28](https://github.com/NamJungHyeon/B2-2/pull/28) — docs: team/min.md 내용 수정 및 충돌 해결** · Merged `4e7dda6` · Closes #26
- 커밋: `f97554a` 내용 수정(`국내힙합` → `국내 힙합`, 한마디 강조 표기) → `646730a` modify/delete 충돌 해결(merge commit)
- 역할: **충돌 실습 2의 충돌 발생·해결 브랜치**
- 리뷰: 유영민 Approve

**[PR #12](https://github.com/NamJungHyeon/B2-2/pull/12) — docs: 트러블슈팅 실습 브랜치 예시에서 -revert 제거** · Merged `34440bc` · Closes #11
- 변경: `docs/CONTRIBUTING.md` (+1/-1) · 커밋: `5cfcaa0`
- 이 브랜치에서 `git commit --amend` 실습을 수행
- 리뷰: 유영민 "revert 제거 확인했습니다." + Approve

**[PR #34](https://github.com/NamJungHyeon/B2-2/pull/34) — docs: 충돌 해결 기록 작성** · Merged `c52b4f1` · Closes #33
- 변경: `docs/conflict-resolution.md` 신규 (+388) — 충돌 2건의 기준 커밋·재현 명령·충돌 마커 원문·해결 전략·배운 점
- 리뷰: 유영민 `[P2] Recommend` 어조 통일 제안 → 반영 → "제안드린 문구 수정 사항 확인했습니다. 승인하겠습니다!"

### Code Reviews

| 대상 PR                                                                                                                                                                                                                                                                 | 작성자         | 내용                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [#4](https://github.com/NamJungHyeon/B2-2/pull/4)                                                                                                                                                                                                                       | 남정현         | **실질 리뷰** — `[P2] Recommend: 문서 간 표기 통일을 위해, 다른 팀원들의 문서와 동일하게 백틱을 제거해주시면 좋을 것 같습니다.`                                                                                    |
| [#8](https://github.com/NamJungHyeon/B2-2/pull/8)                                                                                                                                                                                                                       | 남정현         | **실질 리뷰** — `[P1] Must Fix: 추후 문서 내용이 중복되거나 서로 다른 내용으로 작성되는 상황을 방지하기 위해 conflict-practice.md, troubleshooting-practice.md 파일은 삭제 부탁드립니다.` Changes requested로 제출 |
| [#10](https://github.com/NamJungHyeon/B2-2/pull/10), [#16](https://github.com/NamJungHyeon/B2-2/pull/16), [#22](https://github.com/NamJungHyeon/B2-2/pull/22), [#23](https://github.com/NamJungHyeon/B2-2/pull/23), [#27](https://github.com/NamJungHyeon/B2-2/pull/27) | 남정현, 유영민 | 승인                                                                                                                                                                                                               |

실질 리뷰 **2개** — 기준 충족.

### Review 반영

| PR                                                  | 받은 리뷰                                                                             | 반영 커밋                              | 답글                             |
| --------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------- | -------------------------------- |
| [#5](https://github.com/NamJungHyeon/B2-2/pull/5)   | `[P2]` `라떼`가 모호하니 `카페 라떼`, `바닐라 라떼`처럼 구체적인 메뉴명 제안 (유영민) | `3235718` (`라떼` → `아인슈페너 라떼`) | **없음 — 보완 필요**             |
| [#34](https://github.com/NamJungHyeon/B2-2/pull/34) | `[P2]` 어조 통일을 위해 `두 번째 시도다` → `두 번째 시도이다` (유영민)                | 반영 완료                              | "수정했습니다." (커밋 링크 없음) |

### 결과물 기여 커밋

- `de3c7fc` — `team/soyeon.md` 신규 작성
- `3235718` — 리뷰 반영 수정

### 실습 참여

- `git commit --amend` (담당) — 브랜치 `feature/sy-fix-contributing-branch-example`, [troubleshooting-log.md](docs/troubleshooting-log.md) 1절
- 충돌 실습 1·2 모두 **충돌 발생·해결 담당**
- `docs/conflict-resolution.md` 작성 (PR #34)

---

## 유영민 (`@imyoman99`)

### Issues

| #                                                     | 제목                                   | 상태            |
| ----------------------------------------------------- | -------------------------------------- | --------------- |
| [#3](https://github.com/NamJungHyeon/B2-2/issues/3)   | [Docs] 유영민 팀원 소개 문서 작성      | Closed (PR #6)  |
| [#20](https://github.com/NamJungHyeon/B2-2/issues/20) | [Conflict] 충돌 실습 2 (선병합)        | Closed (PR #23) |
| [#25](https://github.com/NamJungHyeon/B2-2/issues/25) | [Conflict] 충돌 실습 2 재시도 (선병합) | Closed (PR #27) |
| [#29](https://github.com/NamJungHyeon/B2-2/issues/29) | [Fix] 잘못 추가된 문서 파일 제거       | Closed (PR #30) |
| [#31](https://github.com/NamJungHyeon/B2-2/issues/31) | [Docs] 트러블슈팅 로그 문서 추가       | Closed (PR #32) |

### Pull Requests

**[PR #6](https://github.com/NamJungHyeon/B2-2/pull/6) — docs: 유영민 팀원 소개 문서 추가** · Merged `a524b03` · Closes #3
- 변경: `team/min.md` 신규 (+45)
- 커밋: `1f50e4b` 소개 문서 추가 → `72fc1d3`, `6886022` 리뷰 반영 수정
- 리뷰: 남정현 `[P2] Recommend` → 반영 → Approve

**[PR #23](https://github.com/NamJungHyeon/B2-2/pull/23) — docs: team/min.md를 docs/youngmin.md로 이동** · Merged `1af7044` · Closes #20
- 변경: `docs/youngmin.md` 신규 (+45) · 커밋: `363a62b`
- 역할: 충돌 실습 2의 **1차 시도 선병합.** 실제로는 복사만 하고 원본을 지우지 않아 충돌 미발생
- 리뷰: 강소연 Approve

**[PR #27](https://github.com/NamJungHyeon/B2-2/pull/27) — docs: team/min.md 삭제** · Merged `5ce9c85` · Closes #25
- 변경: `team/min.md` 삭제, `docs/SUBMISSION.md`·`docs/troubleshooting-log.md` 신규 (+541/-45) · 커밋: `50c6c9d`
- 역할: **충돌 실습 2의 선병합 브랜치.** 원본을 실제로 삭제해 modify/delete 충돌을 성립시킴
- 리뷰: 강소연 Approve

**[PR #30](https://github.com/NamJungHyeon/B2-2/pull/30) — fix: 잘못 추가된 문서 파일 제거** · Merged `d86683d` · Closes #29
- 변경: `docs/SUBMISSION.md`, `docs/troubleshooting-log.md` 삭제 (+0/-541) · 커밋: `c287b92`
- PR #27에 의도치 않게 함께 들어간 문서 2종을 정리
- 리뷰: 남정현 Approve

**[PR #32](https://github.com/NamJungHyeon/B2-2/pull/32) — docs: 트러블슈팅 로그 문서 추가** · Merged `77b1089` · Closes #31
- 변경: `docs/troubleshooting-log.md` 신규 (+357) — amend·reset·revert·stash 4종 기록
- 커밋: `c991ca9` 문서 추가 → `84ff3be` 리뷰 반영(제목 이모지 제거)
- 리뷰: 남정현 `[P2] Recommend` → 반영 → Approve

### Code Reviews

| 대상 PR                                                                                                                                                     | 작성자         | 내용                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [#5](https://github.com/NamJungHyeon/B2-2/pull/5)                                                                                                           | 강소연         | **실질 리뷰** — `[P2] Recommend: 라떼라는 표현이 조금 모호한 것 같습니다. 카페 라떼, 바닐라 라떼처럼 구체적인 메뉴명을 작성하면 사용자가 어떤 메뉴인지 더 쉽게 이해할 수 있을 것 같습니다.` |
| [#24](https://github.com/NamJungHyeon/B2-2/pull/24)                                                                                                         | 강소연         | **실질 리뷰** — `[P3] FYI: 21번 줄 깔끔하게 정리 잘해주셨습니다.` 변경 전후 인용                                                                                                            |
| [#34](https://github.com/NamJungHyeon/B2-2/pull/34)                                                                                                         | 강소연         | **실질 리뷰** — `[P2] Recommend: 문서 전체의 어조 통일과 가독성 향상을 위해 "두 번째 시도다"를 "두 번째 시도이다"로 수정`                                                                   |
| [#8](https://github.com/NamJungHyeon/B2-2/pull/8), [#12](https://github.com/NamJungHyeon/B2-2/pull/12), [#28](https://github.com/NamJungHyeon/B2-2/pull/28) | 남정현, 강소연 | 승인                                                                                                                                                                                        |

실질 리뷰 **3개** — 기준 충족.

### Review 반영

| PR                                                  | 받은 리뷰                                      | 반영 커밋 | 답글                                                                                                                  |
| --------------------------------------------------- | ---------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| [#6](https://github.com/NamJungHyeon/B2-2/pull/6)   | `[P2]` 영어 표기를 제외하고 수정 제안 (남정현) | `6886022` | "말씀해주신 내용 반영하여 34번째 줄의 문구 수정 및 포맷팅 정리 완료했습니다. 변경 전: 뉴욕(New York) / 변경 후: 뉴욕" |
| [#32](https://github.com/NamJungHyeon/B2-2/pull/32) | `[P2]` 제목의 이모지 제거 제안 (남정현)        | `84ff3be` | "의견을 반영하여 docs/troubleshooting-log.md 파일의 최상단 제목에 있던 이모지를 제거했습니다."                        |

### 결과물 기여 커밋

- `1f50e4b` — `team/min.md` 신규 작성
- `72fc1d3`, `6886022` — 리뷰 반영 수정

### 실습 참여

- `git reset --soft HEAD~1` (담당) — 브랜치 `feature/Min-troubleshoot`, [troubleshooting-log.md](docs/troubleshooting-log.md) 2절
- `git revert` (담당) — 브랜치 `feature/Min-troubleshoot`, 3절
- 충돌 실습 2 선병합 담당
- `docs/troubleshooting-log.md` 작성 (PR #32)

---

## Conflict Resolution

상세 기록은 [docs/conflict-resolution.md](docs/conflict-resolution.md) 참고 (PR #34).

### 충돌 #1 — `README.md` 같은 hunk 동시 수정 (비자명)

| 항목             | 값                                                                                |
| ---------------- | --------------------------------------------------------------------------------- |
| 참여자           | 남정현(선병합) · 강소연(충돌 해결)                                                |
| 공통 기준 커밋   | `2e1deec`                                                                         |
| 충돌 브랜치 커밋 | `7e28eb1` (`feature/sy-conflict-1-retry`)                                         |
| 병합해 온 main   | `8b58cf2` (PR #16 병합)                                                           |
| 해결 커밋        | [`9c66e85`](https://github.com/NamJungHyeon/B2-2/commit/9c66e85) (merge commit)   |
| 최종 병합        | [`8885aca`](https://github.com/NamJungHyeon/B2-2/commit/8885aca) (PR #18)         |
| 충돌 메시지      | `CONFLICT (content): Merge conflict in README.md`                                 |
| 해결 전략        | `choose one` — 두 문장이 같은 사실을 다르게 서술해 합치면 중복이므로 main 쪽 채택 |

### 충돌 #2 — `team/min.md` 삭제 vs 내용 수정 (modify/delete, 비자명)

| 항목             | 값                                                                                                       |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| 참여자           | 유영민(선병합) · 강소연(충돌 해결)                                                                       |
| 공통 기준 커밋   | `730d2c8`                                                                                                |
| 충돌 브랜치 커밋 | `f97554a` (`feature/sy-conflict-2-retry`)                                                                |
| 병합해 온 main   | `5ce9c85` (PR #27 병합)                                                                                  |
| 해결 커밋        | [`646730a`](https://github.com/NamJungHyeon/B2-2/commit/646730a) (merge commit)                          |
| 최종 병합        | [`4e7dda6`](https://github.com/NamJungHyeon/B2-2/commit/4e7dda6) (PR #28)                                |
| 충돌 메시지      | `CONFLICT (modify/delete): team/min.md deleted in 5ce9c85 and modified in HEAD.`                         |
| 해결 전략        | 파일 살리기(`git add`) — README가 `team/min.md`를 링크하고 미션 요구사항이 `team/` 아래 소개 파일을 요구 |

`modify/delete` 유형은 충돌 마커가 생기지 않는다. `git status --short`의 `UD`와
`git ls-files -u`의 stage 1·2만 존재하는 상태로 확인했다.

### 충돌이 재현되지 않은 1차 시도

| 실습 | 1차 시도                                                                                                  | 원인                                                                                                                                              |
| ---- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | [#10](https://github.com/NamJungHyeon/B2-2/pull/10) → [#14](https://github.com/NamJungHyeon/B2-2/pull/14) | 충돌 브랜치가 선병합 PR 병합 **후**의 main(`c7c6599`)에서 분기해 merge-base가 `c788b02`가 됨. 상대 변경을 이미 포함하고 있어 갈라진 역사가 없었음 |
| 2    | [#23](https://github.com/NamJungHyeon/B2-2/pull/23) → [#24](https://github.com/NamJungHyeon/B2-2/pull/24) | "이동" 커밋 `363a62b`가 실제로는 `docs/youngmin.md` 추가만 하고 원본을 지우지 않음. Git이 무관한 두 변경으로 보고 자동 병합                       |

두 실패 모두 원인과 재발 방지 방법을 `docs/conflict-resolution.md`에 기록했다.

---

## Git Troubleshooting

상세 기록은 [docs/troubleshooting-log.md](docs/troubleshooting-log.md) 참고 (PR #32).

| #   | 시나리오                      | 담당   | 실습 브랜치                                  | 실습 내용                                                                  |
| --- | ----------------------------- | ------ | -------------------------------------------- | -------------------------------------------------------------------------- |
| 1   | `git commit --amend`          | 강소연 | `feature/sy-fix-contributing-branch-example` | 오타가 포함된 로컬 커밋 메시지(`-revert 젝ㅓ`)를 push 전에 수정            |
| 2   | `git reset --soft HEAD~1`     | 유영민 | `feature/Min-troubleshoot`                   | 잘못된 파일이 포함된 로컬 커밋 `e2f4bf8`을 취소하고 변경은 스테이징에 유지 |
| 3   | `git revert`                  | 유영민 | `feature/Min-troubleshoot`                   | push한 더미 파일 추가 커밋을 새 커밋으로 되돌리고 기존 기록 유지 확인      |
| 4   | `git stash` / `git stash pop` | 남정현 | `feature/Nam-troubleshoot-stash`             | 추적 중인 `team/junghyun.md` 수정을 보관하고 main 왕복 후 복원             |

팀원 3명 모두 최소 1개 시나리오에 참여했고, 각 기록에 담당자 이름과 실습일이 명시되어 있다.

---

## Bonus

| 보너스                           | 담당   | 상태                                                                                                                                                     |
| -------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. `git rebase -i` 히스토리 정리 | 남정현 | [PR #36](https://github.com/NamJungHyeon/B2-2/pull/36) — 진행 중. `docs/rebase-practice.md`에 squash(4→1) / reword 전후 히스토리, reflog, 안전 수칙 기록 |
| 2. CODEOWNERS / 리뷰어 자동화    | 남정현 | [PR #22](https://github.com/NamJungHyeon/B2-2/pull/22) — 완료. `.github/CODEOWNERS`로 파일별 책임 리뷰어 지정                                            |

---

## Key Documents

| 문서                                                        | 작성 PR                                                                                                                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [협업 가이드](docs/CONTRIBUTING.md)                         | [#8](https://github.com/NamJungHyeon/B2-2/pull/8), [#12](https://github.com/NamJungHyeon/B2-2/pull/12), [#22](https://github.com/NamJungHyeon/B2-2/pull/22) |
| [충돌 해결 기록](docs/conflict-resolution.md)               | [#34](https://github.com/NamJungHyeon/B2-2/pull/34)                                                                                                         |
| [Git 트러블슈팅 기록](docs/troubleshooting-log.md)          | [#32](https://github.com/NamJungHyeon/B2-2/pull/32)                                                                                                         |
| [interactive rebase 실습 (보너스)](docs/rebase-practice.md) | [#36](https://github.com/NamJungHyeon/B2-2/pull/36)                                                                                                         |
| [PR 템플릿](.github/pull_request_template.md)               | [#8](https://github.com/NamJungHyeon/B2-2/pull/8)                                                                                                           |
| [Issue 템플릿](.github/ISSUE_TEMPLATE/task.md)              | [#8](https://github.com/NamJungHyeon/B2-2/pull/8)                                                                                                           |
| [CODEOWNERS (보너스)](.github/CODEOWNERS)                   | [#22](https://github.com/NamJungHyeon/B2-2/pull/22)                                                                                                         |

## Team Introduction

- [강소연](team/soyeon.md) — PR [#5](https://github.com/NamJungHyeon/B2-2/pull/5)
- [남정현](team/junghyun.md) — PR [#4](https://github.com/NamJungHyeon/B2-2/pull/4)
- [유영민](team/min.md) — PR [#6](https://github.com/NamJungHyeon/B2-2/pull/6)

## Repository Settings

- 저장소 형태: 옵션 B (개인 저장소 + Collaborator 초대). 팀원 3명 모두 Write 권한
- `main` 브랜치 보호 규칙
  - PR을 통해서만 병합 (직접 push 금지)
  - 작성자 외 최소 1명 승인 필요
  - 새 커밋이 올라오면 기존 승인 해제 (Dismiss stale approvals)
  - 리뷰 대화 해결 후 병합 (Require conversation resolution)
  - 관리자도 우회 불가 (Do not allow bypassing)
  - force push · 브랜치 삭제 금지
- 병합 방식: `Create a merge commit`으로 통일 — squash 시 `git log --graph`에 브랜치 흐름이 남지 않기 때문
- 모든 충돌 해결은 force push 없이 일반 merge와 일반 push로 수행
- `rebase -i`는 push 전 로컬 커밋에만 적용 (PR #36)

## Evidence

| 증빙                         | 경로                                   | 상태   |
| ---------------------------- | -------------------------------------- | ------ |
| Git 히스토리 텍스트          | `docs/evidence/git-log.txt`            | 미작성 |
| main 보호 설정 화면          | `docs/evidence/branch-protection.png`  | 미작성 |
| 충돌 마커 캡처               | `docs/evidence/conflict-1-markers.png` | 미작성 |
| modify/delete 충돌 상태 캡처 | `docs/evidence/conflict-2-status.png`  | 미작성 |

Git 히스토리는 최종 PR 병합 후 아래 명령으로 생성한다.

```
git switch main
git pull --ff-only origin main
mkdir -p docs/evidence
git log --oneline --graph --all > docs/evidence/git-log.txt
```

## Final Checklist

- [x] 팀원 3명이 협업 권한으로 하나의 저장소에 참여
- [x] `main` 브랜치 보호 설정 완료, 직접 push 없이 PR로만 병합
- [x] 모든 작업 PR이 Issue와 `Closes #번호`로 연동
- [x] 팀원별 병합된 PR 2개 이상 (남정현 5 · 강소연 7 · 유영민 5)
- [x] 팀원별 타인 PR 실질 리뷰 2개 이상 (남정현 2 · 강소연 2 · 유영민 3)
- [x] 충돌 해결 기록 2회 이상, 그중 비자명 충돌 2회 (같은 hunk 1회, modify/delete 1회)
- [x] `amend` · `reset --soft` · `revert` · `stash/pop` 4종 실습 완료, 팀원 전원 참여
- [x] 협업 문서 3종 작성 완료
- [x] `team/`에 소개 파일 3개, 각자 기여 커밋과 README 링크 존재
- [x] 보너스 과제 2종 수행 (rebase 히스토리 정리, CODEOWNERS)
- [x] **강소연 PR #5 리뷰 반영 답글** — 반영 커밋 `3235718`은 있으나 답글 없음
- [x] PR #36 병합
- [x] `SUBMISSION.md`를 저장소 루트에 추가 (현재 README 링크가 깨진 상태)
- [x] `docs/youngmin.md` 정리



