"""
Examples demonstrating how to use the XBRL2 module for statement rendering.
"""

from pathlib import Path
from rich.console import Console

from edgar.xbrl2.xbrl import XBRL

def render_financial_statements():
    """
    Demonstrates how to render financial statements in a tabular format.
    """
    # Path to XBRL files
    sample_dir = Path(__file__).parent / "aapl"
    
    # Create an XBRL object by parsing the directory
    xbrl = XBRL.parse_directory(sample_dir)
    
    console = Console()
    
    # Display entity information
    console.print("\n[bold]Entity Information:[/bold]")
    for key, value in xbrl.entity_info.items():
        console.print(f"{key}: {value}")
    
    # Display available reporting periods
    console.print("\n[bold]Available Reporting Periods:[/bold]")
    for i, period in enumerate(xbrl.reporting_periods):
        if period['type'] == 'instant':
            console.print(f"{i+1}. As of {period['date']}")
        else:
            console.print(f"{i+1}. {period['start_date']} to {period['end_date']}")
    
    # Show available period views for each statement
    console.print("\n[bold]Available Period Views for Balance Sheet:[/bold]")
    bs_views = xbrl.get_period_views("BalanceSheet")
    for view in bs_views:
        console.print(f"- {view['name']}: {view['description']}")
    
    console.print("\n[bold]Available Period Views for Income Statement:[/bold]")
    is_views = xbrl.get_period_views("IncomeStatement")
    for view in is_views:
        console.print(f"- {view['name']}: {view['description']}")
    
    # Render Balance Sheet using default view
    console.print("\n[bold]Balance Sheet (Default View):[/bold]")
    balance_sheet = xbrl.render_statement("BalanceSheet")
    console.print(balance_sheet)
    
    # Render Balance Sheet with Current Only view if available
    if bs_views and any(v['name'] == 'Current Only' for v in bs_views):
        console.print("\n[bold]Balance Sheet (Current Only View):[/bold]")
        current_only_bs = xbrl.render_statement("BalanceSheet", period_view="Current Only")
        console.print(current_only_bs)
    
    # Render Income Statement using default view
    console.print("\n[bold]Income Statement (Default View):[/bold]")
    income_statement = xbrl.render_statement("IncomeStatement")
    console.print(income_statement)
    
    # Render Income Statement with a quarterly view if available
    quarterly_view = next((v for v in is_views if 'Quarterly' in v['name']), None)
    if quarterly_view:
        console.print(f"\n[bold]Income Statement ({quarterly_view['name']}):[/bold]")
        quarterly_is = xbrl.render_statement("IncomeStatement", period_view=quarterly_view['name'])
        console.print(quarterly_is)
    
    # Render Cash Flow Statement
    console.print("\n[bold]Cash Flow Statement:[/bold]")
    cash_flow = xbrl.render_statement("CashFlowStatement")
    console.print(cash_flow)
    
    # Get a specific period for rendering
    if xbrl.reporting_periods:
        # Use the most recent instant period for Balance Sheet
        instant_periods = [p for p in xbrl.reporting_periods if p['type'] == 'instant']
        
        if instant_periods:
            period = instant_periods[0]  # Most recent period
            period_key = f"instant_{period['date']}"
            
            console.print(f"\n[bold]Balance Sheet (As of {period['date']} only):[/bold]")
            single_period_bs = xbrl.render_statement("BalanceSheet", period_filter=period_key)
            console.print(single_period_bs)
        
        # Use most recent duration period for Income Statement
        duration_periods = [p for p in xbrl.reporting_periods if p['type'] == 'duration']
        
        if duration_periods:
            period = duration_periods[0]  # Most recent period
            period_key = f"duration_{period['start_date']}_{period['end_date']}"
            
            console.print(f"\n[bold]Income Statement ({period['start_date']} to {period['end_date']} only):[/bold]")
            single_period_is = xbrl.render_statement("IncomeStatement", period_filter=period_key)
            console.print(single_period_is)

if __name__ == "__main__":
    render_financial_statements()