import os
import json
import base64
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import pandas as pd
from configfile import (
    SES_SMTP_HOST,
    SES_SENDER,
    SES_SMTP_PORT,
    SES_SMTP_USERNAME,
    SES_SMTP_PASSWORD,
    SES_RECEIVERS,
    SES_SENDER_NAME
)

def send_mail(subject: str,
              df: pd.DataFrame,
              df2: pd.DataFrame,
              df3: pd.DataFrame,
              csv_path: str = None):
    """
    Send pytest execution report email using AWS SES SMTP
    df  -> detailed test result
    df2 -> module-wise summary
    df3 -> overall summary
    """

    # ================= VALIDATION =================
    if df is None or df.empty:
        raise ValueError("Detailed DataFrame (df) is empty or None")

    if df2 is None or df2.empty:
        raise ValueError("Summary DataFrame (df2) is empty or None")

    if df3 is None or df3.empty:
        raise ValueError("Summary DataFrame (df3) is empty or None")

    # ================= STATUS COLOR =================
    def status_color(status):
        status = str(status).lower()
        if status == "pass":
            return "#28a745"
        elif status == "fail":
            return "#dc3545"
        else:
            return "#ffc107"

    # ================= TABLE 1 : DETAILED =================
    table_rows = ""
    for _, row in df.iterrows():
        table_rows += f"""
        <tr>
            <td>{row.get('S No', '')}</td>
            <td>{row.get('Module', '')}</td>
            <td>{row.get('Test Description', '')}</td>
            <td style="background-color:{status_color(row.get('Status'))};
                       color:white;font-weight:bold;">
                {row.get('Status', '')}
            </td>
        </tr>
        """

    html_table_1 = f"""
    <table border="1" cellspacing="0" cellpadding="8"
           style="border-collapse:collapse;width:95%;
                  font-family:Calibri;text-align:center;">
        <tr style="background-color:#002060;color:white;font-weight:bold;">
            <th>S No</th>
            <th>Module</th>
            <th>Test Description</th>
            <th>Status</th>
        </tr>
        {table_rows}
    </table>
    """

    # ================= TABLE 2 : SUMMARY =================
    table_rows_2 = ""
    for _, row in df2.iterrows():
        table_rows_2 += f"""
        <tr>
            <td>{row.get('S No', '')}</td>
            <td>{row.get('Module', '')}</td>
            <td>{row.get('Total_Test_Case', '')}</td>
            <td>{row.get('Executed_Test_Case', '')}</td>
            <td>{row.get('Pending_Test_Case', '')}</td>
            <td>{row.get('PASS', '')}</td>
            <td>{row.get('FAIL', '')}</td>
        </tr>
        """

    html_table_2 = f"""
    <table border="1" cellspacing="0" cellpadding="8"
           style="border-collapse:collapse;width:95%;
                  font-family:Calibri;text-align:center;margin-top:20px;">
        <tr style="background-color:#002060;color:white;font-weight:bold;">
            <th>S No</th>
            <th>Module</th>
            <th>Total Test-case</th>
            <th>Executed Test-case</th>
            <th>Pending Test-case</th>
            <th>PASS</th>
            <th>FAIL</th>
        </tr>
        {table_rows_2}
    </table>
    """

    # ================= TABLE 3 : OVERALL SUMMARY =================
    table_rows_3 = ""
    for _, row in df3.iterrows():
        table_rows_3 += f"""
         <tr>
             <td>{row.get('S No', '')}</td>
             <td>{row.get('Total Test Case', '')}</td>
             <td>{row.get('Executed Test Case', '')}</td>
             <td>{row.get('Pending Test Case', '')}</td>
             <td>{row.get('PASS', '')}</td>
             <td>{row.get('FAIL', '')}</td>
         </tr>
         """

    html_table_3 = f"""
     <table border="1" cellspacing="0" cellpadding="8"
            style="border-collapse:collapse;width:95%;
                   font-family:Calibri;text-align:center;margin-top:20px;">
         <tr style="background-color:#002060;color:white;font-weight:bold;">
             <th>S No</th>
             <th>Total Test-case</th>
             <th>Executed Test-case</th>
             <th>Pending Test-case</th>
             <th>PASS</th>
             <th>FAIL</th>
         </tr>
         {table_rows_3}
     </table>
     """

    # ================= EMAIL BODY =================
    body = f"""
    <html>
    <body style="font-family:Calibri;">
        <h3 style="color:#002060;text-align:center;">
            {subject}
        </h3>

        <p>Hello Team,</p>

        <p>Please find below the pytest execution summary:</p>

        <h4>📌 Detailed Test Results</h4>
        {html_table_1}

        <h4>📊 Module-wise Summary</h4>
        {html_table_2}

        <br>
        <h4>📊 Total Test Summary</h4>
        {html_table_3}

        <br>
        <p>Detailed CSV report is attached for reference.</p>

        <br>
        <p><b>Regards,</b><br>Codifi QA Team</p>
    </body>
    </html>
    """

    # ================= AWS SES SMTP CONFIG =================
    # Get these from Props config
    SMTP_HOST = SES_SMTP_HOST  
    SMTP_PORT = SES_SMTP_PORT
    SMTP_USERNAME = SES_SMTP_USERNAME
    SMTP_PASSWORD = SES_SMTP_PASSWORD
    
    # Parse receivers
    receivers = [e.strip() for e in SES_RECEIVERS.split(",")]

    # ================= CREATE EMAIL MESSAGE =================
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{SES_SENDER_NAME} <{SES_SENDER}>"
        msg['To'] = ", ".join(receivers)
        
        # Attach HTML body
        html_part = MIMEText(body, 'html')
        msg.attach(html_part)
        
        # ================= CSV ATTACHMENT =================
        if csv_path and os.path.exists(csv_path):
            with open(csv_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {os.path.basename(csv_path)}',
            )
            msg.attach(part)
        
        # ================= SEND EMAIL VIA SES SMTP =================
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SES_SENDER, SES_RECEIVERS, msg.as_string())
        
        print("✅ Mail sent successfully via AWS SES SMTP")
        return True
        
    except Exception as e:
        print(f"❌ Mail failed: {str(e)}")
        return False

