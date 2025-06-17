# RoboCup2025 Trajectory Prediction Challenge

## License and Collaboration Instructions

This project is distributed under the GNU General Public License (GNU GPL), adapted for **non-commercial** use, for **educational** and **research** purposes only.  
**Commercial use is not allowed.**

### Authors
- André Gualberto
- Ilson Gualberto
- Guilherme Gualberto

### How to collaborate

1. Fork this repository.
2. Create a branch for your contribution.
3. Submit a pull request describing your proposed changes.
4. Respect the license and cite the original authors in derivative works.

---

## GNU General Public License v3.0 Adapted

Copyright (C) 2025  
André Gualberto, Ilsin Gualberto, Guilherme Gualberto

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License.

**Additional restrictions:**  
- This software is permitted for educational and research purposes only.  
- Any direct or indirect commercial use is strictly prohibited.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  
If not, see <https://www.gnu.org/licenses/>.

---

## How to Use

### Requirements

Install the required libraries with:

```bash
pip install -r requirements.txt
```

### Directory Structure

```
.
├── tools/
│   ├── create_stp_test_data.py
│   ├── evaluation-rc2025.py
│   └── validate_submission.py
├── notebooks/
│   └── analysis.ipynb
├── models/
│   ├── predictor.py
│   └── utils.py
├── results/
│   └── evaluation_log.txt
├── data/
│   └── full-matches/
│       └── README.txt
├── requirements.txt
├── README.md
```

### Usage

#### 1. Generate Test Data

Extract test data (e.g., last 30 frames before a goal event):

```bash
python tools/create_stp_test_data.py <input_dir> <output_dir>
```

#### 2. Validate Submission

Check if your submission files are in the correct format:

```bash
python tools/validate_submission.py --input <test_data_dir> --submit <submission_dir>
```

#### 3. Evaluate Prediction

Compare your predictions with the ground truth:

```bash
python tools/evaluation-rc2025.py --gt <ground_truth_dir> --submit <submission_dir>
```

### Model

- The prediction logic is implemented in `models/predictor.py` and `models/utils.py`.
- The model uses polar coordinates and a simple kinematic model with optional interception logic ("Iron Dome").

### Notebooks

- Use `notebooks/analysis.ipynb` for data visualization and debugging.

---

## Contact

For questions or suggestions, please open an issue or contact the authors.