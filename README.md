# REGSHIELD
# SENTINEL-G

### AI-Powered Anti-Money Laundering & Cyber-Forensic Intelligence Platform

<p align="center">

**Detect. Investigate. Explain. Protect.**

An intelligent AML platform designed to help financial institutions detect suspicious transaction behaviour, uncover mule networks, investigate financial crime, and maintain an auditable compliance trail.

</p>

---

## 🚨 Overview

**SENTINEL-G** is an AI-powered Anti-Money Laundering (AML) and financial cyber-forensics platform designed for banks, fintech companies, and financial institutions.

Traditional AML systems often rely heavily on static rules and generate large volumes of alerts that require manual investigation.

SENTINEL-G takes a broader approach by combining:

* Multi-engine AML risk detection
* Behavioural feature analysis
* Graph-based transaction intelligence
* Explainable AI
* AI-assisted investigation
* KYC and PEP risk analysis
* Jurisdiction risk analysis
* Real-time dashboard architecture
* Compliance case management
* Immutable audit trails

The objective is not to replace compliance officers.

**SENTINEL-G is designed to make investigators faster, better informed, and more consistent.**

---

# 🎯 Problem Statement

Money laundering and mule-account networks are becoming increasingly sophisticated.

Criminals can:

* Split large transactions into smaller amounts
* Rapidly move funds between multiple accounts
* Use multiple mule accounts
* Create circular transaction patterns
* Route funds through multiple jurisdictions
* Use apparently unrelated accounts to hide relationships
* Change their behaviour to avoid conventional rules

A single suspicious transaction may look normal when viewed independently.

The real pattern often appears only when we analyse:

**Behaviour + Time + Relationships + Network + Context**

SENTINEL-G is designed around this principle.

---

# 💡 Our Approach

Instead of asking only:

> "Is this transaction suspicious?"

SENTINEL-G asks:

> **"Does this transaction fit the customer's normal behaviour, and what does it reveal about the surrounding financial network?"**

The platform combines multiple independent signals to generate a transparent risk assessment.

```text
Transaction
     │
     ▼
Feature Engineering
     │
     ├── Structuring Analysis
     ├── Velocity Analysis
     ├── Network Analysis
     ├── PEP Analysis
     ├── Jurisdiction Analysis
     └── KYC Analysis
     │
     ▼
Risk Aggregation
     │
     ▼
Explainable Investigation
     │
     ▼
Compliance Officer
     │
     ▼
Case / STR Workflow
     │
     ▼
Immutable Audit Trail
```

---

# 🔍 Core Features

## 1. Multi-Engine AML Detection

SENTINEL-G combines six major risk engines.

### Structuring Engine

Detects potential:

* Transaction splitting
* Smurfing
* Threshold avoidance
* Repeated sub-threshold transactions

Example:

```text
₹4,00,000
₹3,00,000
₹5,00,000
₹3,00,000
```

Individual transactions may appear normal, but their cumulative behaviour can indicate potential structuring.

---

### Velocity Engine

Detects unusual changes in transaction frequency and speed.

Examples:

* Sudden transaction bursts
* Large numbers of transactions in short periods
* Rapid movement of funds
* Abnormal transaction frequency compared with historical behaviour

---

### Network Engine

Represents financial activity as a graph.

```text
Account = Node
Transaction = Edge
```

The engine can analyse:

* Degree centrality
* Betweenness centrality
* PageRank
* Community structures
* Transaction cycles
* Connected account clusters

This helps expose potential:

* Mule rings
* Layered laundering
* Hub accounts
* Circular fund movement
* Hidden financial relationships

---

### PEP Engine

Identifies relationships or exposure associated with Politically Exposed Persons and supports enhanced risk assessment.

---

### Jurisdiction Engine

Evaluates transaction exposure to:

* High-risk jurisdictions
* Cross-border activity
* Jurisdictional risk indicators

---

### KYC Engine

Evaluates consistency between customer information and observed financial behaviour.

Examples:

```text
Declared Income: ₹25,000/month
Observed Activity: ₹20,00,000/month
```

Such inconsistencies can contribute to elevated risk.

---

# 🧠 2. Explainable Risk Scoring

SENTINEL-G does not rely solely on a black-box "High Risk" label.

Risk can be decomposed into contributing signals.

Example:

```text
Structuring Risk       → 22
Velocity Risk          → 18
Network Risk           → 27
Jurisdiction Risk      → 10
KYC Risk               → 12
                         ───
Overall Risk           → 89
```

