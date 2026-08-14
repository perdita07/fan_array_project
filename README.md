# Fan Array Project

Experimental characterisation of a PC-fan array's electrical, aerodynamic, and control behaviour — how PWM duty cycle relates to RPM and airflow, and how to model that relationship for closed-loop control.

This repo contains the full analysis pipeline as a sequence of Jupyter notebooks, from raw datalogger exports through to a validated inverse model (`Duty = f(Voltage)`) used for control, plus the supporting project documentation (reports, review presentations).

### Additional resources (reference papers, logs, readings, etc): https://drive.google.com/drive/folders/1X09Ndj4WAZ8-77vm1_YXIhqzWv36yzKz?usp=sharing

## What's in here

The project answers a few core questions about the fan array:

- **How does fan speed (RPM) respond to PWM duty cycle**, at different switching frequencies (20 kHz and 25 kHz), and is that response the same going up as going down (hysteresis)?
- **How does anemometer voltage (a proxy for local air velocity) behave over time and across probe positions** `(z, r)` in the array's flow field?
- **What's the calibration curve between duty cycle and RPM**, fit from raw tachometer/multimeter logs?
- **Can voltage be inverted back to duty cycle** — i.e. given a measured air-velocity signal, what duty cycle produced it? This is the model used for control.
- **How repeatable are these measurements**, and how strongly are duty cycle, RPM, and velocity correlated?

## Notebook pipeline

The notebooks are numbered in the order you'd run them — each builds on outputs from the ones before it.

| # | Notebook | What it does |
|---|----------|---------------|
| 01 | `01_Data_Preprocessing.ipynb` | Converts raw `.txt` datalogger exports into cleaned CSVs; includes the Colab file-upload step used to bring data into the notebooks. |
| 02 | `02_Sensor_Voltage_Time_Characterisation.ipynb` | Raw anemometer voltage-vs-time traces per probe position `(z, r)`, with duty-change markers, plus combined velocity-vs-RPM and voltage-vs-time summary views across all positions. |
| 03 | `03_Duty_Cycle_Sweep_RPM_Response.ipynb` | Up/down duty-cycle sweeps at 20 kHz and 25 kHz PWM — RPM response curves and hysteresis between ramp-up and ramp-down. |
| 04 | `04_Fan_Log_Duty_RPM_Calibration.ipynb` | Parses the raw multimeter/tachometer log, detects ramp direction, filters noise, and fits a linear duty–RPM calibration. |
| 05 | `05_Voltage_to_Duty_Inverse_Mapping.ipynb` | The core modelling notebook: builds and validates the inverse model `Duty = f(Voltage)` used for closed-loop control. Compares candidate model forms (linear, polynomial, exponential, log) by RMSE/MAE/R², and validates the chosen model against synthetic voltage traces. |
| 06 | `06_Duty_RPM_Repeated_Trials.ipynb` | Independent experimental replicates of the duty–RPM relationship across multiple measurement sessions, used to assess repeatability. |
| 07 | `07_Correlation_Analysis.ipynb` | Pearson correlation between duty cycle and RPM/velocity metrics, with an explicit audit table showing which datasets went into each correlation. |
| 08 | `08_Project_Planning.ipynb` | Administrative Gantt-style work plan — not scientific analysis, kept separate from the rest of the pipeline. |
| 09 | `09_Experiments_and_Exploratory_Work.ipynb` | An archive of every superseded, abandoned, or exploratory cell from the original working notebook, grouped by sub-theme. Nothing here feeds the "final" results — it's preserved so the modelling decisions in notebooks 03–07 are traceable and nothing tried along the way is lost. |

There's also `fan_array_aerodynamics.ipynb` at the repo root, which covers the aerodynamic/flow-field side of the project separately from the electrical characterisation pipeline above.

### Why there's a "leftover experiments" notebook

