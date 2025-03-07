from datetime import datetime

class QAmodels:
    def __init__(self, schema):
        self.schema = schema  # Store schema as an instance attribute

    def enhancement_prompt(self, user_question, prompt_instructions="", current_date=None):
        """
        Generates an enhancement prompt to refine the user's question.
        """
        if current_date is None:
            current_date = datetime.now().strftime('%Y-%m-%d')  # Default to today's date

        enhancement_prompt = f"""
    You are a highly skilled SQL expert and data analyst. Your task is to enhance a given user question
    by making it more structured, detailed, and aligned with the provided schema and prompt instructions.
    *Today's Date:* {current_date}
    *Schema:* {self.schema}
    *Prompt Instructions:* {prompt_instructions}
    *User Question:* {user_question}
    Transform the user's question into a clear analysis plan using plain text only. Do not use markdown, bullets, or numbering. Format your response as follows:
 
    "Analysis Plan: [Restate the core question in specific terms]
    Data needed: [List the specific tables and fields required]
    Time periods: [Define exact date ranges with specific months and years]
    Calculations: [Specify exact formulas for all metrics mentioned]
    Filters: [Define precise filtering conditions]
    Sorting: [Specify the order of results]"
    For example, if the user asks "Find materials where consumption rate increased by 30% in the last quarter compared to previous year," your enhancement should be:
    "Analysis Plan: Identify materials whose consumption rate in Q4 2024 (Oct-Dec 2024) increased by at least 30% compared to Q4 2023 (Oct-Dec 2023).
    Data needed: Materials table with material_id, material_name; Consumption table with material_id, consumption_amount, consumption_date.
    Time periods: Q4 2024 = October 1, 2024 to December 31, 2024; Q4 2023 = October 1, 2023 to December 31, 2023.
    Calculations: Q4 2024 consumption = SUM(consumption_amount) for each material in Q4 2024; Q4 2023 consumption = SUM(consumption_amount) for each material in Q4 2023; Percentage increase = ((Q4 2024 consumption - Q4 2023 consumption) / Q4 2023 consumption) * 100.
    Filters: Include only materials where percentage increase >= 30% AND Q4 2023 consumption > 0.
    Sorting: Order by percentage increase descending."
    For example, if the user asks "Find the Same invoice number raised twice by the same vendor in the same financial year 2024," you should take only take EBELN, LIFNR, BUDAT_MKPF columns from mseg table. 
    Keep your response simple, clear, and in plain text format. Focus on making vague terms specific and defining precise calculations.
 
    Note: - For consumption calculations, only consider records where SHKZG = 'H'. (Important)
          - For procurement or supply calculations, only consider recods where SHKZG='S'.(Important)
          - For inventory calculation,consider b oth 'S' = Addition (positive MENGE) and 'H' = Deduction (negative MENGE). (Important)
          - For invoice number, vendor number and financial year take EBELN, LIFNR, and BUDAT_MKPF columns from mseg table. (Important)
          - Convert the datatype of BUDAT_MKPF from 'YYYYMMDD' to 'YYYY-MM-DD'. (Important).
    """
        return enhancement_prompt

    def sql_prompt(self, enhanced_question):
        """
        Generate the SQL prompt for OpenAI based on the user question.
        """
        current_date = datetime.now().strftime('%Y-%m-%d')
        sql_prompt = f"""
You are a highly skilled Spark SQL expert and data analyst specializing in Fabric lakehouse environments. Generate an optimized Spark SQL query strictly using only the tables mseg (Material Document Segment) and mbewh (Material Valuation History) from the database schema.
Enhanced User Question: {enhanced_question}
Today's date is: {current_date}

Table Reference Rules:
- Columns from mseg:
  - MATNR (Material Number, STRING)
  - BUDAT_MKPF (Posting Date, STRING)
  - SHKZG (Debit/Credit Indicator, STRING)
  - MENGE (Quantity, STRING)
  - LIFNR (Vendor Number, STRING)
  - EBELN (Invoice No./Purchase Order No., STRING)
- Columns from mbewh:
  - MATNR (Material Number, STRING)
  - LFMON (Financial Month, STRING)
  - LFGJA (Fiscal Year, STRING)
  - LBKUM (Closing Stock, STRING)

Column Logic:
- For SHKZG (Debit/Credit Indicator):
  - 'S' = Addition (positive MENGE) that is Procurement quantity or Supply
  - 'H' = Deduction (negative MENGE) that is Consumption
- String comparisons should use equality operators (= or <>) with proper quoting
- For string pattern matching, use LIKE operator with appropriate wildcards

Opening Stock Calculation:
- Opening Stock for each month = Previous month's LBKUM.
- Use LFMON - 1 for the previous month.
- If LFMON = 1 (April), use LFMON = 12 of the previous year (LFGJA - 1).

Calendar to LFMON Conversion:  
- April = 1, May = 2, June = 3, July = 4, August = 5, September = 6, October = 7, November = 8, December = 9, January = 10, February = 11, March = 12.

Additional Guidelines:
- Use the schema name {self.schema} for all table references without square brackets (e.g., schema.mseg instead of [schema].mseg).
- Use only the mseg and mbewh tables; no other tables are allowed.
- Ensure MENGE is adjusted based on SHKZG logic.
- Dynamically calculate Opening Stock from mbewh.
- Properly handle all string comparisons by using single quotes around string literals (e.g., SHKZG = 'S', not SHKZG = S)
- When comparing string values in WHERE clauses or joins, use proper string equality operators (= or <>)
- For string pattern matching, use LIKE with appropriate wildcards (%, _)
- For string concatenation, use the concat() function instead of the + operator
- Handle potential NULL values in string columns appropriately (use IS NULL or IS NOT NULL)
- Optimize the SQL query for Spark SQL performance:
  - Use appropriate window functions instead of self-joins when possible
  - Minimize subqueries that require shuffling large amounts of data
  - Use proper date functions compatible with Spark SQL
  - Consider data partitioning when filtering on date columns
- Do not include explanations—return only the SQL query as plain text (no Markdown formatting).
- Apply all the necessary calculations which enhanced_question [{enhanced_question}] mentioned.
- Do not use square brackets [] anywhere in the SQL query, as they're not supported in Spark SQL.
- Use backticks (`) if identifiers need to be escaped, rather than square brackets.
- For consumption and Procurement quantity or Supply refer to column logic.
- When using CTEs, place them at the beginning of the query using WITH syntax.
- For date functions, use Spark SQL-compatible functions (date_add, date_sub, etc.).
- For conditional logic, ensure CASE statements are properly formatted for Spark SQL.
- Ensure all string comparisons are case-sensitive unless specified otherwise
- First, inspect the actual column names available in the mseg table schema. Based on the error message, BUDAT_MKPF is not available but there might be columns like BUDAT_MKPF_, CPUDT_MKPF, or BUSTM.

Note: 
- For consumption calculations, only consider records where SHKZG = 'H'. (Important)
- For procurement or supply calculations, only consider records where SHKZG = 'S'. (Important)
- For inventory calculation, consider both 'S' = Addition (positive MENGE) and  'H' = Deduction (negative MENGE). (Important)
- For invoice number, vendor number and financial year take EBELN, LIFNR, and BUDAT_MKPF columns from mseg table. (Important)
- String columns like MATNR, LIFNR, EBELN, CHARG, etc. should be properly quoted in the query for comparison.

Provide only the SQL query as plain text without any formatting or additional text.
 
"""
        return sql_prompt