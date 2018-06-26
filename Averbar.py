import os.path, time, glob, shutil
import datetime
#cttime
#print("last modified: %s" % time.ctime(os.path.getmtime(file)))
#print "Mes: %d" % now.month

now = datetime.datetime.now()
dia = now.day
mes = now.month
ano = now.year
d = datetime.date(ano,mes,dia)

pasta1 = "C:\\NFE\\Exportadas\\EmissorFlagCTe\\05975316000112\\xmlEnviado\\Autorizados\\Protocolo\\"

if mes < 10:
	mes2 = '0'+str(mes)
else:
	mes2 = mes
	
pasta11 = pasta1 +str(ano)+str(mes2)+"\\"
formato = d.strftime("%a %b %d")

arquivos = os.listdir(pasta11)
pastaaverbar = "C:\\ATM\\ATM_SDOCe\\Averbar\\11320377"

for file in arquivos:
	if file.endswith(".xml"):
		ncc = pasta11 + file
		gg = str(time.ctime(os.path.getctime(ncc)))
		if formato in gg:
			print str(ncc)
			shutil.copy(ncc,pastaaverbar)

pasta22 = "D:\\Users\\Administrador\\Desktop\\AVERBAR\\XML\\"
arquivos2 = os.listdir(pasta22)
for file2 in arquivos2:
	if file2.endswith(".xml"):
		ncc2 = pasta22 + file2
		gg2 = str(time.ctime(os.path.getctime(ncc2)))
		if formato in gg2:
			print str(ncc2)
			caminhocd = pasta22 + file2
			shutil.move(ncc2,pastaaverbar)