This allows investigators to understand:

* Why an account was flagged
* Which engines contributed
* Which indicators increased risk
* What evidence requires investigation

---

# 🤖 3. AI Investigator

The AI Investigator converts analytical results into human-readable investigation summaries.

Instead of showing only:

```text
Risk Score: 89
```

the platform can provide an explanation such as:

```text
The account exhibited a significant increase in transaction
velocity and interacted with multiple new beneficiaries within
a short period. Network analysis also identified connections
to several high-risk accounts.
```

The AI is designed as an **investigation assistant**, not an autonomous compliance decision-maker.

---

# 🕸️ 4. Graph-Based Financial Forensics

Money laundering is often a network problem rather than an individual transaction problem.

SENTINEL-G models transactions as:

```text
          Account B
         /          \
        /            \
Account A ───────── Account C
        \            /
         \          /
          Account D
```

This enables investigators to move from:

**Transaction-level analysis**

to

**Network-level analysis**

and identify relationships that may not be obvious from individual transactions.

---

# 👤 5. Behavioural Intelligence

The platform derives behavioural features from transaction history.

Examples include:

* Transaction frequency
* Average transaction amount
* Transaction velocity
* Beneficiary count
* Cash transaction ratio
* Night-time transaction ratio
* Weekend activity
* Behaviour change indicators
* Transaction entropy
* Graph connectivity

The production vision is to maintain a continuously evolving behavioural profile for each customer.

---

# 🛡️ 6. Human-in-the-Loop Compliance

SENTINEL-G is designed around the principle:

> **AI assists. Humans decide.**

The platform does not assume that an AI prediction alone should automatically result in an account freeze or regulatory action.

A typical workflow is:

```text
Alert
  ↓
Investigation
  ↓
Evidence Review
  ↓
AI Explanation
  ↓
Compliance Officer
  ↓
Manager / Checker
  ↓
STR Workflow
```

This maintains human accountability throughout the investigation lifecycle.

---

# 📁 7. Evidence Management

Investigators can associate evidence with a case, including:

* Transaction information
* Risk analysis
* Network visualizations
* Investigation notes
* Generated reports
* Supporting documents

This creates a central investigation context rather than forcing officers to work across disconnected systems.

---

# 🔐 8. Immutable Compliance Ledger

SENTINEL-G includes a tamper-evident audit architecture based on cryptographic hash chaining.

A simplified chain looks like:

```text
Record 1
Hash: A123
   │
   ▼
Record 2
Previous Hash: A123
Hash: B456
   │
   ▼
Record 3
Previous Hash: B456
Hash: C789
```

If an earlier record is modified, its hash changes and the chain becomes inconsistent.

This provides:

* Auditability
* Traceability
* Data integrity
* Accountability
* Tamper detection

The implementation is **blockchain-inspired**, rather than claiming to be a decentralized blockchain network.

---

# 📊 9. Real-Time Dashboard Architecture

The platform is designed for live monitoring through:

* REST APIs
* WebSockets
* Buffered updates
* Dynamic visualizations

The dashboard provides visibility into:

* Transaction activity
* Risk distribution
* Alerts
* Customer risk
* Network relationships
* Investigation status

---

# 📄 10. Automated Reporting

The platform supports generation of investigation and compliance-oriented reports.

Technologies include:

* `jsPDF`
* `html2canvas`

These can be used to generate reports containing:

* Risk summaries
* Investigation findings
* Visual analytics
* Evidence
* Network graphs

---

# 🏗️ System Architecture

