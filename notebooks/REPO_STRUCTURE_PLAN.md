
## Maintainability Recommendations (separate from restructuring)

These are **suggestions for future refactoring**, not applied to the notebooks above, since the brief was to reorganise rather than rewrite:

1. **Extract a `voltage_duty_data.py` / `velocity_data.py` module.** The `velocity_data` dict (cells 3, 5, 41) and `voltage_data` dict (cells 7, 8) are each hardcoded three/two times. Moving them to a shared module (or a small CSV) would remove ~150 lines of duplication and guarantee all plots use identical numbers.

2. **Extract a `load_averaged_duty_voltage(path, sheet)` helper.** The "load Excel → strip columns → dropna → groupby(Duty).mean()" pattern appears near-verbatim in cells 15/16/17/18/28/30/31/34. A single helper (returning a tidy DataFrame) would remove most of notebook 05's remaining duplication.

3. **Extract a `fit_and_score(model_fn, V, D)` helper.** Every candidate-model cell (19, 26/27, 35/36, 38/39) repeats the same `curve_fit` → RMSE/MAE/R² → print block. A shared function taking a model callable and returning a metrics dict would let candidate models be compared in a loop instead of copy-pasted cells.

4. **Extract a `summarize_duty_rpm_trial(raw_samples_dict)` helper for notebook 06.** The raw→mean(±std)→linear-fit pattern is repeated 6 times (cells 49–56) with only the raw data changing. A shared function would turn each trial into a 2-line call plus its unique dataset.

5. **Centralise file paths.** Several cells hardcode `/content/...` Colab paths or bare filenames (`"z=2,r=0.xlsx"`, `"fan_log.csv"`). A small `config.py` (or notebook-top `DATA_DIR` variable) would make the notebooks portable outside Colab.

6. **Consider dropping (or clearly archiving) the true near-duplicates in `09_Experiments`** once the supervisor/team confirms nothing in them is still needed — cells 9, 11, 15–17, 26, 30–33, 35, 38, 43–45, 52, 53 contribute no result not already captured by their "final" counterparts.
