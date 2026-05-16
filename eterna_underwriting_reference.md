# ETERNA INSURANCE SOLUTIONS
## Master Underwriting Intelligence Reference
### Version 1.0 | May 2026 | AI Underwriting Layer — Phase 1

---

> **Purpose:** This document is the structured underwriting knowledge base for the Eterna AI underwriting assistant. It is designed to be converted into vector database embeddings, API-accessible decision logic, and AI agent retrieval systems. Compiled from the Eterna Google Drive (carrier guides, field underwriting references, trivia documents, and training material), supplemented by carrier-published guidelines.

---

## TABLE OF CONTENTS
1. [Carrier Overview & Philosophy](#carrier-overview)
2. [Carrier-by-Carrier Underwriting Profiles](#carrier-profiles)
3. [Cross-Carrier Pattern Analysis](#pattern-analysis)
4. [Health Condition Reference Matrix](#condition-matrix)
5. [Medication Reference Table](#medication-table)
6. [Build/BMI Reference](#bmi-reference)
7. [Issue Pathway Speed Ranking](#speed-ranking)
8. [Product Suitability Matrix](#suitability-matrix)
9. [AI Decision Examples](#ai-examples)
10. [Data Gaps & Update Flags](#data-gaps)

---

## 1. CARRIER OVERVIEW & PHILOSOPHY {#carrier-overview}

| Carrier | Style | Primary Strength | Avoid For |
|---------|-------|-----------------|-----------|
| **Mutual of Omaha** | Conservative-Moderate | FE seniors, controlled conditions | CHF, dementia, active cancer |
| **Ethos** | Tech-forward / Instant | Fastest issue, wide age range, GI backup | Complex impaired risk |
| **CoreBridge (AIG)** | Moderate + GIWL backstop | GIWL for declined clients, IUL accumulation | SIWL for CHF/dementia |
| **InstaBrain** | Instant issue platform | Absolute fastest placement | Any impaired risk |
| **National Life Group** | Accumulation-focused | Max-funded IUL, wealth transfer | FE market (no FE product) |
| **Transamerica** | Brand-recognition / Moderate | Brand-loyal clients, FE, term | Complex impaired risk |
| **American Amicable** | Simplified / FE | Senior FE up to age 85 | IUL strategies |
| **Foresters Financial** | Moderate + member benefits | Cannabis users, living benefits, community | IUL (limited) |
| **F&G Life** | MOST AGGRESSIVE | Impaired risk IUL, Hepatitis, CHF IUL | Pure accumulation vs NLG |

---

## 2. CARRIER-BY-CARRIER UNDERWRITING PROFILES {#carrier-profiles}

---

### MUTUAL OF OMAHA (MOO)
**Style:** Conservative-Moderate | **Best Market:** Final Expense Seniors

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| Living Promise Level | SIWL (FE) | 45-85 | $2K-$40K | ✅ Yes |
| Living Promise Graded | Graded WL (FE) | 45-85 | $2K-$25K | ✅ Yes |
| IULE | IUL | 18-75 | $25K-$350K | ❌ AU |
| Children's WL | Juvenile WL | 0-17 | $5K-$50K | ❌ |

#### Underwriting Tendencies
- **Type 2 Diabetes:** ✅ FAVORABLE — Standard possible; controlled A1C, oral meds (Metformin)
- **Type 1 Diabetes:** ⚠️ MODERATE — Level FE possible if no complications; IUL typically decline
- **COPD (no oxygen):** ✅ FAVORABLE — MOO Living Promise Level is go-to
- **COPD (with oxygen):** ❌ DECLINE — Push to Corebridge GIWL
- **CHF:** ❌ DECLINE SIWL — Push to Corebridge GIWL
- **Cancer 2+ yrs remission:** ✅ FAVORABLE — Level FE possible
- **Cancer active:** ❌ DECLINE — Corebridge GIWL only
- **Stroke 3+ yrs, no deficits:** ✅ FAVORABLE — Level FE
- **Stroke <2 yrs:** ⚠️ GRADED
- **Dementia:** ❌ DECLINE SIWL — Corebridge GIWL only
- **Dialysis/ESRD:** ❌ DECLINE — Corebridge GIWL only
- **Controlled Hypertension:** ✅ Standard
- **Controlled Hyperlipidemia:** ✅ Standard
- **Tobacco:** ✅ Available at tobacco rates
- **DUI:** 5-year lookback; recent = rate or decline
- **Felony:** Case-by-case; within 5 years typically declines

#### Knockout Conditions
Active cancer treatment | CHF (for SIWL Level) | Dementia/Alzheimer's | Dialysis | Oxygen use (for Level FE)

#### Key Contacts
- **New Business:** (800) 775-7894 | statuslines@mutualofomaha.com
- **Underwriting:** (800) 775-7896
- **Quick Quote:** ainqq@mutualofomaha.com
- **Portal:** producer.mutualofomaha.com

#### Living Benefits
✅ Chronic + Terminal on IULE and WL products

#### Best-Fit Client Scenarios
- Senior 65+ with COPD (managed, no oxygen) wanting FE
- Controlled T2 diabetic 50-75 wanting FE
- Stroke survivor 3+ years out, no deficits, wanting FE
- Conservative buyer wanting guaranteed WL

---

### ETHOS (TruStage Platform)
**Style:** Tech-Forward / Instant Issue | **Best Market:** Speed + GI backup

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| TruStage Advantage | SIWL | 20-85 (scaled) | $5K-$100K | ✅ Same-day |
| TruStage Guaranteed | GI WL | 40-85 | $2K-$25K | ✅ Same-day |
| Ethos IUL | IUL | 20-65 | $25K-$1M | ⚠️ AU |

*TruStage Guaranteed: First 2 years = ROP + 10% (modified benefit)*

#### Key Underwriting Notes
- **Cannabis/Marijuana:** May treat casual users as non-tobacco — verify current guidelines
- **Guaranteed Issue:** No health questions at all on TruStage Guaranteed
- **Instant Decisions:** Among fastest in market
- **DUI:** Recent DUI likely declines on Advantage; GI has no concern

#### Knockout (Advantage Product)
Active cancer treatment | Recent organ transplant | HIV+ (non-GI)

#### Living Benefits
✅ Critical + Chronic + Terminal on IUL and WL

#### Best-Fit Client Scenarios
- Client needing same-day issued policy
- Highest-risk client declined elsewhere → TruStage Guaranteed
- Healthy 20-50 wanting IUL with fast decision
- Agent who needs proof of coverage within 24 hours

---

### COREBRIDGE FINANCIAL (AIG)
**Style:** Moderate + GIWL Backstop | **Best Market:** IUL accumulation + FE declined clients

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| SimpliNow Legacy SIWL | SIWL (FE) | 50-80 | $5K-$35K | ✅ |
| GIWL | Guaranteed Issue WL | 50-80 | $5K-$25K | ✅ |
| Agile UW+ (IUL/Term) | AU Program | 18-65 | Up to $2M | ⚠️ 24-72hr |
| QoL Max Accumulator+ | IUL | 18-65 | $50K+ | ❌ Full UW |

**⭐ GIWL KEY INSIGHT:** Corebridge GIWL = **no health questions, no exam** — the ultimate backstop for any FE client who cannot qualify for simplified issue. Best-in-market product for CHF, active cancer, dementia, dialysis clients.

#### Underwriting Tendencies (AU Program, Ages 18-60)
- **Anxiety / Depression:** ✅ All AU age groups
- **Asthma:** ✅ All AU age groups
- **OSA (treated):** ✅ All AU age groups
- **Controlled HTN:** ✅ All AU age groups
- **Controlled Hyperlipidemia:** ✅ All AU age groups
- **Type 2 Diabetes (51-60):** ✅ Standard possible
- **Stroke (18-40):** ❌ Decline AU — F&G only option
- **Heart Disease (18-40):** ❌ Very likely decline
- **CHF (SIWL):** ❌ Decline → GIWL is the answer
- **Dementia:** ❌ SIWL decline → GIWL is the answer
- **Dialysis:** ❌ SIWL decline → GIWL is the answer
- **Active Cancer:** ❌ SIWL decline → GIWL is the answer

#### Knockout for SIWL (but GIWL available)
CHF | Active cancer | Dementia | Dialysis | Recent major cardiac events

#### Key Contacts
- **Main:** (877) 686-7954
- **Advanced Sales:** (855) 323-6923
- **Email:** aig_ain@aglife.com

#### Living Benefits
✅ On IUL products | ❌ Not on SIWL or GIWL

#### Best-Fit Client Scenarios
- **CHF history wanting FE → GIWL is the ONLY viable option in the lineup**
- **Active cancer treatment wanting FE → GIWL**
- **Dementia or memory issues → GIWL**
- **Dialysis → GIWL**
- Healthy 35-55 wanting max-funded IUL → QoL Max Accumulator+
- Any client declined by all other FE carriers → GIWL as last resort

---

### INSTABRAIN
**Style:** Instant Issue Platform | **Best Market:** Fastest possible placement

#### Key Facts
- Algorithm-based instant underwriting decisions
- Health history, RX database, and MVR checked at point of sale
- **Fastest time-to-issued-policy in the Eterna lineup**
- Not appropriate for impaired risk or complex health histories

> ⚠️ **DATA GAP FLAG:** Pull current product lineup, issue ages, coverage amounts, and carrier partnerships from Eterna contracting portal. Verify current InstaBrain guidelines before submitting — this platform evolves rapidly.

#### Best-Fit Client Scenarios
- Completely healthy client (clean health, driving, background)
- Agent needs same-call policy issuance
- Client resistant to delays and wants coverage NOW

---

### NATIONAL LIFE GROUP (NLG)
**Style:** Accumulation-Focused / Moderate | **Best Market:** Max-funded IUL

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| FlexLife IUL | IUL | 0-85 | $50K-$2M+ | ❌ AU/Full UW |
| FlexLife NL (NY) | IUL (NY) | 0-85 | $50K-$2M+ | ❌ |

**WriteAway AU Program:** Ages 18-60 | Up to $2M — no exam accelerated

#### Structuring FlexLife for Max Accumulation
1. **MEC Avoidance:** Yes-Adjust Face
2. **Solve for:** Minimum DB / Max Cash Value
3. **Pay to:** A65 (retirement focus)
4. **Allocation:** Specified by client risk tolerance
5. **Premium Mode:** Monthly most common

#### Underwriting Tendencies
- **Anxiety/Depression:** ✅ Ages 18-60
- **Asthma:** ✅ All ages
- **OSA (treated):** ✅ All ages
- **Controlled HTN:** ✅ All ages
- **Hyperlipidemia (statin):** ✅ All ages
- **Obesity meds (GLP-1):** ✅ NA accepts
- **Bariatric surgery (5+ yrs):** ✅
- **Epilepsy (Grand/Petit mal):** ✅ Possible
- **T2 Diabetes:** ✅ Ages 51-60 — standard possible
- **Stroke (18-40):** ❌ Decline AU
- **Heart Disease (18-40):** ❌ Very likely decline

#### Key Contacts
- **Phone:** (800) 906-3310
- **Portal:** nationallife.com/agent → iGo eApp

#### Living Benefits
✅ Chronic + Critical + Terminal on FlexLife

#### Best-Fit Client Scenarios
- High-premium client wanting maximum tax-free retirement accumulation
- Wealth transfer planning with large death benefit needs
- Business owner or high-earner wanting premium-financed IUL strategy
- Client 0-85 wanting permanent IUL (widest age range for IUL in lineup)

---

### TRANSAMERICA
**Style:** Brand-Recognition / Moderate-Conservative | **Best Market:** Brand-loyal clients

#### Products
- Final Expense Whole Life (SIWL)
- Term Life (AU/Full UW)
- IUL Products

#### Key Notes
- Strong brand recognition — use when client specifically trusts the Transamerica name
- **Living benefits primarily terminal illness** on WL (weaker than Foresters/MOO)
- **Foreign national capability** — international review team available
- Not the top choice for impaired risk or max accumulation IUL

#### Key Contacts
- **New Business:** (800) 451-7586 | bgacasemanagement@transamerica.com
- **Sales:** (866) 545-9058 | lifesales@transamerica.com
- **Foreign National:** international@transamerica.com

#### Best-Fit Client Scenarios
- Client specifically requesting Transamerica by name
- Foreign national requiring coverage
- Simple FE client wanting brand-name recognition

---

### AMERICAN AMICABLE (AMAM)
**Style:** Simplified Issue / FE Focused | **Best Market:** Senior FE up to age 85

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| Family Choice | WL | 0-49 | Max $30K | ✅ |
| Senior Choice | WL (FE) | 50-85 | Max $50K | ✅ |

- **All banks accepted** (no physical bank requirement)
- Simple application process — streamlined FE workflow

#### Best-Fit Client Scenarios
- Senior 50-85 wanting FE up to $50K
- Client needing all-bank-accepted simplified issue
- Family product for younger members (Family Choice 0-49)

---

### FORESTERS FINANCIAL
**Style:** Moderate + Member Benefits | **Best Market:** Cannabis users, living benefits, community

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| PlanRight SIWL | SIWL (FE) | 50-85 | $2K-$35K | ✅ |
| Live Well Plus | Participating WL | 18-60 | Varies | ❌ Full UW |

#### ⭐ KEY COMPETITIVE ADVANTAGE: Cannabis = NON-TOBACCO
**Foresters treats casual marijuana/cannabis use as NON-TOBACCO.** This is unique in the market and can save clients hundreds of dollars per year vs tobacco rates they'd receive at other carriers.

#### Underwriting Tendencies
- **Cannabis (casual):** ✅ NON-TOBACCO rate (unique in Eterna lineup)
- **Cancer 2+ yrs remission:** ✅ Level FE
- **Cancer <2 yrs:** ⚠️ Graded option
- **Stroke 3+ yrs, no deficits:** ✅ Level FE
- **Stroke <2 yrs:** ⚠️ Graded
- **Renal disease (no dialysis):** ⚠️ Graded
- **Dialysis:** ❌ Corebridge GIWL
- **Dementia:** ❌ Corebridge GIWL
- **Drug history:** ⚠️ 10-year lookback questionnaire (alcohol, amphetamines, cocaine, opiates, marijuana, etc.)
- **Child rider:** ✅ Available
- **Member benefits:** ✅ Fraternal benefits — grants, scholarships, community events

#### Drug History Questionnaire (10-Year Lookback)
Foresters requires a Drug or Substance Use Questionnaire covering: Alcohol, Amphetamines, Barbiturates, CBD, Cocaine, Hallucinogens, Marijuana (method + frequency + prescription?), Opiates, Solvents, and other substances. Also: IV drug use history, Hepatitis B/C positive status.

#### Knockout
Active cancer treatment (Level) | Dialysis | Dementia

#### Key Contacts
- **New Business:** (866) 466-7166, Opt 2 | nbunewbiz@foresters.com
- **Portal:** myezbiz.foresters.com

#### Living Benefits
✅ Chronic + Critical + Terminal on WL and FE — **Strongest living benefits suite in FE market**

#### Best-Fit Client Scenarios
- **Cannabis/marijuana user** — saves tobacco rate premium (unique to Foresters)
- FE client wanting **full** living benefits (chronic + critical + terminal)
- Client valuing fraternal community benefits, grants, scholarships
- Cancer history 2+ years in remission
- Stroke survivor 3+ years

---

### F&G LIFE (Fidelity & Guaranty Life)
**Style:** MOST AGGRESSIVE — Broadest Impaired Risk Acceptance | **Best Market:** Impaired risk IUL, hepatitis, CHF IUL

#### Products
| Product | Type | Ages | Coverage | Instant? |
|---------|------|------|----------|----------|
| Pathsetter IUL | IUL (Accumulation) | 0-80 | $50K-$1M+ | InstApproval® |
| ExecuDex IUL | Instant Decision IUL | 18-60 | $150K-$1M | ✅ Instant |
| Everlast IUL | IUL (Protection Focus) | — | — | AU |

**InstApproval® Free/Exam-Free:** Ages 0-60 (61-65 with evidence) | Max $1M

#### ⭐ F&G IS THE CARRIER OF LAST RESORT FOR IMPAIRED RISK IUL

#### Underwriting Tendencies by Age Group

**Ages 18-40:**
| Condition | F&G Decision |
|-----------|--------------|
| Diabetes Type 1 (onset 20+) | ✅ Highly rated at best |
| Diabetes Type 2 | ✅ Typically rated at best |
| Arrhythmia | ✅ Typically rated |
| Asthma | ✅ Approvable |
| Bipolar | ✅ Highly rated |
| COPD | ✅ Approvable |
| Crohn's/UC | ✅ Rated |
| Depression/Anxiety | ✅ Approvable |
| Epilepsy (Grand/Petit Mal) | ✅ Possible |
| Hepatitis B/C | ✅ **ONLY carrier in lineup** |
| Heart Disease | ❌ Very likely decline (all accelerated) |
| Hyperlipidemia (statin) | ✅ Approvable |
| Hypertension (controlled) | ✅ Approvable |
| MS | ✅ Rated |
| Obesity Meds | ✅ Accepted |
| Bariatric (5+ yrs) | ✅ Accepted |
| OSA (treated) | ✅ Approvable |
| Parkinson's | ✅ Rated |
| RA | ✅ Rated |
| Stroke | All accelerated decline; F&G only option |
| BMI <37 | ✅ Standard-Rated |
| BMI 37-46 | ✅ Rated (F&G only above 37) |

**Ages 41-50:**
| Condition | F&G Decision |
|-----------|--------------|
| Diabetes Type 1 (onset 20+) | ✅ Moderately-Highly rated |
| Diabetes Type 2 | ✅ STD to mildly rated |
| Heart Disease | ✅ Typically moderately rated |
| Stroke | ✅ Highly rated at best |
| Bipolar | ✅ Moderately rated |
| All others from 18-40 | Same or slightly better acceptance |

**Ages 51-60:**
| Condition | F&G Decision |
|-----------|--------------|
| Diabetes Type 1 (onset 20+) | ✅ Highly rated at best |
| Diabetes Type 2 | ✅ Standard possible |
| Heart Disease | ✅ Typically mildly rated |
| Bipolar | ✅ Mildly-Moderately rated |
| CHF | ✅ Typically mildly rated (vs decline at most others) |
| Stroke | ✅ Highly rated at best |
| All impaired conditions | F&G remains most accepting |

#### ⭐ UNIQUE CAPABILITIES (Not available at other Eterna carriers)
1. **Hepatitis B/C** — F&G ONLY. All other carriers decline.
2. **CHF + IUL** — F&G mildly rated for ages 41-60. Others decline or GIWL only.
3. **Stroke + IUL** — F&G only viable AU option for younger clients.
4. **Bipolar + IUL** — F&G highly-moderately rated. Others decline.
5. **BMI 37-46** — F&G only AU carrier above BMI 37.
6. **Diabetes Type 1 IUL** — F&G only (onset age 20+).

#### Knockout Conditions
Very high BMI (>46 typically) | Active cancer treatment (push to Graded/GIWL) | Dialysis (GIWL)

#### Key Contacts
- **Risk Assessment/UW:** (800) 445-6758, Opt 2 Opt 1 | riskassessment@fglife.com
- **New Business:** LifeCaseMgmt@fglife.com
- **Sales:** (800) 357-8734 | Life.Sales@fglife.com
- **Portal:** saleslink.fglife.com

#### Structuring Pathsetter (Max Cash Value)
1. Solve for Max Accumulation → Specified Premiums
2. MEC Avoidance: Minimum Non-MEC Death Benefit checked
3. Pay to A65 (retirement age)
4. Allocation: 50% Blackrock / 50% Morgan Stanley 110% PAR (recommended)

#### Living Benefits
✅ Chronic + Critical + Terminal on Pathsetter and Everlast

#### Best-Fit Client Scenarios
- **Diabetic (T1 or T2) wanting IUL** — F&G primary choice
- **CHF history, non-FE** — F&G rated IUL vs Corebridge GIWL for FE
- **Hepatitis B or C** — F&G or decline (no other option)
- **Stroke survivor 41-60 wanting IUL** — F&G only viable path
- **Bipolar disorder + IUL** — F&G only option in lineup
- **BMI 37-46** — F&G only AU carrier above BMI 37
- **COPD + IUL** — F&G Pathsetter
- **MS, Parkinson's, Crohn's, RA + IUL** — F&G rated at best

---

## 3. CROSS-CARRIER PATTERN ANALYSIS {#pattern-analysis}

### Which Carriers Are Strongest for Diabetics?
| Situation | Best Carrier |
|-----------|-------------|
| T2 Diabetes + FE (senior) | Mutual of Omaha (Level), CoreBridge SIWL |
| T2 Diabetes + IUL (18-50) | **F&G Pathsetter** (strongest) |
| T2 Diabetes + IUL (51-60) | **F&G** (Standard possible) or CoreBridge AU |
| T1 Diabetes + IUL | **F&G ONLY** (onset age 20+, highly rated) |
| T1 Diabetes + FE | MOO Level (no complications) or Corebridge GIWL |

### Which Carriers Are Best for CHF History?
| Situation | Best Carrier |
|-----------|-------------|
| CHF + Final Expense | **Corebridge GIWL** (ONLY — no health questions) |
| CHF + IUL | **F&G** (mildly rated 51-60) |
| CHF + younger adult IUL | F&G (highly rated, but only option) |

### Which Carriers Tolerate Recent DUIs?
- **2 years or less:** All carriers = decline or graded. Push to simplified issue.
- **2-5 years:** F&G (case-by-case), Ethos (simplified track).
- **5+ years:** Most carriers acceptable; preferred rates require 10 years.

### Aggressive vs. Conservative Ranking
1. **F&G** — Most aggressive (widest impaired risk acceptance)
2. **Ethos** — Aggressive on instant issue + GI backup
3. **Foresters** — Aggressive on cannabis, living benefits
4. **CoreBridge** — Moderate (GIWL fills the gaps)
5. **MOO** — Conservative-Moderate
6. **NLG** — Moderate on IUL
7. **American Amicable** — Moderate on FE
8. **Transamerica** — Most conservative for complex cases

### Fastest to Slowest Issue
| Rank | Carrier/Product | Speed |
|------|----------------|-------|
| 1 | InstaBrain | Real-time |
| 2 | Corebridge GIWL | Same day |
| 3 | Ethos TruStage Guaranteed | Same day |
| 4 | Ethos TruStage Advantage | Same day |
| 5 | F&G ExecuDex | Real-time to 24hr |
| 6 | MOO Living Promise | 24-48 hrs |
| 7 | Foresters PlanRight | 24-72 hrs |
| 8 | American Amicable | 24-72 hrs |
| 9 | Corebridge AU+ | 24-72 hrs |
| 10 | F&G InstApproval® | 24-72 hrs |
| 11 | NLG WriteAway | 3-7 days |
| 12 | Transamerica | 3-14 days |
| 13 | Full UW (any carrier) | 2-6 weeks |

### Strongest for Max-Funded IUL
1. **National Life Group FlexLife** — Top accumulation design
2. **Corebridge QoL Max Accumulator+** — Strong competitor
3. **F&G Pathsetter** — Best for impaired risk max-funded

### Easiest Simplified/Guaranteed Issue
1. **Corebridge GIWL** — Zero health questions (GI)
2. **Ethos TruStage Guaranteed** — Zero health questions (GI)
3. **MOO Living Promise** — Quick SIWL decisions
4. **Foresters PlanRight** — SIWL instant
5. **American Amicable** — SIWL easy process

### Best for Older Clients (65+)
1. MOO Living Promise (up to 85)
2. American Amicable Senior Choice (up to 85)
3. Ethos TruStage (up to 85)
4. Foresters PlanRight (up to 85)
5. Corebridge GIWL (50-80)

### Best for Smokers/Tobacco
- **All carriers:** Tobacco rates apply
- **Cannabis users (casual):** **Foresters — NON-TOBACCO rate (unique)** vs tobacco rate everywhere else
- **DUI + smoker:** F&G most flexible for combined risk

---

## 4. HEALTH CONDITION REFERENCE MATRIX {#condition-matrix}

| Condition | MOO | Ethos | CoreBridge | InstaBrain | NLG | Transamerica | AmAm | Foresters | F&G |
|-----------|-----|-------|-----------|-----------|-----|-------------|------|-----------|-----|
| T2 Diabetes (controlled) | ✅ FE Level | ✅ | ✅ AU | ✅ | ✅ | ✅ | ✅ | ✅ FE | ✅ IUL Best |
| T1 Diabetes | ⚠️ FE only | ⚠️ | ❌ IUL | ❌ | ❌ | ❌ | ⚠️ | ⚠️ | ✅ Only IUL option |
| CHF | ❌ SIWL | ❌ | GIWL ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ IUL (rated) |
| COPD (no O2) | ✅ FE | ✅ | ✅ SIWL | ⚠️ | ⚠️ | ⚠️ | ✅ FE | ✅ FE | ✅ IUL |
| COPD (with O2) | ❌ | ❌ | GIWL ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cancer 2+ yr remission | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ |
| Cancer active | ❌ | ❌ | GIWL ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | Graded |
| Stroke 3+ yr | ✅ FE | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ Rated IUL |
| Stroke recent | Graded | Graded | GIWL | ❌ | ❌ | ❌ | Graded | Graded | ✅ Rated |
| Dementia | ❌ | ❌ | GIWL ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Dialysis | ❌ | ❌ | GIWL ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Bipolar | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Only IUL option |
| Hepatitis B/C | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ✅ ONLY |
| Cannabis (casual) | Tobacco | ⚠️ | Tobacco | Tobacco | Tobacco | Tobacco | Tobacco | ✅ Non-Tobacco | Tobacco |
| BMI 37-46 | ❌ AU | ❌ AU | ❌ AU | ❌ | ❌ AU | ❌ | FE only | FE only | ✅ Rated AU |
| Controlled HTN | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Controlled Hyperlipidemia | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Depression (stable, 1 med) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Anxiety (stable) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OSA (treated, CPAP) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hypothyroidism | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GERD | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| MS | ❌ IUL | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Rated |
| Parkinson's | ❌ IUL | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Rated |
| Crohn's/UC | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Rated |

**Legend:** ✅ = Acceptable | ⚠️ = Possible with conditions | ❌ = Decline for that product type

---

## 5. MEDICATION REFERENCE TABLE {#medication-table}

| Medication | Indicates | Carrier Impact |
|-----------|-----------|---------------|
| Metformin | T2 Diabetes | ✅ All carriers favorable — controlled signal |
| Glipizide | T2 Diabetes (oral) | ✅ Favorable — controlled T2 |
| Insulin | T1 or T2 Diabetes (insulin-dependent) | ⚠️ T1 IUL = F&G only; T2 FE = MOO/CB |
| Lisinopril / Losartan / Amlodipine | Hypertension | ✅ All carriers — controlled HTN |
| Atorvastatin / Rosuvastatin / Simvastatin | High Cholesterol | ✅ All carriers — managed lipids |
| Sertraline / Escitalopram | Anxiety / Depression | ✅ Single med, stable = favorable all carriers |
| Bupropion | Depression OR smoking cessation | ⚠️ Document purpose — smoking cessation vs depression affects assessment |
| Metoprolol / Atenolol | Cardiac (Arrhythmia / Heart Disease) | ⚠️ Full cardiac history needed; F&G most flexible |
| Levothyroxine | Hypothyroidism / Hashimoto's | ✅ All carriers — benign thyroid condition |
| Spiriva / Advair / Albuterol | COPD or Asthma | ⚠️ Asthma = all AU carriers OK; COPD = F&G IUL, MOO FE |
| Omeprazole / Pantoprazole | GERD / Acid Reflux | ✅ All carriers — benign GI condition |
| Zolpidem / Trazodone | Sleep Disorder | ⚠️ May indicate depression — probe underlying cause |
| Celecoxib / Ibuprofen Rx | Arthritis / Chronic Pain | ⚠️ Probe underlying cause — RA vs osteoarthritis |
| Ozempic / Wegovy / Semaglutide | Obesity (GLP-1) | ⚠️ NLG, Symetra, F&G accept; others verify |
| CPAP device | Sleep Apnea (OSA) | ✅ Treated OSA = all carriers favorable |
| Inhalers generally | Asthma (mild-intermittent) | ✅ All AU carriers; check age for juveniles |

---

## 6. BUILD / BMI REFERENCE {#bmi-reference}

| BMI Range | AU Carriers | FE/SI Options |
|-----------|------------|---------------|
| Under 30 | ✅ All — Preferred/Standard | ✅ All |
| 30-37 | ✅ All — Standard to Mildly Rated | ✅ All |
| 37-42 | ✅ **F&G only** (rated) | ✅ FE SI carriers |
| 42-46 | ✅ **F&G only** (highly rated) | ✅ FE SI carriers |
| Above 46 | ❌ Decline AU | ✅ FE SI and GI only |
| Max SI BMI | ~50 (varies by carrier/product) | |

---

## 7. ISSUE PATHWAY SPEED RANKING {#speed-ranking}

### Fastest Issue Pathways

| Rank | Product/Program | Speed | Health Flexibility |
|------|----------------|-------|--------------------|
| 1 | InstaBrain | Real-time | Healthy only |
| 2 | Corebridge GIWL | Same day | Any health — no questions |
| 3 | Ethos TruStage Guaranteed | Same day | Any health — no questions |
| 4 | Ethos TruStage Advantage | Same day | Moderate health |
| 5 | F&G ExecuDex (InstApproval®) | Real-time to 24hr | Healthy (18-60) |
| 6 | MOO Living Promise | 24-48 hrs | Moderate FE health |
| 7 | Foresters PlanRight | 24-72 hrs | Moderate FE health |
| 8 | American Amicable | 24-72 hrs | Moderate FE health |
| 9 | Corebridge AU+ | 24-72 hrs | 18-60 manageable health |
| 10 | F&G InstApproval® / AU | 24-72 hrs | 0-60 impaired risk |
| 11 | NLG WriteAway | 3-7 days | 18-60 moderate health |
| 12 | Transamerica AU | 3-14 days | Moderate health |
| 13 | Full UW (any carrier) | 2-6 weeks | Full complexity |

---

## 8. PRODUCT SUITABILITY MATRIX {#suitability-matrix}

### By Product Goal

| Goal | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|
| **Final Expense** | MOO, Corebridge GIWL | Foresters, Ethos, AmAm | Transamerica, F&G Graded |
| **IUL Accumulation** | NLG FlexLife, Corebridge QoL Max | F&G Pathsetter (impaired) | Ethos IUL, Transamerica IUL |
| **IUL Impaired Risk** | **F&G Pathsetter** | Corebridge (manageable) | All others decline |
| **Instant Issue** | InstaBrain, Ethos, Corebridge GIWL | MOO, Foresters, F&G ExecuDex | Corebridge AU+ |
| **Living Benefits (FE)** | Foresters (Chronic+Critical+Terminal) | MOO, Ethos | Transamerica (Terminal only) |
| **Living Benefits (IUL)** | F&G, NLG, Corebridge QoL | Ethos IUL, Transamerica IUL | |
| **Max-Funded IUL** | NLG FlexLife, Corebridge QoL Max Acc+ | F&G Pathsetter | |
| **Clients 65-85** | MOO, AmAm (to 85) | Ethos, Foresters (to 85) | Corebridge GIWL (to 80) |
| **Cannabis Users** | **Foresters (non-tobacco rate)** | Ethos (verify) | All others = tobacco rate |
| **Hepatitis B/C** | **F&G ONLY** | None | N/A — F&G or decline |
| **CHF (FE)** | **Corebridge GIWL ONLY** | None | N/A |
| **CHF (IUL, 41-60)** | **F&G** (mildly rated) | None in lineup | |

---

## 9. AI DECISION EXAMPLES {#ai-examples}

### Example Query 1
**"52-year-old, Type 2 diabetic 4 years, controlled A1C, smoker, wants permanent coverage with living benefits, $300/month budget"**

**AI Recommendation:**
- **Primary:** F&G Pathsetter IUL — T2 diabetic age 51-60: Standard possible. Smoker = tobacco rates but still approvable. $300/month is solid IUL premium. Full living benefits included.
- **Secondary:** Corebridge QoL Max Accumulator+ — only if A1C is excellent and no other risk factors
- **Avoid:** MOO or NLG for IUL — F&G is materially stronger for T2 diabetic 51-60
- **Tobacco note:** All carriers will rate as tobacco. Accept this reality and find best product otherwise.

---

### Example Query 2
**"Client had CHF 7 years ago, wants final expense"**

**AI Recommendation:**
- **Primary:** Corebridge GIWL — CHF = automatic decline on ALL SIWL Level products. GIWL has NO health questions. Max $25K coverage. Issue ages 50-80.
- **Secondary:** F&G IUL if client is younger (41-60) and CHF is well-managed and client wants IUL instead of FE
- **Do NOT submit to:** MOO Living Promise Level, Foresters PlanRight Level, Ethos Advantage, AmAm — all decline CHF

---

### Example Query 3
**"45-year-old casual cannabis user (2x/week recreational), excellent health otherwise, wants whole life with living benefits"**

**AI Recommendation:**
- **Primary:** Foresters Live Well Plus or PlanRight — ONLY carrier treating casual cannabis as NON-TOBACCO. Saves potentially $100-200+/month vs tobacco rates. Full living benefits (Chronic + Critical + Terminal).
- **Secondary:** Ethos (verify current cannabis policy)
- **Avoid:** All other carriers — will rate as tobacco, costing client significantly more

---

### Example Query 4
**"38-year-old with Hepatitis C, otherwise healthy, wants IUL for retirement savings"**

**AI Recommendation:**
- **Primary:** F&G Pathsetter IUL — THE ONLY CARRIER in the Eterna lineup that accepts Hepatitis B/C
- **No secondary option** — all other carriers decline
- **Action:** Quick quote with F&G risk assessment line before presenting to client

---

### Example Query 5
**"Client needs coverage issued this week — healthy 28-year-old, wants IUL, no health issues"**

**AI Recommendation:**
- **Primary:** InstaBrain (fastest) or F&G ExecuDex (instant decision IUL, 18-60)
- **Secondary:** Ethos IUL (same-day decision capability)
- **If IUL not instant:** Corebridge AU+ (24-72 hours)
- **Avoid:** NLG, Transamerica full UW — 2-6 week timeline doesn't serve client

---

### Example Query 6
**"68-year-old with COPD (no oxygen, well managed), wants $15K final expense coverage"**

**AI Recommendation:**
- **Primary:** Mutual of Omaha Living Promise Level — COPD without oxygen = Level FE possible. Age 68 is in 45-85 sweet spot. $15K well within coverage range.
- **If recent exacerbation:** MOO Graded or Foresters PlanRight Graded
- **Last resort:** Corebridge GIWL if Graded also declines

---

### Example Query 7
**"55-year-old with bipolar disorder (managed, on medication), wants IUL with living benefits"**

**AI Recommendation:**
- **Primary:** F&G Pathsetter IUL — ONLY viable IUL option in the lineup for bipolar disorder. Mildly-Moderately rated for ages 51-60.
- **No secondary option** in current lineup
- **Quick quote:** F&G risk assessment line first to confirm rating before presenting

---

## 10. DATA GAPS & UPDATE FLAGS {#data-gaps}

| Carrier | Gap | Action Required |
|---------|-----|-----------------|
| InstaBrain | Current product lineup, issue ages, coverage ranges, carrier partnerships | Pull from Eterna contracting portal |
| F&G | Confirm ExecuDex current face amount range and physical bank requirement | Verify on saleslink.fglife.com |
| MOO | Confirm IULE current product specs and AU eligibility | Verify at producer.mutualofomaha.com |
| Ethos | Confirm current cannabis/marijuana underwriting policy | Verify at agents.ethoslife.com |
| Transamerica | Current FE product specs and living benefit riders | Verify at tatransact.com |
| AmAm | Confirm living benefit rider availability | Verify at americanamicable.com |
| All carriers | GLP-1/obesity medication acceptance (Ozempic, Wegovy) | Rapidly evolving guideline — verify quarterly |
| F&G | Confirm current Hepatitis B/C acceptance is still in effect | Verify with risk assessment line |

---

## LOOKBACK PERIOD QUICK REFERENCE

| Event | Lookback | Notes |
|-------|----------|-------|
| DUI | 5 years (most); 10 for preferred | 2 yrs or less = likely decline all carriers |
| Felony | 5-10 years | Within 5 years = typically decline |
| Cancer (FE Level) | 2+ years in remission | < 2 yrs = Graded or GIWL |
| Cancer (active) | N/A | GIWL only |
| Heart attack (FE Level) | 3+ years | < 3 = Graded |
| Stroke (FE Level) | 3+ years, no deficits | < 3 or deficits = Graded |
| Drug use | 10 years (Foresters); 5-10 others | Varies by substance |
| Hepatitis B/C | N/A (current status matters) | F&G only carrier accepting |

---

*This document is the Phase 1 underwriting intelligence foundation for the Eterna AI assistant. Phase 2 will incorporate real-world submission outcomes (approved/declined/rated) to refine carrier placement probability scores.*

*Compiled from: Eterna Google Drive (carrier guides, field UW reference FILE_0648, Foresters WL comparison, Prime Agency Quick Guide, Life Insurance Trivia, carrier directory spreadsheet, agent scripts), supplemented by published carrier guidelines.*

**Next Steps:**
1. Convert JSON file to vector embeddings (OpenAI, Pinecone, Weaviate, or Chroma)
2. Build API decision tree on top of carrier_pattern_analysis nodes
3. Add real-time quote integration (Integrity, FFL tools)
4. Start logging submitted cases with outcomes to train ML placement model
