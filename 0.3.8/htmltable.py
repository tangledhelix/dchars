#!/usr/bin/python3
# -*- coding: utf-8 -*-

################################################################################
class HtmlTable(list):

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self, header = None):
        self.header = header

    #///////////////////////////////////////////////////////////////////////////
    def get_htmlheader(self):
        """
                HtmlTable.get_htmlheader
        """
        res = ""
        res += "<head>" + "\n"
        res += "\t" + '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">' + "\n"

        res += "\t" + '<style media="screen" type="text/css">' + "\n"
        res += "\t\t" + "table {border-collapse: collapse;}" + "\n"
        res += "\t\t" + "td {border: 1px solid black;}" + "\n"
        res += "\t\t" + "th {border: 2px solid black;}" + "\n"
        res += "\t" + '</style>' + "\n"
        res += "</head>" + "\n"
        return res

    #///////////////////////////////////////////////////////////////////////////
    def get_html(self):
        """
                HtmlTable.get_html
        """
        res = ""
        res += "<html>" + "\n"
        res += self.get_htmlheader()
        res += "<body>" + "\n"
        res += "<table>" + "\n"

        if self.header is not None:
            res += "\t" + "<tr>" + "\n"
            for cellule in self.header:
                res += "\t\t" + "<th>" + str(cellule) + "</th>" + "\n"
            res += "\t" + "<tr>" + "\n"

        for row in self:
            res += "\t" + "<tr>" + "\n"
            for cellule in row:
                res += "\t\t" + "<td>" + str(cellule) + "</td>" + "\n"
            res += "\t" + "</tr>" + "\n"

        res += "</table>" + "\n"
        res += "</body>" + "\n"
        res += "</html>"
        return res

# t = HtmlTable( header = ('A', 'B', 'C') )
# t.append( ("1", "2", "3") )
# t.append( ("a", "b", "c") )
# print(t.get_html())
