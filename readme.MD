📊 LLM-Driven Dynamic Data Visualization Engine (Python)
Overview

This project is a Python-based, LLM-powered dynamic data visualization system that automatically analyzes datasets and recommends the most suitable chart types, then renders them interactively on a web UI.

The goal is to bridge raw data → intelligent chart reasoning → interactive visualization, enabling users to generate meaningful plots without manually deciding how the data should be visualized.

✨ Key Features

🔍 Automatic dataset schema analysis

🧠 LLM-based chart recommendation engine

📈 Dynamic 2D and 3D visualizations

🖥️ Interactive web dashboard (zoom, pan, hover, select)

🔄 Supports multiple data sources (API, CSV, database)

🧩 Modular and extensible architecture

🔒 Safe LLM usage (JSON-only output, no code generation)

🧠 How It Works

Data is fetched from an API, file, or database

Python analyzes column types and basic statistics

An LLM recommends the best visualization types

The LLM outputs a strict JSON chart specification

Python converts the spec into Plotly charts

Charts are rendered dynamically in a Dash web UI

🏗️ System Architecture
Data Source (API / CSV / DB)
        ↓
Schema Analyzer (Pandas)
        ↓
LLM Chart Reasoning Engine
        ↓
Chart Specification (JSON)
        ↓
Chart Factory (Plotly)
        ↓
Web Dashboard (Dash)