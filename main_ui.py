# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1161, 636)
        Form.setStyleSheet("  \n"
                           "/**\n"
                           " * Qt like CSS for doxygen based on 1.8.6 \n"
                           " *\n"
                           " * Frank Enderle <frank.enderle@anamica.de>\n"
                           " */\n"
                           "\n"
                           "body, table, div, p, dl {\n"
                           "  font: 400 13px/1.3 Verdana,DejaVu Sans,Geneva,sans-serif;\n"
                           "}\n"
                           "\n"
                           "/* @group Heading Levels */\n"
                           "\n"
                           "h1.groupheader {\n"
                           "  font-size: 16px;\n"
                           "}\n"
                           "\n"
                           ".title {\n"
                           "  font: 700 18px Verdana,DejaVu Sans,Geneva,sans-serif;  \n"
                           "  margin: 10px 2px;\n"
                           "}\n"
                           "\n"
                           "h2.groupheader {\n"
                           "  border: 0;\n"
                           "  color: #363534;\n"
                           "  font-size: 16px;\n"
                           "  font-weight: 600;\n"
                           "}\n"
                           "\n"
                           "h3.groupheader {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "h1, h2, h3, h4, h5, h6 {\n"
                           "  -webkit-transition: none;\n"
                           "  -moz-transition: none;\n"
                           "  -ms-transition: none;\n"
                           "  -o-transition: none;\n"
                           "  transition: none;\n"
                           "}\n"
                           "\n"
                           "h1.glow, h2.glow, h3.glow, h4.glow, h5.glow, h6.glow {\n"
                           "  text-shadow: none;\n"
                           "}\n"
                           "\n"
                           "dt {\n"
                           "}\n"
                           "\n"
                           "div.multicol {\n"
                           "}\n"
                           "\n"
                           "p.startli, p.startdd {\n"
                           "}\n"
                           "\n"
                           "p.starttd {\n"
                           "}\n"
                           "\n"
                           "p.endli {\n"
                           "}\n"
                           "\n"
                           "p.enddd {\n"
                           "}\n"
                           "\n"
                           "p.endtd {\n"
                           "}\n"
                           "\n"
                           "/* @end */\n"
                           "\n"
                           "caption {\n"
                           "}\n"
                           "\n"
                           "span.legend {\n"
                           "}\n"
                           "\n"
                           "h3.version {\n"
                           "}\n"
                           "\n"
                           "div.qindex, div.navtab {\n"
                           "  background-color: #F6F6F6;\n"
                           "  border: 1px solid #E6E6E6;\n"
                           "}\n"
                           "\n"
                           "div.qindex, div.navpath {\n"
                           "  line-height: 1.5;\n"
                           "}\n"
                           "\n"
                           "div.navtab {\n"
                           "}\n"
                           "\n"
                           "/* @group Link Styling */\n"
                           "\n"
                           "a {\n"
                           "  color: #00732F;\n"
                           "}\n"
                           "\n"
                           ".contents a:visited {\n"
                           "  color: #00732F;\n"
                           "}\n"
                           "\n"
                           "a:hover {\n"
                           "  text-decoration: none;\n"
                           "}\n"
                           "\n"
                           "a.qindex {\n"
                           "}\n"
                           "\n"
                           "a.qindexHL {\n"
                           "}\n"
                           "\n"
                           ".contents a.qindexHL:visited {\n"
                           "}\n"
                           "\n"
                           "a.el {\n"
                           "  font-weight: normal;\n"
                           "}\n"
                           "\n"
                           "a.elRef {\n"
                           "}\n"
                           "\n"
                           "a.code, a.code:visited, a.line, a.line:visited {\n"
                           "  color: #00732F; \n"
                           "}\n"
                           "\n"
                           "a.codeRef, a.codeRef:visited, a.lineRef, a.lineRef:visited {\n"
                           "  color: #00732F; \n"
                           "}\n"
                           "\n"
                           "/* @end */\n"
                           "\n"
                           "dl.el {\n"
                           "}\n"
                           "\n"
                           "pre.fragment {\n"
                           "}\n"
                           "\n"
                           "div.fragment {\n"
                           "}\n"
                           "\n"
                           "div.line {\n"
                           "  -webkit-transition-duration: 0;\n"
                           "  -moz-transition-duration: 0;\n"
                           "  -ms-transition-duration: 0;\n"
                           "  -o-transition-duration: 0;\n"
                           "  transition-duration: 0;\n"
                           "}\n"
                           "\n"
                           "div.line.glow {\n"
                           "  background-color: auto;\n"
                           "  box-shadow: none;\n"
                           "}\n"
                           "\n"
                           "span.lineno {\n"
                           "}\n"
                           "\n"
                           "span.lineno a {\n"
                           "}\n"
                           "\n"
                           "span.lineno a:hover {\n"
                           "}\n"
                           "\n"
                           "div.ah {\n"
                           "  background: none;\n"
                           "  background-color: #F6F6F6;\n"
                           "  color: #66666E;\n"
                           "  border: 1px solid #E6E6E6;\n"
                           "  border-radius: 7px;\n"
                           "  -webkit-border-radius: 7px;\n"
                           "  -moz-border-radius: 7px;\n"
                           "  box-shadow: none;\n"
                           "  -webkit-box-shadow: none;\n"
                           "  -moz-box-shadow: none;\n"
                           "}\n"
                           "\n"
                           "div.groupHeader {\n"
                           "}\n"
                           "\n"
                           "div.groupText {\n"
                           "}\n"
                           "\n"
                           "body {\n"
                           "  color: #363534;\n"
                           "}\n"
                           "\n"
                           "div.contents {\n"
                           "}\n"
                           "\n"
                           "td.indexkey {\n"
                           "}\n"
                           "\n"
                           "td.indexvalue {\n"
                           "}\n"
                           "\n"
                           "tr.memlist {\n"
                           "}\n"
                           "\n"
                           "p.formulaDsp {\n"
                           "}\n"
                           "\n"
                           "img.formulaDsp {\n"
                           "}\n"
                           "\n"
                           "img.formulaInl {\n"
                           "}\n"
                           "\n"
                           "div.center {\n"
                           "}\n"
                           "\n"
                           "div.center img {\n"
                           "}\n"
                           "\n"
                           "address.footer {\n"
                           "}\n"
                           "\n"
                           "img.footer {\n"
                           "  display: none;\n"
                           "}\n"
                           "\n"
                           "/* addition */\n"
                           ".footer a:before {\n"
                           "  content: \"Doxygen\";\n"
                           "}\n"
                           "/* --- */\n"
                           "\n"
                           "/* @group Code Colorization */\n"
                           "\n"
                           "span.keyword {\n"
                           "}\n"
                           "\n"
                           "span.keywordtype {\n"
                           "}\n"
                           "\n"
                           "span.keywordflow {\n"
                           "}\n"
                           "\n"
                           "span.comment {\n"
                           "}\n"
                           "\n"
                           "span.preprocessor {\n"
                           "}\n"
                           "\n"
                           "span.stringliteral {\n"
                           "}\n"
                           "\n"
                           "span.charliteral {\n"
                           "}\n"
                           "\n"
                           "span.vhdldigit { \n"
                           "}\n"
                           "\n"
                           "span.vhdlchar { \n"
                           "}\n"
                           "\n"
                           "span.vhdlkeyword { \n"
                           "}\n"
                           "\n"
                           "span.vhdllogic { \n"
                           "}\n"
                           "\n"
                           "blockquote {\n"
                           "}\n"
                           "\n"
                           "/* @end */\n"
                           "\n"
                           ".search {\n"
                           "}\n"
                           "\n"
                           "form.search {\n"
                           "}\n"
                           "\n"
                           "input.search {\n"
                           "}\n"
                           "\n"
                           "td.tiny {\n"
                           "}\n"
                           "\n"
                           ".dirtab {\n"
                           "}\n"
                           "\n"
                           "th.dirtab {\n"
                           "}\n"
                           "\n"
                           "hr {\n"
                           "  border-top: 1px solid #E6E6E6;\n"
                           "  margin: 10px 8px 0 12px;\n"
                           "}\n"
                           "\n"
                           "hr.footer {\n"
                           "}\n"
                           "\n"
                           "/* @group Member Descriptions */\n"
                           "\n"
                           "table.memberdecls {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "/* addition */\n"
                           "\n"
                           "table.memberdecls a {\n"
                           "  font-weight: 600;  \n"
                           "}\n"
                           "\n"
                           "table.memberdecls .memItemLeft {\n"
                           "  border: solid #E6E6E6;\n"
                           "  border-width: 0 0 0 1px;\n"
                           "}\n"
                           "\n"
                           "table.memberdecls .memItemRight {\n"
                           "  border: solid #E6E6E6;\n"
                           "  border-width: 0 1px 0 0;\n"
                           "}\n"
                           "\n"
                           "table.memberdecls tr:nth-child(2) .memItemLeft {\n"
                           "  border-top-width: 1px;\n"
                           "  border-top-left-radius: 7px;\n"
                           "  padding-top: 6px;\n"
                           "}\n"
                           "\n"
                           "table.memberdecls tr:nth-child(2) .memItemRight {\n"
                           "  border-top-width: 1px;\n"
                           "  border-top-right-radius: 7px;\n"
                           "  padding-top: 6px;\n"
                           "}\n"
                           "\n"
                           "table.memberdecls tr:nth-last-child(2) .memItemLeft {\n"
                           "  border-bottom-width: 1px;\n"
                           "  border-bottom-left-radius: 7px;\n"
                           "  padding-bottom: 6px;\n"
                           "}\n"
                           "\n"
                           "table.memberdecls tr:nth-last-child(2) .memItemRight {\n"
                           "  border-bottom-width: 1px;\n"
                           "  border-bottom-right-radius: 7px;\n"
                           "  padding-bottom: 6px;\n"
                           "}\n"
                           "\n"
                           "/* --- */\n"
                           "\n"
                           ".memberdecls td, .fieldtable tr {\n"
                           "  -webkit-transition-duration: 0;\n"
                           "  -moz-transition-duration: 0;\n"
                           "  -ms-transition-duration: 0;\n"
                           "  -o-transition-duration: 0;\n"
                           "  transition-duration: 0;\n"
                           "}\n"
                           "\n"
                           ".memberdecls td.glow, .fieldtable tr.glow {\n"
                           "  background-color: auto;\n"
                           "  box-shadow: 0;\n"
                           "}\n"
                           "\n"
                           ".mdescLeft, .mdescRight,\n"
                           ".memItemLeft, .memItemRight,\n"
                           ".memTemplItemLeft, .memTemplItemRight, .memTemplParams {\n"
                           "  width: auto;\n"
                           "  background-color: #F6F6F6;\n"
                           "}\n"
                           "\n"
                           ".mdescLeft, .mdescRight {\n"
                           "}\n"
                           "\n"
                           "/* addition */\n"
                           ".mdescLeft {\n"
                           "  padding: 3px 10px 3px 15px;\n"
                           "}\n"
                           "\n"
                           ".mdescRight {\n"
                           "  padding: 3px 15px 3px 10px;\n"
                           "}\n"
                           "/* --- */\n"
                           "\n"
                           ".memSeparator {\n"
                           "  display: none;\n"
                           "}\n"
                           "\n"
                           ".memItemLeft, .memTemplItemLeft {\n"
                           "}\n"
                           "\n"
                           ".memItemRight {\n"
                           "  padding-right: 8px;\n"
                           "}\n"
                           "\n"
                           ".memTemplParams {\n"
                           "}\n"
                           "\n"
                           "/* @end */\n"
                           "\n"
                           "/* @group Member Details */\n"
                           "\n"
                           "/* Styles for detailed member documentation */\n"
                           "\n"
                           ".memtemplate {\n"
                           "}\n"
                           "\n"
                           ".memnav {\n"
                           "}\n"
                           "\n"
                           ".mempage {\n"
                           "}\n"
                           "\n"
                           ".memitem {\n"
                           "  margin-bottom: 20px;\n"
                           "  -webkit-transition-duration: 0;\n"
                           "  -moz-transition-duration: 0;\n"
                           "  -ms-transition-duration: 0;\n"
                           "  -o-transition-duration: 0;\n"
                           "  transition-duration: 0;\n"
                           "}\n"
                           "\n"
                           ".memitem.glow {\n"
                           "  box-shadow: none;\n"
                           "}\n"
                           "\n"
                           ".memname {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           ".memname td {\n"
                           "}\n"
                           "\n"
                           ".memproto, dl.reflist dt {\n"
                           "  border: 1px solid #E6E6E6;\n"
                           "  padding: 5px 10px;\n"
                           "  color: #363534;\n"
                           "  text-shadow: none;\n"
                           "  background: none;\n"
                           "  background-color: #F6F6F6;\n"
                           "  box-shadow: none;\n"
                           "  border-radius: 7px;\n"
                           "  -moz-box-shadow: none;\n"
                           "  -moz-border-radius: 7px;\n"
                           "  -webkit-box-shadow: none;\n"
                           "  -webkit-border-radius: 7px;\n"
                           "}\n"
                           "\n"
                           "/* additional */\n"
                           ".memproto .memname {\n"
                           "  font-weight: bold;\n"
                           "}\n"
                           "\n"
                           ".memproto .memname a {\n"
                           "  font-weight: bold;  \n"
                           "}\n"
                           "/* --- */\n"
                           "\n"
                           ".memdoc, dl.reflist dd {\n"
                           "  border: 0;      \n"
                           "  padding: 0;\n"
                           "  background: none;\n"
                           "  border-radius: 0;\n"
                           "  box-shadow: none;\n"
                           "  -moz-border-radius: 0;\n"
                           "  -moz-box-shadow: none;\n"
                           "  -webkit-border-radius: 0;\n"
                           "  -webkit-box-shadow: none;\n"
                           "}\n"
                           "\n"
                           "dl.reflist dt {\n"
                           "}\n"
                           "\n"
                           "dl.reflist dd {\n"
                           "}\n"
                           "\n"
                           ".paramkey {\n"
                           "}\n"
                           "\n"
                           ".paramtype {\n"
                           "}\n"
                           "\n"
                           ".paramname {\n"
                           "  color: #363534;\n"
                           "}\n"
                           "\n"
                           ".paramname em {\n"
                           "}\n"
                           "\n"
                           ".paramname code {\n"
                           "}\n"
                           "\n"
                           ".params, .retval, .exception, .tparams {\n"
                           "}       \n"
                           "\n"
                           ".params .paramname, .retval .paramname {\n"
                           "}\n"
                           "        \n"
                           ".params .paramtype {\n"
                           "}       \n"
                           "        \n"
                           ".params .paramdir {\n"
                           "}\n"
                           "\n"
                           ".mlabels {\n"
                           "}\n"
                           "\n"
                           "td.mlabels-left {\n"
                           "}\n"
                           "\n"
                           "td.mlabels-right {\n"
                           "}\n"
                           "\n"
                           "span.mlabels {\n"
                           "}\n"
                           "\n"
                           "span.mlabel {\n"
                           "  background-color: #E6E6E6;\n"
                           "  border: 0;\n"
                           "  color: #66666E;\n"
                           "  padding: 4px 5px;\n"
                           "  border-radius: 4px;\n"
                           "  font-size: 11px;\n"
                           "}\n"
                           "\n"
                           "/* @end */\n"
                           "\n"
                           "/* these are for tree view when not used as main index */\n"
                           "\n"
                           "div.directory {\n"
                           "  border: none;\n"
                           "}\n"
                           "\n"
                           ".directory table {\n"
                           "}\n"
                           "\n"
                           ".directory td {\n"
                           "}\n"
                           "\n"
                           ".directory td.entry {\n"
                           "}\n"
                           "\n"
                           ".directory td.entry a {\n"
                           "  font-weight: bold;\n"
                           "}\n"
                           "\n"
                           ".directory td.entry a img {\n"
                           "}\n"
                           "\n"
                           ".directory td.desc {\n"
                           "  border-color: #E6E6E6;\n"
                           "}\n"
                           "\n"
                           ".directory tr.even {\n"
                           "  background: none;\n"
                           "}\n"
                           "\n"
                           ".directory img {\n"
                           "  vertical-align: -30%;\n"
                           "}\n"
                           "\n"
                           ".directory .levels {\n"
                           "}\n"
                           "\n"
                           ".directory .levels span {\n"
                           "}\n"
                           "\n"
                           "div.dynheader {\n"
                           "}\n"
                           "\n"
                           "address {\n"
                           "}\n"
                           "\n"
                           "table.doxtable {\n"
                           "}\n"
                           "\n"
                           "table.doxtable td, table.doxtable th {\n"
                           "  border: 1px solid #E6E6E6;\n"
                           "}\n"
                           "\n"
                           "table.doxtable th {\n"
                           "  background-color: #F6F6F6;\n"
                           "  color: #66666E;\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "table.fieldtable {\n"
                           "  padding: 5px 10px;\n"
                           "  border: 1px solid #E6E6E6;\n"
                           "  background-color: #F6F6F6;\n"
                           "  box-shadow: none;\n"
                           "  border-radius: 7px;\n"
                           "  -moz-box-shadow: none;\n"
                           "  -moz-border-radius: 7px;\n"
                           "  -webkit-box-shadow: none;\n"
                           "  -webkit-border-radius: 7px;\n"
                           "}\n"
                           "\n"
                           ".fieldtable td, .fieldtable th {\n"
                           "}\n"
                           "\n"
                           ".fieldtable td.fieldtype, .fieldtable td.fieldname {\n"
                           "  border: 0;\n"
                           "}\n"
                           "\n"
                           ".fieldtable td.fieldname {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "/* additional */\n"
                           ".fieldtable td.fieldname em {\n"
                           "  font-style: normal;\n"
                           "}\n"
                           "/* --- */\n"
                           "\n"
                           ".fieldtable td.fielddoc {\n"
                           "  border: 0;\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "/* additional */\n"
                           ".fieldtable td.fielddoc * {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "/* --- */\n"
                           "\n"
                           ".fieldtable td.fielddoc p:first-child {\n"
                           "  margin: auto;\n"
                           "}       \n"
                           "        \n"
                           ".fieldtable td.fielddoc p:last-child {\n"
                           "  margin: auto;\n"
                           "}\n"
                           "\n"
                           ".fieldtable tr:last-child td {\n"
                           "}\n"
                           "\n"
                           ".fieldtable th {\n"
                           "  background: none;\n"
                           "  background-color: #E6E6E6;\n"
                           "  font-size: 13px;\n"
                           "  font-weight: normal;\n"
                           "  color: #363534;\n"
                           "  border-radius: 0;\n"
                           "  -moz-border-radius: 0;\n"
                           "  -webkit-border-radius: 0;\n"
                           "  border: 0;\n"
                           "}\n"
                           "\n"
                           ".tabsearch {\n"
                           "}\n"
                           "\n"
                           ".navpath ul {\n"
                           "  background: none;\n"
                           "  background-color: #E6E6E6;\n"
                           "  color: #363534;\n"
                           "  border: 0;\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           ".navpath li {\n"
                           "  color: #363534;\n"
                           "}\n"
                           "\n"
                           ".navpath li.navelem a {\n"
                           "  color: #363534;\n"
                           "}\n"
                           "\n"
                           ".navpath li.navelem a:hover {\n"
                           "  color: #363534;\n"
                           "}\n"
                           "\n"
                           ".navpath li.footer {\n"
                           "  color: #363534;\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "div.summary {\n"
                           "  margin: 20px;\n"
                           "  width: auto;\n"
                           "  display: inline-block;\n"
                           "  text-align: left;\n"
                           "  color: transparent;\n"
                           "  line-height: 0;\n"
                           "  padding: 15px 25px;      \n"
                           "  border: 1px solid #E6E6E6;\n"
                           "  background-color: #F6F6F6;\n"
                           "  border-radius: 7px;\n"
                           "  -moz-border-radius: 7px;\n"
                           "  -webkit-border-radius: 7px;\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           "div.summary a {\n"
                           "  display: block;  \n"
                           "  line-height: 1.5;\n"
                           "}\n"
                           "\n"
                           "div.ingroups {\n"
                           "}\n"
                           "\n"
                           "div.ingroups a {\n"
                           "}\n"
                           "\n"
                           "div.header {\n"
                           "  background: none;\n"
                           "  border: 0;\n"
                           "}\n"
                           "\n"
                           "div.headertitle {\n"
                           "}\n"
                           "\n"
                           "dl {\n"
                           "}\n"
                           "\n"
                           "/* dl.note, dl.warning, dl.attention, dl.pre, dl.post, dl.invariant, dl.deprecated, dl.todo, dl.test, dl.bug */\n"
                           "dl.section {\n"
                           "}\n"
                           "\n"
                           "dl.note {\n"
                           "}\n"
                           "\n"
                           "dl.warning, dl.attention {\n"
                           "}\n"
                           "\n"
                           "dl.pre, dl.post, dl.invariant {\n"
                           "}\n"
                           "\n"
                           "dl.deprecated {\n"
                           "}\n"
                           "\n"
                           "dl.todo {\n"
                           "}\n"
                           "\n"
                           "dl.test {\n"
                           "}\n"
                           "\n"
                           "dl.bug {\n"
                           "}\n"
                           "\n"
                           "dl.section dd {\n"
                           "}\n"
                           "\n"
                           "#projectlogo {\n"
                           "}\n"
                           " \n"
                           "#projectlogo img { \n"
                           "}\n"
                           "\n"
                           "#projectname {\n"
                           "  font: 24px Verdana,DejaVu Sans,Geneva,sans-serif;  \n"
                           "  font-weight: bold;\n"
                           "  display: inline;\n"
                           "}\n"
                           "\n"
                           "#projectbrief {\n"
                           "  font: 16px Verdana,DejaVu Sans,Geneva,sans-serif;  \n"
                           "  display: inline;\n"
                           "}\n"
                           "\n"
                           "#projectnumber {\n"
                           "  font: 16px Verdana,DejaVu Sans,Geneva,sans-serif;  \n"
                           "  display: inline;\n"
                           "}\n"
                           "\n"
                           "#titlearea {\n"
                           "  border: 0;\n"
                           "  background-color: #E6E6E6;\n"
                           "}\n"
                           "\n"
                           ".image {\n"
                           "}\n"
                           "\n"
                           ".dotgraph {\n"
                           "}\n"
                           "\n"
                           ".mscgraph {\n"
                           "}\n"
                           "\n"
                           ".diagraph {\n"
                           "}\n"
                           "\n"
                           ".caption {\n"
                           "}\n"
                           "\n"
                           "div.zoom {\n"
                           "}\n"
                           "\n"
                           "dl.citelist {\n"
                           "}\n"
                           "\n"
                           "dl.citelist dt {\n"
                           "}\n"
                           "\n"
                           "dl.citelist dd {\n"
                           "}\n"
                           "\n"
                           "div.toc {\n"
                           "}\n"
                           "\n"
                           "div.toc li {\n"
                           "}\n"
                           "\n"
                           "div.toc h3 {\n"
                           "}\n"
                           "\n"
                           "div.toc ul {\n"
                           "}       \n"
                           "\n"
                           "div.toc li.level1 {\n"
                           "}\n"
                           "\n"
                           "div.toc li.level2 {\n"
                           "}\n"
                           "\n"
                           "div.toc li.level3 {\n"
                           "}\n"
                           "\n"
                           "div.toc li.level4 {\n"
                           "}\n"
                           "\n"
                           ".inherit_header {\n"
                           "}\n"
                           "\n"
                           ".inherit_header td {\n"
                           "}\n"
                           "\n"
                           ".inherit {\n"
                           "}\n"
                           "\n"
                           "tr.heading h2 {\n"
                           "}\n"
                           "\n"
                           "/* tooltip related style info */\n"
                           "\n"
                           ".ttc {\n"
                           "}\n"
                           "\n"
                           "#powerTip {\n"
                           "}\n"
                           "\n"
                           "#powerTip div.ttdoc {\n"
                           "}\n"
                           "\n"
                           "#powerTip div.ttname a {\n"
                           "}\n"
                           "\n"
                           "#powerTip div.ttname {\n"
                           "}\n"
                           "\n"
                           "#powerTip div.ttdeci {\n"
                           "}\n"
                           "\n"
                           "#powerTip div {\n"
                           "  font: 13px/1.3 Verdana,DejaVu Sans,Geneva,sans-serif;\n"
                           "  color: #363534;\n"
                           "}\n"
                           "\n"
                           "#powerTip:before, #powerTip:after {\n"
                           "}\n"
                           "\n"
                           "#powerTip.n:after,  #powerTip.n:before,\n"
                           "#powerTip.s:after,  #powerTip.s:before,\n"
                           "#powerTip.w:after,  #powerTip.w:before,\n"
                           "#powerTip.e:after,  #powerTip.e:before,\n"
                           "#powerTip.ne:after, #powerTip.ne:before,\n"
                           "#powerTip.se:after, #powerTip.se:before,\n"
                           "#powerTip.nw:after, #powerTip.nw:before,\n"
                           "#powerTip.sw:after, #powerTip.sw:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.n:after,  #powerTip.s:after,\n"
                           "#powerTip.w:after,  #powerTip.e:after,\n"
                           "#powerTip.nw:after, #powerTip.ne:after,\n"
                           "#powerTip.sw:after, #powerTip.se:after {\n"
                           "}\n"
                           "\n"
                           "#powerTip.n:before,  #powerTip.s:before,\n"
                           "#powerTip.w:before,  #powerTip.e:before,\n"
                           "#powerTip.nw:before, #powerTip.ne:before,\n"
                           "#powerTip.sw:before, #powerTip.se:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.n:after,  #powerTip.n:before,\n"
                           "#powerTip.ne:after, #powerTip.ne:before,\n"
                           "#powerTip.nw:after, #powerTip.nw:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.n:after, #powerTip.ne:after, #powerTip.nw:after {\n"
                           "}\n"
                           "#powerTip.n:before {\n"
                           "}\n"
                           "#powerTip.n:after, #powerTip.n:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.nw:after, #powerTip.nw:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.ne:after, #powerTip.ne:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.s:after,  #powerTip.s:before,\n"
                           "#powerTip.se:after, #powerTip.se:before,\n"
                           "#powerTip.sw:after, #powerTip.sw:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.s:after, #powerTip.se:after, #powerTip.sw:after {\n"
                           "}\n"
                           "\n"
                           "#powerTip.s:before, #powerTip.se:before, #powerTip.sw:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.s:after, #powerTip.s:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.sw:after, #powerTip.sw:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.se:after, #powerTip.se:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.e:after, #powerTip.e:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.e:after {\n"
                           "}\n"
                           "\n"
                           "#powerTip.e:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.w:after, #powerTip.w:before {\n"
                           "}\n"
                           "\n"
                           "#powerTip.w:after {\n"
                           "}\n"
                           "\n"
                           "#powerTip.w:before {\n"
                           "}\n"
                           "\n"
                           "/* tabs.css */\n"
                           "\n"
                           ".tabs, .tabs2, .tabs3 {\n"
                           "  background: none;\n"
                           "  background-color: #F6F6F6;\n"
                           "  font: 13px Verdana,DejaVu Sans,Geneva,sans-serif;\n"
                           "  border-bottom: 1px solid #E6E6E6;\n"
                           "}\n"
                           "\n"
                           ".tabs2 {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           ".tabs3 {\n"
                           "  font-size: 13px;\n"
                           "}\n"
                           "\n"
                           ".tablist {\n"
                           "}\n"
                           "\n"
                           ".tablist li {\n"
                           "  background: none;\n"
                           "  line-height: 1.5;\n"
                           "}\n"
                           "\n"
                           ".tablist a {\n"
                           "  padding: 0 10px;\n"
                           "  font-weight: normal;\n"
                           "  background: none;\n"
                           "  color: #00732F;\n"
                           "  text-shadow: none;\n"
                           "}\n"
                           "\n"
                           ".tabs3 .tablist a {\n"
                           "}\n"
                           "\n"
                           ".tablist a:hover {\n"
                           "  background: none;\n"
                           "  color: #00732F;\n"
                           "  text-shadow: none;\n"
                           "}\n"
                           "\n"
                           ".tablist li.current a {\n"
                           "  background: none;\n"
                           "  color: #00732F;\n"
                           "  text-shadow: none;\n"
                           "}\n"
                           "\n"
                           "/* navtree.css */\n"
                           "\n"
                           "#nav-tree .children_ul {\n"
                           "}\n"
                           "\n"
                           "#nav-tree ul {\n"
                           "}\n"
                           "\n"
                           "#nav-tree li {\n"
                           "}\n"
                           "\n"
                           "#nav-tree .plus {\n"
                           "}\n"
                           "\n"
                           "#nav-tree .selected {\n"
                           "  background: none;\n"
                           "  background-color: #E6E6E6;\n"
                           "  color: #00732F;\n"
                           "  text-shadow: none;\n"
                           "}\n"
                           "\n"
                           "#nav-tree img {\n"
                           "}\n"
                           "\n"
                           "#nav-tree a {\n"
                           "}\n"
                           "\n"
                           "#nav-tree .label {\n"
                           "  font: 12px Verdana,DejaVu Sans,Geneva,sans-serif;\n"
                           "}\n"
                           "\n"
                           "#nav-tree .label a {\n"
                           "}\n"
                           "\n"
                           "#nav-tree .selected a {\n"
                           "  color: #00732F;\n"
                           "}\n"
                           "\n"
                           "#nav-tree .children_ul {\n"
                           "}\n"
                           "\n"
                           "#nav-tree .item {\n"
                           "}\n"
                           "\n"
                           "#nav-tree {\n"
                           "  background-color: #F6F6F6; \n"
                           "}\n"
                           "\n"
                           "#doc-content {\n"
                           "}\n"
                           "\n"
                           "#side-nav {\n"
                           "}\n"
                           "\n"
                           ".ui-resizable .ui-resizable-handle {\n"
                           "}\n"
                           "\n"
                           ".ui-resizable-e {\n"
                           "  background: none;\n"
                           "  background-color: #E6E6E6;\n"
                           "}\n"
                           "\n"
                           ".ui-resizable-handle {\n"
                           "}\n"
                           "\n"
                           "#nav-tree-contents {\n"
                           "}\n"
                           "\n"
                           "#nav-tree {\n"
                           "  background: none;\n"
                           "  background-color: #F6F6F6;\n"
                           "}\n"
                           "\n"
                           "#nav-sync {\n"
                           "}\n"
                           "\n"
                           "#nav-sync img {\n"
                           "}\n"
                           "\n"
                           "#nav-sync img:hover {\n"
                           "}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 40, 540, 540))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("source/chessboard.jpg"))
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(77, 30, 128, 128))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(123)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("source/avatar/1.png"))
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(47, 160, 202, 66))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 30, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(257, 30, 20, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(17, 290, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(17, 20, 250, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 36, 36))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("source/black.png"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(47, 450, 202, 66))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(17, 300, 250, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(257, 310, 20, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 530, 36, 36))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("source/white.png"))
        self.label_5.setObjectName("label_5")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(17, 580, 251, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(77, 320, 128, 128))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(123)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("source/avatar/1.png"))
        self.label_12.setObjectName("label_12")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(10, 310, 20, 281))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 230, 101, 51))
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(140, 520, 101, 51))
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 230, 61, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 520, 61, 51))
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 590, 543, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("font: 16pt \"华文行楷\";\n"
                                        "background-image: url(\"/source/button.png\");")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(850, 20, 301, 601))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_3.addWidget(self.lcdNumber_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setEnabled(True)
        self.comboBox.setTabletTracking(False)
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.layoutWidget.raise_()
        self.label_2.raise_()
        self.lcdNumber.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        self.label_11.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.label_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.label_5.raise_()
        self.line_7.raise_()
        self.label_12.raise_()
        self.line_8.raise_()
        self.lcdNumber_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label.setBuddy(self.listView)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "昵称:  \n"
                                                "积分：0      级别：0    \n"
                                                "总盘数：0    游戏币：0    \n"
                                                "胜：0     负：0    平：0  "))
        self.label_4.setText(_translate("Form", "昵称:  \n"
                                                "积分：0      级别：0    \n"
                                                "总盘数：0    游戏币：0    \n"
                                                "胜：0     负：0    平：0  "))
        self.label_7.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">倒计时：</span></p></body></html>"))
        self.label_8.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">倒计时：</span></p></body></html>"))
        self.pushButton_6.setText(_translate("Form", "设置"))
        self.pushButton_2.setText(_translate("Form", "悔棋"))
        self.pushButton_4.setText(_translate("Form", "匹配对手"))
        self.pushButton_3.setText(_translate("Form", "和棋"))
        self.pushButton_5.setText(_translate("Form", "认输"))
        self.label_6.setText(_translate("Form", "在线人数："))
        self.label_9.setText(_translate("Form", "在线列表："))
        self.comboBox.setItemText(0, _translate("Form", "大家好，很高兴见到各位！"))
        self.comboBox.setItemText(1, _translate("Form", "快点吧，我等到花儿也谢了。"))
        self.comboBox.setItemText(2, _translate("Form", "你的牌打得太好了！"))
        self.comboBox.setItemText(3, _translate("Form", "我们交个朋友吧，能告诉我你的联系方法吗？"))
        self.comboBox.setItemText(4, _translate("Form", "各位，真不好意思，我要离开一会。"))
        self.comboBox.setItemText(5, _translate("Form", "又断线了，网络怎么这么差啊！"))
        self.comboBox.setItemText(6, _translate("Form", "不要吵了，有什么好吵的，专心玩游戏吧。"))
        self.comboBox.setItemText(7, _translate("Form", "你是MM，还是GG？"))
        self.comboBox.setItemText(8, _translate("Form", "下次再玩吧，我要走了。"))
        self.comboBox.setItemText(9, _translate("Form", "再见了，我会想念大家的。"))
        self.comboBox.setItemText(10, _translate("Form", "和你合作真是太愉快啦。"))
        self.comboBox.setItemText(11, _translate("Form", "不要走，决战到天亮。"))
        self.pushButton.setText(_translate("Form", "发送"))
