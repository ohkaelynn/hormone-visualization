

# Hormonal Health Tracker

The **Hormonal Health Tracker** is a tool to track and visualize hormone levels over time. It helps you:

- Track hormone changes over time.
- Visualize trends in hormone levels with interactive plots.
- Monitor changes in hormones using emojis to represent increases, decreases, or stability.
- View a responsive, user-friendly table that displays reference ranges, the latest hormone results, and their changes.

## Features

- **Interactive Plots**: Visualize hormone levels over time for any individual hormone or a selection of hormones.
- **Change Tracking**: Track changes in hormone levels from one measurement to the next, displayed using emojis (e.g., 📈 for increases, 📉 for decreases, ➡️ for no change).
- **Reference Table**: See a comprehensive table with the latest hormone results compared to reference ranges (e.g., Cis Female, Cis Male).
- **Easy to Use**: The application is designed to be user-friendly, making hormone tracking simple and intuitive.

## How it Works

1. **Upload Your Data**: Provide your hormone level measurements in a CSV format.
2. **Track Trends**: The app will process your data, displaying trends and changes over time with visual aids.
3. **View Results**: The application will show the current values of hormones, compare them against reference ranges, and indicate the status of each hormone with emojis representing increases, decreases, or neutral changes.

## CSV Format

To use the tracker, your data should be in the following format:

```
Date,Hormone,Value
2025-01-01,Estradiol,120.5
2025-01-01,Testosterone,1.2
2025-01-01,Progesterone,2.5
2025-02-01,Estradiol,125.3
2025-02-01,Testosterone,1.3
```

- **Date**: The date of the hormone measurement.
- **Hormone**: The name of the hormone (e.g., Estradiol, Testosterone).
- **Value**: The numerical value of the hormone level at that point in time.

## Getting Started

To run the Hormonal Health Tracker locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hormonal-health-tracker.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run hht.py
   ```

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and handling hormone data.
- **Matplotlib**: For creating interactive plots to visualize hormone trends.

## Disclaimer

This tool is intended for visualization purposes only. It is not scientifically or medically accurate and should not be used as a substitute for professional advice. The content is generated mostly with the help of AI and is designed to track hormone levels over time for personal use, but should not be relied upon for health decisions.

