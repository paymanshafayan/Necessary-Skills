# Necessary-Skills 🚀

> **مجموعه مهارت‌ها و دستورالعمل‌های ضروری هوش مصنوعی برای توسعه و طراحی نرم‌افزار**  
> **Essential AI Skills & System Prompts for Modern Web Design & Software Engineering**

---

## 🇮🇷 راهنمای فارسی (Persian Guide)

این مخزن شامل ابزارها، منابع داده، دیزاین سیستم‌ها و پرامپت‌های تخصصی برای طراحی وب‌سایت‌ها و رابط‌های کاربری مدرن، تمیز و استاندارد است. در این نسخه، مجموعه مهارتی قدرتمند **UI/UX Pro Max** به‌صورت کامل نصب و پیکربندی شده است تا هر مدل هوش مصنوعی (AI Model) با خواندن دستورالعمل‌های آن بتواند وب‌سایت‌هایی در سطح جهانی طراحی کند.

### 🌟 امکانات و منابع نصب‌شده در این ریپو

مجموعه کامل قابلیت‌های زیر در پوشه `ui-ux-pro-max/` نصب شده و آماده استفاده است:

- **۸۴ سبک رابط کاربری (84 UI Styles)** — شامل Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Box Grid, Dark Mode (OLED), AI-Native UI, Soft UI Evolution, E-Ink, Pixel Art و ...
- **۱۹۲ پالت رنگی (192 Color Palettes)** — پالت‌های اختصاصی و هماهنگ (1:1) با ۱۹۲ نوع محصول نرم‌افزاری بر اساس متغیرهای معنایی (Primary, Secondary, Accent, Card, Muted, Border و ...).
- **۷۴ ترکیب تایپوگرافی (74 Font Pairings)** — ترکیب‌های حرفه‌ای از فونت‌های Google Fonts همراه با دستورات ایمپورت CSS و تناسب با حال‌وهوای برند.
- **۲۵ نوع نمودار (25 Chart Types)** — توصیه‌های تخصصی برای طراحی داشبوردها و تحلیل داده (Line, Bar, Pie/Donut, Heatmap, Treemap, Funnel, Waterfall, OHLC و ...) همراه با قوانین دسترسی‌پذیری.
- **۲۲ استک فناوری (22 Tech Stacks)** — دستورالعمل‌های معماری و استایل‌دهی برای:
  - `React`, `Next.js`, `shadcn/ui`
  - `Vue`, `Nuxt.js`, `Nuxt UI`
  - `Angular`, `Laravel (Blade/Livewire/Inertia)`
  - `Svelte`, `Astro`, `Three.js`, `HTML + Tailwind CSS` (پیش‌فرض)
  - `SwiftUI (iOS)`, `Jetpack Compose (Android)`, `React Native`, `Flutter`
  - `JavaFX`, `WPF`, `WinUI 3`, `UWP`, `Avalonia`, `Uno Platform`
- **۹۸ دستورالعمل تجربه کاربری (98 UX Guidelines)** — بهترین شیوه‌ها، الگوهای ممنوعه (Anti-patterns)، دسترسی‌پذیری و تعاملات واکنش‌گرا.
- **۱۶۱ قانون استدلال هوشمند (161 Reasoning Rules)** — قوانین تولید دیزاین سیستم بر اساس صنایع مختلف (Tech & SaaS, Finance, Healthcare, E-commerce, Services, Creative, Lifestyle, Emerging Tech).
- **سبک‌های دسته‌بندی‌شده (67 Available Styles)**:
  - **۴۹ سبک عمومی (General Styles)**
  - **۸ سبک صفحه فرود (Landing Page Styles)**
  - **۱۰ سبک داشبوردهای هوش تجاری و تحلیلی (BI/Analytics Dashboard Styles)**

---

### 📋 فایل پرامپت واحد و جامع (Single Unified AI Agent System Prompt)

برای اینکه من (عامل هوش مصنوعی در Arena) یا هر مدل هوش مصنوعی دیگری (مانند Claude, GPT-4o, Gemini, Cursor, DeepSeek, Qwen و غیره) بداند چگونه از این امکانات برای ساخت یک وب‌سایت مدرن، تمیز و عالی استفاده کند، **یک فایل پرامپت واحد و جامع** در ریشه مخزن ساخته شده است:

