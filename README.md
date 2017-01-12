# GoToChar

This is a Sublime Text 3 plug-in to go to a char.

## Features

* Can go to next/previous character.
* Can add the characters in between to selection.
* Works with multi-cursor selections.

## Installation

You can install it from Package Control. Search for GoToChar.

## Usage

These are the default key bindings set in this plug-in:

```javascript
{ "keys": ["alt+t"], "command": "in_between", "args": {"mode": "next"} },
{ "keys": ["alt+r"], "command": "in_between", "args": {"mode": "back"} },
{ "keys": ["shift+alt+t"], "command": "in_between", "args": {"mode": "next", "select": true} },
{ "keys": ["shift+alt+r"], "command": "in_between", "args": {"mode": "back", "select": true} },
```

Enjoy!
