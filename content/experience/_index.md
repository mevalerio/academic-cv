---
title: Experience
date: 2022-10-24

# Page type
type: landing

# Page SEO
seo:
  title: Experience
  description: My professional experience.
  # Choose an image to show on social media
  #   E.g. `image:
  #         filename: experience.jpg`


sections:
  - block: markdown
    content:
      title: ''
      text: |
        <style>
        .experience-cards {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 25px;
          margin: 40px 0;
          padding: 0 10px;
        }
        .exp-card {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          padding: 30px 20px;
          border-radius: 15px;
          color: white;
          text-align: center;
          text-decoration: none;
          transition: all 0.3s ease;
          box-shadow: 0 4px 15px rgba(0,0,0,0.1);
          position: relative;
          overflow: hidden;
        }
        .exp-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 8px 25px rgba(0,0,0,0.2);
          text-decoration: none;
        }
        .exp-card::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(255,255,255,0.1);
          opacity: 0;
          transition: opacity 0.3s ease;
        }
        .exp-card:hover::before {
          opacity: 1;
        }
        .exp-card-icon {
          font-size: 48px;
          margin-bottom: 15px;
          display: block;
        }
        .exp-card-title {
          margin: 0 0 10px 0;
          font-size: 20px;
          font-weight: bold;
          color: white;
        }
        .exp-card-subtitle {
          margin: 0 0 10px 0;
          font-size: 14px;
          opacity: 0.9;
          color: white;
        }
        .exp-card-stats {
          margin: 10px 0 0 0;
          font-size: 13px;
          opacity: 0.85;
          color: white;
        }
        .exp-card.positions { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .exp-card.skills { background: linear-gradient(135deg, #06beb6 0%, #48b1bf 100%); }
        .exp-card.awards { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
        .exp-card.phd { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .exp-card.visiting { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
        .exp-card.examiner { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
        
        @media (max-width: 768px) {
          .experience-cards {
            grid-template-columns: 1fr;
          }
        }
        </style>
        
        <div class="experience-cards">
          <a href="#experience" class="exp-card positions">
            <span class="exp-card-icon">🏢</span>
            <h3 class="exp-card-title">Professional Positions</h3>
            <p class="exp-card-subtitle">Career journey & roles</p>
            <p class="exp-card-stats">6 positions • 10+ years</p>
          </a>
          
          <a href="#skills" class="exp-card skills">
            <span class="exp-card-icon">💻</span>
            <h3 class="exp-card-title">Skills</h3>
            <p class="exp-card-subtitle">Technical expertise & soft skills</p>
          </a>
          
          <a href="#awards" class="exp-card awards">
            <span class="exp-card-icon">🏆</span>
            <h3 class="exp-card-title">Awards</h3>
            <p class="exp-card-subtitle">Recognition & achievements</p>
          </a>
          
          <a href="#phd-supervision" class="exp-card phd">
            <span class="exp-card-icon">👨‍🎓</span>
            <h3 class="exp-card-title">PhD Students supervision</h3>
            <p class="exp-card-subtitle">Current & completed supervision</p>
            <p class="exp-card-stats">3 current • 4 completed</p>
          </a>
          
          <a href="#visiting-phd" class="exp-card visiting">
            <span class="exp-card-icon">🌍</span>
            <h3 class="exp-card-title">Visiting PhD Students supervision</h3>
            <p class="exp-card-subtitle">International students</p>
          </a>
          
          <a href="#examiner" class="exp-card examiner">
            <span class="exp-card-icon">📝</span>
            <h3 class="exp-card-title">PhD Examination</h3>
            <p class="exp-card-subtitle">Internal & external duties</p>
            <p class="exp-card-stats">3 internal • 1 external</p>
          </a>
        </div>
    design:
      columns: '1'
      
  - block: experience
    id: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Associate Professor in Business Research Methods
          company: Business School - London South Bank University (UK)
          company_url: 'https://www.lsbu.ac.uk/our-schools/business'
          company_logo: 'lsbu'
          location: London, UK
          department: Dep. of Finance, Economics, Accounting and Analytics
          date_start: '2023-08-01'
          date_end: ''
          description: |2-
              -  Teaching Business Research Methods to undergraduate and postgraduate students with innovative teaching. **I am proud to hit the mark with 80%+ in student satisfaction consistently!**
              -  Supervising **PhD** students to **successful completion**, supporting their academic and professional growth.  
              -  Publishing **1-2 internationally excellent papers annually**, contributing to high-quality research in business, finance, and data science.  
              -  Serving as the **Unit of Assessment 17 Lead**:
                - ✍ Preparing the **People, Culture, and Environment** narrative to showcase **research developments, interdisciplinarity, and sustainability**.  
                - ⚒️ Managing **Impact Case Studies** to highlight societal and academic contributions.  
                -  Overseeing **research output selection**, ensuring alignment with REF submission criteria and the Business School's strategic targets.  
              -  Managed the **GLA-funded Inclusive Supply Chain project**, driving diversity and inclusion in procurement. Led the support for **300+ companies**, helping them secure **over £1 million in contract bids** while integrating **student-led business projects** to provide innovative solutions. Delivered in partnership with **Newable**.

        - title: Senior Lecturer in Business Research Methods
          company: Business School - London South Bank University (UK)
          company_url: 'https://www.lsbu.ac.uk/our-schools/business'
          company_logo: 'lsbu'
          location: London, UK
          department: Dep. of Marketing, Management and People
          date_start: '2020-01-01'
          date_end: '2023-07-30'
          description: |2-
              -  Led multiple modules, consistently achieving high student satisfaction rates. Modules such as Management Consultancy and Research Methods have been my proudest successes.
              - ‍♂️  Provided guidance to **students and colleagues** in developing their research plans. Mentored **Early Career Researchers**, supporting them in navigating their first steps in research, refining methodologies, and strengthening their academic contributions.  
              -  Contributed with 5 papers to the Research Excellence Framework 2021. 
              -  Led the **Unit of Assessment** for REF 2021, ensuring the **strategic alignment** of research outputs, impact case studies, and the environment statement. Oversaw the **evaluation and selection** of submissions, optimising research quality and impact. The greatest achievement was securing **over 50% of impact case studies rated 4***. 

        - title: Deputy Director of Research and Enterprise Office
          company: Business School - London South Bank University (UK)
          company_url: 'https://www.lsbu.ac.uk/our-schools/business'
          company_logo: 'lsbu'
          location: London, UK
          date_start: '2020-01-01'
          date_end: '2022-12-31'
          description: |2-
              - ‍ I spearheaded a transformative project focused on revising and producing a new work allocation hour model for research that could help and support **Early Career Researchers** in developing their research within LSBU - Business School, a post-92 university with a focus on teaching, which makes research development more challenging.
              -  The Ideated work allocation model maximised **Significant Responsibility for Research** within the school, ensuring alignment with the needs and goals of the **REF 2021** submission. This involved carefully considering output submission rules, impact cases, and the environment statement to support the school's strategic priorities.
      
        - title: Pricing Specialist in Derivatives Evaluation
          company: Deloitte's Pricing Centre (UK)
          company_url: 'https://www2.deloitte.com/uk/en/explore/home.html'
          company_logo: 'Deloitte'
          location: London, UK
          date_start: '2018-01-01'
          date_end: '2019-12-31'
          description: |2-
              Responsibilities include:
              - Priced complex financial derivatives, ensuring compliance with, for example, **IFRS 9 - Financial Instruments**, which outlines requirements for fair value measurement, recognition, and impairment of financial assets and liabilities. This accounted for approximately 75% of the workload.
              - Reviewed pricing models from large audit clients  focusing on validating the methodologies and inputs used for valuation.
              - Assisted in risk assessment and valuation for advisory clients, which accounted for the remaining 25% of the workload, providing tailored solutions for derivative pricing and risk management.
              - Developed a strong understanding of fixed-income products, options, swaps, and other complex financial instruments.

        - title: Postdoctoral Researcher in Quantitative Finance
          company: Faculty of Economics, Polytechnic University of Marche (Italy)
          company_url: 'https://www.econ.univpm.it/content/department-management?language=en'
          company_logo: 'Logo_Università_Politecnica_delle_Marche'
          location: Ancona, Italy
          department: Dep. of Management
          date_start: '2018-01-01'
          date_end: '2018-12-31'
          description: |2-
              Responsibilities include:
              - Conducted research in quantitative finance and option pricing.
              - Published in peer-reviewed journals.
              - Collaborated with faculty on joint research projects.
              - Taught modules where **maths for finance and economics** was a key focus, helping students understand quantitative methods and their application in financial and economic contexts.

        - title: Consultant and Intern in Financial Data Analytics
          company: FAO - Food and Agriculture Organization of the United Nations (Italy)
          company_url: 'https://www.fao.org/home/en'
          company_logo: 'FAO_logo'
          location: Rome, Italy
          department: CSFT – Treasury / Finance Division
          date_start: '2015-01-01'
          date_end: '2016-12-31'
          description: |2-
              Responsibilities include:
              - Analysed financial data and FAO's portfolio performance.
              - Developed risk reports and set up data pipelines for finance operations.
              - Assisted in creating replicable models for portfolio management.
    design:
      columns: '1'
      
  - block: skills
    id: skills
    content:
      title: Skills
      text: 'My technical and professional expertise across various domains.'
      username: valerio-ficcadenti
    design:
      columns: '1'

  - block: accomplishments
    id: awards
    content:
      title: Awards
      subtitle: ''
      text: ''
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `items` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Best Delegate @ WHO Simulation
          url: https://ecointernazionale.com/2017/03/cwmun-2017-corrispondenze-in-diretta-da-new-york-city/
          date_start: '2017-03-19'
          organization: Change the World Model United Nations
          description: |2-
            Awarded Best Delegate at the 2017 Change the World Model United Nations for my role as the delegate of Jamaica in the World Health Organization (WHO) workings simulation. The event was both a challenge and a lot of fun, where I showcased my skills in diplomacy, public speaking, and problem-solving.
    design:
      columns: '1'
      
  - block: accomplishments
    id: phd-supervision
    content:
      title: PhD Supervision
      subtitle: 'Doctoral students under my supervision and guidance'
      text: ''
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # PhD Students - Ongoing
      items:
        - title: "Mr Felipe Lago"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2022-01-01'
          description: |2-
            **Second Supervisor, Part Time**  
            Current PhD student working on business and finance research under my co-supervision.
            
        - title: "Mr Anton Novikov"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2021-01-01'
          description: |2-
            **Director of Studies, Full Time**  
            Current PhD student under my primary supervision, focusing on advanced research in business methods.
            
        - title: "Mr Stefano Marmani"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2018-01-01'
          description: |2-
            **Director of Studies, Part Time**  
            Long-term PhD student under my primary supervision, conducting research in applied business analytics.
    design:
      columns: '1'
      
  - block: accomplishments
    content:
      title: PhD Supervision - Completed
      subtitle: 'Successfully completed doctoral supervisions'
      text: ''
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # PhD Students - Completed
      items:
        - title: "Dr Mohamed Mehbali"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2019-01-01'
          date_end: '2024-12-31'
          description: |2-
            **Second Supervisor, Part Time**  
            Successfully completed PhD in 2024. Dr Mehbali's research focused on quantitative finance and business analytics.
            
        - title: "Dr Thamila Madji"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2017-01-01'
          date_end: '2021-12-31'
          description: |2-
            **Director of Studies, Full Time**  
            Successfully completed PhD in 2021. Dr Madji's research contributed significantly to business research methodology.
            
        - title: "Dr Rouhollah Ebrahimabadi"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2017-01-01'
          date_end: '2021-12-31'
          description: |2-
            **Second Supervisor, Full Time**  
            Successfully completed PhD in 2021. Dr Ebrahimabadi's work focused on applied economics and business analytics.
            
        - title: "Dr Rishiram Aryal"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2017-01-01'
          date_end: '2020-12-31'
          description: |2-
            **Second Supervisor, Full Time**  
            Successfully completed PhD in 2020. Dr Aryal's research contributed to quantitative business methods and analytics.
    design:
      columns: '1'
      
  - block: accomplishments
    id: visiting-phd
    content:
      title: Visiting PhD Supervision
      subtitle: 'International visiting doctoral students under supervision'
      text: ''
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Visiting PhD Students
      items:
        - title: "Mr Alessio Di Paolo"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2024-10-01'
          date_end: '2025-03-31'
          description: |2-
            **LSBU Supervisor: Dr. Valerio Ficcadenti**  
            **Home Supervisor: [Prof. Francesco Cesarone](https://www.uniroma3.it/persone/M1pzTHEwcUdFNmYwWUc2ZllLYSsxWitoM3Rad2FzKzFkSjFHanRMeHFRZz0=/), Roma Tre University (Italy)**  
            Visiting PhD student from Roma Tre University conducting research in finance and quantitative methods during a 6-month international exchange program (October 2024 - March 2025).
            
        - title: "Mr Vincenzo Scardigno"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2025-01-01'
          date_end: '2025-07-31'
          description: |2-
            **LSBU Supervisor: Dr. Valerio Ficcadenti**  
            **Home Supervisor: [Ass. Prof. Mariantonietta Intonti](https://www.uniba.it/it/docenti/intonti-mariantonietta), University of Bari (Italy)**  
            Visiting PhD student from University of Bari conducting research in business and economics during a 7-month international exchange program (January 2025 - July 2025).
    design:
      columns: '1'
      
  - block: accomplishments
    id: examiner
    content:
      title: PhD Examination - Internal Examiner
      subtitle: 'Internal examining duties at London South Bank University'
      text: ''
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Internal Examiner roles
      items:
        - title: "Miss Liping Wu"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2024-09-01'
          description: |2-
            **Internal Examiner**  
            Served as internal examiner for PhD thesis examination, contributing to the assessment of doctoral research quality and academic standards at LSBU Business School.
            
        - title: "Dr Motunrayo Morohunfoluwa Duro-Ishola"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2024-02-01'
          description: |2-
            **Internal Examiner**  
            Served as internal examiner for PhD thesis examination, ensuring rigorous academic evaluation and maintaining high standards of doctoral research assessment.
            
        - title: "Dr Nyerho Odje Odje"
          organization: "Business School - London South Bank University (UK)"
          date_start: '2023-11-01'
          description: |2-
            **Internal Examiner**  
            Served as internal examiner for PhD thesis examination, contributing to the academic evaluation process and upholding doctoral research standards.
    design:
      columns: '1'
      
  - block: accomplishments
    content:
      title: PhD Examination - External Examiner
      subtitle: 'External examining duties at international institutions'
      text: ''
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # External Examiner roles
      items:
        - title: "Dr Patrick Donkor"
          organization: "University of Macerata (Italy)"
          date_start: '2024-08-01'
          description: |2-
            **External Examiner**  
            Served as external examiner for PhD thesis examination at the University of Macerata, providing independent academic assessment and contributing to international academic collaboration in doctoral evaluation processes.
    design:
      columns: '1'
---