- 📄 **`PROMPT.md`** — **پرامپت واحد و جامع (Single Unified Prompt)**:  
  هر بار که خواستید وب‌سایت یا رابط کاربری ساخته شود، **فقط آدرس همین فایل (`PROMPT.md`)** را به مدل هوش مصنوعی بدهید. این فایل به مدل دستور می‌دهد:
  1. دیزاین سیستم (رنگ‌ها، سبک‌های ۸۴گانه، تایپوگرافی‌های ۷۴گانه و قوانین UX) را از `ui-ux-pro-max` استخراج کند.
  2. کامپوننت‌های مدرن را با استفاده از متغیر محیطی / Secret ذخیره‌شده با نام **`API_KEY`** و از طریق سرور MCP سایت 21st.dev (`21st-magic`) دریافت کند.
  3. کامپوننت دریافتی را بلافاصله بر اساس توکن‌های پروژه بومی‌سازی و سفارشی‌سازی (Customize) کند.

---

### 💻 نحوه استفاده برای طراحی وب‌سایت

هر مدل هوش مصنوعی یا توسعه‌دهنده می‌تواند از طریق اسکریپت پایتون یا بررسی مستقیم فایل‌های داده، دیزاین سیستم مناسب را تولید کند:

```bash
# تولید دیزاین سیستم اختصاصی برای یک محصول SaaS
python3 ui-ux-pro-max/scripts/search.py "saas landing ai tool" --design-system -p "MyAIProduct"

# تولید دیزاین سیستم برای اپلیکیشن بانکی و مالی
python3 ui-ux-pro-max/scripts/search.py "fintech banking" --design-system -f markdown

# جستجو در سبک‌های بصری (مثلاً Glassmorphism)
python3 ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style

# جستجو در راهنمای استک‌های فناوری (مثلاً React یا Tailwind)
python3 ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind
```

---

### ⚡ ترکیب با MCP Server سایت 21st.dev (`21st-magic`)

اگر از دستیارهای هوش مصنوعی مانند **Cursor**, **Windsurf** یا **Claude Desktop** استفاده می‌کنید، می‌توانید با افزودن تنظیمات زیر (موجود در فایل `MCP_CONFIG.json`) به محیط خود، از کامپوننت‌های مدرن سایت 21st.dev در کنار دیزاین سیستم UI/UX Pro Max استفاده کنید:

```json
{
  "mcpServers": {
    "21st-magic": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@21st-dev/magic@latest"],
      "env": {
        "API_KEY": "کلید_ای_پی_آی_شما_از_سایت_21st"
      }
    }
  }
}
```
**پروتکل استفاده همزمان (Synergy Protocol):**  
مدل هوش مصنوعی ابتدا سبک بصری، پالت رنگی و ترکیب فونت را از `ui-ux-pro-max` استخراج می‌کند، سپس کامپوننت‌های پیشرفته را از طریق `21st-magic` جستجو و دریافت کرده و در نهایت استایل کامپوننت را با توکن‌های پروژه سفارشی‌سازی (Customize) می‌کند.  
*(نکته: در محیط‌های خط فرمان یا سرور که IDE گرافیکی وجود ندارد، عامل هوش مصنوعی می‌تواند با استفاده از اسکریپت `python3 ui-ux-pro-max/scripts/magic_21st.py` مستقیماً با سرور 21st.dev ارتباط برقرار کند).*

---

## 🇺🇸 English Guide

Welcome to **Necessary-Skills**, a curated repository of AI skills, design systems, and agent system prompts for modern web development and software engineering.

This repository integrates the complete **UI/UX Pro Max** design intelligence package, providing AI assistants and developers with the exact rules, styles, color palettes, and typography pairings needed to design **modern, clean, and excellent websites**.

### 🚀 What is Installed in this Repository

The `ui-ux-pro-max/` folder (along with auto-discovery paths in `.claude/skills/`, `.cursor/skills/`, and `.agents/skills/`) contains:

