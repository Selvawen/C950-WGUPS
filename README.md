# WGUPS Package Delivery Optimization

This project implements an efficient package delivery system for WGUPS, designed to optimize routes and ensure all 40 packages are delivered on time while meeting specific criteria. The solution keeps the combined total distance traveled by all trucks under 140 miles and provides real-time tracking for package delivery progress.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Screenshots](#screenshots)
- [License](#license)

---

## Overview

The WGUPS Package Delivery Optimization program:
- Routes packages using an efficient algorithm to minimize total travel distance.
- Ensures all delivery requirements are met, including deadlines and package-specific constraints.
- Tracks and displays the progress of deliveries in real-time based on package variables (e.g., delivery time, location, and status).

The solution is scalable for use in other cities where WGU operates, beyond the initial Salt Lake City deployment.

---

## Features

- **Optimized Routing**: Uses a custom algorithm to minimize total delivery distance while meeting constraints.
- **Real-Time Tracking**: Displays package delivery progress, including timestamps and status updates.
- **Scalable Design**: Easily adaptable for other cities with minimal adjustments.
- **Detailed Comments**: Code is extensively commented for clarity and maintainability.

---

## How It Works

1. **Input Data**:
   - Package details from the `WGUPS Package File`.
   - Delivery distances from the `WGUPS Distance Table`.
   - Locations from the `Salt Lake City Downtown Map`.

2. **Optimization**:
   - Calculates the most efficient routes for three trucks, each with specific constraints.
   - Ensures all deadlines are met while keeping the total distance traveled under 140 miles.

3. **Tracking**:
   - Tracks each truck’s progress, including current location, delivered packages, and remaining deliveries.

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/wgups-delivery-optimization.git
   cd wgups-delivery-optimization
    ```
2. Add the required data files:
   - **WGUPS Package File**: Contains package details and delivery requirements.
   - **WGUPS Distance Table**: Provides distances between delivery locations.
   - **Salt Lake City Downtown Map**: Shows the locations used for routing.

   Place these files in the appropriate directory as specified in the project documentation.

3. Run the program:
   ```bash
   python main.py
   ```
4. View delivery progress and results in the terminal or output logs:
   - The program outputs detailed progress for each truck, including packages delivered, delivery times, and remaining packages.
   - Logs can also be saved for later review or debugging purposes.

---

## Dependencies

This project requires the following libraries:
- `numpy`
- `pandas`
- `matplotlib` (for visualizing delivery routes, optional)

Install them via the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a detailed explanation of your changes.

---

## Screenshots
![E](https://github.com/user-attachments/assets/f7ec4b77-a68e-420e-a625-01d613270e3b)
![D1](https://github.com/user-attachments/assets/f7cac5e9-3c48-4ffc-9689-fb4f693d6258)
![D2](https://github.com/user-attachments/assets/d139e1ab-78b0-4572-8833-9241489470ed)
![D3](https://github.com/user-attachments/assets/378eef3b-b287-40aa-8e8e-dc0d577da1a4)

---

## License

MIT License

Copyright (c) 2024 Benjamin Anderson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
