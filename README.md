# tipcode-cpu.github.io — 심장내과 임상 도구 허브

https://tipcode-cpu.github.io/

계산기·시뮬레이터·워크플로 도구·연구 하네스를 네 개의 큰 카테고리로 나눠 연결하는
인덱스 사이트입니다. 루트에서 카테고리를 고르고, 카테고리 페이지에서 개별 도구의
실행 주소와 저장소로 이동합니다.

An index site that connects the tools across four categories. Korean and English,
switched with the `한국어 / EN` buttons; the choice is stored on the device.

| 주소 | 내용 |
|---|---|
| `/` | 큰 카테고리 4개 |
| `/calculators/` | 임상 계산기 (5) |
| `/simulators/` | 교육 시뮬레이터 (3) |
| `/workflow/` | 진료 워크플로 도구 (5) |
| `/research/` | 연구·행정 하네스 (6) |

## 고치는 법 / How to edit

**페이지를 직접 고치지 마세요.** 다섯 페이지 모두 `_src/data.py` 한 파일에서
생성됩니다. 도구를 추가·수정한 뒤 다시 생성하면 네 카테고리 페이지와 루트 인덱스가
함께 갱신되므로, 페이지마다 따로 손대다 내용이 서로 어긋나는 일이 생기지 않습니다.

```bash
python3 _src/gen.py .        # data.py → index.html + 4 category pages
```

Do not hand-edit the pages. All five are generated from `_src/data.py`, so a tool
added or reworded in one place shows up everywhere at once.

CSS와 i18n 런타임은 `assets/`에 공유 파일로 두었습니다. 언어 전환 방식은
`echo-sim` · `htn-risk` · `score2-ap`와 같습니다: 한국어가 문서 기본값으로
마크업에 그대로 들어 있고, 영어는 사전으로 붙습니다.

## 면책 / Disclaimer

여기서 연결하는 계산기와 시뮬레이터는 임상 교육 및 판단 보조 목적입니다.
정식 검사와 임상의의 종합 평가를 대체하지 않습니다.

The calculators and simulators linked here are for clinical education and
decision support, and do not replace formal studies or the clinician's
comprehensive assessment.
