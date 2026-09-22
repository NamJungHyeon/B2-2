---
name: "Git 트러블슈팅 실습"
about: "amend / reset --soft / revert / stash 실습. 결과는 docs/troubleshooting-log.md에 기록"
title: "[Troubleshoot] "
labels: troubleshooting
assignees: ""
---

<!-- 예) [Troubleshoot] git revert로 push된 실습 커밋 되돌리기 (유영민) -->

## 시나리오
- [ ] `git commit --amend` — push하지 않은 최근 커밋 메시지 수정 (담당: 남정현)
- [ ] `git reset --soft HEAD~1` — 로컬 커밋 취소 + 변경 스테이징 유지 (담당: 강소연)
- [ ] `git revert <커밋ID>` — 원격에 push된 커밋을 새 커밋으로 되돌리기 (담당: 유영민)
- [ ] `git stash` / `git stash pop` — 작업 보관 후 브랜치 전환 (공동)

## 참여자와 역할
- 실습 수행:
- 기록 작성:
- 검토:

## 상황 (재현 가능하게)
<!-- 어떤 브랜치에서, 어떤 파일을, 어떤 상태로 만들어 놓고 시작하는지 -->


## 실습 브랜치
`feature/<이름>-troubleshoot-<시나리오>`

## 주의
- `amend`, `reset`은 **push하지 않은 로컬 실습 커밋**에만 사용한다.
- `amend`/`reset`은 히스토리에서 흔적이 사라지므로 실행 **전후** `git log --oneline -3` 출력을 텍스트로 복사해 둔다.
- `revert`는 실제 소개 내용이 아니라 실습용 변경을 대상으로 한다.
- `stash`는 추적 중인 파일로 실습한다 (새 파일은 기본적으로 보관되지 않는다).
- main에서 실습하지 않는다.

## 완료 조건
- [ ] 실행 전 상태(브랜치, `git log`, `git status`)를 남겼다.
- [ ] 실행한 명령을 순서대로 남겼다.
- [ ] 실행 후 결과를 남겼다.
- [ ] `docs/troubleshooting-log.md`에 참여자·역할, 상황, 실행 전 상태, 절차와 명령, 결과, 주의점, 선택 이유(예: reset 대신 revert를 쓴 이유), 증빙을 기록했다.

## 관련 PR
- 기록 PR: #
