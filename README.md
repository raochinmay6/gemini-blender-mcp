\# Gemini Blender MCP



Gemini Blender MCP is a local Model Context Protocol–style bridge that allows

Gemini (via its normal chat UI) to directly control Blender using Python (bpy).



No cloud API.

No rate limits.

No instability.



Gemini acts as the brain.

Blender acts as the hands.



---



\## How it works



Gemini Chat → Clipboard → Local MCP Server → Blender Addon → bpy



You write instructions in Gemini.

Gemini outputs Blender Python code.

The code is sent to Blender and executed instantly.



---



\## Features



\- Blender scene control via natural language

\- Object rename, lighting, camera, materials

\- No UI automation (pure bpy access)

\- Gemini Pro friendly

\- Works with Hindi / Hinglish prompts



---



\## Installation



\### 1. Blender Addon

\- Open Blender

\- Edit → Preferences → Add-ons → Install

\- Select `blender\_addon/gemini\_mcp\_addon.py`

\- Enable the addon

\- Press `F3` → Start Gemini MCP



\### 2. MCP Server

```bash

pip install pyperclip

python server/clipboard\_listener.py