```text
┌───────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                     │
│                                                           │
│ Next.js + React + TypeScript + Tailwind + shadcn/ui      │
│                                                           │
│ Dashboard | Alerts | AI Investigator | Network Graph     │
└───────────────────────────┬───────────────────────────────┘
                            │
                    REST / WebSocket
                            │
┌───────────────────────────▼───────────────────────────────┐
│                         API LAYER                         │
│                                                           │
│                    FastAPI / Flask                        │
│                                                           │
│ Authentication | APIs | AI Integration | Case Workflow  │
└───────────────────────────┬───────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────┐
│                    ANALYTICS LAYER                        │
│                                                           │
│ Python AML Engines | Pandas | NetworkX                   │
│                                                           │
│ Structuring | Velocity | Network | PEP | KYC | Jurisdiction│
└───────────────────────────┬───────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────┐
│                  INTELLIGENCE LAYER                       │
│                                                           │
│ AI Investigator | Explainability | Risk Aggregation      │
└───────────────────────────┬───────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────┐
│                  COMPLIANCE LAYER                         │
│                                                           │
│ Case Management | STR Workflow | Evidence | Audit Ledger │
└───────────────────────────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology         | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| **Next.js 16**     | Frontend framework, routing and application architecture |
| **React 19**       | Component-based user interface                           |
| **TypeScript**     | Type-safe frontend development                           |
| **Tailwind CSS 4** | Responsive cybersecurity UI                              |
| **shadcn/ui**      | Reusable interface components                            |
| **Recharts**       | Data visualization and analytics charts                  |
| **HTML5 Canvas**   | Custom graphical visualizations                          |
| **Python 3.13**    | AML processing and analytical backend                    |
| **FastAPI**        | High-performance REST API layer                          |
| **Flask**          | Integration for compatible backend modules               |
| **Uvicorn**        | ASGI server for FastAPI                                  |
| **Pandas**         | Transaction processing and feature engineering           |
| **NetworkX**       | Financial graph analytics                                |
| **OpenPyXL**       | Spreadsheet processing                                   |
| **Groq / Llama**   | AI-powered investigation assistance                      |
| **Gemini**         | AI-powered natural language analysis                     |
| **WebSockets**     | Real-time dashboard communication                        |
| **jsPDF**          | PDF report generation                                    |
| **html2canvas**    | Visual report capture                                    |
| **SHA-256**        | Tamper-evident audit hash chain                          |

---

# ⚡ Real-Time Production Architecture

The current prototype demonstrates the AML intelligence using available evaluator/synthetic transaction data.

For a production banking deployment, the input layer can be replaced by an event-streaming architecture.

```text
UPI
 │
NEFT
 │
RTGS
 │
IMPS
 │
ATM
 │
Cards
 │
Internet Banking
 │
 ▼
Kafka / Event Streaming
 │
 ▼
Feature Processing
 │
 ▼
SENTINEL-G AML Engines
 │
 ├── Structuring
 ├── Velocity
 ├── Network
 ├── PEP
 ├── Jurisdiction
 └── KYC
 │
 ▼
Dynamic Risk Assessment
 │
 ▼
AI Investigator
 │
 ▼
Compliance Officer
```

This architecture allows SENTINEL-G to evolve from a dataset-driven prototype into a real-time transaction monitoring platform.

---

# 📈 Scalability

SENTINEL-G is designed around modular and horizontally scalable services.

### Stateless API Architecture

Backend API instances can be replicated behind a load balancer.

```text
             Load Balancer
             /     |      \
            /      |       \
       API-1     API-2     API-3
```

As traffic increases, additional instances can be deployed.

### Event Streaming

A production streaming layer such as Kafka can absorb transaction bursts and distribute events to downstream services.

### Independent AML Engines

Detection engines are modular, allowing individual components to be scaled or upgraded independently.

---

# 🛡️ Fault Tolerance

SENTINEL-G is designed to isolate failures between components.

For example:

```text
PEP Engine Failure
       │
       ├── Structuring → Continues
       ├── Velocity    → Continues
       ├── Network     → Continues
       ├── KYC         → Continues
       └── Jurisdiction→ Continues
```

The frontend also uses error-handling mechanisms to provide fallback states when backend services become unavailable.

In a production event-streaming architecture, persistent queues can allow processing to resume after temporary service failures.

---

# 🔒 Security Considerations

A production banking deployment would require strong controls around:

* Authentication
* Role-Based Access Control
* Encryption in transit
* Encryption at rest
* Secret management
* API security
* Audit logging
* Data retention policies
* Network segmentation
* Monitoring and incident response

Sensitive customer information should never be exposed unnecessarily between services or participating institutions.

---

# 🧩 Why SENTINEL-G is Different

Traditional AML systems often focus heavily on generating alerts.

SENTINEL-G is designed as an **end-to-end financial crime investigation platform**.

### Traditional Approach

```text
Transaction
    ↓
Rule
    ↓
Alert
```

### SENTINEL-G Approach

```text
Transaction
    ↓
Behaviour
    ↓
Multiple Risk Engines
    ↓
Transaction Network
    ↓
Explainable Risk
    ↓
AI Investigation
    ↓
Evidence
    ↓
Human Review
    ↓
STR Workflow
    ↓
