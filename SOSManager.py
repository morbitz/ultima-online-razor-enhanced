#===============================================#
#                   SOS Manager                 #
#===============================================#
#                                               #
#   Author: CookieLover                         #
#   Latest Release: 10/07/2017                  #
#                                               #
#===============================================#
#                                               #
#   Info:                                       #
#   - by selecting a SOS and hitting Move       #
#     all the SOS in that sector will be moved  #
#     in the targeted container                 #
#                                               #
#   What you need:                              #
#   - a bag full of SOS                         #
#                                               #
#   Credits:                                    #
#   the degrees - coordinates formula is taken  #   
#   from Enhanced Map                           #
#                                               #
#===============================================#




import clr, math
from datetime import datetime

clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')

import System
from System.Collections.Generic import List
from System.Drawing import Point, Color, Size
from System.Windows.Forms import (Application, Button, Form, BorderStyle, 
    Label, FlatStyle, DataGridView, DataGridViewAutoSizeColumnsMode,
    DataGridViewSelectionMode, DataGridViewEditMode, CheckBox)
from System.Data import DataTable

class SOS(object):
    x = y = 0
    serial = 0
    def __init__(self, _serial, _x, _y):
        
        self.serial = _serial
        self.x = _x
        self.y = _y
        
class SOSManager(Form):
    CurVer = '1.0.1'
    ScriptName = 'SOS Manager'

    SOSBag = None
    SOS = []
    
    def __init__(self, bag):
        self.SOSBag = bag
        self.MapCatalogue()
        
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.Size = Size(300, 404)
        self.Text = '{0} - v{1}'.format(self.ScriptName, self.CurVer)
                
        self.DataGridSetup()

        self.btnRemove = Button()
        self.btnRemove.Text = 'Remove'
        self.btnRemove.BackColor = Color.FromArgb(50,50,50)
        self.btnRemove.Location = Point(180, 328)
        self.btnRemove.Size = Size(60, 30)
        self.btnRemove.FlatStyle = FlatStyle.Flat
        self.btnRemove.FlatAppearance.BorderSize = 1
        self.btnRemove.Click += self.btnRemovePressed
        
        self.btnMove = Button()
        self.btnMove.Text = 'Move'
        self.btnMove.BackColor = Color.FromArgb(50,50,50)
        self.btnMove.Location = Point(110, 328)
        self.btnMove.Size = Size(60, 30)
        self.btnMove.FlatStyle = FlatStyle.Flat
        self.btnMove.FlatAppearance.BorderSize = 1
        self.btnMove.Click += self.btnMovePressed
        
        self.btnOpen = Button()
        self.btnOpen.Text = 'Open'
        self.btnOpen.BackColor = Color.FromArgb(50,50,50)
        self.btnOpen.Location = Point(40, 328)
        self.btnOpen.Size = Size(60, 30)
        self.btnOpen.FlatStyle = FlatStyle.Flat
        self.btnOpen.FlatAppearance.BorderSize = 1
        self.btnOpen.Click += self.btnOpenPressed
        
        self.Controls.Add(self.DataGrid)
        self.Controls.Add(self.btnOpen)
        self.Controls.Add(self.btnMove)
        self.Controls.Add(self.btnRemove)

    def DataGridSetup(self):
        self.DataGrid = DataGridView()
        self.DataGrid.RowHeadersVisible = False
        self.DataGrid.MultiSelect = False
        self.DataGrid.SelectionMode = DataGridViewSelectionMode.FullRowSelect
        self.DataGrid.BackgroundColor = Color.FromArgb(25,25,25)
        self.DataGrid.RowsDefaultCellStyle.BackColor = Color.Silver
        self.DataGrid.AlternatingRowsDefaultCellStyle.BackColor = Color.Gainsboro
        self.DataGrid.ForeColor = Color.FromArgb(25,25,25)
        self.DataGrid.Location = Point(20, 12)
        self.DataGrid.Size = Size(240, 306)
        self.DataGrid.DataSource = self.Data()
        self.DataGrid.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells
        self.DataGrid.EditMode = DataGridViewEditMode.EditProgrammatically
        self.DataGrid.BorderStyle = BorderStyle.None
     
    def btnOpenPressed(self, sender, args):
        row = self.DataGrid.SelectedCells[0].RowIndex
        
        if row == -1:
            Misc.SendMessage('{0}: No row selected.'.format(self.ScriptName), 33)
            return
            
        col = self.DataGrid.SelectedCells[0].ColumnIndex
        serial = self.DataGrid.Rows[row].Cells[col].Value
        
        Items.UseItem(int(serial, 0))
    
    def btnMovePressed(self, sender, args):
        row = self.DataGrid.SelectedCells[0].RowIndex
        
        if row == -1:
            Misc.SendMessage('{0}: No row selected.'.format(self.ScriptName), 33)
            return
            
        col = self.DataGrid.SelectedCells[3].ColumnIndex
        sector = self.DataGrid.Rows[row].Cells[col].Value
        Misc.SendMessage('{0}: Select the bag in which to put the sos.'.format(self.ScriptName), 67)
        bag = Target.PromptTarget()
        if bag == -1:
            Misc.SendMessage('{0}: No bag selected.'.format(self.ScriptName), 33) 
        Misc.SendMessage('{0}: Please wait until the process is complete.'.format(self.ScriptName), 67)
        self.MoveAll(sector, bag)
        
        
    def btnRemovePressed(self, sender, args):
        row = self.DataGrid.SelectedCells[0].RowIndex
        
        if row == -1:
            Misc.SendMessage('{0}: No row selected.'.format(self.ScriptName), 33)
            return
            
        col = self.DataGrid.SelectedCells[0].ColumnIndex
        serial = self.DataGrid.Rows[row].Cells[col].Value
        
        self.DeleteRow(serial)
    
    def MoveAll(self, sector, bag):
        rows = []
        for r in xrange(self.DataGrid.DataSource.Rows.Count):
            row = self.DataGrid.DataSource.Rows[r]
            
            if row['Sector'] == sector:
                Items.Move(int(row['ID'], 0), bag, 0)
                rows.append(row)
                Misc.Pause(600)
                
        for r in rows:
            self.DataGrid.DataSource.Rows.Remove(r)
            
        Misc.SendMessage('{0}: Moving process complete.'.format(self.ScriptName), 67)
                
    def DeleteRow(self, serial):
        for r in xrange(self.DataGrid.DataSource.Rows.Count):
            row = self.DataGrid.DataSource.Rows[r]
            if row['ID'] == serial:
                self.DataGrid.DataSource.Rows.Remove(row)
                return
            
    def Data(self):
        data = DataTable()
        data.Columns.Add('ID', clr.GetClrType(str))
        data.Columns.Add('X', clr.GetClrType(int))
        data.Columns.Add('Y', clr.GetClrType(int))
        data.Columns.Add('Sector', clr.GetClrType(str))
        
        for sos in self.SOS:
            sector = self.GetSector(sos.x, sos.y)
            data.Rows.Add(hex(sos.serial), sos.x, sos.y, sector)
        
        Misc.SendMessage('{0}: SOS Data has been loaded.'.format(self.ScriptName), 67)   
        return data
    
    def MapCatalogue(self):
        sosbag = Items.FindBySerial(self.SOSBag)
        Items.WaitForContents(sosbag, 8000)
        Misc.Pause(600)
        csv_lines = []
        
        for i in sosbag.Contains:
            if i.ItemID == 0x14EE:
                Gumps.ResetGump()
                Items.UseItem(i)
                Gumps.WaitForGump(1426736667, 3000)
                
                if Gumps.CurrentGump() != 1426736667 or Gumps.LastGumpGetLineList().Count < 3:
                    Misc.SendMessage('{0}: Gump error. Retry once.'.format(self.ScriptName), 33)
                    
                    if self.LoadRetry(i):
                        Misc.SendMessage('{0}: Gump error. Skipped.'.format(self.ScriptName), 33)
                        continue
                    
                line = Gumps.LastGumpGetLine(2)
                degrees = line.replace('°', '|').replace('\'', "|").replace(',', '|').split('|')
                lat = int(degrees[0]) + int(degrees[1]) * .01
                lon = int(degrees[3]) + int(degrees[4]) * .01
                dir1 = degrees[2]
                dir2 = degrees[5]
                x, y = self.MapXY(lat, lon, dir1, dir2)
                csv_lines.append((x, y))

                self.SOS.append(SOS(i.Serial, x, y))
                Gumps.SendAction(1426736667, 0)
                Misc.Pause(600)

        epoch_secs = str((datetime.now() - datetime.utcfromtimestamp(0)).total_seconds())[:10]
        filename = 'C:\\Users\\athl33t\\Documents\\uo\\aaabooty_{}'.format(epoch_secs)
        with open(filename, 'w') as fp:
            for xy in csv_lines:
                fp.write('<Marker Name="7" X="{}" Y="{}" Icon="LEVEL3" Facet="0" Identifier="aaabooty"/>\n'.format(xy[0], xy[1]))

    
    def LoadRetry(self, sos):
        Misc.Pause(600)
        Gumps.ResetGump()
        Items.UseItem(sos)
        Gumps.WaitForGump(1426736667, 3000)
        
        if Gumps.CurrentGump() != 1426736667 or Gumps.LastGumpGetLineList().Count < 3:
            return True
            
        return False
            
    def MapXY(self, lat, lon, dir1, dir2):
        if dir1 == 'S':
            y = math.floor(lat) * 60. + lat % 1. * 100.
        else:
            y = -1.0 * math.ceil(lat) * 60. + lat % 1. * 100.
        y = int(y / 21600. * 4096.) + 1624
        
        if y < 0:
            y += 4096
        if y >= 4096:
            y -= 4096
            
        if dir2 == 'E':
            x = math.floor(lon) * 60. + lon % 1. * 100.
        else:
            x = -1.0 * math.ceil(lon) * 60. + lon % 1. * 100.
            
        x = int(x / 21600. * 5120.) + 1323
        
        if x < 0:
            x += 5120
        if x >= 5120:
            x -= 5120

        return x, y

    def GetSector(self, x, y):
        if x < 1385 and 0 <= y < 1280:
            return 'Yew'
        elif x < 1000 and 1280 <= y < 2027:
            return 'Shame'
        elif x < 1000 and 2036 <= y < 2450:
            return 'Skara'
        elif x < 1300 and 2450 <= y < 3200:
            return 'Destard'
        elif x < 1900 and 3200 <= y <= 4096:
            return 'Jhelom'
        elif 1385 <= x < 2690 and y < 900:
            return 'Wrong'
        elif 1385 <= x < 2100 and 1280 <= y < 2030:
            return 'Britain'
        elif 2100 <= x < 2690 and 1280 <= y < 2030:
            return 'Cove'
        elif 1385 <= x < 2690 and 2030 <= y < 3075:
            return 'Trinsic'
        elif 1900 <= x < 2690 and 3075 <= y <= 4096:
            return 'Valor'
        elif 2580 <= x < 3250 and y < 1890:
            return 'Vesper'
        elif 3250 <= x < 4100 and y < 1890:
            return "Nujel'm"
        elif 2100 <= x < 3850 and 1890 <= y < 3075:
            return 'Bucca'
        elif 2690 <= x < 3850 and 3075 <= y <= 4096:
            return 'Fire'
        elif x >= 4100 and y < 1890:
            return 'Moonglow'
        elif x >= 3850 and 1890 <= y < 2890:
            return 'Sea Market'
        elif x >= 3850 and y >= 2890:
            return 'Hythloth'
        else:
            return 'None'

Misc.SendMessage('Select the SOS container.', 67)
sbag = Target.PromptTarget()
if sbag > -1:
    SH = SOSManager(sbag)
    Application.Run(SH)