# WEB DESIGN PROMPT & AGENT INSTRUCTION LIBRARY (UI/UX PRO MAX)
# کتابخانه پرامپت‌ها و دستورالعمل‌های طراحی وب‌سایت

This document provides quick-start prompts, agent instructions, and system message templates for configuring any AI model (Claude, GPT-4o, Gemini, Cursor, Windsurf, Copilot, Qwen, DeepSeek, etc.) to use the **UI/UX Pro Max** design intelligence installed in this repository (`paymanshafayan/Necessary-Skills`).

---

## 📖 Available System Prompts in this Repository

1. **`PROMPT.md`** — The complete **English-language AI System Prompt** covering all 84 UI styles, 192 color palettes, 74 font pairings, 25 chart types, 22 tech stacks, 98 UX guidelines, and 161 reasoning rules.
2. **`PROMPT_FA.md`** — The complete **Persian-language AI System Prompt (نسخه کامل فارسی)** for Persian-speaking users and AI models.

---

## 🚀 How to Feed These Prompts to Any AI Model

### Option A: Cursor / Windsurf / IDE Custom Rules (`.cursorrules` / `.windsurfrules`)
Add the following reference to your project's rules file:
```markdown
Always follow the UI/UX Pro Max Web Design System Prompt located in `PROMPT.md` (or `PROMPT_FA.md` for Persian projects). Before generating any UI code, consult `ui-ux-pro-max/data/products.csv`, `styles.csv`, `colors.csv`, and `typography.csv` to ensure industry-specific design, accessible contrast (4.5:1), SVG icons (no emojis), and mobile-first responsive layouts.
```

### Option B: Claude Code / Universal AI Agents (`.claude/` / `.agents/`)
When asking Claude Code or an AI Agent to build a website, start your conversation with:
```
Read PROMPT.md (or PROMPT_FA.md) and use the ui-ux-pro-max skill in ui-ux-pro-max/ to generate a complete design system and build a modern, clean, and excellent website for [YOUR_PROJECT_NAME].
```

### Option C: Custom GPTs / Claude Projects / System Prompt Box
Copy and paste the entire contents of **`PROMPT.md`** (or **`PROMPT_FA.md`**) into the System Instructions / Custom Instructions box of your AI assistant.

---

## 📋 Quick-Start System Prompt Snippet (Bilingual English / Farsi)

You can copy-paste this concise snippet into any AI chat session:

```markdown
You are an Elite AI Web Designer & Frontend Architect (UI/UX Pro Max Agent) operating inside the `paymanshafayan/Necessary-Skills` repository.
You must read and strictly adhere to `PROMPT.md` (or `PROMPT_FA.md`).
When building or modifying any website or UI:
1. NEVER use cliché AI aesthetics (no purple/pink linear gradients, no flat gray-on-gray boxes).
2. NEVER use emojis as UI icons; always use SVG vector icons (Heroicons/Lucide).
3. ALWAYS query `python3 ui-ux-pro-max/scripts/search.py "<domain>" --design-system` (or inspect `ui-ux-pro-max/data/` CSVs directly) to obtain:
   - One of the 84 UI styles (or 67 categorized styles: 49 General, 8 Landing, 10 BI/Analytics).
   - One of the 192 Color Palettes (using semantic variables: --color-primary, --color-secondary, etc.).
   - One of the 74 Font Pairings (imported from Google Fonts).
   - Appropriate chart recommendations from the 25 Chart Types.
   - Stack rules from the 22 Tech Stacks.
4. Enforce the 10 Priority UX & Accessibility rules (WCAG AA/AAA, 4.5:1 contrast, touch target 44x44px, smooth 150-300ms hover/focus transitions, cursor-pointer on all clickable elements).
5. Ensure mobile-first responsiveness across 375px, 768px, 1024px, and 1440px without horizontal scroll.
```

---

## 🎨 Quick Reference of Included Datasets

| Dataset | File Path | Total Entries | Description |
|---------|-----------|---------------|-------------|
| **UI Styles** | `ui-ux-pro-max/data/styles.csv` | **84 Styles** | Glassmorphism, Claymorphism, Minimalism, Neumorphism, Bento Grid, Dark Mode, AI-Native UI, Soft UI Evolution, E-Ink, Pixel Art, etc. |
| **Color Palettes** | `ui-ux-pro-max/data/colors.csv` | **192 Palettes** | 1:1 aligned with product types; semantic primary, secondary, accent, background, foreground, card, border tokens. |
| **Font Pairings** | `ui-ux-pro-max/data/typography.csv` | **74 Pairings** | Curated Google Fonts import URLs, Heading + Body fonts, mood alignment. |
| **Chart Types** | `ui-ux-pro-max/data/charts.csv` | **25 Chart Types** | Line, Bar, Pie, Heatmap, Scatter, Treemap, Funnel, Waterfall, Candlestick/OHLC, etc. |
| **Tech Stacks** | `ui-ux-pro-max/data/stacks/` | **22 Stacks** | React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel, Three.js, JavaFX, WPF, WinUI 3, UWP, Avalonia, Uno Platform. |
| **UX Guidelines** | `ui-ux-pro-max/data/ux-guidelines.csv` | **98 Guidelines** | Accessibility, Touch/Interaction, Performance, Layout, Animation, Forms, Navigation, Charts. |
| **Reasoning Rules** | `ui-ux-pro-max/data/ui-reasoning.csv` | **161 Rules** | Domain-specific logic for SaaS, Finance, Healthcare, E-commerce, Services, Creative, Lifestyle, Emerging Tech. |

---

## 🌟 Persian Summary / خلاصه فارسی

برای طراحی هر وب‌سایت مدرن و حرفه‌ای در این پروژه:
1. فایل `PROMPT_FA.md` یا `PROMPT.md` را مطالعه کنید.
2. از طریق اسکریپت `search.py` یا مشاهده مستقیم فایل‌های CSV در مسیر `ui-ux-pro-max/data/`، سبک رابط کاربری (از میان ۸۴ سبک)، پالت رنگی (از میان ۱۹۲ پالت)، ترکیب فونت (از میان ۷۴ ترکیب)، و نوع نمودار (از میان ۲۵ نمودار) را مشخص کنید.
3. قوانین دسترسی‌پذیری (WCAG AA/AAA، حداقل کنتراست 4.5:1، عدم استفاده از ایموجی به‌جای آیکون، استفاده از `cursor-pointer` و انیمیشن‌های ۱۵۰-۳۰۰ میلی‌ثانیه‌ای) را در تمامی ۲۲ استک فناوری رعایت کنید.
