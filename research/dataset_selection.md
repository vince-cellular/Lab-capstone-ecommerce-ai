# Public Dataset Selection

## Objective

Identify and evaluate public datasets that could support the proposed AI-Powered E-commerce Revenue Optimization Advisor.

The selected dataset must provide sufficient information to support the Round 1 dashboard and the initial AI use-case analysis.

## Evaluation Criteria

Candidate datasets will be evaluated according to:

1. Customer journey data
2. Marketing / acquisition data
3. Cart and purchase behaviour
4. Product data
5. Revenue / transaction data
6. Data quality and completeness
7. Suitability for Power BI
8. Suitability for an n8n proof of concept
9. Potential for a Round 2 MVP
10. Public accessibility and documentation

## Candidate Datasets

| Dataset | Source | Customer Journey | Marketing | Cart / Purchase | Products | Revenue | Power BI | POC | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Google Analytics 4 E-commerce Sample | Google BigQuery Public Dataset | Strong | Potentially strong | Strong potential | Yes | Yes | Yes | Strong potential | Requires schema inspection; data is obfuscated |
| UCI Online Retail | UCI Machine Learning Repository | Limited | No direct marketing data | Purchase data available | Yes | Yes | Yes | Moderate | Strong transactional dataset |
| UCI Online Retail II | UCI Machine Learning Repository | Limited | No direct marketing data | Purchase/cancellation data | Yes | Yes | Yes | Moderate | Larger dataset with two years of transactions |
| UCI Online Shoppers Purchasing Intention | UCI Machine Learning Repository | Strong | Traffic type available; no ad spend | Strong purchase / non-purchase signal | No detailed product data | Revenue outcome available | Yes | Strong potential | 12,330 sessions; 17 features; no missing values; particularly strong for conversion analysis |
## Dataset Comparison

### Current Assessment

The Google Analytics 4 E-commerce Sample is currently the strongest candidate because it appears to provide a richer view of the e-commerce customer journey, including traffic sources, user behaviour, e-commerce interactions, and transactions.

However, the dataset has not yet been selected.

Before making the final selection, the dataset schema must be inspected to verify the availability of the specific variables required for:

- customer journey analysis
- conversion analysis
- revenue analysis
- marketing performance analysis
- cart abandonment analysis

In particular, the availability of advertising spend / cost data must be verified before making any claims about wasted marketing expenditure or return on advertising spend (ROAS).

The UCI Online Retail and Online Retail II datasets are strong backup candidates for transactional, product, customer, and revenue analysis but provide less direct information about the full digital customer journey and acquisition channels.

## Quick Data Inspection

The UCI Online Shoppers Purchasing Intention dataset was downloaded and inspected locally before making the final dataset selection.

### Dataset dimensions

- Rows: 12,330
- Columns: 18
- Predictive features: 17
- Target variable: `Revenue`

### Data types

The dataset contains:

- Integer variables for page counts and coded categorical variables
- Floating-point variables for durations and rates
- Categorical variables: `Month`, `VisitorType`
- Boolean variables: `Weekend`, `Revenue`

### Missing values

No missing values were found in any of the 18 columns.

### Duplicate rows

The initial inspection identified 125 exact duplicate rows.

Because these rows were identical across all available fields, they were removed from the working dataset before dashboard development.

The original raw CSV has been preserved unchanged.

A reproducible cleaning script (`data/clean_dataset.py`) was created to perform this operation.

After removing the 125 exact duplicates, the working dataset contains 12,205 rows.

This cleaning decision applies only to exact duplicate records. It does not assume that different sessions with similar behaviour are duplicates.

### Revenue distribution

The `Revenue` variable contains:

- 10,422 sessions without revenue
- 1,908 sessions with revenue

This corresponds to approximately:

- 84.5% non-revenue sessions
- 15.5% revenue sessions

The dataset therefore provides a clear purchase/non-purchase outcome that can support conversion analysis.

### Initial Data Quality Assessment

Overall, the dataset is suitable for further analysis because:

- It contains no missing values.
- It contains a clear revenue outcome.
- It contains customer-session behaviour variables.
- It contains traffic and visitor-type information.
- It contains engagement, bounce, exit and page-value measures.

The presence of 125 duplicate rows must be considered during the cleaning and analysis stage.

### Working dataset

The cleaned dataset contains 12,205 rows and 20 columns.

Two additional labelled fields were created for dashboard readability:

- `Revenue_Label`
- `Weekend_Label`

### Relevance to the Proposed AI Solution

The dataset can support the analysis of potential revenue loss during the digital customer journey.

For example, we can investigate relationships between:

- Product-related engagement and conversion
- Bounce/exit behaviour and conversion
- Visitor type and conversion
- Traffic type and conversion
- Page value and conversion
- Session behaviour and revenue outcome

The dataset does not contain advertising expenditure, campaign-level cost, or actual cart recovery actions.

Therefore, the project will not claim to calculate advertising waste or ROAS from this dataset.

Instead, the AI solution will identify potential conversion/revenue opportunities and recommend possible actions for human validation.
## Selected Dataset

**Status:** Selected

**Dataset:** UCI Online Shoppers Purchasing Intention Dataset

**Source:** UCI Machine Learning Repository

**DOI:** 10.24432/C5F88Q

## Selection Justification

The UCI Online Shoppers Purchasing Intention Dataset was selected because it provides a strong fit with the proposed AI-Powered E-commerce Revenue Optimization Advisor.

The project focuses on identifying potential revenue opportunities across the digital customer journey and recommending data-driven actions that could improve conversion.

The dataset contains 12,330 shopping sessions and provides behavioural, engagement, traffic and visitor-type variables together with a `Revenue` outcome.

This allows the project to investigate which customer-session characteristics are associated with purchase and non-purchase outcomes.

The dataset is also well suited to the Round 1 requirements because it:

- Is publicly accessible and documented.
- Contains a clear revenue outcome.
- Has no missing values.
- Contains both behavioural and acquisition-related variables.
- Can be analysed and communicated through Power BI.
- Can provide structured inputs for a simple n8n AI proof of concept.
- Provides a potential foundation for a small predictive or recommendation component in Round 2.

The dataset is therefore considered sufficiently relevant for demonstrating the business problem while keeping the initial MVP scope manageable.

## Limitations

The dataset does not contain:

- Advertising expenditure
- Campaign-level advertising cost
- Detailed campaign identifiers
- Actual cart abandonment events
- Individual product information
- Customer support interactions
- Actual recovery actions

Therefore, the project will not claim to measure actual advertising waste, ROAS, or recovered revenue from this dataset.

Marketing analysis will be limited to the available traffic-related variables and their relationship with session outcomes.

Cart recovery will be treated as a potential recommended intervention rather than something directly observed in the dataset.

The dataset also contains 125 duplicate rows. Their treatment will be considered during the data-cleaning stage before downstream analysis.

Finally, the dataset represents historical shopping sessions from a specific e-commerce context. Findings should therefore be treated as a proxy for the fictional client scenario rather than as evidence about Chleo's actual company.