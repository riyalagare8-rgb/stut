import sys
if len (sys.argv) == 3:
  script name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("user provided input valuse:")
else:
  script name = sys.argv[0]
  name ="deepa"
  rollno ="101"
  print("no input given - using default values:")
  print ("script name:, script name)
  print ("student name:",name)
  print ("roll number:",rollno)
