**LUXURY HOUSING ANALYSIS- BENGALURU**

**Project Overview**

The Luxury Housing Analysis – Bengaluru project focuses on analyzing premium residential properties in Bengaluru using SQL and Power BI. The main objective of this project is to understand pricing trends, location-based luxury hotspots, developer performance, and market segmentation in the luxury housing sector.

This project helps identify high-value investment areas and provides business insights through interactive dashboards and data visualization.

**Objectives**

Analyze luxury housing trends in Bengaluru
Study price per square foot across premium locations
Identify top-performing developers
Understand luxury property distribution by location
Create interactive Power BI dashboards for decision-making
Tools and Technologies Used
SQL (MySQL) – Backend database and query processing
Power BI – Dashboard creation and data visualization
Power Query – Data cleaning and transformation
DAX – Calculated measures and KPIs
GitHub – Project version control and repository management
Dataset Details

**The dataset contains the following fields:**

Property ID
Location
Total Sqft
Price
Price per Sqft
BHK
Property Type
Builder Name
Locality Infrastructure Score

**Key Visualization:**

1. Average Price by Developer
✅ Best Visual: Clustered Bar Chart
Axis: developer_name
Values: Average of price

🎯 Insight: Compare average selling price across developers

2. Price vs Unit Size
✅ Best Visual: Scatter Plot
X-axis: unit_size
Y-axis: price
Legend: developer_name

🎯 Insight: Understand pricing trend based on property size

3. Top Developers
✅ Best Visual: Horizontal Bar Chart
Axis: developer_name
Values: Count of properties/projects

🎯 Insight: Identify most active developers

4. Price Distribution by Developer
✅ Best Visual: Box Plot (Best)
Alternative: Column Chart
Category: developer_name
Values: price

🎯 Insight: Detect premium developers + price variation

5. Sales Channel Distribution
✅ Best Visual: Donut Chart
Legend: sales_channel
Values: Count of properties

🎯 Insight: Understand contribution of each sales channel

6. Average Unit Size by Developer
✅ Best Visual: Column Chart
Axis: developer_name
Values: Average of unit_size

🎯 Insight: Compare unit size preferences by developers

7. Developer-wise Average Price
✅ Best Visual: Treemap
Alternative: Bar Chart
Group: developer_name
Values: Average of price

🎯 Insight: Shows pricing dominance visually

8. Sales Channel Performance
✅ Best Visual: Stacked Bar Chart
Axis: sales_channel
Values: Total sales / Average price

🎯 Insight: Compare effectiveness of sales channels

9. Premium Property Trend
✅ Best Visual: Line Chart
Axis: listed_date / month / year
Values: Average of premium property price

🎯 Insight: Track luxury market growth over time

10. Developer Performance
✅ Best Visual: Clustered Bar Chart ⭐ (Best)
Axis: developer_name
Values: Average of locality_infra_score

🎯 Insight: Rank developers based on locality quality

**SQL Backend Features**

Data storage and management using MySQL
Price per sqft calculation
Luxury category segmentation
Developer performance analysis
Location-wise pricing aggregation
Business intelligence support for Power BI dashboards
Business Insights
Whitefield, Indiranagar, and Koramangala are major luxury hotspots
Price per sqft is significantly higher in premium IT corridor regions
Some compact luxury properties have higher value than larger homes
Developer reputation strongly influences pricing trends
Infrastructure score impacts buyer preference and pricing

**Conclusion**

This project provides a complete business intelligence solution for analyzing luxury housing trends in Bengaluru. Using SQL and Power BI together helps transform raw real estate data into meaningful insights for better investment and business decisions.

Future Enhancements
Real-time property data integration
Machine learning-based price prediction
Investment recommendation engine
Expansion to multi-city luxury housing analysis
