---
title: "Can Prompted LLMs Fake Benford?"
subtitle: "A controlled prompt-level simulation with synthetic accounting amounts"

event: DySES 2026 - Dynamics of Socio-Economic Systems
event_url: https://www.dyses.it/2026/

location: Naples, IT
address:
  street: ''
  city: Naples
  region: ''
  postcode: ''
  country: Italy

summary: "A DySES 2026 talk on whether prompted LLMs can generate synthetic accounting amounts that resemble Benford-compliant data, and how explicit Benford instructions change detectability."

abstract: |
  This talk was originally conceived and submitted as *Do ChatGPT-Generated Texts Follow Benford’s Law? First-Digit Tests on Word-Frequency Profiles*, with Gurjeet Dhesi, Valerio Ficcadenti, Parmjit Kaur, and Raffaele Mattera.

  During the preparation of the DySES 2026 presentation, the study was experimentally tailored into a more controlled prompt-level simulation. The final version, titled *Can Prompted LLMs Fake Benford?*, shifts the empirical object from word-frequency profiles in ChatGPT-generated texts to synthetic accounting amounts generated under controlled LLM prompts.

  The revised design keeps the Benford Law question at the centre, but makes the experiment more directly focused on numerical generation. Four prompt conditions compare legitimate and fraudulent accounting scenarios, with and without explicit Benford instructions.

  The aim is to test whether Benford diagnostics can distinguish LLM-generated accounting amounts under ordinary and adversarial prompting, and whether telling the model about Benford’s Law reduces detectability.

  The presentation argues that prompt engineering changes not only the prose surrounding generated data, but also the numerical distribution produced by the model. The experiment therefore becomes less about whether Benford’s Law simply “catches” an LLM, and more about how prompts shape the numerical world that an LLM creates.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2026-06-18T00:00:00Z'
date_end: '2026-06-20T00:00:00Z'
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: '2026-06-21T00:00:00Z'

authors:
  - gurjeet-dhesi
  - valerio-ficcadenti
  - parmjit-kaur
  - raffaele-mattera


tags: 
 - Benford's Law
 - Large Language Models
 - Prompt Engineering
 - Synthetic Accounting Data
 - Fraud Analytics
 - Digit Analysis

# Is this a featured talk? (true/false)
featured: true

image:
  caption: 'Title page of my talk'
  focal_point: Top

url_code: ''
url_pdf: ''
url_slides: 'llm_benford_beamer.pdf'
url_vide: ''

# Custom links (optional)
links:
  - name: Programme
    url: https://www.dyses.it/2026/scientific-programme/
    icon_pack: fas
    icon: file-alt


# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

**Event:** [DySES 2026 - Dynamics of Socio-Economic Systems](https://www.dyses.it/2026/)  
**Location:** Naples, Italy  
**Date:** June 18-21, 2026

---

This talk investigates whether large language models can generate synthetic accounting figures that resemble Benford-compliant numerical data. Using a controlled prompt-level experiment, I compare four conditions: legitimate accounting amounts, fraudulent accounting amounts, legitimate amounts generated with explicit Benford guidance, and fraudulent amounts generated with explicit Benford guidance.

The central question is whether first-digit tests can detect differences between ordinary LLM-generated numerical data and data produced under prompts that explicitly ask the model to respect Benford’s Law. The talk therefore connects Benford diagnostics, synthetic data generation, prompt engineering, and fraud analytics, showing how the wording of a prompt can affect not only the explanation produced by an LLM, but also the numerical distribution it generates.
