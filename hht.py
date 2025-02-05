import streamlit as st
import pandas as pd
import plotly.express as px

# Set wide layout
st.set_page_config(layout="wide")

# Load your data
data = pd.read_csv('bloods.csv')

# GLRR reference ranges for the hormones, including units
reference_ranges = {
    'Estradiol': {
        'Cis Male': ('41.4 - 159.0', 'pmol/L'),
        'Cis Female': ('41.4 - 159.0', 'pmol/L')
    },
    'Testosterone': {
        'Cis Male': ('8.64 - 29.0', 'nmol/L'),
        'Cis Female': ('0.7 - 2.0', 'nmol/L')
    },
    'Progesterone': {
        'Cis Male': ('< 1.0', 'nmol/L'),
        'Cis Female': ('Follicular: 0.3 - 2.0, Luteal: 5.0 - 20.0', 'nmol/L')
    },
    'Prolactin': {
        'Cis Male': ('86 - 324', 'mIU/L'),
        'Cis Female': ('86 - 324', 'mIU/L')
    },
    'FSH': {
        'Cis Male': ('1.5 - 12.4', 'IU/L'),
        'Cis Female': ('Follicular: 3.5 - 12.5, Luteal: 1.7 - 7.7', 'IU/L')
    },
    'LH': {
        'Cis Male': ('1.7 - 8.6', 'IU/L'),
        'Cis Female': ('Follicular: 2.0 - 10.0, Luteal: 0.5 - 14.0', 'IU/L')
    },
    'SHBG': {
        'Cis Male': ('18.3 - 54.1', 'nmol/L'),
        'Cis Female': ('18.3 - 54.1', 'nmol/L')
    },
    'FAI': {
        'Cis Male': ('35.0 - 92.6', '%'),
        'Cis Female': ('35.0 - 92.6', '%')
    }
}

# Title
st.title("Hormonal Health Tracker")

# Create the first chart: All hormones displayed in one graph
fig1 = px.line(data, x='Date', y='Value', color='Hormone', title='All Hormones Over Time')

# Customizing the first chart for better visibility (adding markers)
fig1.update_traces(
    mode='lines+markers',  # Adding markers to the lines
    marker=dict(
        size=6,  # Smaller marker size
        line=dict(width=2, color='black')  # Adding a border to markers for visibility
    ),
    hoverinfo='x+y+name',  # Displaying both the date (x) and value (y) when hovering
)

# Show the plot
st.plotly_chart(fig1)

# Latest Results table creation (adding changes and emojis)
# Get the latest results (most recent for each hormone)
latest_results = data.sort_values('Date').drop_duplicates('Hormone', keep='last')

# Define the function to get the change emoji
def get_change_emoji(hormone, current_value):
    # Find the previous value for comparison
    previous_value = data[data['Hormone'] == hormone].sort_values('Date').iloc[-2:]['Value'].values
    if len(previous_value) > 0:
        previous_value = previous_value[0]
        if current_value > previous_value:
            return "🔼"  # Increase
        elif current_value < previous_value:
            return "🔽"  # Decrease
        else:
            return "↔️"  # No change
    return "↔️"  # Default to no change if no previous value

# Merge the latest results with reference ranges
latest_results_with_references = pd.DataFrame(latest_results)
latest_results_with_references['Cis Female Range'] = latest_results_with_references['Hormone'].map(
    lambda hormone: reference_ranges[hormone]['Cis Female'][0] if hormone in reference_ranges else "N/A"
)
latest_results_with_references['Cis Male Range'] = latest_results_with_references['Hormone'].map(
    lambda hormone: reference_ranges[hormone]['Cis Male'][0] if hormone in reference_ranges else "N/A"
)

# Add emoji for change
latest_results_with_references['Change Emoji'] = latest_results_with_references.apply(
    lambda row: get_change_emoji(row['Hormone'], row['Value']), axis=1
)

# Select the columns to display in the final table with new headers
final_table = latest_results_with_references[['Hormone', 'Cis Female Range', 'Cis Male Range', 'Value', 'Change Emoji']]
final_table = final_table.rename(columns={'Value': 'Latest Result', 'Change Emoji': 'Change'})

# Display the dataframe (latest results with reference ranges and change)
st.write("### Latest Results with Reference Ranges and Change")
st.dataframe(final_table, use_container_width=True)

# Interactive Dropdown for selecting a hormone for the second chart
st.write("### Select a Hormone to View Over Time")
selected_hormone = st.selectbox("Choose a Hormone", data['Hormone'].unique())

# Create the second chart: Only the selected hormone
fig2 = px.line(data[data['Hormone'] == selected_hormone], x='Date', y='Value', 
               title=f"{selected_hormone} Levels Over Time", 
               labels={"Value": f"{selected_hormone} Levels"})

# Adding unit to the selected hormone's Y-axis
if selected_hormone in reference_ranges:
    # Safely retrieving the unit from the reference range
    unit = reference_ranges[selected_hormone].get('Cis Female', ('', ''))[1]  # Default to empty if not found
    fig2.update_layout(
        yaxis_title=f"{selected_hormone} Levels ({unit})",
        xaxis_title="Date",
        hovermode='x unified',  # Unified hovermode for clarity
    )
    
    # Update marker and line properties for better visibility
    fig2.update_traces(
        mode='lines+markers',  # Adding markers to the lines
        marker=dict(
            size=6,  # Smaller marker size
            color='rgb(31, 119, 180)',  # Marker color matching the line color
            symbol='circle', 
            opacity=0.8,  # Slight opacity for smoothness
            line=dict(width=2, color='black')  # Adding a border to markers for visibility
        ),
        line=dict(
            width=3,  # Set line width
            color='rgb(31, 119, 180)'  # Line color matching marker color
        ),
        hoverinfo='x+y+name'  # Displaying both the date (x) and value (y) when hovering
    )

# Show the second plot
st.plotly_chart(fig2)