- **84 UI Styles** — Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, AI-Native UI, Soft UI Evolution, E-Ink, Pixel Art, and more.
- **192 Color Palettes** — Industry-specific palettes aligned 1:1 with the 192 product types, organized by semantic tokens (`Primary`, `Secondary`, `Accent`, `Background`, `Foreground`, `Card`, `Border`, etc.).
- **74 Font Pairings** — Curated typography combinations with Google Fonts imports, font weights, and mood alignment.
- **25 Chart Types** — Dashboard and analytics recommendations with SVG vs. Canvas thresholds and WCAG accessibility fallbacks.
- **22 Tech Stacks** — Comprehensive styling and architectural guidelines for React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel, Three.js, JavaFX, WPF, WinUI 3, UWP, Avalonia, and Uno Platform.
- **98 UX Guidelines** — Best practices, accessibility guardrails, interactive touch rules, and anti-patterns.
- **161 Reasoning Rules** — Industry-specific design system generation across Tech & SaaS, Finance, Healthcare, E-commerce, Services, Creative, Lifestyle, and Emerging Tech.
- **67 Categorized Master Styles**:
  - **49 General Styles**
  - **8 Landing Page Styles**
  - **10 BI/Analytics Dashboard Styles**

---

### 📖 Single Unified AI System Prompt (`PROMPT.md`)

To instruct any LLM on how to build modern websites by uniting both **UI/UX Pro Max** design intelligence and **21st.dev Magic MCP Server (`21st-magic`)** components, pass **only the single unified prompt file**:

- **`PROMPT.md`** — The canonical Single Unified AI Agent System Prompt (with Persian quick reference). Instructs agents to establish visual truth from `ui-ux-pro-max/`, fetch components from 21st.dev using **`API_KEY`** (`ui-ux-pro-max/scripts/magic_21st.py`), and immediately customize imported components to enforce 4.5:1 contrast, SVG icons, `cursor-pointer`, and 150-300ms smooth transitions.

---

### 📂 Directory Structure

```
Necessary-Skills/
├── PROMPT.md                     # Single Unified Master AI System Prompt
├── MCP_CONFIG.json               # 21st.dev Magic MCP Server Config Guide
├── README.md                     # Repository Overview (This file)
├── ui-ux-pro-max/                # Core Skill Installation Folder
│   ├── SKILL.md                  # Canonical Skill Metadata
│   ├── data/                     # CSV & Stack Databases
│   │   ├── styles.csv            # 84 UI Styles
│   │   ├── colors.csv            # 192 Color Palettes
│   │   ├── typography.csv        # 74 Font Pairings
│   │   ├── charts.csv            # 25 Chart Types
│   │   ├── products.csv          # 192 Product Types
│   │   ├── ui-reasoning.csv      # 161 Reasoning Rules
│   │   ├── ux-guidelines.csv     # 98 UX Guidelines
│   │   └── stacks/               # 22 Tech Stack Guidelines
│   ├── scripts/                  # Search & Design System Generator (Python 3)
│   │   ├── search.py             # CLI Search Tool
│   │   ├── design_system.py      # Design System Generator
│   │   ├── core.py               # BM25 Search Engine
│   │   └── validate_data.py      # Data Validation Script
│   ├── references/               # Quick References & Pro Rules
│   │   ├── quick-reference.md    # 98 UX Rules Detailed Reference
│   │   └── pro-rules.md          # Pro Polish Rules & Pre-Delivery Checklist
│   └── projects/                 # Real Example Web Projects
│       ├── saas-landing/         # Example SaaS Landing Page (HTML + Tailwind)
│       ├── healthcare-dashboard/ # Example Analytics Dashboard
│       └── portfolio-dark/       # Example Dark Mode Portfolio
├── .claude/skills/ui-ux-pro-max/ # Claude Code Auto-Discovery Path
├── .cursor/skills/ui-ux-pro-max/ # Cursor IDE Auto-Discovery Path
└── .agents/skills/ui-ux-pro-max/ # Universal AI Agent Auto-Discovery Path
```

---

### 🛠️ Quick Command Examples

```bash
# Generate a complete design system for a product
python3 ui-ux-pro-max/scripts/search.py "fintech crypto dashboard" --design-system -p "CryptoPro"

# Persist design system to design-system/MASTER.md
python3 ui-ux-pro-max/scripts/search.py "wellness spa booking" --design-system --persist -p "SerenitySpa"

# Search typography pairings
python3 ui-ux-pro-max/scripts/search.py "luxury elegant serif" --domain typography

# Search tech stack guidelines for React / shadcn
python3 ui-ux-pro-max/scripts/search.py "accessible modal form" --stack shadcn
```
