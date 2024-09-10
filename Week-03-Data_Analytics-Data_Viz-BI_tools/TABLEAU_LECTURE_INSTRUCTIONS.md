# Dashboard Instructions

### Create new vis

### Upload listings.csv from computer (drag and drop into the “Data Source”  tab. 

### Create a New Worksheet.  Rename tab “Map of Listings, Colored by Borough”

0. Convert Latitude and Longitude to Dimension quantities
0. Select both Latitude and Longitude.
0. Click “Show Me” - Symbol Map (if necessary)
0. Drag **Price** to the filter pane.
    * Select "All Values" if prompted.
    * Right click and select, "Show Filter"
    * Right click and apply to all sheets using this data. 

0. Drag Neighborhood Group to the Color box in the Marks pane

0. In the Filters pane, Right Click on Price and set “Apply to Worksheets” -> “All Using this Data Source”
0. You can adjust size with the “Size” under “Marks”
    * Adjust the Size to be smaller.
    * Adjust color to be less opaque 

### Create a New Worksheet.  Rename tab “Price Histogram By Borough”
0. Right click on **Price** (in Data).  “Create“ -> “bins
0. Set “Size of Bins” to 30
0. Drag “Price (Bins)” to columns
0. Drag “listings.csv (Count)” into the table
0. Drag “Neighborhood Group” into “Color”  under “Marks”
0. Click “Show Me”  and the Vertical bars
0. Drag “Neighborhood Group”  into columns


### Create a New Worksheet.  Rename tab “Box and Whisker”
0. Drag Neighborhood group to ‘Columns’ and ‘Color’ (under ‘Marks’)
0. Drag ‘listings.csv (Count)’ to ‘Detail’  under marks
0. Drag ‘Neighborhood Group’ to ‘Columns’
0. Drag **Price** to Rows
0. Under analysis, turn off “Aggregate Measures”
0. Click on show me and select the box and whisker plot. 
0. Right click on the left axis and set scale to “Logarithmic”


### Create a new Dashboard
0. Add your widgets.  The key and the price slider should appear when you add the map
