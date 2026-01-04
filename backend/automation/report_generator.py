from datetime import datetime

def generate_report(sales=0, visitors=0):
    report = f"""
WEEKLY REPORT
Date: {datetime.now()}
Visitors: {visitors}
Sales: {sales}
Conversion: { (sales / visitors * 100) if visitors else 0:.2f}%
"""
    with open("automation_data/weekly_report.txt", "w") as f:
        f.write(report)

    return report