The notebooks above were reorganised from a single original working notebook (59 cells). Where multiple cells did essentially the same analysis — an early attempt and a later, cleaner version — only the final version was kept in the numbered pipeline; the superseded attempts were moved into `09_Experiments_and_Exploratory_Work.ipynb` rather than deleted, so the reasoning behind each modelling choice stays visible. The full cell-by-cell mapping and the rationale for every merge decision is documented in [`REPO_STRUCTURE_PLAN.md`](./REPO_STRUCTURE_PLAN.md) — worth a look if you want to understand *why* a particular model or fit was chosen over the alternatives.

## Project documentation

| File | Contents |
|------|----------|
| `project_report.docx` | Full written project report. |
| `Final Year Project First Review.pptx` | First review presentation. |
| `Second phase First Review (1).pptx` | Second-phase first review presentation. |
| `_Second phase Second Review.pptx` | Second-phase second review presentation. |
| `Results (4).pptx` | Results summary presentation. |
| `REPO_STRUCTURE_PLAN.md` | Full cell-by-cell mapping from the original notebook to this repo's structure, plus notes on which cells were merged/superseded and why. |

## Getting started

### Requirements

The notebooks were developed in Google Colab and expect:

- Python 3.9+
- `pandas`, `numpy`, `matplotlib`, `scipy` (curve fitting via `curve_fit`, interpolation via `interp1d`)
- `openpyxl` (for reading `.xlsx` sensor/log data)
- Jupyter (if running locally instead of in Colab)

Install the core dependencies with:

```bash
pip install pandas numpy matplotlib scipy openpyxl jupyter
```

### Running the notebooks

**Option A — Google Colab (recommended, matches how these were built):**
1. Open a notebook directly from GitHub in Colab (`File → Open notebook → GitHub`, paste the repo URL), or upload it manually.
2. Run `01_Data_Preprocessing.ipynb` first — it includes the file-upload step (`files.upload()`) used to bring your raw data into the session.
3. Work through the remaining notebooks in numeric order (02 → 07); each expects the outputs/data conventions established by the earlier ones.

**Option B — Local Jupyter:**
1. Clone the repo and install the dependencies above.
2. Replace any Colab-specific paths (e.g. `/content/...`) or the `files.upload()` call with a local file path pointing to your data.
3. Launch Jupyter and run the notebooks in order:
   ```bash
   git clone https://github.com/perdita07/fan_array_project.git
   cd fan_array_project
   jupyter notebook
   ```

### Data

The notebooks expect raw sensor exports (multimeter/tachometer logs, anemometer voltage logs) as `.txt` or `.xlsx` files with names like `z=2,r=0.xlsx` and `fan_log.csv`. These are referenced by hardcoded filenames/paths within the notebooks — check the top of each notebook and update paths to match wherever your own raw data lives.

> **Note:** file paths and data filenames are currently hardcoded per-notebook rather than centralised in a config file. If you're adapting this pipeline to new data, expect to update paths inside each notebook individually — see the "Maintainability Recommendations" section of `REPO_STRUCTURE_PLAN.md` for suggested refactors (a shared config module, reusable data-loading/fitting helper functions, etc.) that would make this easier going forward.

## Repo structure

```
fan_array_project/
├── 01_Data_Preprocessing.ipynb
├── 02_Sensor_Voltage_Time_Characterisation.ipynb
├── 03_Duty_Cycle_Sweep_RPM_Response.ipynb
├── 04_Fan_Log_Duty_RPM_Calibration.ipynb
├── 05_Voltage_to_Duty_Inverse_Mapping.ipynb
├── 06_Duty_RPM_Repeated_Trials.ipynb
├── 07_Correlation_Analysis.ipynb
├── 08_Project_Planning.ipynb
├── 09_Experiments_and_Exploratory_Work.ipynb
├── fan_array_aerodynamics.ipynb
├── project_report.docx
├── REPO_STRUCTURE_PLAN.md
└── *.pptx                     # review/results presentations
```

## License

This work is licensed under CC BY-NC-ND 4.0 (Attribution–NonCommercial–NoDerivatives). You're welcome to view and share this work with credit, but non-commercial use only, and no modified/derivative versions may be redistributed. This project reflects unpublished academic work — for reuse beyond what the license permits, please contact the author.
