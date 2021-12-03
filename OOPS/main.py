class A:
      def __init__(self, n = 'Rahul'):
              self.name = n
class B(A):
      def __init__(self, roll):
              self.roll = roll
              A.__init__(self) # if we miss to define this we get an error message.
  
object = B(23)
print (object.name)