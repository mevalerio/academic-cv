---
name: hugoblox-academic
description: 'Configure and customize HugoBlox academic websites. Use for setting up academic CV sites, customizing Hugo templates, configuring menus and parameters, collecting researcher information, managing publications and talks, deploying to Netlify or GitHub Pages, troubleshooting Hugo builds, and finalizing academic portfolio websites.'
argument-hint: 'What aspect to work on (setup, content, deploy, customize, validate)'
---

# HugoBlox Academic Website Builder

Expert workflow for creating, customizing, and deploying professional academic websites using Hugo and HugoBlox Builder (formerly Wowchemy).

## When to Use

- **Initial Setup**: Bootstrapping a new academic CV website
- **Customization**: Modifying themes, layouts, styles, or components
- **Content Management**: Adding publications, talks, projects, team members
- **Configuration**: Setting up menus, params, languages, modules
- **Asset Handling**: Managing images, icons, custom SCSS
- **Deployment**: Configuring Netlify/GitHub Pages and troubleshooting builds
- **Finalization**: Pre-deployment quality checks and validation

## Workflow Overview

The complete process follows these phases:

1. **Information Gathering** → Collect academic profile details
2. **Configuration Setup** → Configure Hugo settings and parameters
3. **Template Customization** → Customize theme, styles, and layout
4. **Content Population** → Add publications, talks, projects, team
5. **Asset Management** → Handle images, icons, and media files
6. **Build Validation** → Test locally and fix errors
7. **Deployment Setup** → Configure hosting and deploy

---

## Phase 1: Information Gathering

### Academic Profile Checklist

Collect the following information from the user:

**Personal Information**
- [ ] Full name and title (e.g., "Dr. Jane Smith" or "Professor John Doe")
- [ ] Current position and institution
- [ ] Professional email address
- [ ] Office location and contact details
- [ ] Profile photo (high-quality headshot)

**Research Profile**
- [ ] Main research interests (3-5 key areas)
- [ ] Research summary (2-3 paragraphs)
- [ ] Expertise keywords for SEO
- [ ] Current research projects

**Professional Links**
- [ ] Personal website URL (if different)
- [ ] Google Scholar profile
- [ ] ORCID iD
- [ ] ResearchGate or Academia.edu
- [ ] LinkedIn profile
- [ ] GitHub account (if applicable)
- [ ] Twitter/X handle (if applicable)

**Content Assets**
- [ ] Publications list (BibTeX or structured data)
- [ ] Talks and presentations
- [ ] Teaching experience
- [ ] Projects and grants
- [ ] PhD students/team members
- [ ] CV/Resume file

### Data Collection Strategy

1. **Review existing CV/Resume**: Extract structured information
2. **Check online profiles**: Verify links and gather bio text
3. **Identify gaps**: Note missing information for follow-up
4. **Organize assets**: Create folder structure for images/files

---

## Phase 2: Configuration Setup

### Hugo Configuration (`config/_default/`)

**Check and configure these files:**

#### `hugo.yaml`
- Set `baseURL` to deployment URL
- Configure `title` (site name)
- Set `copyright` notice
- Verify `theme` is set to `github.com/HugoBlox/hugo-blox-builder/modules/blox-bootstrap/v5`

#### `params.yaml`
- **Contact details**: Email, phone, address
- **Office hours**: If applicable
- **Social links**: Configure all academic/professional networks
- **Site features**: Enable/disable comments, search, reading time
- **Marketing**: Google Analytics, verification codes
- **Security**: Email protection settings

#### `menus.yaml`
- Configure main navigation menu
- Add sections: About, Publications, Talks, Projects, Team, Contact
- Set menu weights for ordering
- Verify all menu links point to created content

**Custom Menu Branding Example** (from this site):
```yaml
main:
  - name: <span class="collab-col">Col</span><span class="collab-lab">LAB</span>
    url: '/people/'
    weight: 55
```
Then style in `assets/scss/custom.scss`:
```scss
.collab-col {
  color: #000000; /* Adapts to theme */
}
.collab-lab {
  color: #e74c3c; /* Always red */
}
[data-theme="dark"] .collab-col {
  color: #ffffff;
}
```
This creates "ColLAB" branding where "Col" adapts to light/dark themes and "LAB" stays red.

