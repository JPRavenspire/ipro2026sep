# HTML Tags & Attributes

There are many different tags and attributes that can be used across HTML and CSS. Below is a list of some of the most common ones we've discussed so far, or will discuss in the coming week.

You can always look up new tags, search online for help with ones you don't understand, or simply experiment with tags you come across online but hadn't seen before.

> **Tip:** You can inspect almost any website to view its HTML. It's an excellent way to learn how real websites are built.

---

# HTML Tags

## Document Structure

| Tag | Description |
|------|-------------|
| `<html>` | Contains the entire HTML document. |
| `<head>` | Contains metadata such as the page title, linked stylesheets, viewport settings, character encoding, and other information not displayed on the page itself. |
| `<body>` | Contains all visible content shown on the webpage. |

## Metadata

| Tag | Description |
|------|-------------|
| `<title>` | Sets the title displayed in the browser tab. |
| `<link>` | Links external resources such as CSS files. Example: `<link rel="stylesheet" href="style.css">` |

## Semantic Layout

| Tag | Description |
|------|-------------|
| `<header>` | Contains introductory content such as the logo, page title, or navigation bar. |
| `<main>` | Contains the primary content of the webpage. |
| `<footer>` | Contains information shown at the bottom of the page, such as contact information, navigation links, or copyright notices. |
| `<nav>` | Contains navigation links for the website. |
| `<div>` | A generic container used to group and organise content. |

## Text Elements

| Tag | Description |
|------|-------------|
| `<p>` | A paragraph of text. |
| `<h1>` | Heading level 1 (largest). |
| `<h2>` | Heading level 2. |
| `<h3>` | Heading level 3. |
| `<h4>` | Heading level 4. |
| `<h5>` | Heading level 5. |
| `<h6>` | Heading level 6 (smallest). |
| `<br>` | Inserts a line break. |
| `<a>` | Creates a hyperlink to another page or website. Example: `<a href="https://www.google.com/">Google</a>` |

## Lists

| Tag | Description |
|------|-------------|
| `<ul>` | Unordered (bulleted) list. |
| `<ol>` | Ordered (numbered) list. |
| `<li>` | A list item. |

## Tables

| Tag | Description |
|------|-------------|
| `<table>` | Creates a table. |
| `<tr>` | Defines a table row. |
| `<th>` | Defines a table heading cell. |
| `<td>` | Defines a table data cell. |

## Media

| Tag | Description |
|------|-------------|
| `<img>` | Displays an image using the `src` attribute. Example: `<img src="image.jpg" alt="Description">` |

---

# HTML Attributes

| Attribute | Description |
|-----------|-------------|
| `style` | Applies inline CSS styling to an element. |
| `href` | Specifies the destination of a hyperlink or linked resource. |
| `src` | Specifies the source of media such as images, videos, or scripts. |
| `width` | Sets the width of an element. |
| `height` | Sets the height of an element. |

---

# CSS Flexbox

Flexbox is a layout system that makes it much easier to arrange elements on a webpage.

To enable Flexbox, set the `display` property of a container to `flex`:

```css
display: flex;
```

Once Flexbox is enabled, you can use the properties you've learned in **Flexbox Froggy** to control the layout of the items inside the container.

Some commonly used Flexbox properties include:

| Property | Purpose |
|----------|---------|
| `justify-content` | Controls horizontal alignment. |
| `align-items` | Controls vertical alignment. |
| `flex-direction` | Sets whether items are laid out in a row or column. |
| `flex-wrap` | Allows items to wrap onto multiple lines. |
| `gap` | Adds spacing between flex items. |
| `flex-grow` | Controls how much an item expands. |
| `flex-shrink` | Controls how much an item shrinks. |

---

# Remember

- HTML provides the **structure** of your webpage.
- CSS controls the **appearance** of your webpage.
- Use semantic HTML tags whenever possible (`<header>`, `<main>`, `<footer>`, etc.) to make your code easier to understand and improve accessibility.
- When you're unsure how something works, inspect existing websites or consult the MDN Web Docs.