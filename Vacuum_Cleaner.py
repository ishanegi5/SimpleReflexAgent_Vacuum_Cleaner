import random
class Environment(object):
  def __init__(self):
    self.locationcondition={'A':0,'B':0}
    self.locationcondition['A']=random.randint(0,1)
    self.locationcondition['B']=random.randint(0,1)
class SimpleReflexVacuumAgent(Environment):
  def __init__(self,Environment):
    print(Environment.locationcondition)
    score=0
    vacuumlocation=random.randint(0,1)
    if vacuumlocation==0:
     print("vacuum is randomly placed at location A")
     if Environment.locationcondition['A']==1:
      print("Location A is dirty")
      score+=1
      Environment.locationcondition['A']=0
      print('location A is now clean')
     else:
      print("Location A is clean already")
     print("Moving to location B")
     if Environment.locationcondition['B']==1:
        print("Location B is dirty")
        score+=1
        Environment.locationcondition['B']=0
        print("Location b is now clean.")
     else:
        print("Location b is clean already.")
    elif vacuumlocation==1:
      print("Vacuum is randomly placed at location B.")
      if Environment.locationcondition['B']==1:
        print("Location B is dirty.")
        score+=1
        Environment.locationcondition['B']=0
        print("Location B is clean now.")
        print("Moving to location A")
      else:
        print("Location B is clean already.")
        print("Moving to location A")
      if Environment.locationcondition['A']==1:
        print("Location A is dirty.")
        score+=1
        Environment.locationcondition['A']=0
        print("Location A is clean now.")
      else:
        print("Location A is clean already.")
    print("Environment is clean.")
    print(Environment.locationcondition)
    print(f"Performance score= {score}")
theenvironment=Environment()
thevacuum=SimpleReflexVacuumAgent(theenvironment)
