import sys 
import _pickle as cPickle
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer 
from mainwindowReclamo import Ui_MainWindow
from widgetReclamos import Ui_Form
from editorReclamo import Ui_Dialog

#Este es el Pop de opciones del  Reclamo
class Reclamo(QDialog, Ui_Dialog):
	"""docstring for Reclamo"""
	def __init__(self,*args,**kwargs):
		QDialog.__init__(self,*args,**kwargs)
		self.setupUi(self)

		#Diccionario para Almacenar los datos que se muestran
		#en el editor
		self.front = {
		"Venta": "Ingrese Venta",
		"Nombre": "Ingrese Nombre",
		"Estado": "Ingrese Estado",
		"Devolucion": "textDevolucion"
		}
		self.back = {
		"Direccion": "Ingrese Direccion",
		"DNI": "Ingrese DNI",
		"Nota":"Ingrese Nota",
		"Llave": 0
		}

		#Leo los datos del Diccionario, y completo
		#los campos
		self.Completar()

		#Conecto Botones
		self.botonGuardar.clicked.connect(self.guardarReclamo)
	
	#Leo los datos, y completo la ficha para el usuario
	def Completar(self):
		self.lineEdit.setPlaceholderText(self.front["Venta"])
		self.lineEdit.setText(self.front["Venta"])
		self.lineEdit_2.setPlaceholderText(self.front["Nombre"])
		self.lineEdit_2.setText(self.front["Nombre"])
		self.lineEdit_3.setPlaceholderText(self.back["Direccion"])
		self.lineEdit_3.setText(self.back["Direccion"])
		self.lineEdit_4.setPlaceholderText(self.back["DNI"])
		self.lineEdit_4.setText(self.back["DNI"])
		self.textEdit.setText(self.back["Nota"])
	
	#Obtengo valores desde la venta Principal
	def ObtenerValores(self, data1=None, data2=None):
		self.front = data1
		self.back = data2
		self.Completar()

	#Guardo los datos ingresados, en el Diccionario	
	def guardarReclamo(self):
		self.front["Venta"] = self.lineEdit.text()
		self.front["Nombre"] = self.lineEdit_2.text()
		self.back["Direccion"] = self.lineEdit_4.text()
		self.back["DNI"] = self.lineEdit_3.text()
		self.front["Estado"] = self.comboBox.currentText()
		self.front["Devolucion"] = self.comboBox_2.currentText()
		self.back["Nota"] = self.textEdit.toPlainText()
		self.close()

	#Devuelvo los datos al widget del reclamo
	def enviarReclamoFront(self):
		self.guardarReclamo()
		return self.front
	#Devuelvo los datos al widget 	
	def enviarReclamoBack(self):
		self.guardarReclamo()
		return self.back

#Este es el Widget de reclamo, que aparece en la lista de Main window		
class WidgetReclamo(QWidget, Ui_Form):
	"""docstring for ClassName"""
	def __init__(self,*args,**kwargs):
		QWidget.__init__(self,*args,**kwargs)
		self.setupUi(self)

		#Diccionario para Almacenar los datos que se muestran
		#en la pantalla principal
		self.front = {
		"Venta": "textVenta",
		"Nombre": "textNombre",
		"Estado": "textEstado",
		"Devolucion": "textDevolucion"
		}
		self.back = {
		"Direccion": "Ingrese Direccion",
		"DNI": "Ingrese DNI",
		"Nota":"Ingrese Nota",
		"Llave": 0
		}
		#Creo el Editor
		self.Dialog = Reclamo(self)
		#Actualizo datos
		self.Actualizar()

		#Conecto los Botones
		self.pushButton.clicked.connect(self.Editor)
	#Tomo datos del popUp
	def TomarDatosFront(self):
		self.front = self.Dialog.enviarReclamoFront()
	def TomarDatosBack(self):
		self.back = self.Dialog.enviarReclamoBack()
	#Llamo al Editor de Opciones del reclamo
	def Editor(self):
		self.Dialog.exec_()
		#Tomo los datos
		self.TomarDatosFront()
		self.TomarDatosBack()
		#Actualizo la lista con los datos del Front
		self.Actualizar()
	#Actualizo el widget
	def Actualizar(self):
		self.infoVenta.setText(self.front["Venta"])
		self.infoEstado.setText(self.front["Estado"])
		self.infoNombre.setText(self.front["Nombre"])
		self.labelDevolucion.setText(self.front["Devolucion"])
		#Envio los datos al Dialog
		self.Dialog.ObtenerValores(self.front,self.back)
	#Envio los datos al Main
	def EnviarDatosFront(self):
		#self.TomarDatosFront()
		return self.front
	#Envio los datos back al Main
	def EnviarDatosBack(self):
		#self.TomarDatosBack()
		return self.back

	def ObtenerValores(self,data1=None,data2=None):
		self.front = data1
		self.back = data2
		self.Dialog.ObtenerValores(self.front, self.back)
		self.Actualizar()



		
