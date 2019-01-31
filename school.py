class School:

	def __init__(self, name = None, roster = {}):
		self.name = name
		self.roster = roster

	def add_student(self, student_name, grade):
		if grade not in self.roster.keys():
            		self.roster[grade] = [student_name]
        	else:
            		self.roster[grade].append(student_name)	