# Valerio Ficcadenti - Academic CV Website

[![Hugo](https://img.shields.io/badge/Hugo-0.129-blue.svg)](https://gohugo.io)
[![Hugo Blox](https://img.shields.io/badge/Hugo%20Blox-v5.9-brightgreen)](https://hugoblox.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)

**Professional academic website showcasing research, teaching, and industry experience in business research methods, quantitative finance, and data science.**

🌐 **[View Live Website →](https://your-website-url.com)**

## About

This website serves as the professional academic portfolio for **Valerio Ficcadenti**, Associate Professor in Business Research Methods at London South Bank University. Built with Hugo and Hugo Blox Builder, it showcases:

- 📚 **Academic Profile**: Research interests in computational linguistics, text mining, and quantitative finance
- 💼 **Professional Experience**: Leadership roles in academia and industry (LSBU, Deloitte, FAO)
- 🎯 **Research Excellence**: Publications, talks, and REF contributions
- 👥 **Team Leadership**: PhD supervision and research mentorship
- 🔗 **Professional Networks**: Social media and academic platform links

## Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Social Integration**: LinkedIn, GitHub, Google Scholar, ORCID, and more
- **Academic Focus**: Publication lists, talks, and research highlights
- **Industry Appeal**: Recruiter-friendly experience section
- **Team Showcase**: Dedicated pages for PhD students and collaborators
- **Contact Integration**: Interactive maps and direct contact options

## Technical Stack

- **Framework**: [Hugo](https://gohugo.io/) (Static Site Generator)
- **Theme**: [Hugo Blox Builder Academic CV](https://hugoblox.com/templates/)
- **Deployment**: Ready for GitHub Pages, Netlify, or Vercel
- **Content**: Markdown with YAML frontmatter
- **Icons**: Font Awesome, Academicons, and custom SVGs

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/academic-cv.git
   cd academic-cv
   ```

2. **Install Hugo** (if not already installed):
   ```bash
   # Ubuntu/Debian
   sudo apt install hugo
   
   # macOS
   brew install hugo
   
   # Windows
   choco install hugo-extended
   ```

3. **Run the development server**:
   ```bash
   hugo server
   ```

4. **Open your browser** and visit `http://localhost:1313`

## Customization

### Content Updates
- **Profile**: Edit `content/authors/valerio-ficcadenti/_index.md`
- **Homepage**: Modify `content/_index.md`
- **Experience**: Update work history in the author profile
- **Publications**: Add to `content/publication/`
- **Talks**: Add to `content/talks/`

### Styling
- **Colors & Themes**: Configure in `config/_default/params.yaml`
- **Custom CSS**: Add to `assets/scss/custom.scss`
- **Icons**: Place custom SVGs in `assets/media/icons/`

### Deployment Options

#### GitHub Pages
1. Create a new repository on GitHub
2. Push your code
3. Enable GitHub Pages in repository settings
4. Set source to "GitHub Actions"

#### Netlify
1. Connect your GitHub repository to Netlify
2. Build command: `hugo --gc --minify`
3. Publish directory: `public`

#### Vercel
1. Import your GitHub repository to Vercel
2. Framework preset: Hugo
3. Build command: `hugo --gc --minify`

## Content Structure

```
content/
├── _index.md                    # Homepage
├── authors/
│   └── valerio-ficcadenti/     # Main profile
├── experience/                  # Work experience pages
├── talks/                      # Conference talks & presentations
├── publication/                # Academic publications
└── contact/                    # Contact information
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Built with [Hugo Blox Builder](https://hugoblox.com/)
- Theme: [Academic CV](https://github.com/HugoBlox/theme-academic-cv)
- Icons: [Font Awesome](https://fontawesome.com/), [Academicons](https://jpswalsh.github.io/academicons/)

## Contact

**Valerio Ficcadenti**  
Associate Professor  
London South Bank University  
📧 ficcadv2@lsbu.ac.uk  
🔗 [LinkedIn](https://www.linkedin.com/in/valerio-ficcadenti/) | [GitHub](https://github.com/mevalerio) | [Google Scholar](https://scholar.google.com/citations?user=iC-WRSMAAAAJ&hl=it)

## AI Assistant Configuration

This section provides context and instructions for AI assistants working on this project.

### Project Context
- **Owner**: Valerio Ficcadenti, Associate Professor at London South Bank University
- **Purpose**: Professional academic website showcasing research and teaching expertise
- **Target Audience**: Academic colleagues, industry recruiters, students, research collaborators
- **Framework**: Hugo with Hugo Blox Builder theme

### AI Assistant Instructions
When working on this project, please:

1. **Maintain Academic Standards**: Use scholarly tone while ensuring accessibility
2. **Focus on Professional Appeal**: Content should attract both academic and industry opportunities  
3. **Follow Hugo Blox Conventions**: Use correct syntax, file structure, and naming conventions
4. **Preserve Social Network Configuration**: Use the working `social:` format with proper `icon_pack` values
5. **Ensure Responsive Design**: Test changes across different screen sizes
6. **Optimize for Discovery**: Include proper SEO metadata and structured content

### Common Tasks
- Adding publications, talks, or experience entries
- Updating team member profiles and collaborations
- Modifying homepage layout and content organization
- Managing social media links and contact information
- Optimizing content for academic job market and industry recruitment

### Technical Notes
- Social icons use Hugo Blox classic format (`social:` with `icon_pack`)
- Content is organized in `/content/` directory with proper frontmatter
- Deployment via GitHub Actions to GitHub Pages
- Local development: `hugo server` for testing changes

---

*Last updated: July 2025*
