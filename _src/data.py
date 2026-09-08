# -*- coding: utf-8 -*-
"""Single source of truth for the hub pages.

The category pages are generated from this file rather than hand-written, so
they cannot drift apart the way the two echo-sim editions did.
"""

SITE = {
    "title_ko": "심장내과 임상 도구 모음",
    "title_en": "Cardiology tools",
    "byline_ko": '최강운 · 영남대학교병원 심장내과 — <a href="https://github.com/tipcode-cpu">github.com/tipcode-cpu</a>',
    "byline_en": 'Kang-Un Choi, MD, PhD · Division of Cardiology, Yeungnam University Medical Center — <a href="https://github.com/tipcode-cpu">github.com/tipcode-cpu</a>',
    "lede_ko": "진료·교육·연구에서 반복되는 작업을 줄이기 위해 만든 도구들입니다. 계산기와 시뮬레이터는 브라우저에서 바로 열리는 단일 파일이며, 환자 식별정보를 입력받거나 저장하지 않습니다.",
    "lede_en": "Tools built to take the repetition out of clinical work, teaching and research. The calculators and simulators are single files that open straight in a browser, and none of them ask for or store patient-identifying information.",
}

GH = "https://github.com/tipcode-cpu/"
PG = "https://tipcode-cpu.github.io/"