#### `languages.yaml`
- Set primary language (usually `en`)
- Configure region-specific settings
- Add multilingual support if needed

#### `module.yaml`
- Verify HugoBlox module imports
- Check for custom module additions

### Decision Points

**Q: Is this a personal site or group/lab website?**
- Personal → Use biography widget, single author
- Group/Lab → Enable team member pages, multiple authors

**Q: What content types are priority?**
- Research-focused → Emphasize publications, projects
- Teaching-focused → Highlight courses, resources
- Industry-facing → Emphasize experience, projects, skills

---

## Phase 3: Template Customization

### Theme Customization

**Custom Styles** (`assets/scss/custom.scss`)
- Color scheme adjustments
- Typography modifications
- Custom spacing and layout
- Responsive design tweaks

**Custom Icons** (`assets/media/icons/custom/`)

This site uses custom SVG icons with dark mode support:

1. **Create icon pairs** for light/dark modes:
   - `bloomberg.svg` + `bloomberg-dark.svg`
   - `overleaf.svg` + `overleaf-dark.svg`
   - Or use CSS filters for automatic inversion

2. **Apply dark mode filters** in `assets/scss/custom-icons.scss`:
```scss
@media (prefers-color-scheme: dark) {
  img[src*="bloomberg.svg"],
  img[src*="overleaf.svg"] {
    filter: invert(1) brightness(100%) !important;
  }
}
```

3. **Available custom icons**:
   - Bloomberg, Overleaf (finance/academic tools)
   - R programming logo
   - Network, chart, boxing glove (skills/interests)
   - Rotary, Rotaract (organizations)

4. **Use in author profiles**:
```yaml
social:
  - icon: custom/bloomberg
    icon_pack: custom
    link: https://bloomberg.com/profile
```

**Layouts** (if creating custom templates)
- Widget customizations
- Section layouts
- List vs. card views

### Bootstrap Integration

HugoBlox uses Bootstrap 5. Common customizations:
- Override Bootstrap variables in SCSS
- Use Bootstrap utility classes in content
- Customize responsive breakpoints

### Timeline Customization

**Advanced Organization-Specific Timeline Styling**

This site implements a sophisticated timeline with company-specific colors:

1. **Define company colors** in `asyour-name/_index.md`)

⚠️ **Important**: Use your actual name as folder name (e.g., `valerio-ficcadenti`), not `admin`.

```yaml
---
title: Valerio Ficcadenti
author: admin  # This marks you as the main user
first_name: Valerio
last_name: Ficcadenti
status:
  icon: 👋
  text: Hello!
superuser: true
highlight_name: true
role: Associate Professor
organizations:
  - name: London South Bank University (LSBU) - Business School
    url: https://www.lsbu.ac.uk/our-schools/business
bio: Specialist in business research methods and quantitative finance
interests:
  - Computational Linguistics
  - Text Mining
  - Quantitative Finance
  - Portfolio Optimization
education:
  courses:
    - course: PhD in Economics and Management
      institution: Università Politecnica delle Marche
      year: 2018
social:
  - icon: envelope
    icon_pack: fas
    link: 'mailto:your.email@lsbu.ac.uk'
  - icon: google-scholar
    icon_pack: ai
    link: https://scholar.google.com/citations?user=YOUR_ID
  - icon: orcid
    icon_pack: ai
    link: https://orcid.org/0000-0000-0000-0000
  - icon: linkedin
    icon_pack: fab
    link: https://linkedin.com/in/yourprofile
---
```

**Team Members / Co-authors**

Auto-generated via `create_authors.py`, then manually enhanced:

1. **Run automation**: `python create_authors.py`
2. **Add to user groups** in each co-author's `_index.md`:
```yaml
user_groups:
  - co-authors
```
3. **Add avatar images**: Place `avatar.jpg` (400x400px) in each author folder
4. **Enhance profiles**: Add social links, organizations, bio

**Display on People Page** (`content/people/index.md`):
```yaml
sections:
  - block: people
    content:
      title: ColLAB
      user_groups:
        - co-authors
``` University
    date_start: '2020-01-01'
    date_end: '2021-12-31'
  - title: Consultant       # New company = filled badge
    company: Deloitte
    date_start: '2018-01-01'
    date_end: '2019-12-31'
