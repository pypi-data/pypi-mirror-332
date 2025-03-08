# macro-gridder

A Python library for real-time macro grid calculation for stock daily and tick-level data.

[中文文档](docs/README_zh.md) | [English Documentation](docs/README_en.md)

## Overview

macro-gridder is a specialized library designed to transform price data into grid-based representations, supporting both macro grids and micro units. It's particularly useful for technical analysis, algorithmic trading, and visualization of price movements in financial markets.

## Features

- Support for both daily and tick-level data
- Real-time grid calculation for streaming data
- Efficient data structures for high-frequency updates
- Visualization tools for grid-based analysis
- Compatible with various data sources

## Installation

```bash
pip install macro-gridder
```

## Quick Start

```python
import pandas as pd
from macro_gridder import MacroGridder

# Load your price data
data = pd.read_csv('stock_data.csv')
prices = data['close']
times = data.index

# Configure the grid
config = {
    'horizontal_step': 10,  # Time dimension grid step
    'vertical_step': 20,    # Price dimension grid step
    'min_price_tick': 0.01  # Minimum price tick
}

# Create a grid
gridder = MacroGridder(config)
grid_df = gridder.create_grid(times, prices)

# Analyze grid data
print(grid_df.head())
```

## Real-time Processing

```python
from macro_gridder import RealtimeMacroGridder

# Initialize with historical data
gridder = RealtimeMacroGridder(config)
gridder.initialize_with_history(history_times, history_prices)

# Process new tick data
for time, price in new_data:
    h_idx, v_idx = gridder.update_with_tick(time, price)
    grid_info = gridder.get_current_macro_grid()
    # Use grid_info for trading decisions
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
