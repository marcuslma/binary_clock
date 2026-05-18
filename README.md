# Binary Clock 🕓

![binary_clock preview](assets/binary_clock.gif)

A visual binary clock with a "hacker terminal" theme built using HTML, CSS, and JavaScript.

Made with Claude Design.

## What it is 🚀

This project displays a binary clock showing local time in BCD (Binary-Coded Decimal), along with UTC time, date, and epoch readings.

It also includes:
- 🌧️ a lightweight Matrix-style rain background animation
- 🎨 selectable color themes
- 🖥️ a vintage terminal look with scanlines and CRT effects
- ⌨️ support for `ESC` to pause/resume and `SPACE` for a pulse animation

## How to use ▶️

Open the `main.html` file in a modern browser.

### Recommended ✅

To avoid local file restrictions, run a simple HTTP server from the project directory:

```bash
cd /home/marcus/Development/marcus/binary_clock
python3 -m http.server 8000
```

Then open in your browser:

```text
http://localhost:8000/main.html
```

## Keys ⌨️

- `ESC` — pause / resume the clock
- `SPACE` — pulse animation on the panel

## Themes 🎨

`main.html` offers five themes:
- phosphor
- amber
- ice
- blood
- matrix

## Compatibility 🌐

Works in modern browsers with support for HTML5, CSS custom properties, and ES6 JavaScript.
