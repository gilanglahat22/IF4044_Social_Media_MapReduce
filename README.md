# Social Media MapReduce Analytics

This project implements a MapReduce framework to analyze social media data from multiple platforms. It processes JSON data from different social media sources, extracts relevant information, and performs aggregation to analyze posting patterns and user engagement across platforms.

## Project Overview

The project aims to:
1. Convert JSON data from various social media platforms into a standardized format
2. Implement a MapReduce framework to process large volumes of social media data
3. Extract posting dates and engagement metrics from different platforms
4. Aggregate and analyze the data to identify usage patterns

## Project Structure

```
IF4044_Social_Media_MapReduce/
├── docs/                           # Documentation
│   └── TUGAS 1_ MapReduce Social Media_13520137.pdf
│
├── src/                            # Source code
│   ├── convert_json_to_txt.py      # Utility to convert JSON to text format
│   ├── socmed_mapper.py            # Mapper implementation for MapReduce
│   ├── socmed_reducer.py           # Reducer implementation for MapReduce
│   ├── test_json_to_txt.ipynb      # Notebook for testing JSON conversion
│   ├── mapper_exec.ipynb           # Notebook for executing mapper operations
│   ├── test_reducer.ipynb          # Notebook for testing reducer operations
│   └── test_mapreduce.ipynb        # Complete MapReduce workflow testing
│
├── raw_json/                       # Raw JSON data from social media platforms (not included in repo)
│
└── README.md                       # Project documentation
```

## Data Processing Pipeline

1. **Data Collection**: 
   - JSON data is collected from various social media platforms (Facebook, Instagram, Twitter, YouTube)
   - Additional data from other sources is also processed (anaktester_go, byu.id, gridoto_news, myxl, telkomsel)

2. **Data Preprocessing**:
   - The `convert_json_to_txt.py` module converts JSON files to a line-by-line text format
   - Each line contains a JSON object for efficient processing in the MapReduce framework

3. **MapReduce Implementation**:
   - **Mapper Phase** (`socmed_mapper.py`):
     - Parses each line of input data
     - Extracts the social media platform, posting date, and sets a count of 1
     - Outputs key-value pairs in the format: `<platform>\t<date>\t<count>`
   
   - **Reducer Phase** (`socmed_reducer.py`):
     - Processes the output from the mapper
     - Directly writes the data to a CSV file with headers: social_media, date, count
     - This output can then be used for further analysis or visualization

## Implementation Details

### JSON to Text Conversion

The `convert_json_to_txt.py` module:
- Takes a target filename and search pattern as inputs
- Searches for JSON files matching the pattern in the `raw_json` directory
- Converts each JSON file to a text file with one JSON object per line

### Mapper Implementation

The mapper processes input data based on the social media platform:
- **Facebook**: Extracts created_time from posts and comments
- **Instagram**: Converts UNIX timestamps to readable dates
- **Twitter**: Parses Twitter's specific date format
- **YouTube**: Extracts publishedAt dates from video metadata
- **Other Sources**: Extracts timestamps and comment data when available

### Reducer Implementation

The reducer:
- Defines CSV headers (social_media, date, count)
- Creates a CSV writer for the output
- Processes each line from the mapper and writes it to the output CSV

## Usage Instructions

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Required Python packages: json, csv, sys, datetime

### Running the Pipeline

1. **Convert JSON files to text format**:
   ```python
   from convert_json_to_txt import convert_json_to_txt
   convert_json_to_txt("facebook", "facebook_post")
   ```

2. **Execute the mapper**:
   - Use the Jupyter notebooks in the `src` directory to run the mapper for specific platforms
   - Each notebook contains code to process data from different social media sources

3. **Execute the reducer**:
   - The reducer can be run to process the mapper's output and create a CSV file
   - The CSV file will contain aggregated data for further analysis

4. **Complete MapReduce workflow**:
   - The `test_mapreduce.ipynb` notebook demonstrates the complete workflow from data loading to final output

## Future Enhancements

Potential improvements for this project include:
- Implementing a more sophisticated reducer to aggregate counts by platform and date
- Adding visualizations for the output data
- Extending the framework to process more metadata from social media posts
- Implementing a streaming version for real-time social media analysis