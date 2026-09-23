# B2-2 github-workflow-practice

강소연, 남정현, 유영민 세 명이 GitHub Flow로 협업하는 연습 저장소입니다.
Issue, PR, 코드 리뷰, 충돌 해결, Git 복구 실습의 전 과정을 기록으로 남깁니다.

## 팀원 소개

강소연, 남정현, 유영민 세 명이 함께 진행합니다.

- [강소연](team/soyeon.md)
- [남정현](team/junghyun.md)
- [유영민](team/min.md)

## 관련 문서

- [기여 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [Git 문제 해결 기록](docs/troubleshooting-log.md)
- [interactive rebase 실습](docs/rebase-practice.md)
- [제출물 인덱스](SUBMISSION.md)

## 폴더 구조

```
B2-2/
├── README.md                      # 팀 소개와 문서 목차
├── SUBMISSION.md                  # 제출물 인덱스 (팀원별 Issue·PR·리뷰·증빙 링크)
├── .github/
│   ├── pull_request_template.md   # PR 본문 양식 (연결 이슈 / What / Why / How / 확인 사항)
│   └── ISSUE_TEMPLATE/
│       ├── config.yml             # 빈 이슈 생성 비활성화
│       └── task.md                # Issue 양식 (목적 / 변경할 파일 / 완료 조건 / 작업 브랜치 / 리뷰어)
├── docs/
│   ├── CONTRIBUTING.md            # 브랜치·커밋·Issue·PR·리뷰 규칙, 충돌 대응 흐름
│   ├── conflict-resolution.md     # 충돌 해결 기록 (2회 이상, 비자명 충돌 포함)
│   ├── troubleshooting-log.md     # amend / reset / revert / stash 실습 기록
│   └── rebase-practice.md         # interactive rebase squash·reword 실습 기록 (보너스)
│   
├── team/
│   ├── soyeon.md                  # 강소연 소개
│   ├── junghyun.md                # 남정현 소개
│   └── min.md                     # 유영민 소개
└── src/
    └── string_utils.py            # 문자열 유틸 (rebase 실습 대상)
```

| 경로            | 내용                                                                              |
| --------------- | --------------------------------------------------------------------------------- |
| `team/`         | 팀원별 소개 문서. 각자 자신의 PR로 작성한다.                                      |
| `docs/`         | 협업 규칙과 실습 기록. 충돌·트러블슈팅 실습의 결과는 여기에 남긴다.               |
| `.github/`      | Issue·PR 템플릿과 CODEOWNERS. 새 Issue / PR 화면에서 자동으로 적용된다.           |
| `src/`          | 예시 코드. `string_utils.py`는 rebase 실습 대상으로 작성했다.                     |
| `SUBMISSION.md` | 팀원별로 "내가 만든 Issue / PR / 리뷰 / 리뷰 반영"을 한눈에 볼 수 있는 제출 목차. |

## 작업 흐름

```
Issue 생성 → feature/<이름>-<작업내용> 브랜치 → 커밋·push → PR (Closes #번호)
→ 리뷰 (근거 있는 코멘트 1개 이상) → 반영 커밋 + 답글 → 승인 → Create a merge commit → 브랜치 삭제
```

- `main`은 항상 제출 가능한 상태로 유지하고 직접 push하지 않습니다.
- 모든 변경은 PR과 다른 팀원 1명 이상의 승인을 거쳐 merge합니다.
- 자세한 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 따릅니다.
