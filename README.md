# GoToChar

This is a Sublime Text 3 plug-in for **going to a character**.

![Colored](http://i.imgur.com/bAA4Bkw.gif)

## Features

* Can go to next/previous character.
* Can add the characters in between to selection.
* Works with multi-cursor selections.

## Installation

You can install it from Package Control. Search for GoToChar.

## Usage

Hit **alt+t a** to go to the next "**a**". **shift+alt+t** also selects the area.
**alt+r a** to go to previous a. **shift+alt+r** also selects the area.

This plug-in is case sensitive, there for **a** and **A** are different.

These are the default key bindings set in this plug-in:

```javascript
{ "keys": ["alt+t"], "command": "go_to_char", "args": {"mode": "next"} },
{ "keys": ["alt+r"], "command": "go_to_char", "args": {"mode": "back"} },
{ "keys": ["shift+alt+t"], "command": "go_to_char", "args": {"mode": "next", "select": true} },
{ "keys": ["shift+alt+r"], "command": "go_to_char", "args": {"mode": "back", "select": true} },
```

You can override them to your liking.

Enjoy!
