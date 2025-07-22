from os import error
import os.path
from string import whitespace
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUiType
import matplotlib.pyplot as plt
from transformationutils import Transformation

ui_path = os.path.dirname(os.path.abspath(__file__))
ui, _ = loadUiType(os.path.join(ui_path, "window.ui"))

class main(QMainWindow, ui):
    def __init__(self, parent=None):
        '''initialize main window'''
        super(main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitBE()
        self.InitUI() # bind elements to events
        self.show()

    def InitBE(self):
        self._index = 0
        self._points = [
            [0.0,0.0,0.0],
            [0.0,0.0,0.0],
            [0.0,0.0,0.0]
            ]
        self._points_t = None

        self.widget.canvas.axes.axhline(linewidth=0.01, color=(0, 0, 0, 0.5))
        self.widget.canvas.axes.axvline(linewidth=0.01, color=(0, 0, 0, 0.5))
        self.widget.plot(0, 0)
        self.widget.canvas.draw()
        #clear the table too
        try:
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(str("X;Y").split(";"))
            #self.tableWidget.setRowCount(0)
        except Exception:
            pass

    def InitUI(self):
        self.pushButton_previous.clicked.connect(self.previous)
        self.pushButton_next.clicked.connect(self.next)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_plot.clicked.connect(self.plot)
        self.pushButton_clear.clicked.connect(self.clear)

        self.lineEdit_x_translate.textEdited.connect(self.transform)
        self.lineEdit_y_translate.textEdited.connect(self.transform)

        self.lineEdit_x_point.textEdited.connect(self.save_point)
        self.lineEdit_y_point.textEdited.connect(self.save_point)

        self.doubleSpinBox_x_scale.valueChanged.connect(self.transform)
        self.doubleSpinBox_y_scale.valueChanged.connect(self.transform)

        self.doubleSpinBox_rotate.valueChanged.connect(self.transform)

    def save_point(self):
        #print('save point')
        self._x = self.ff(0.0)(self.lineEdit_x_point.text().lstrip().rstrip())
        self._y = self.ff(0.0)(self.lineEdit_y_point.text().lstrip().rstrip())

        self._currentPoint = [self._x, self._y]

        self._points[self._index] = [self._x, self._y, 1]
        for i in range(2):
            item = QTableWidgetItem(str(self._currentPoint[i]))
            self.tableWidget.setItem(self._index, i, item)

    def previous(self):
        self.save_point()
        if self._index > 0:
            self._index -= 1
            #print(self._index)
            self.labelIndex.setText('Current Index: '+ str(self._index))
        else:
            #disable previous button
            pass
        self._currentPoint = self._points[self._index]
        if self._currentPoint == [0.0, 0.0, 0.0]:
            #if the current point retrieved is 0, 0
            self.lineEdit_x_point.clear()
            self.lineEdit_y_point.clear()
        else:
            #if the current point is not 0, 0
            self.lineEdit_x_point.setText(str(self._currentPoint[0]))
            self.lineEdit_y_point.setText(str(self._currentPoint[1]))
    
    def ff(self, default_value=0.0):
        def to_float(var):
            #print('check input')
            if var is None or var in whitespace:
                return default_value
            elif var == '-':
                return -1
            else:
                return float(var)
        return to_float

    def text(self, object):
        try:
            return object.text().lstrip().rstrip()
        except error:
            pass
    def spinBoxText(self, object):
        pass

    def next(self):
        self.save_point()
        self._index += 1
        #print(self._index)
        self.labelIndex.setText('Current Index: '+ str(self._index))
        # every time index changes, display new index in its label

        #check if the values at this index is not zero, then fill into lineedit
        if self._index < len(self._points):
            self._currentPoint = self._points[self._index]
            if self._currentPoint == [0.0, 0.0, 0.0]:
                #if the current point retrieved is 0, 0
                self.lineEdit_x_point.clear()
                self.lineEdit_y_point.clear()
            else:
                #if the current point is not 0, 0
                self.lineEdit_x_point.setText(str(self._currentPoint[0]))
                self.lineEdit_y_point.setText(str(self._currentPoint[1]))
        else:
            # if the array does not have enough rows
            self._points.append([0.0, 0.0, 0.0])
            #bind th elength of the numpy array to the length of the tablewidget
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            #clear lineEdits
            self.lineEdit_x_point.clear()
            self.lineEdit_y_point.clear()
    def save(self):
        pass
    def transform(self):
        self._tx, self._ty = map(self.ff(0.0), (self.text(self.lineEdit_x_translate), self.text(self.lineEdit_y_translate)))
        self._rt = self.doubleSpinBox_rotate.value()
        self._sx, self._sy = map(self.ff(1.0), (self.text(self.doubleSpinBox_x_scale), self.text(self.doubleSpinBox_y_scale)))
        # if the points are less than 3, wait until points are up to 3
        #if not self._points_t:
        #    self._points_t = Transformation(self._points)
        
        self._points_t = Transformation(self._points)

        self._points_t.translate(self._tx, self._ty)
        self._points_t.scale(self._sx, self._sy)
        self._points_t.rotate(self._rt)
        self.plot(transform=True)

    def plot(self, transform=False):
        #plot graph
        # get points from self._points
        # if transform, retain raw plot and draw new plot alonngside
        # if not transform, clear canvas and plot new points as raw
        try:
            self.widget.clear_canvas()
        except Exception:
            pass

        if not self._points_t:
            self._points_t = Transformation(self._points)
        if not transform:
            # plotting raw data
            x0, y0, *_ = list(map(list, zip(*self._points)))
            x1, y1 = [], []
            tup = (x0, y0)
        else:
            x0, y0, *_ = list(map(list, zip(*self._points_t.matrix)))
            x1, y1, *_ = list(map(list, zip(*self._points_t._matrix)))
            tup = (x0, y0, x1, y1)
        for l in tup:
            l += [l[0]]

        self.widget.plot(x0, y0, 'g')
        self.widget.plot(x1, y1, 'b')

        self.widget.canvas.axes.axhline(linewidth=0.01, color=(0, 0, 0, 0.1))
        self.widget.canvas.axes.axvline(linewidth=0.01, color=(0, 0, 0, 0.1))

        self.widget.canvas.axes.set_aspect('equal', adjustable='datalim')
        self.widget.canvas.draw()

    def clear(self):
        #clear canvas
        #clear tableWidget
        self.widget.clear_canvas()
        self._index = 0
        #create onChanged signals
        self.labelIndex.setText('Current Index: '+ str(self._index))
        self.InitBE()
        #also remove the extra row

if __name__ == "__main__":
    app = QApplication([])

    app.setStyle('Plastique')
    window = main()
    app.exec_()