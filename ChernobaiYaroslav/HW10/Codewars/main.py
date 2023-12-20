import modules.ball as ball
import modules.colorGhost as colorGhost
import modules.AdamAndEve as AaE
import modules.classyClasses as classyCls
import modules.buildingSpheres as spheres
import modules.dynamicClasses as dynamicCls

print("""
List of tasks:
1. Ball-super-ball
2. Color-ghost
3. Basic-subclasses-Adam-and-Eve
4. Classy-classes
5. Building Spheres
6. Dynamic Classes
      
Enter '0' to exit the program.
""")

while True:
    match input("\nEnter your choice: "):
        
        case "0":
            print("Exiting the program...")
            break
        
        case "1":
            print("Set the ball's type. Default type is 'regular'.\n")
            regularBall = ball.Ball()
            print(f"Default ball's type: {regularBall.ball_type}")
            superBall = ball.Ball('super')
            print(f"'super' ball's type: {superBall.ball_type}")
        
        case "2":
            print("Ghost objects are given a random color attribute of \
'white' or 'yellow' or 'purple' or 'red' when instantiated.\n")
            ghosts = [colorGhost.Ghost().color for _ in range(50)]
            print(f"The list of 50 ghosts' colors: {ghosts}")
            print(f"White ghosts: {ghosts.count('white')}")
            print(f"Yellow ghosts: {ghosts.count('yellow')}")
            print(f"Purple ghosts: {ghosts.count('purple')}")
            print(f"Red ghosts: {ghosts.count('red')}")
        
        case "3":
            print("The creation method must return an array of length 2 \
containing objects (representing Adam and Eve).\n\
The first object in the array should be an instance of the class Man. \
The second should be an instance of the class Woman. \n\
Both objects have to be subclasses of Human.\n")
            print(f"Is Adam an instance of Man? \
{isinstance(AaE.God()[0], AaE.Man)}")
            print(f"Is Eve an instance of Woman? \
{isinstance(AaE.God()[1], AaE.Woman)}")
            print(f"Are they both instances of Human? \
{isinstance(AaE.God()[0], AaE.Human) and isinstance(AaE.God()[1], AaE.Human)}")
        
        case "4":
            print("Create a Constructor method to accept a name as string and \
an age as number.\n\
Complete the get Info property and \
getInfo method/Info getter which should return {name}s age is {age}.\n")
            print(classyCls.Person('john', 36).info)

        case "5":
            print("Create a Sphere class with attributes 'radius' and 'mass'.\n\
Create methods get_radius(), get_mass(), get_volume(), \
get_surface_area(), get_density().\n\
The last three methods must return float rounded to 5 place after the decimal.")
            mySphere = spheres.Sphere(2, 50)
            print(f"""
Sphere's attributes:
- radius: {mySphere.get_radius()}
- mass: {mySphere.get_mass()}
- volume: {mySphere.get_volume()}
- surface area: {mySphere.get_surface_area()}
- density: {mySphere.get_density()}""")
        
        case "6":
            print("Create a function, which can change name of given class.\n\
Proposed function should allow only names with alphanumeric chars \
(upper & lower letters plus ciphers), but starting only with upper \
case letter.\nIn other case it should raise an exception.\n")
            class FirstName():
                pass
            print(f"The class name before changing: {FirstName.__name__}")
            dynamicCls.class_name_changer(FirstName, input("New name: "))
            print(f"The class name after changing: {FirstName.__name__}")
        
        case _:
            print("Wrong number.")