# AGENTS.md

## Project Overview

This is a Ren'Py 8 visual novel project named:

《SFLS~我挚爱的时光》

The game is based on SFLS campus life. The protagonist is a new Grade 10 student who gradually becomes familiar with the school, classmates, and campus life.

The overall style is:

- Campus daily life
- Light comedy
- Character interaction
- Internet/anime culture references and jokes
- Character growth

The current narrative structure is:

Common main story + character relationship side stories + campus event side stories + multiple endings.

---

## Technical Stack

- Engine: Ren'Py 8
- Language: Ren'Py Script + Python
- Editor: Visual Studio Code
- Version control: Git + GitHub

`.rpy` files are Ren'Py scripts, not normal Python files.

Use Ren'Py syntax correctly.

---

## General Editing Rules

1. Make the smallest necessary change for the requested task.

2. Do not perform large refactors unless explicitly requested.

3. Preserve the existing project structure, naming conventions, labels, character variables, and coding style.

4. Do not delete existing story content, variables, images, audio references, or labels unless explicitly requested.

5. Before modifying a file, inspect relevant nearby files and definitions when necessary.

6. Do not invent existing resources.
   If an image, audio file, character, or label does not exist, either:
   - use a clearly marked TODO placeholder, or
   - explain that the resource is missing.

7. Do not modify unrelated files.

---

## Ren'Py Rules

When editing `.rpy` files:

- Use Ren'Py 8 syntax.
- Keep indentation valid.
- Check all `label` names.
- Check all `jump` and `call` targets.
- Avoid duplicate labels.
- Use `default` for variables that belong to save-game state.
- Use `define` for static definitions such as characters.
- Do not treat Ren'Py Script as plain Python.

Example:

```renpy
default relation_a = 0

define a = Character("A")

label lunch_event:

    a "要不要一起去食堂？"

    menu:
        "一起去":
            $ relation_a += 1
            jump cafeteria_event

        "算了":
            jump afternoon