CATEGORIES = [
 {
  "dir": "calculators",
  "ko": "임상 계산기", "en": "Clinical calculators",
  "note_ko": "진료 중 바로 쓰는 위험도·점수 계산기. 모두 설치형 웹앱(PWA)이며 오프라인에서 동작합니다.",
  "note_en": "Risk scores for use at the bedside. All are installable web apps (PWA) and work offline.",
  "tools": [
   {"repo":"cardioquick","ko":"CardioQuick","en":"CardioQuick","live":PG+"cardioquick/",
    "dko":"PREVENT · ASCVD 위험도와 CKD-EPI를 한 화면에서 계산하고 항목별로 복사합니다.",
    "den":"PREVENT and ASCVD risk with CKD-EPI on one screen, with per-field copy."},
   {"repo":"htn-risk","ko":"고혈압 심뇌혈관 위험도","en":"Hypertension CV risk","live":PG+"htn-risk/",
    "dko":"대한고혈압학회 2026 진료지침 표 10·11·13과 권고 8–13에 따른 위험도 분류와 목표 혈압. 입력한 검사 수치는 자동으로 위험인자에 반영됩니다.",
    "den":"Risk stratification and blood pressure targets per the Korean Society of Hypertension 2026 guideline, Tables 10, 11 and 13 and Recommendations 8–13. Laboratory values entered are folded into the risk factor count automatically."},
   {"repo":"score2-ap","ko":"SCORE2 Asia-Pacific","en":"SCORE2 Asia-Pacific","live":PG+"score2-ap/",
    "dko":"아시아·태평양 재보정 SCORE2로 10년 심혈관 위험도를 산출합니다. 모든 계수는 원 논문 부록에서 직접 옮겼습니다 (EHJ 2021 · 2025).",
    "den":"10-year cardiovascular risk using SCORE2 recalibrated for the Asia-Pacific region. Every constant was taken from the published supplementary material (EHJ 2021 · 2025)."},
   {"repo":"CardiacScore","ko":"심장장애 정도 판정","en":"Cardiac disability grading","live":PG+"CardiacScore/",
    "dko":"장애 정도 판정 기준에 따른 심장장애 점수 계산기.",
    "den":"Korean cardiac disability grading score calculator."},
   {"repo":"pmid-refs","ko":"PMID 레퍼런스","en":"PMID references","live":PG+"pmid-refs/",
    "dko":"PMID를 넣으면 저자·저널·연도를 정리해 참고문헌 목록을 만들어 주는 PWA.",
    "den":"Enter PMIDs and get an ordered reference list with author, journal and year."},
  ],
 },
 {
  "dir": "simulators",
  "ko": "교육 시뮬레이터", "en": "Teaching simulators",
  "note_ko": "변수를 직접 움직이며 원리를 확인하는 인터랙티브 교육 도구. 전공의·학생 강의용으로 만들었습니다.",
  "note_en": "Interactive tools that show a principle by letting you move the variable. Built for resident and student teaching.",
  "tools": [
   {"repo":"echo-sim","ko":"심초음파 시뮬레이터","en":"Echocardiography simulators","live":PG+"echo-sim/","tag":"KO / EN",
    "dko":"도플러 aliasing·PISA 역류 정량·프레임률 상충·AS 중증도·심박출량·이완기능 6종. 한국어와 영어를 한 파일에서 전환합니다.",
    "den":"Six simulators — Doppler aliasing, PISA regurgitation quantification, frame-rate trade-offs, aortic stenosis severity, cardiac output, and diastolic function. Korean and English in one file."},
   {"repo":"ICU-sim","ko":"중환자 혈역학 시뮬레이터","en":"ICU haemodynamics simulators","live":PG+"ICU-sim/",
    "dko":"혈역학 프로파일과 쇼크 4형 분류(Forrester·Nohria·SCAI), VExUS 정맥울혈, 우심도자·Fick 심박출량과 폐고혈압 혈역학 분류.",
    "den":"Haemodynamic profiles and four-type shock classification (Forrester, Nohria, SCAI), VExUS venous congestion, and right heart catheterisation with Fick cardiac output and pulmonary hypertension classification."},
   {"repo":"rv-pv-loop-simulator","ko":"RV 압력–용적 곡선","en":"RV pressure–volume loop","live":PG+"rv-pv-loop-simulator/",
    "tag_ko":"프로토타입","tag_en":"prototype",
    "dko":"Ees·Ea·EDV·V0로 우심실 압력–용적 관계와 심실–동맥 커플링(Ees/Ea)을 계산합니다. 초기 프로토타입이며 곡선 형태는 아직 이상화된 사각형입니다.",
    "den":"Right ventricular pressure–volume relationship and ventricular–arterial coupling (Ees/Ea) from Ees, Ea, EDV and V0. An early prototype — the loop is still drawn as an idealised rectangle."},
  ],
 },
 {
  "dir": "workflow",
  "ko": "진료 워크플로 도구", "en": "Clinical workflow tools",
  "note_ko": "판독문 작성, DICOM 비식별화, 영상 자료 제작처럼 진료·발표 준비에서 반복되는 작업을 처리합니다.",
  "note_en": "For the repetitive parts of reporting, de-identification and preparing imaging material.",
  "tools": [
   {"repo":"tee-report-maker","ko":"TEE Report Maker","en":"TEE Report Maker",
    "live":PG+"tee-report-maker/TEE_Report_Maker.html",
    "dko":"체크·클릭으로 표준 TEE 결론문을 생성해 판독 시스템에 붙여넣습니다. 단일 HTML, 완전 오프라인, 어떤 데이터도 저장하지 않습니다.",
    "den":"Build a standard TEE conclusion by checkbox and paste it into the reporting system. Single HTML file, fully offline, nothing stored."},
   {"repo":"dicom_anon","ko":"dicom-anon","en":"dicom-anon",
    "dko":"DICOM 헤더의 환자정보 태그를 비우고 UID를 새로 발급하는 CLI. 원본은 건드리지 않습니다. 픽셀에 새겨진 정보는 제거하지 못하므로 육안 확인이 필요합니다.",
    "den":"CLI that blanks patient tags in DICOM headers and reissues UIDs, leaving the original untouched. It cannot remove information burned into the pixels — check those by eye."},
   {"repo":"dicom2pptx","ko":"dicom2pptx","en":"dicom2pptx",
    "dko":"DICOM 시네 루프를 실제로 재생되는 PowerPoint 덱으로 변환합니다. 완전 로컬 실행이며, 사람이 직접 확인하기 전에는 다음 단계로 넘어가지 않습니다.",
    "den":"Turns DICOM cine loops into a PowerPoint deck that actually plays. Runs entirely locally and will not advance a stage until a human has looked at the preview."},
   {"repo":"video-to-pptx","ko":"video-to-pptx","en":"video-to-pptx",
    "dko":"영상 파일을 슬라이드당 여러 개씩 배치하고 반복재생·되감기를 OOXML에 직접 기록합니다. 비식별화가 끝난 자료의 덱 조립용.",
    "den":"Places videos several to a slide and writes loop and rewind directly into the OOXML. For assembling decks from material that is already de-identified."},
   {"repo":"frontend-medslides","ko":"frontend-medslides","en":"frontend-medslides",
    "dko":"PowerPoint 덱을 디자인 시스템으로 해석해, 저자의 디자인 언어를 유지한 채 편집 가능한 HTML 프레젠테이션으로 재구성합니다.",
    "den":"Reads a PowerPoint deck as a design system and rebuilds it as an editable, component-based HTML presentation that keeps the author's design language."},
  ],
 },
 {
  "dir": "research",
  "ko": "연구 · 행정 하네스", "en": "Research &amp; administration harnesses",
  "note_ko": "Claude Code / Cowork 플러그인 형태의 연구 워크플로. 설계에서 투고까지, 그리고 IRB·행정 서류를 단계별 게이트로 처리합니다.",
  "note_en": "Research workflows packaged as Claude Code / Cowork plugins — design through submission, plus IRB and administrative paperwork, each behind a phase gate.",
  "tools": [
   {"repo":"yumc-research-design","ko":"임상연구 설계 (Phase 0–3)","en":"Study design (Phase 0–3)",
    "dko":"문헌 검색·가설 정련·프로토콜 작성에서 사전등록 <code>prereg.json</code> 잠금까지.",
    "den":"Literature search, hypothesis refinement and protocol writing through to a locked <code>prereg.json</code>."},
   {"repo":"yumc-research-analysis","ko":"임상연구 분석·집필 (Phase 4–6)","en":"Analysis &amp; writing (Phase 4–6)",
    "dko":"데이터 점검·통계 분석·원고 집필. 설계 단계의 <code>prereg.json</code>을 입력으로 받아 STROBE 기준으로 진행합니다.",
    "den":"Data inspection, statistical analysis and manuscript writing, taking the design stage's <code>prereg.json</code> as input and following STROBE."},
   {"repo":"yumc-case","ko":"증례보고 (C0–C5)","en":"Case reports (C0–C5)",
    "dko":"증례 접수부터 투고 직전 자체 동료검토까지. CARE 2013 13항목 구조의 원고를 산출합니다.",
    "den":"From intake to a self-administered peer review before submission, producing a manuscript in the CARE 2013 13-item structure."},
   {"repo":"yeungnam-irb-protocol","ko":"영남대 IRB 제출 문서","en":"Yeungnam IRB documents",
    "dko":"연구계획서·계획서 요약[서식1]·동의면제 점검표[서식41] 생성, 그리고 다기관 연구에서 주관기관 원본을 참여기관용으로 재구성.",
    "den":"Generates the protocol, the protocol summary [Form 1] and the consent waiver checklist [Form 41], and rebuilds a coordinating site's originals for participation as a study site."},
   {"repo":"research-graphical-abstract","ko":"Graphical Abstract","en":"Graphical abstract",
    "dko":"완성된 원고와 핵심 결과에서 저널 톤에 맞는 graphical abstract 생성 프롬프트를 작성합니다.",
    "den":"Turns a finished manuscript and its headline finding into a prompt for a journal-appropriate graphical abstract."},
   {"repo":"research-fund-claim-harness","ko":"연구조성활동비 지급신청","en":"Research fund claims",
    "dko":"학회 참석 후 출장비·등록비 지급신청을 Phase 0–4로 처리합니다. 학회 확인·영수증 정리·출장허가원·신청서 작성·제출 메일 초안.",
    "den":"Handles post-conference travel and registration reimbursement in Phases 0–4: conference lookup, receipts, travel authorisation, the application form, and the submission email."},
  ],
 },
]

FOOT_KO = [
 "<b>면책</b> — 여기 있는 계산기와 시뮬레이터는 임상 교육 및 판단 보조 목적입니다. 정식 검사와 임상의의 종합 평가를 대체하지 않으며, 자동 분류는 교육을 위해 단순화된 것이므로 개별 환자의 진료 판단에 그대로 사용해서는 안 됩니다.",
 "<b>데이터</b> — 웹 도구에는 환자 식별정보 입력란이 없고, 입력값을 저장하거나 외부로 전송하지 않습니다. DICOM을 다루는 도구는 원본 파일을 로컬 밖으로 내보내지 않으며, 픽셀에 새겨진 환자정보는 사람이 직접 확인하도록 게이트를 둡니다.",
]
FOOT_EN = [
 "<b>Disclaimer</b> — the calculators and simulators here are for clinical education and decision support. They do not replace formal studies or the clinician's comprehensive assessment, and their automated classifications are simplified for teaching and must not be applied directly to an individual patient's care.",
 "<b>Data</b> — the web tools have no patient-identifying fields and neither store nor transmit what is entered. The DICOM tools keep original files local and gate on a human check for information burned into the pixels.",
]
