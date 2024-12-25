# Project Setup Guide

## Prerequisites
1. **Python 3.8** - Ensure Python 3.8 is installed on your system.

2. **Virtual Environment** - Use Python 3.8 to create and manage a virtual environment.

---

## Setting up the Environment

1. **Create Virtual Environment:**
   python3.8 -m venv .venv

2. **Activate the Virtual Environment:**
   source .venv/bin/activate

3. **Install Dependencies:**
   pip install -r requirements.txt

---

## Running the Scripts
#### Weather Dataset Scripts:
1. iTransformer:
   ```bash
   bash ./scripts/long_term_forecast/Weather_script/iTransformer.sh
   ```
2. TimeXer:
   ```bash
   bash ./scripts/long_term_forecast/Weather_script/TimeXer.sh
   ```
3. TimeMixer:
   ```bash
   bash ./scripts/long_term_forecast/Weather_script/TimeMixer.sh
   ```

#### ETT Dataset Scripts:
1. iTransformer_Etth2:
   ```bash
   bash ./scripts/long_term_forecast/ETT_script/iTransformer_Etth2.sh
   ```
2. TimeXer_Etth2:
   ```bash
   bash ./scripts/long_term_forecast/ETT_script/TimeXer_Etth2.sh
   ```
3. TimeMixer_Etth2:
   ```bash
   bash ./scripts/long_term_forecast/ETT_script/TimeMixer_Etth2.sh
   ```

---
