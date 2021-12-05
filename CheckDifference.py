import difflib
File1=r"\Users\Admin\AppData\Local\Programs\Python\Python39\ISPResearchPaper\Text1.txt"
File2=r"\Users\Admin\AppData\Local\Programs\Python\Python39\ISPResearchPaper\Text1.1.txt"
File1_lines=open(File1).readlines()
File2_lines=open(File2).readlines()
difference=difflib.HtmlDiff().make_file(File1_lines, File2_lines, File1, File2)
difference_report=open(r'\Users\Admin\AppData\Local\Programs\Python\Python39\ISPResearchPaper\Difference\Difference_Report.html','w')
difference_report.write(difference)
difference_report.close()
