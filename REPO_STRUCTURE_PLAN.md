# Repository Restructuring Plan
Fan characterisation / wind-profile project — notebook reorganisation

---

## SECTION 1: Repository Structure

### 01_Data_Preprocessing.ipynb
**Purpose:** Utility/infrastructure steps used to prepare raw instrument exports before any analysis runs.
**Contents:** Cell 1 (raw `.txt` datalogger → cleaned CSV), Cell 42 (Colab file upload).

### 02_Sensor_Voltage_Time_Characterisation.ipynb
**Purpose:** Raw anemometer voltage-vs-time traces per probe position `(z, r)` with duty-change markers, plus derived velocity-vs-RPM and voltage-vs-time summaries across all positions.
**Contents:** Cells 2, 4, 6 (per-position traces) → Cell 8, Cell 7 (all-position summaries) → Cell 41, Cells 3 & 5 (velocity-RPM views).

### 03_Duty_Cycle_Sweep_RPM_Response.ipynb
**Purpose:** Up/down duty-cycle sweeps at 20 kHz and 25 kHz PWM, RPM response and hysteresis.
**Contents:** Cell 12 (20 kHz, final), Cell 10 (20 kHz averaged table), Cell 13 (25 kHz, final).

### 04_Fan_Log_Duty_RPM_Calibration.ipynb
**Purpose:** Parse the raw multimeter/tachometer log, detect ramp direction, filter noise, fit linear duty–RPM relationship.
**Contents:** Cell 46 (final cumulative version of a 4-step development chain).

### 05_Voltage_to_Duty_Inverse_Mapping.ipynb
**Purpose:** Build and validate the inverse model `Duty = f(Voltage)` used for closed-loop control; compare candidate model forms; validate on example voltage traces.
**Contents:** Cell 18 → Cell 19 → Cell 28 → Cell 27 → Cell 34 → Cell 36 → Cell 39 → Cell 40.

### 06_Duty_RPM_Repeated_Trials.ipynb
**Purpose:** Independent experimental replicates of the duty–RPM relationship across sessions.
**Contents:** Cell 48, Cell 49, Cell 50, Cell 51, Cells 54+55, Cell 56.

### 07_Correlation_Analysis.ipynb
**Purpose:** Pearson correlation between duty cycle and RPM/velocity metrics, computed with an explicit audit table.
**Contents:** Cell 57 (helper function), Cell 58 (datasets), Cell 59 (run analyses).

### 08_Project_Planning.ipynb
**Purpose:** Administrative Gantt-style work plan. Not scientific analysis; kept separate.
**Contents:** Cell 47.

### 09_Experiments_and_Exploratory_Work.ipynb
**Purpose:** Preserves every superseded/abandoned/exploratory cell verbatim, grouped by sub-theme, so nothing is lost and future students can see what was tried.
**Contents:** Cells 9, 11, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 35, 37, 38, 43, 44, 45, 52, 53.

---

## SECTION 2: Cell Mapping