#Ventana principal, la columna del programa
class ProgramaReclamos(QMainWindow, Ui_MainWindow): 
	def __init__(self,*args,**kwargs):
		QMainWindow.__init__(self,*args,**kwargs)
		self.setupUi(self)
	#Defino las varaibles
		#Almaceno los DATOS de los reclamos 
		#sin resolver
		self.BaseDatosSinRevoler = []

		#Almaceno los Reclamos sin Resolver
		self.dictItems = {}

		#Almaceno los Reclamos resueltos
		self.dictItemsResueltos = {}
		#Creo el widget
		self.Item_Widget = WidgetReclamo()
		#Lo utilizo como axuliar para poder guardar y cargar
		#la info en un archivo
		self.front = {
		"Venta": "Ingrese Venta",
		"Nombre": "Ingrese Nombre",
		"Estado": "Ingrese Estado",
		"Devolucion": "textDevolucion"
		}
		self.back = {
		"Direccion": "Ingrese Direccion",
		"DNI": "Ingrese DNI",
		"Nota":"Ingrese Nota",
		"Llave": 0
		}

		self.Info ={"front":self.front , "back":self.back}

	#Inicio un contador para guardar cada 60 secs
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.GuardarBase)
		self.timer.start(60000)
		
	#Llamo a las funciones iniciales
		self.LeerBase()
		self.LeerBaseResueltos()
		#self.ActualizarLista()
		self.CargarReclamos()

	#Conecto botones
		self.pushButton_2.clicked.connect(self.AbrirReclamo)
		self.pushButton_4.clicked.connect(self.GuardarBase)

	#Agrego un reclamo vacio a la lista, para que sea editado
	#La llave es un numero tomado del dict de Items
	def AbrirReclamo(self):
		#I will store the items on a dict. I will read how many there are
		cont = len(self.dictItems)
		#and store a new QListWidgetItem in each entrey
		self.dictItems[cont] = QtWidgets.QListWidgetItem(self.listWidget)
		#I build my custom wdiget
		self.Item_Widget = WidgetReclamo()
		self.dictItems[cont].setSizeHint(self.Item_Widget.size())
		self.listWidget.addItem(self.dictItems[cont])
		self.listWidget.setItemWidget(self.dictItems[cont], self.Item_Widget)
		#print(self.dictItems[cont])

	
	#Actualiza la lista de reclamos
	def ActualizarLista(self):
		print("Borro la lista")
		
		for key in self.dictItems:
			self.listWidget.addItem(self.dictItems[key])
			self.listWidget.setItemWidget(self.dictItems[key],self.Item_Widget)

	#Cargo los reclamos del archivo
	def CargarReclamos(self):
		#print(len(self.BaseDatosSinRevoler))
		for key in self.BaseDatosSinRevoler:
			self.AbrirReclamo()
			data1 = self.BaseDatosSinRevoler[key]["front"]
			data2 = self.BaseDatosSinRevoler[key]["back"]
			self.listWidget.itemWidget(self.listWidget.item(key)).ObtenerValores(data1, data2)
		#self.ActualizarLista()

	def Borrar(self):
			pass	
	#Este Reclamo "resuelve le reclamo".
	#Lo pasa de sin resolver, a Resueltos.
	def Resolver(self):
		pass

	#Primero tengo que tomar toda la informacion de los reclamos
	#Pasarlos a un diccionario, y ahi recien puedo guardarlo.
	def GuardarBase(self):
		#Guardo los Reclamos sin Resolver
		for key in range(self.listWidget.count()):

		with open("BaseDatosSinRevoler", 'wb') as fp:
			cPickle.dump(self.BaseDatosSinRevoler, fp)
		print("Guardando la base")
	
	#Lee una base de datos Cpickle, si no existe, la crea.
	def LeerBase(self):
		FlagEOF = 0
		#Pruebo si existe la Base, sino, la creo.
		try:
			fp = open("BaseDatosSinRevoler","rb")
			while FlagEOF == 0 :
				try:

					self.BaseDatosSinRevoler = cPickle.load(fp)
					#print(self.BaseDatosSinRevoler)
				except EOFError:
					FlagEOF = 1
					fp.close()
				
		except FileNotFoundError:
			fp = open("BaseDatosSinRevoler","wb")
			fp.close()
	def LeerBaseResueltos(self):
		FlagEOF = 0
		try:
			fp = open("BaseDatosResueltos","rb")
			while FlagEOF == 0 :
				try:
					self.BaseDatosResueltos = cPickle.load(fp)
				except EOFError:
					FlagEOF = 1
					fp.close()
				
		except FileNotFoundError:
			fp = open("BaseDatosResueltos","wb")
			fp.close()
		
	
	def Almacenar(self):
		pass
if __name__ == '__main__':
	app = QApplication(sys.argv)
	prog = ProgramaReclamos()
	prog.show()
	sys.exit(app.exec_())