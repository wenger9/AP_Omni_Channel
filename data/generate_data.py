import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the basic structure of your dataset
data = {
    'ICS Segment': [],
    'Average Purchase Value': [],
    'Purchase Frequency': [],
    'Preferred Purchase Channel': [],
    'Peak Purchase Time': [],
    'Stickiness': [],
    'Date': []
}

# Define your ICS segments
segments = ['A', 'B', 'C']

# Sample data generation
start_date = datetime.now()
num_days = 30  # Number of days for time-series data

for segment in segments:
    for day in range(num_days):
        data['ICS Segment'].append(segment)
        data['Average Purchase Value'].append(np.random.uniform(50, 200))  # Random values
        data['Purchase Frequency'].append(np.random.randint(1, 10))  # Random values
        data['Preferred Purchase Channel'].append(np.random.choice(['Online', 'In-store', 'Mobile App']))
        data['Peak Purchase Time'].append(np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night']))
        data['Stickiness'].append(np.random.uniform(0.1, 1.0))  # Random values
        data['Date'].append(start_date + timedelta(days=day))

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('ics_segments_data.csv', index=False)