| Original Cell | Destination Notebook | Position | Reason |
|---|---|---|---|
| 1 | 01_Data_Preprocessing | 1 | Raw txt → CSV cleaning; foundational preprocessing step. |
| 2 | 02_Sensor_Voltage_Time | 1 | Voltage-time trace, z=1,r=0; final, no duplicate. |
| 3 | 02_Sensor_Voltage_Time | 8 (ref.) | Velocity-RPM subplot grid; same data as 5 & 41, different chart type — kept as reference alongside final (41). |
| 4 | 02_Sensor_Voltage_Time | 2 | Voltage-time trace, z=2,r=0; final. |
| 5 | 02_Sensor_Voltage_Time | 9 (ref.) | Velocity-RPM overlay; same data as 3 & 41 — kept as reference. |
| 6 | 02_Sensor_Voltage_Time | 3 | Voltage-time trace, z=2,r=1; final. |
| 7 | 02_Sensor_Voltage_Time | 5 (ref.) | Per-position voltage-time subplot grid; same `voltage_data` as 8. |
| 8 | 02_Sensor_Voltage_Time | 4 | Voltage-time overlay, all positions; clearest combined view of same data as 7. |
| 9 | 09_Experiments | 1 | 20 kHz sweep plot; **superseded by Cell 12** (identical logic + added ticks/aesthetics). Merge note: 9→12. |
| 10 | 03_Duty_Cycle_Sweep | 2 | 20 kHz averaged up/down table; unique analysis, no duplicate. |
| 11 | 09_Experiments | 2 | 25 kHz sweep plot; **superseded by Cell 13**. Merge note: 11→13. |
| 12 | 03_Duty_Cycle_Sweep | 1 | 20 kHz sweep with ticks/aesthetics; final version (supersedes 9). |
| 13 | 03_Duty_Cycle_Sweep | 3 | 25 kHz sweep with ticks/aesthetics; final version (supersedes 11). |
| 14 | 09_Experiments | 4 | Linear `interp1d` voltage→duty; earliest attempt, superseded by later fits. |
| 15 | 09_Experiments | 5 | First-pass averaged voltage-duty plot; **superseded by Cell 18** (does the same plus more). |
| 16 | 09_Experiments | 6 | Grouping/sorting step, continuation of 15; superseded by 18. |
| 17 | 09_Experiments | 7 | Plot half of the 16/17 pair; superseded by 18. |
| 18 | 05_Voltage_to_Duty | 1 | Combined, final version of 15+16+17 (adds array extraction & printing). |
| 19 | 05_Voltage_to_Duty | 2 | 3rd-degree polynomial fit; distinct candidate model, not a duplicate. |
| 20 | 09_Experiments | 8 | Second linear-interpolation attempt (sorted); duplicate of approach in 14. |
| 21 | 09_Experiments | 9 | Exponential+spline fit setup (function def); alternative not carried forward. |
| 22 | 09_Experiments | 10 | Exponential+spline fit, continuation of 21. |
| 23 | 09_Experiments | 11 | Exponential fit, cell 1 of a 3-cell split (data). |
| 24 | 09_Experiments | 12 | Exponential fit, cell 2 of 3 (curve_fit call). |
| 25 | 09_Experiments | 13 | Exponential fit, cell 3 of 3 (plot); whole 23-24-25 sequence superseded by tuned fit in 26/27. |
| 26 | 09_Experiments | 14 | Untuned exponential fit; **superseded by Cell 27** (adds RMSE/R²). |
| 27 | 05_Voltage_to_Duty | 4 | Tuned exponential fit + error metrics; the chosen production model. |
| 28 | 05_Voltage_to_Duty | 3 | Raw (unaveraged) scatter diagnostic; informs the modelling decision, kept as diagnostic. |
| 29 | 09_Experiments | 15 | Piecewise (2-region) exponential fit; alternative approach not used downstream. |
| 30 | 09_Experiments | 16 | Apply fixed exponential coefficients, error table (unaveraged pipeline). Superseded by Cell 34. |
| 31 | 09_Experiments | 17 | Same as 30 + CSV export; still superseded by Cell 34's cleaner averaged-data approach. |
| 32 | 09_Experiments | 18 | Reload CSV from 31, recompute metrics; part of the superseded pipeline. |
| 33 | 09_Experiments | 19 | Continuation of 32 — error/percentage-error plots; superseded pipeline. |
| 34 | 05_Voltage_to_Duty | 5 | Re-averaged-data error pipeline; final production version, saves `error_analysis_avg_voltage.csv` used by 36/39. |
| 35 | 09_Experiments | 20 | Refit exp/poly/log models (trimmed range); **superseded by Cell 36** (adds metrics + CSV export). |
| 36 | 05_Voltage_to_Duty | 6 | Final refit of 3 candidate models on the working voltage range, with full metrics. |
| 37 | 09_Experiments | 21 | Synthetic voltage-profile generation (visual only, no duty conversion); precursor to Cell 40. |
| 38 | 09_Experiments | 22 | Compare 2 fixed exponential models; **superseded by Cell 39** (nicer side-by-side format). |
| 39 | 05_Voltage_to_Duty | 7 | Final model-comparison table (Model A vs. Model B). |
| 40 | 05_Voltage_to_Duty | 8 | Applies chosen model to synthetic voltage profiles; final validation/application step. |
| 41 | 02_Sensor_Voltage_Time | 6 | Velocity-RPM split by axial/radial; clearest final view of the `velocity_data` also used in 3 & 5. |
| 42 | 01_Data_Preprocessing | 2 | Colab upload utility, used before fan-log parsing. |
| 43 | 09_Experiments | 23 | Fan-log parsing, basic averaging only; superseded by 44→45→46 chain. |
| 44 | 09_Experiments | 24 | Fan-log parsing + ramp detection; superseded by 45→46. |
| 45 | 09_Experiments | 25 | Fan-log parsing + filtering + styling; superseded by 46 (adds linear fit). |
| 46 | 04_Fan_Log_Calibration | 1 | Final cumulative version: parse + filter + ramp-split + linear fit. |
| 47 | 08_Project_Planning | 1 | Gantt-style work plan; administrative, not scientific analysis. |
| 48 | 06_Duty_RPM_Trials | 1 | Simple pre-averaged reference curve; kept as an early/quick-reference trial. |
| 49 | 06_Duty_RPM_Trials | 2 | Distinct 10-sample trial (stabilised last-5 mean); no duplicate exists. |
| 50 | 06_Duty_RPM_Trials | 3 | Distinct 10-sample "3rd set" trial with std error bars; no duplicate exists. |
| 51 | 06_Duty_RPM_Trials | 4 | Hand-computed mean/std summary of a run; distinct from raw-sample trials. |
| 52 | 09_Experiments | 26 | 60-sample trial; **identical raw data to Cells 54/55** — duplicate analysis, kept for reference only. |
| 53 | 09_Experiments | 27 | Same 60-sample dataset as 52/54/55 with a 3-panel breakdown; duplicate, kept for reference only. |
| 54 | 06_Duty_RPM_Trials | 5a | 60-sample trial data definition; cleanest split of data vs. processing among the 52/53/54/55 group — kept as the canonical version. |
| 55 | 06_Duty_RPM_Trials | 5b | Processing + plot for Cell 54's data; pairs with 54. |
| 56 | 06_Duty_RPM_Trials | 6 | Separate 60-sample trial (different raw values from 52-55) — genuinely distinct session, kept. |
| 57 | 07_Correlation_Analysis | 1 | Pearson correlation helper function; utility, final. |
| 58 | 07_Correlation_Analysis | 2 | Dataset definitions used by the correlation analysis. |
| 59 | 07_Correlation_Analysis | 3 | Runs all correlation analyses using 57 + 58. |