# -------------------------------
# Read CSV
# -------------------------------
df = pd.read_csv("pythonSel\login_test_results.csv")
print(df)
df.columns = df.columns.str.strip().str.lower()


# -------------------------------
# Derive Module
# -------------------------------
def derive_module(row):
    if pd.notna(row.get('username')) or pd.notna(row.get('otp')):
        return "Login"
    if row.get('page') == "Watchlist":
        return "Watchlist"
    if row.get('page') == "Order Window":
        return "Orderbook"
    if row.get('page') == 'Dashboard':
        return "Dashboard"
    if row.get('page') == 'Order Book':
        return "Order Book"
    if row.get('page') == 'Position':
        return "Position"
    if row.get('page') == 'Holdings':
        return "Holdings"
    if row.get('page') == 'Funds':
        return "Funds"
    if row.get('page') == 'Profile':
        return "Profile"
    return None


df['module'] = df.apply(derive_module, axis=1)

# Remove rows without module
df = df.dropna(subset=['module'])
print(df)

# -------------------------------
# Derive Test Description
# -------------------------------
df['test_description'] = (
    df['actual']
    .fillna(df['actual'])
    .fillna("Test case")
)


# -------------------------------
# Derive Status (Pass / Fail / Pending)
# -------------------------------
def derive_status(value):
    if pd.isna(value):
        return "Pending"
    return value.capitalize()


df['final_status'] = df['status'].apply(derive_status)

# -------------------------------
# Build Final Report
# -------------------------------
final_df = df[['module', 'test_description', 'final_status', 'order_type']].copy()

final_df.insert(0, 'S No', range(1, len(final_df) + 1))

final_df.rename(columns={
    'module': 'Module',
    'test_description': 'Test Description',
    'final_status': 'Status'
}, inplace=True)

# -------------------------------
# Calculate Module-wise Summary
# -------------------------------
summary = df.groupby('module').agg(
    Total_Test_Case=('module', 'count'),
    Executed_Test_Case=('status', lambda x: x.notna().sum()),
    PASS=('status', lambda x: (x.str.lower() == 'pass').sum()),
    FAIL=('status', lambda x: (x.str.lower() == 'fail').sum())
).reset_index()

summary['Pending_Test_Case'] = (
        summary['Total_Test_Case'] - summary['Executed_Test_Case']
)

summary.insert(0, 'S No', range(1, len(summary) + 1))

summary.rename(columns={'module': 'Module'}, inplace=True)

summary = summary[
    ['S No', 'Module',
     'Total_Test_Case', 'Executed_Test_Case',
     'Pending_Test_Case', 'PASS', 'FAIL']
]

# -------------------------------
# Overall Summary Calculation
# -------------------------------
total_test_case = len(df)
executed_test_case = df['status'].notna().sum()
pending_test_case = total_test_case - executed_test_case

pass_count = (df['status'].str.lower() == 'pass').sum()
fail_count = (df['status'].str.lower() == 'fail').sum()

# -------------------------------
# Create Overall Summary DataFrame
# -------------------------------
overall_summary = pd.DataFrame([{
    "S No": 1,
    "Total Test Case": total_test_case,
    "Executed Test Case": executed_test_case,
    "Pending Test Case": pending_test_case,
    "PASS": pass_count,
    "FAIL": fail_count
}])

# -------------------------------
# Export CSV
# -------------------------------
overall_summary.to_csv("overall_execution_summary.csv", index=False)

# -------------------------------------------------
# SEND MAIL via AWS SES SMTP ✅
# -------------------------------------------------
send_mail(
    subject="Pytest Automation Execution Report",
    df=final_df,  # detailed table
    df2=summary,  # module-wise summary table
    df3=overall_summary,  # overall summary table
    csv_path=""  # attachment (optional)
)