Immutable Audit Trail
```

### Key Differentiators

**1. Multi-dimensional risk analysis**

Multiple independent AML engines contribute evidence.

**2. Graph-based intelligence**

Detects relationships and networks rather than isolated transactions.

**3. Explainable AI**

Provides natural-language explanations for analytical results.

**4. Human-in-the-loop**

AI assists investigators while compliance officers retain decision authority.

**5. End-to-end workflow**

Detection → Investigation → Evidence → Approval → Reporting → Audit.

**6. Tamper-evident compliance history**

Hash-chained records preserve investigation integrity.

---

# 🚀 Production Roadmap

The current prototype can be extended toward production through:

### Phase 1 — Live Data

* Core banking integration
* Kafka/event streaming
* Live transaction ingestion

### Phase 2 — Behavioural Intelligence

* Continuous customer profiles
* Behavioural baselines
* Behavioural drift detection

### Phase 3 — Device & Identity Intelligence

* Device fingerprinting
* IP intelligence
* Identity correlation
* Shared-device detection

### Phase 4 — Advanced Graph Intelligence

* Persistent graph database
* Advanced community detection
* Graph Neural Networks
* Cross-account behavioural modelling

### Phase 5 — Enterprise Deployment

* Role-based access control
* High availability
* Monitoring
* Disaster recovery
* Model governance
* Regulatory integrations
* Multi-bank intelligence sharing

---

# 🧪 Current Prototype vs Production Vision

| Capability              | Current Prototype              | Production Vision                         |
| ----------------------- | ------------------------------ | ----------------------------------------- |
| Transaction Input       | Evaluator / synthetic data     | Live banking event streams                |
| AML Engines             | Implemented analytical engines | Continuously running services             |
| Graph Analysis          | Network analytics              | Persistent large-scale graph              |
| AI Investigator         | AI-assisted explanation        | Governed enterprise AI                    |
| Dashboard               | Real-time capable UI           | Production monitoring platform            |
| Audit                   | Hash-chain approach            | Enterprise immutable audit infrastructure |
| Streaming               | Architecture-ready             | Kafka/event-stream deployment             |
| Cross-Bank Intelligence | Roadmap                        | Secure consortium integration             |
| Behavioural Profile     | Feature-based analysis         | Continuous customer digital profile       |
| Device Intelligence     | Roadmap                        | Device/IP/entity correlation              |

---

# 💻 Local Development

## Prerequisites

* Node.js
* npm
* Python 3.13+
* Git

---

## Backend

```bash
# Clone repository
git clone <YOUR_REPOSITORY_URL>

cd SENTINEL-G

# Install Python dependencies
pip install -r requirements.txt

# Start backend
python app.py
```

Backend:

```text
http://localhost:5000
```

---

## Frontend

```bash
cd frontend/new-ui

npm install

npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

# 📁 High-Level Project Structure

```text
SENTINEL-G/
│
├── engines/
│   ├── structuring/
│   ├── velocity/
│   ├── network/
│   ├── pep/
│   ├── jurisdiction/
│   └── kyc/
│
├── backend/
│   ├── api/
│   ├── services/
│   └── models/
│
├── frontend/
│   └── new-ui/
│       ├── app/
│       ├── components/
│       ├── lib/
│       └── public/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

> Adjust the directory names above to match the final repository structure before publishing.

---

# 🏆 Project Highlights

* AI-powered AML investigation
* Six-core AML risk analysis
* Graph-based mule network detection
* Behavioural feature engineering
* Explainable risk scoring
* Human-in-the-loop compliance
* AI-generated investigation summaries
* Evidence management
* STR-oriented workflow
* Hash-chained audit trail
* Real-time dashboard architecture
* Modular backend architecture
* Production-oriented scalability design

---

# ⚠️ Disclaimer

SENTINEL-G is a research and hackathon prototype.

The current implementation uses non-production transaction data for demonstration and evaluation. Real banking deployment would require integration with authorised banking systems, regulatory requirements, security controls, data governance, model validation, operational monitoring, and appropriate compliance approval.

The platform should be treated as **decision-support software**, not as an autonomous system for making regulatory or customer-account decisions.

---

# 👥 Team

**Team SENTINEL-G**

Built for the **IOB Hackathon / Grand Finals**

> **Built for speed. Built for security. Built to hunt financial crime.**

---

# 📜 License

Add your chosen open-source or proprietary license before public deployment.

For example:

```text
MIT License
```

or use a proprietary license if the project is intended for controlled demonstration or commercial development.