**Explicit merges (near-duplicate → kept version):**
- Cell 9 → Cell 12 (20 kHz sweep plot, ticks added)
- Cell 11 → Cell 13 (25 kHz sweep plot, ticks added)
- Cells 15, 16, 17 → Cell 18 (averaged voltage-duty plot, combined + extended)
- Cell 26 → Cell 27 (exponential fit, metrics added)
- Cells 30–33 → Cell 34 (error pipeline, re-averaged data, cleaner)
- Cell 35 → Cell 36 (refit, metrics + export added)
- Cell 38 → Cell 39 (model comparison, formatting improved)
- Cells 43–45 → Cell 46 (fan-log parsing, cumulative)
- Cells 52, 53 → Cells 54+55 (identical raw dataset, cleanest split kept)

---

## Maintainability Recommendations (separate from restructuring)

These are **suggestions for future refactoring**, not applied to the notebooks above, since the brief was to reorganise rather than rewrite:

1. **Extract a `voltage_duty_data.py` / `velocity_data.py` module.** The `velocity_data` dict (cells 3, 5, 41) and `voltage_data` dict (cells 7, 8) are each hardcoded three/two times. Moving them to a shared module (or a small CSV) would remove ~150 lines of duplication and guarantee all plots use identical numbers.

2. **Extract a `load_averaged_duty_voltage(path, sheet)` helper.** The "load Excel → strip columns → dropna → groupby(Duty).mean()" pattern appears near-verbatim in cells 15/16/17/18/28/30/31/34. A single helper (returning a tidy DataFrame) would remove most of notebook 05's remaining duplication.

3. **Extract a `fit_and_score(model_fn, V, D)` helper.** Every candidate-model cell (19, 26/27, 35/36, 38/39) repeats the same `curve_fit` → RMSE/MAE/R² → print block. A shared function taking a model callable and returning a metrics dict would let candidate models be compared in a loop instead of copy-pasted cells.

4. **Extract a `summarize_duty_rpm_trial(raw_samples_dict)` helper for notebook 06.** The raw→mean(±std)→linear-fit pattern is repeated 6 times (cells 49–56) with only the raw data changing. A shared function would turn each trial into a 2-line call plus its unique dataset.

5. **Centralise file paths.** Several cells hardcode `/content/...` Colab paths or bare filenames (`"z=2,r=0.xlsx"`, `"fan_log.csv"`). A small `config.py` (or notebook-top `DATA_DIR` variable) would make the notebooks portable outside Colab.

6. **Consider dropping (or clearly archiving) the true near-duplicates in `09_Experiments`** once the supervisor/team confirms nothing in them is still needed — cells 9, 11, 15–17, 26, 30–33, 35, 38, 43–45, 52, 53 contribute no result not already captured by their "final" counterparts.
