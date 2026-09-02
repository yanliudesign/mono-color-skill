<div align="center">

[中文](./README.zh.md) · [English](./README.md) · **한국어**

# 모노컬러 에디토리얼 프린트

**포스터, 진(zine), 인물, 패키지, 시각 관찰 노트를 위한 1도 / 제어된 2도 인쇄 에디토리얼 이미지 스킬.**

[![Version](https://img.shields.io/badge/VERSION-1.2.0-2ea44f?style=flat-square&labelColor=333)](./CHANGELOG.md)
[![Skills](https://img.shields.io/badge/SKILLS-1-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Stars](https://img.shields.io/github/stars/yanliudesign/mono-color-skill?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/mono-color-skill/stargazers)
[![Validate skill](https://github.com/yanliudesign/mono-color-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/yanliudesign/mono-color-skill/actions/workflows/validate.yml)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![SKILL.md](https://img.shields.io/badge/Agent-SKILL.md-214f9b?style=flat-square&labelColor=1a1a1a)](./SKILL.md)

</div>

주제, 문장, 사물, 또는 제공된 사진을 독창적인 에디토리얼 이미지로 바꿉니다. 이 스킬은 기본적으로 제어된 2도 인쇄를 사용합니다. 주도판 하나가 화면을 이끌고, 보조판 하나는 좁게 정해진 역할만 맡습니다. 1도나 모노크롬을 명시적으로 요청하면 순수한 1도 인쇄를 유지합니다. 바탕지는 이미지와 팔레트에 맞춰 화이트, 쿨 그레이, 페일 베이지 중에서 고르며, 기본 방향은 현대적인 에디토리얼이고 빈티지 처리는 요청이 있을 때만 적용합니다.

레퍼런스를 복제하는 대신 시각 시스템을 보존합니다. 모든 구성은 주제, 의도, 문구, 이미지의 역할을 중심으로 새로 짜입니다.

## 예시 선별

| 여름 사이클링 | 필드 스터디 | 평범한 공간 |
|:---:|:---:|:---:|
| <img src="./examples/example-cycling.png" alt="코발트와 테라코타 여름 사이클링 에디토리얼 프린트" width="280"> | <img src="./examples/example-zebra.png" alt="코발트와 오렌지 얼룩말 필드 스터디 에디토리얼 프린트" width="280"> | <img src="./examples/example-chair.png" alt="그린과 옥스블러드 의자 진 에디토리얼 프린트" width="280"> |

| 정어리 패키지 | 헤드폰 패키지 | 선크림 패키지 |
|:---:|:---:|:---:|
| <img src="./examples/example-sardines.png" alt="바이올렛과 오렌지 정어리 통조림 패키지" width="280"> | <img src="./examples/example-headphones.png" alt="코발트와 블랙 헤드폰 패키지" width="280"> | <img src="./examples/example-sunscreen.png" alt="시안과 코랄 선크림 패키지" width="280"> |

| 작은 온기 | 브랜드 굿즈 | 느린 잎 |
|:---:|:---:|:---:|
| <img src="./examples/example-teapot.png" alt="그린 하프톤 티팟 에디토리얼 포스터" width="280"> | <img src="./examples/example-merchandise.png" alt="코발트와 오렌지 모노컬러 굿즈 컬렉션" width="280"> | <img src="./examples/example-tea.png" alt="그린 하프톤 차 패키지" width="280"> |

| 야경 사진 | 일요일의 라디오 | 야시장 |
|:---:|:---:|:---:|
| <img src="./examples/example-night-photography.png" alt="코발트 도시 야경 사진전 포스터" width="280"> | <img src="./examples/example-radio.png" alt="코발트와 블랙 라디오 청취 포스터" width="280"> | <img src="./examples/example-night-market.png" alt="레드와 시안 버섯 야시장 포스터" width="280"> |

이 열두 장의 원본 생성 예시는 스킬의 표현 범위를 보여 주는 결과물이며, 그대로 재현할 템플릿이 아닙니다.

## 시각 레퍼런스

시각 시스템은 열두 장의 이미지 리서치 세트를 바탕으로 만들어졌습니다. 전체 이미지 목록, 리서치 노트, 출처 표기 상태, 수정 요청 링크는 [Visual References and Attribution](./REFERENCES.md)을 참고하세요. 제3자 레퍼런스는 각 창작자와 권리자의 소유입니다.

| 01 | 02 | 03 |
|:---:|:---:|:---:|
| <a href="./examples/reference-01.png"><img src="./examples/reference-01.png" alt="시각 레퍼런스 01" width="280"></a> | <a href="./examples/reference-02.png"><img src="./examples/reference-02.png" alt="시각 레퍼런스 02" width="280"></a> | <a href="./examples/reference-03.png"><img src="./examples/reference-03.png" alt="시각 레퍼런스 03" width="280"></a> |
| 04 | 05 | 06 |
| <a href="./examples/reference-04.png"><img src="./examples/reference-04.png" alt="시각 레퍼런스 04" width="280"></a> | <a href="./examples/reference-05.png"><img src="./examples/reference-05.png" alt="시각 레퍼런스 05" width="280"></a> | <a href="./examples/reference-06.png"><img src="./examples/reference-06.png" alt="시각 레퍼런스 06" width="280"></a> |
| 07 | 08 | 09 |
| <a href="./examples/reference-07.png"><img src="./examples/reference-07.png" alt="시각 레퍼런스 07" width="280"></a> | <a href="./examples/reference-08.png"><img src="./examples/reference-08.png" alt="시각 레퍼런스 08" width="280"></a> | <a href="./examples/reference-09.png"><img src="./examples/reference-09.png" alt="시각 레퍼런스 09" width="280"></a> |
| 10 | 11 | 12 |
| <a href="./examples/reference-10.png"><img src="./examples/reference-10.png" alt="시각 레퍼런스 10" width="280"></a> | <a href="./examples/reference-11.jpg"><img src="./examples/reference-11.jpg" alt="시각 레퍼런스 11" width="280"></a> | <a href="./examples/reference-12.jpg"><img src="./examples/reference-12.jpg" alt="시각 레퍼런스 12" width="280"></a> |

## 무엇을 하나

| 시스템 | 방향 |
|---|---|
| **입력** | 주제, 문구, 사물, 글의 아이디어, 또는 제공된 사진 |
| **팔레트** | 상황에 맞춘 중성 화이트·쿨 그레이·페일 베이지 바탕 + 기본값은 제어된 2도 인쇄. 1도를 명시하면 1도 유지 |
| **모드** | 순수 1도, 유채색 + 블랙, 보색 듀오톤, 또는 오버프린트 듀오톤 |
| **이미지** | 하프톤, 리소그래프 입자, 시아노타입 노광, 또는 복사기 번짐 |
| **여백** | 비대칭 에디토리얼 그리드 위에 25%–55%의 빈 종이를 남김 |
| **타이포** | 내용에 따라 고르는 문학적 세리프, 문화적 그로테스크, 컨덴스드 시빅, 프로그램형, 회전, 손글씨, 글자 자체를 오브제로 쓰는 역할 |
| **출력** | 생성된 래스터 이미지, 실제 사용한 프로덕션 프롬프트, 짧은 레시피 |

## 활용 예

- 포스터: 이벤트, 파티, 전시, 도시 산책, 컨셉 포스터
- 소셜 미디어: 샤오홍슈 커버, 위챗 아티클 헤더, 팟캐스트 커버, 문화 비평 일러스트
- 브랜드 자료: 엽서, 초대장, 티켓, 프로그램, 메뉴, 패키지 스티커
- 기념품: 여행 일기, 사진 앨범 커버, 기념일 카드
- 책과 출판물: 표지, 속표지, 장 도입부, 진(zine) 본문
- 문구: 문학 발췌, 시, 개인적 선언

이 모든 형식은 단 한 가지 잉크만으로도 인쇄 비용을 낮추면서 독특한 시각적 정체성을 유지할 수 있습니다.

## 작동 방식

```text
1  입력 읽기        →  주제, 의도, 문구, 이미지의 역할을 파악
2  레이아웃 선택     →  이미지, 스페시멘, 선언, 오브젝트 필드, 오버프린트, 저널, 커버 중 선택
3  판 배정          →  기본은 역할이 정해진 두 판. 명시적으로 요청하면 한 판으로 전환
4  페이지 구성       →  25%–55%의 여백을 지키고 의도된 파격 하나를 더함
5  생성과 점검       →  잉크 수, 정체성, 위계, 질감, 독창성을 확인
```

## 잉크 시스템

**1도 팔레트:** Cobalt, Royal Blue, Botanical Green, Mint Green, Terracotta Orange, Signal Red, Aubergine, Charcoal.

| 색상 | 잉크 | Hex |
|---|---|---|
| ![Cobalt](./swatches/cobalt.svg) | Cobalt / Ultramarine (코발트 / 울트라마린) | `#2148B8` |
| ![Royal Blue](./swatches/royal-blue.svg) | Royal Blue (로열 블루) | `#2058D4` |
| ![Botanical Green](./swatches/botanical-green.svg) | Botanical Green (보태니컬 그린) | `#008A4B` |
| ![Mint Green](./swatches/mint-green.svg) | Mint Green (민트 그린) | `#5EB783` |
| ![Terracotta Orange](./swatches/terracotta.svg) | Terracotta Orange (테라코타 오렌지) | `#C65F38` |
| ![Signal Red](./swatches/signal-red.svg) | Signal Red (시그널 레드) | `#C83232` |
| ![Aubergine](./swatches/aubergine.svg) | Aubergine (오버진) | `#63365F` |
| ![Charcoal](./swatches/charcoal.svg) | Charcoal (차콜) | `#30343A` |

**2도 레시피:** Powder Blue + Signal Red, Cobalt + Terracotta, Botanical Green + Oxblood, Charcoal + Signal Red, Electric Blue + Carbon, Mint Green + Charcoal, Ultramarine + Safety Orange, Cyan + Brick Red, Tangerine + Slate Blue.

| 색상 | 2도 레시피 | Hex |
|---|---|---|
| ![Powder Blue and Signal Red](./swatches/powder-blue-signal-red.svg) | Powder Blue + Signal Red (파우더 블루 + 시그널 레드) | `#9EB8D3` + `#C83232` |
| ![Cobalt and Terracotta](./swatches/cobalt-terracotta.svg) | Cobalt + Terracotta (코발트 + 테라코타) | `#2148B8` + `#C65F38` |
| ![Botanical Green and Oxblood](./swatches/botanical-green-oxblood.svg) | Botanical Green + Oxblood (보태니컬 그린 + 옥스블러드) | `#008A4B` + `#8F3434` |
| ![Charcoal and Signal Red](./swatches/charcoal-signal-red.svg) | Charcoal + Signal Red (차콜 + 시그널 레드) | `#30343A` + `#C83232` |
| ![Electric Blue and Carbon](./swatches/electric-blue-carbon.svg) | Electric Blue + Carbon (일렉트릭 블루 + 카본) | `#173AE3` + `#242321` |
| ![Mint Green and Charcoal](./swatches/mint-green-charcoal.svg) | Mint Green + Charcoal (민트 그린 + 차콜) | `#5EB783` + `#302D2E` |
| ![Ultramarine and Safety Orange](./swatches/ultramarine-safety-orange.svg) | Ultramarine + Safety Orange (울트라마린 + 세이프티 오렌지) | `#263E99` + `#E55D2B` |
| ![Cyan and Brick Red](./swatches/cyan-brick-red.svg) | Cyan + Brick Red (시안 + 브릭 레드) | `#159DDA` + `#B64032` |
| ![Tangerine and Slate Blue](./swatches/tangerine-slate-blue.svg) | Tangerine + Slate Blue (탠저린 + 슬레이트 블루) | `#E46C2D` + `#4773A5` |

2도 인쇄에서는 주도판이 보통 인쇄 면적의 70%–85%를 차지합니다. 보조판은 15%–30%를 맡되 날짜, 주석, 선택된 사물, 오버프린트 교차부처럼 구체적인 임무가 있어야 합니다. 바탕지는 세 번째 색이 아니며, 두 판이 겹쳐 생기는 더 어두운 색도 세 번째 잉크가 아닙니다.

**바탕지는 상황에 맞춰 고르며, 기본값이 회고적이지 않습니다:** 중성 화이트 `#FAFAF7`은 선명한 문화·소셜·이벤트·이미지 중심 작업에, 쿨 그레이 `#E9E9E5`는 건축·기술·차콜 중심 시스템·절제된 브랜딩에, 페일 베이지 `#F5F1E8`는 촉각적·여행·음식·친밀한·아카이브 성격이거나 명시적으로 향수를 요청한 주제에 어울립니다. 제한된 잉크와 하프톤이 자동으로 빈티지 스타일을 뜻하지는 않습니다.

## 시각 규칙

1. **인쇄 잉크는 최대 두 가지.** 제어된 2도 인쇄가 기본입니다. 주도판 70%–85%, 보조판 15%–30%, 각 판은 서로 다른 역할을 맡습니다. 1도를 명시적으로 요청하면 한 판만 씁니다.
2. **종이가 보여야 합니다.** 결과물은 인쇄된 페이지이지, 디지털로 색을 입힌 모노크롬 워시가 아닙니다.
3. **기계적 복제가 주도합니다.** 사진은 망점, 입자, 날아간 하이라이트, 잉크 고임, 판 사이의 가벼운 핀 어긋남으로 바뀝니다.
4. **여백에도 구조가 있습니다.** 빈 종이가 캔버스의 25%–55%를 차지하며 호흡을 조절합니다.
5. **타이포에는 긴장과 폭이 있습니다.** 내용에 맞는 디스플레이 골격 하나와 유틸리티 보이스 하나를 고르고, 손글씨는 짧은 삽입구로만 선택적으로 씁니다. 시리즈라면 한 가지 하우스 스타일을 반복하지 않고 디스플레이 계열을 바꿀 수 있습니다.
6. **정체성은 유지됩니다.** 제공된 인물, 사물, 장면은 알아볼 수 있어야 합니다.
7. **레퍼런스는 문법이지 템플릿이 아닙니다.** 제공된 레퍼런스마다 구조 변수를 최소 네 가지 이상 바꿉니다.

## 이런 것이 아닙니다

- 모노크롬 필터를 씌운 풀컬러 사진이 아닙니다
- 임의의 2색 장식이나 세 판 이상의 인쇄가 아닙니다
- 광택 목업, 3D 렌더, 그라디언트 포스터, 시네마틱 장면이 아닙니다
- 중앙 정렬 템플릿, 카드 그리드, 스티커 콜라주, 장식용 블롭 시스템이 아닙니다
- 빽빽한 스크랩북 그런지나 찢어진 종이 스타일이 아닙니다
- 하프톤이나 제한된 잉크를 썼다는 이유로 자동으로 레트로, 황변, 세피아, 낡음, 향수 스타일이 되지 않습니다
- 마케팅 문구, 지어낸 브랜딩, 가짜 스폰서, URL, QR 코드가 아닙니다
- 레퍼런스 포스터나 작가 시그니처의 재구성이 아닙니다

## 설치

Claude Code 스킬 디렉터리에 저장소를 클론합니다:

```bash
git clone https://github.com/yanliudesign/mono-color-skill.git \
  ~/.claude/skills/mono-color
```

설치 후 Claude Code를 재시작합니다. 다른 에이전트 환경에서는 [`SKILL.md`](./SKILL.md)를 스킬 진입점으로 불러올 수 있습니다.

## 써 보기

```text
mono-color로 심야 편의점을 주제로 한 세로형 포스터를 만들어 줘.
헤드라인은 정확히 “still open”으로.
```

```text
이 인물 사진을 코발트 1도 에디토리얼 진 커버로 바꿔 줘.
인물의 정체성과 표정은 유지해 줘.
```

```text
고사리를 주제로 보태니컬 그린 리소그래프 필드 노트를 만들어 줘.
제목은 “field note 07”.
```

```text
도시 사이클링을 주제로 Ultramarine + Safety Orange 오버프린트 포스터를 만들어 줘.
자전거와 초대형 제목이 일부 영역에서 겹치도록 해 줘.
```

```text
이 제품을 Cyan + Brick Red 반복 오브젝트 커버로 바꿔 줘.
제목과 사실 정보용 작은 글자를 넣을 빈 영역 하나를 남겨 줘.
```

```text
루프탑 모임을 위한 Signal Red 1도 파티 포스터를 만들어 줘.
헤드라인은 “after sunset”, 날짜는 작게.
```

```text
콘크리트 건축을 주제로 Charcoal + Signal Red 전시 포스터를 디자인해 줘.
레드 판은 날짜, 장소, 기하학적 파격 하나에만 써 줘.
```

```text
이 거리 사진으로 코발트 도시 산책 포스터를 만들어 줘.
건물은 굵은 하프톤으로 바꾸고 제목은 “north by foot”.
```

```text
주말 플리마켓을 주제로 Terracotta Orange 샤오홍슈 커버를 만들어 줘.
초대형 중국어 헤드라인 하나를 쓰고 종이의 최소 3분의 1은 비워 둬.
```

```text
이 진행자 인물 사진을 Aubergine 1도 팟캐스트 커버로 바꿔 줘.
얼굴은 알아볼 수 있게 유지하고 에피소드 제목은 “the quiet hour”.
```

```text
독립 서점 오픈을 위한 Botanical Green + Oxblood 초대장을 만들어 줘.
그린은 종이 질감과 이미지를, 옥스블러드는 행사 정보만 맡게 해 줘.
```

```text
이 여행 사진들을 Cobalt + Terracotta 엽서 시리즈로 바꿔 줘.
시리즈 전체에 같은 그리드를 유지하되 크롭과 손글씨 주석은 매 장 다르게.
```

```text
“we kept the window open”이라는 문장을 위한 Mint Green + Charcoal 시 속표지를 디자인해 줘.
사진 없이, 넉넉한 여백과 작은 아카이브 스타일 메모 하나만.
```

## 전달 형식

한 번의 실행으로 다음을 돌려줍니다:

1. 이미지 생성 도구를 쓸 수 있으면 생성된 래스터 이미지
2. 생성에 실제로 사용한 프로덕션용 프롬프트
3. 인쇄 모드, 정확한 잉크 팔레트, 레이아웃 계열, 타이포 조합, 인쇄 공정, 독창성을 위해 바꾼 요소를 명시한 레시피

이미지 생성이 불가능하면 프로덕션용 프롬프트를 돌려주고 그 제약을 명시합니다.

## 안정성과 검증

프롬프트를 조립하기 전에 스킬은 모든 요청을 고정된 레시피 매니페스트로 해석합니다. 지정하지 않은 요청은 `3:4` 비율, 중성 화이트 바탕지, 현대적 에디토리얼 방향, 35% 여백, 그리고 결정론적 팔레트·레이아웃 규칙을 사용합니다. 이미지와 잉크의 대비가 요구하면 바탕지는 쿨 그레이나 페일 베이지로 바뀔 수 있습니다. 제공된 사진은 기본적으로 충실하게 재현하며, 추상적·예술적·느슨한·실험적·덜 사실적인 처리를 요청하면 2–4개의 정체성 앵커를 보존하는 결정론적 심볼 추출로 전환합니다. 사용자의 명시적 선택은 2도 인쇄와 독창성 한계 안에서 여전히 우선합니다.

`design-system/` 카탈로그는 시각 문법을 재사용하고 점검할 수 있게 만듭니다. 색 토큰, 타이포 역할, 구성 기하, 매체별 신호, 시각 리듬, 제어된 인쇄 불완전성을 산문 워크플로와 분리해 보관합니다. 카탈로그 ID는 레퍼런스 보드, 레시피, 검증기가 공유하는 계약입니다.

`design-system/rhythm.json`은 이완을 균일하게 낮춘 강도가 아니라 고르지 않은 에너지 분포로 정의합니다. 각 페이지는 초대형 글자, 극단적인 크롭, 거대한 디테일 하나, 집중된 오버프린트, 비정상적인 스케일 관계 같은 대담한 초점 사건 하나를 고르고, 나머지는 종이, 옅은 스크린, 드문 기능성 텍스트로 풀어 줍니다. 사진이 제공되지 않으면 인물은 완전한 스톡 이미지나 안전한 "왼쪽 제목 / 오른쪽 사진" 배치가 아니라 2–4개의 식별 앵커와 부분 크롭으로 표현됩니다. 여백과 열린 가장자리는 이제 고정 비율이 아니라 초점 사건에 따라 결정됩니다.

제어된 우연은 복제 레이어에만 머뭅니다. 현대적 작업은 0–2개의 절제된 효과를, 촉각적·빈티지·아카이브 노화 작업은 고르지 않은 잉크 농도, 마른 가장자리 번짐, 하프톤 드리프트, 핀 어긋남, 끊어진 손짓 하나 같은 경계가 정해진 효과 2–3개를 고릅니다. 안정된 레시피 시드가 재시도 간에 같은 흔적을 유지하므로 구성이 움직이거나 텍스트 가독성이 떨어지지 않습니다.

![모노컬러 시각 시스템 레퍼런스 보드](./examples/mono-color-design-system-board.png)

네 개의 레퍼런스 분석 보드는 시스템의 근거가 된 타이포그래피, 색, 레이아웃, 스타일 증거를 기록합니다:

### 타이포그래피

![타이포그래피 시스템](./examples/reference-system-v2-typography.png)

### 색

![색 시스템](./examples/reference-system-v2-color.png)

### 레이아웃

![레이아웃 시스템](./examples/reference-system-v2-layout.png)

### 스타일

![스타일 시스템](./examples/reference-system-v2-style.png)

카탈로그를 수정한 뒤에는 카탈로그 기반 전체 보드를 다시 생성합니다:

```bash
python3 scripts/build_design_system_board.py
```

평가 계약은 기본값, 제공된 인물 사진, 식물 작업, 오버프린트, 행사 정보, 장문 텍스트, 프롬프트 전용 출력, 상충하는 색 요청, 반복 오브젝트, 레퍼런스 복제 요청을 다룹니다. 로컬에서 실행합니다:

```bash
python3 scripts/validate_evals.py
python3 scripts/validate_design_system.py
```

GitHub Actions가 모든 풀 리퀘스트와 `main` 푸시에서 같은 계약을 실행합니다.

## 저장소 구조

```text
mono-color-skill/
├── .github/workflows/ # 지속적 검증
├── design-system/    # 기계가 읽는 색, 구성, 리듬, 인쇄 패턴
├── examples/         # README에 실린 원본 생성 예시
├── scripts/          # 평가 및 디자인 시스템 검증기
├── swatches/         # 1도·2도 팔레트 미리보기
├── SKILL.md          # 트리거 규칙, 시각 시스템, 워크플로, 품질 게이트
├── README.md         # 영문 문서
├── README.zh.md      # 中文说明
├── README.ko.md      # 한국어 문서
├── CHANGELOG.md      # 릴리스 이력
└── evals/
    ├── evals.json    # 대표 프롬프트와 결정론적 단언
    └── schema.json   # 평가 계약 스키마
```

## 독창성

이 스킬은 팔레트, 인쇄 공정, 여백, 위계, 소통 톤 같은 시스템 수준의 특성을 추출합니다. 레퍼런스의 구성, 문구, 라벨, 로고, 테두리 시스템, 특징적인 배치는 복제하지 않습니다.

사용자가 사진을 제공하면 피사체는 내용으로서 보존되지만 크롭, 스크리닝, 그리드, 글자 배치, 메타데이터 처리는 새로 구성됩니다.

## 라이선스

소스 코드, 스킬 지침, 스크립트는 [MIT 라이선스](./LICENSE)로 제공됩니다.

[`examples/`](./examples)에 있는 Yan Liu의 원본 예시는 © 2026 Yan Liu의 저작물이며 MIT 라이선스에 포함되지 않습니다. 열두 장의 제3자 리서치 레퍼런스는 각 창작자와 권리자의 소유입니다. 자세한 내용은 [시각 자산 라이선스](./ASSET-LICENSE.md)와 [Visual References and Attribution](./REFERENCES.md)을 참고하세요.

---

Created by [Dreameryanyan](https://www.linkedin.com/in/yanliudesign/) · [LinkedIn](https://www.linkedin.com/in/yanliudesign/) · [X](https://x.com/yanliudreamer)
