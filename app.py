import os
import pickle
import PySimpleGUI as sg
sg.ChangeLookAndFeel('Dark')

class Gui:
	def __init__(self):
		self.layout = [ [sg.Text('Search Term',size =(10,1)),sg.Input(size =(45,1),focus = True,key ="TERM"),sg.Radio("contains",group_id ="choice",key="CONTAINS",default = True),sg.Radio("Startswith", group_id="choice",key="STARTSWITH"),
		sg.Radio("Endswith", group_id="choice",key="ENDSWITH")],[sg.Text("Root path",size=(10,1)),  sg.Input('C:/',size =(45,1),key="PATH"),sg.FolderBrowse('Browse',size =(10,1)),sg.Button("Re-Index",size=(10,1),key="_INDEX_"),sg.Button("Search",size=(10,1),bind_return_key= True,key="_SEARCH_")],[sg.Output(size=(100,30))]
		]
		self.window =sg.Window("File Search Engine").Layout(self.layout)

 
class SearchEngine:
	def __init__(self):
                
		self.file_index = []
		self.results = []
		self.matches = 0
		self.records =0
	
	def create_new_index(self,values):
                
		''' create a new index and save to file '''
		root_path = values['PATH']
		
		self.file_index = [(root,files) for root,dirs,files in os.walk(root_path) if files]
		
		with open('file_index.pkl','wb') as f:
			pickle.dump(self.file_index,f)

	def load_existing_index(self):
		''' load existing index '''

		try:
			with open('file_index.pkl','rb') as f:
				self.file_index =pickle.load(f)
		except:
			self.file_index =[]
	def search(self,values):
		''' Search on term based on search type '''
		# reset variable
		self.results.clear()
		self.matches= 0
		self.records =0
		term = values["TERM"]

		#perofm search
		for path,files in self.file_index:
			for file in files:
				self.records +=1
				if(values["CONTAINS"] and term.lower() in file.lower() or values["STARTSWITH"]and file.lower().startswith(term.lower()) or values["ENDSWITH"] and file.lower().endswith(term.lower())):
				    result = path.replace('\\','/') + '/' + file
				    self.results.append(result)
				    self.matches +=1
				else:
					continue

		with open('search_file.txt','w') as f:
			for row in self.results:
				f.write(row + '\n')
    
def test():
	s =SearchEngine()
	s.create_new_index('C:/')
	s.search('pythfest')

	print()
	print(">> There were {:,d} matches out of  {:,d} records searched.".format(s.matches,s.records))
	print()
	print('>> This query produced the following matches:\n')
	for match in s.results:
		print(match)
def main():
	g= Gui()
	s=SearchEngine()
	s.load_existing_index()

	while True:
		event,values = g.window.Read()
		if event is None:
			break

		if event == "_INDEX_":
			s.create_new_index(values)
			print()
			print(">> New index has been created.")
			print()


		if event == "_SEARCH_":
			s.search(values)
			print()

			for  result in s.results:
				print(result)
			print(">> There were {:,d} matches out of  {:,d} records searched.".format(s.matches,s.records))
			print()
			print('>> This query produced the following matches\n')
	        
main()