```

**Visual Result**: Creates a professional timeline where company changes are highlighted with filled badges, and role progressions within the same company use outlined badges.

---

## Phase 4: Content Population

### Author Profiles (`content/authors/`)

**Main Profile** (`content/authors/admin/_index.md`)
```yaml
---
title: First Last
role: Position Title
organizations:
  - name: Institution
    url: https://institution.edu
superuser: true
bio: Brief bio for metadata
interests:
  - Research Interest 1
  - Research Interest 2
education:
  courses:
    - course: PhD in Subject
      institution: University
      year: 2020
social:
  - icon: envelope
    icon_pack: fas
    link: 'mailto:email@example.com'
  - icon: google-scholar
    icon_pack: ai
    link: https://scholar.google.com/citations?user=ID
---
```

**Team Members** (Co-authors, PhD students)
- Create subfolder for each: `content/authors/firstname-lastname/`
- Add `_index.md` with profile
- Include headshot: `avatar.jpg`
- Link publications to authors

### Publications (`content/publication/`)

**Automated BibTeX Workflow** (Recommended)

This site uses a Python automation script for managing publications:

1. **Maintain `publications.bib`** in the root directory
   - Add new publications to this single source of truth
   - Standard BibTeX format
   - Include DOI, publisher, page numbers

2. **Run `create_authors.py`** to auto-generate co-author profiles
   ```powershell
   python create_authors.py
   ```
   - Auto-installs dependencies: `bibtexparser`, `unidecode`
   - Extracts unique authors from `.bib` file
   - Creates folders in `content/authors/` for each co-author
   - Handles name normalization and special characters

3. **Create publication folders** manually or with Hugo Academic CLI
   - Structure: `content/publication/firstname-year-keyword/`
   - Example: `ficcadenti-2024-economic/`
   - Each folder needs `index.md`

4. **Link authors** in publication frontmatter using folder names
   - Main author: `valerio-ficcadenti` (username, not display name)
   - Co-authors: Use their folder names (e.g., `roy-cerqueti`)

**Publication Entry Template**
```yaml
---
title: "Article Title"
authors:
  - valerio-ficcadenti  # Main profile (admin)
  - roy-cerqueti        # Co-author (use folder name)
  - marcel-ausloos
author_notes: []
date: '2024-01-01'
publishDate: '2025-06-15T09:41:42.906191Z'
publication_types:
  - article-journal
publication: '*Journal Name*'
abstract: "Full abstract text..."
featured: true
tags:
  - Research Area
  - Methodology
doi: "10.1016/j.journal.2024.123456"
url_pdf: "paper.pdf"
---
```

**Best Practices**:
- Add esteem indicators in note field: `\textbf{Esteem Indicator(s): AJG 2021: 3*, Included in REF 2021}`
- Include mathematical symbols in titles with LaTeX: `{S}\&{P}500`, `{COVID-19}`
- Use `publication_types` for filtering: `article-journal`, `conference-paper`, `book-chapter`
- Set `view: 4` in `content/publication/_index.md` for citation style

### Talks (`content/talks/`)

For each presentation:
- Create folder: `content/talks/event-year/`
- Add `index.md` with event details
- Include slides or links
- Add featured image if available

### Projects (`content/project/`)

For funded projects or major research initiatives:
- Create folder per project
- Include project description, timeline, funding
- Link to related publications
- Add project logo/image

### Experience (`content/experience/_index.md`)

Use the experience widget to show career timeline:
```yaml
---
widget: experience
headless: true
weight: 20
title: Experience
date_format: Jan 2006
experience:
  - title: Position
    company: Organization
    location: City, Country
    date_start: '2020-01-01'
    date_end: ''
    description: |2-
        Responsibilities:
        * Task 1
        * Task 2
---
```

---

## Phase 5: Asset Management

### Images and Media

**Organize assets:**
```
static/uploads/          # PDFs, CV, documents
assets/media/
  └── albums/demo/       # Photo galleries
  └── icons/
      ├── brands/        # Brand logos
      └── custom/        # Custom SVG icons
