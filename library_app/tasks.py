from __future__ import unicode_literals
import frappe

def monthly():
    # pdf_content =
    frappe.sendmail('customeremail', attachments = [
        {
            'fcontent':'pdf_content',
            'fname': 'report.pdf'
            
        }
    ])