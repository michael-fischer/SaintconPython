from mailmerge import MailMerge

template = "Module 11 - Office Documents/Remediation Report Template.docx"
outfile = "test.docx"

document = MailMerge(template)
print(document.get_merge_fields())

findings = [{
    'FindingSeverity': 'Severe',
    'FindingStatus': 'Open',
    'FindingId': '1234',
    'FindingText': 'blah'
},

{
    'FindingSeverity': 'Medium',
    'FindingStatus': 'Open',
    'FindingId': '1234',
    'FindingText': 'blah blah'
},

{
    'FindingSeverity': 'Low',
    'FindingStatus': 'Open',
    'FindingId': '1234',
    'FindingText': 'neh'
}
]

document.merge(ReportDate='2019/10/31', BLA_DATE='2018/05/19', ProductName='My test')
document.merge_rows('FindingId', findings)
document.write(outfile)