content/authors/*/       # Author headshots (avatar.jpg)
content/publication/*/   # Featured images (featured.jpg)
content/project/*/       # Project images
```

**Image Best Practices:**
- Profile photos: 400x400px minimum, square aspect ratio
- Featured images: 1200x675px (16:9), WebP or JPEG
- Icons: SVG format preferred for scalability
- File naming: Lowercase, hyphens, no spaces

**Icon Packs Available:**
- Font Awesome (`fas`, `fab`, `far`)
- Academicons (`ai`) - Google Scholar, ORCID, ResearchGate
- Custom SVG in `assets/media/icons/custom/`

### File Organization Tips

1. **Keep assets near content**: Publish-specific files in publication folders
2. **Use static/ for downloadable files**: CV, papers, datasets
3. **Optimize images**: Compress before uploading, use WebP when possible
4. **Validate links**: Ensure all URLs and file paths work

---

## Phase 6: Build Validation

### Local Testing

**Start Hugo development server:**
```powershell
hugo server -D
```

**Check for common issues:**
- [ ] Site loads at http://localhost:1313
- [ ] Navigation menu works correctly
- [ ] All pages render without errors
- [ ] Images and icons display properly
- [ ] Social links function correctly
- [ ] Internal links work (publications, talks, projects)
- [ ] Mobile responsiveness (test multiple screen sizes)

### Build for Production

**Generate static site:**
```powershell
hugo --minify
```

**Validation checklist:**
- [ ] Build completes without errors
- [ ] Check console for warnings
- [ ] Verify `public/` directory created
- [ ] Test generated HTML files
- [ ] Validate links with `hugo server` from `public/`

### Common Build Errors

**Error: Hugo version mismatch**
- Solution: Install Hugo Extended v0.123+
- Check: `hugo version`

**Error: Module not found**
- Solution: Run `hugo mod get -u` to update modules
- Check `module.yaml` configuration

**Error: Failed to render shortcode**
- Solution: Review shortcode syntax in Markdown files
- Common issue: Mismatched brackets or quotes

**Error: Template not found**
- Solution: Verify widget names match theme widgets
- Check frontmatter `widget:` field spelling

---

## Phase 7: Deployment Setup

### Netlify Deployment

**Configuration file** (`netlify.toml` in root):
```toml
[build]
  command = "hugo --gc --minify -b $URL"
  publish = "public"

[build.environment]
  HUGO_VERSION = "0.129.0"
  HUGO_ENABLEGITINFO = "true"

[context.production.environment]
  HUGO_ENV = "production"

[[plugins]]
  package = "netlify-plugin-hugo-cache-resources"
```

**Deployment steps:**
1. Push repository to GitHub
2. Connect Netlify to GitHub repo
3. Configure build settings (or use `netlify.toml`)
4. Deploy and verify
5. Set custom domain (if applicable)

### GitHub Pages Deployment

**Workflow file** (`.github/workflows/hugo.yaml`):
```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.129.0'
          extended: true
      - name: Build
        run: hugo --minify
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Pre-Deployment Checklist

- [ ] `baseURL` set to production URL
- [ ] Google Analytics configured (if using)
- [ ] Social media preview images set
- [ ] Robots.txt configured
- [ ] 404 page customized
- [ ] Favicons generated and added
- [ ] SSL certificate active (provided by Netlify/GitHub)
- [ ] Contact form configured (if using)
- [ ] Email addresses verified and active

---

## Quality Assurance

### Content Review

- [ ] All text proofread for typos and grammar
- [ ] Publications list complete and accurate
- [ ] Dates formatted consistently
- [ ] Links tested (internal and external)
- [ ] Author attributions correct
- [ ] Bio and research interests current

### SEO Optimization

- [ ] Page titles descriptive and unique
- [ ] Meta descriptions under 160 characters
- [ ] Keywords in content naturally
- [ ] Alt text for all images
- [ ] Structured data (Schema.org) present
- [ ] XML sitemap generated

### Performance

- [ ] Images optimized and compressed
- [ ] Minification enabled (`hugo --minify`)
- [ ] CDN configured (Netlify/Cloudflare)
- [ ] Lighthouse score >90 for performance

### Accessibility

- [ ] Color contrast ratios meet WCAG standards
- [ ] Keyboard navigation functional
- [ ] Screen reader friendly
- [ ] Semantic HTML used
- [ ] Focus indicators visible

---

## Troubleshooting

### Common Issues and Solutions

**Problem: Changes not showing after deployment**
- Clear browser cache or test in incognito
- Check Netlify/GitHub deployment logs
- Verify build completed successfully

**Problem: Publications not displaying**
- Check frontmatter YAML syntax
- Verify `publication_types` field
- Ensure files in correct directory structure

**Problem: Social icons missing**
- Verify icon names match Font Awesome/Academicons
- Check `icon_pack` value (`fas`, `ai`, etc.)
- Ensure custom icons in correct directory

**Problem: Menu links not working**
- Check `menus.yaml` URLs match content structure
- Verify content files exist at specified paths
- Check for case sensitivity in URLs

**Problem: Theme not loading correctly**
- Run `hugo mod clean` then `hugo mod get -u`
- Check `module.yaml` configuration
- Verify internet connection for module downloads

---

## Advanced Customization

### Custom Widgets

Create custom widgets in `layouts/partials/widgets/`:
- Copy existing widget as template
- Modify HTML structure
- Add custom styling in SCSS
- Reference in page frontmatter

### Multilingual Sites

Configure in `languages.yaml`:
```yaml
en:
  languageName: English
  weight: 1
es:
  languageName: Español
  weight: 2
  params:
    description: Descripción en español
```

Create content in language-specific folders:
- `content/en/`
- `content/es/`

### Custom Shortcodes

Create in `layouts/shortcodes/`:
```html
<!-- layouts/shortcodes/highlight.html -->
<div class="highlight-box">
  {{ .Inner | markdownify }}
</div>
```

Use in content:
```markdown
{{< highlight >}}
Important information here
{{< /highlight >}}
```

---

## Maintenance

### Regular Updates

**Monthly:**
- [ ] Update Hugo version: `hugo mod get -u`
- [ ] Check for theme updates
- [ ] Review and add new publications
- [ ] Update CV/Resume

**Quarterly:**
- [ ] Review and update research interests
- [ ] Audit all external links
- [ ] Check analytics and optimize
- [ ] Update team member pages

**Annually:**
- [ ] Complete content audit
- [ ] Refresh design elements
- [ ] Update profile photos
- [ ] Review SEO performance

---

## Quick Commands Reference

```powershell
# Development
hugo server -D                    # Start dev server with drafts
hugo server --disableFastRender  # Full rebuild on changes

# Build
hugo --minify                     # Production build
hugo --gc --minify               # Build with cleanup

# Modules
hugo mod get -u                   # Update all modules
hugo mod clean                    # Clear module cache
hugo mod graph                    # View dependency tree

# Content
hugo new content/publication/article-2024/index.md  # New publication
hugo new content/talks/talk-2024.md                # New talk

# Debugging
hugo --debug                      # Verbose output
hugo --verbose                    # Detailed logging
hugo config                       # View merged config
```

---

## Resources

**Official Documentation:**
- [Hugo Documentation](https://gohugo.io/documentation/)
- [HugoBlox Documentation](https://hugoblox.com/docs/)
- [Hugo Blox GitHub](https://github.com/HugoBlox/hugo-blox-builder)

**Community:**
- [HugoBlox Discord](https://discord.gg/z8wNYzb)
- [Hugo Discourse Forum](https://discourse.gohugo.io/)

**Tools:**
- [Hugo Academic CLI](https://github.com/wowchemy/hugo-academic-cli) - Import publications
- [BibTeX to Markdown converter](https://github.com/davidar/bibtex-to-markdown)
- [Favicon Generator](https://realfavicongenerator.net/)

---

## Decision Tree

Use this to quickly navigate to the right phase:

```
Starting fresh?
├─ Yes → Phase 1: Information Gathering
└─ No
   ├─ Need to configure settings? → Phase 2: Configuration
   ├─ Want to change appearance? → Phase 3: Customization
   ├─ Adding/editing content? → Phase 4: Content Population
   ├─ Managing files/images? → Phase 5: Asset Management  
   ├─ Testing before deploy? → Phase 6: Build Validation
   └─ Ready to go live? → Phase 7: Deployment
```

**Already deployed?**
- Regular updates → See Maintenance section
- Problems with site → See Troubleshooting section
- Advanced features → See Advanced Customization section
