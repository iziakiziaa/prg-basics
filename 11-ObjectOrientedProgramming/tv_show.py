import tv
from tv import TV
def main():
   my_tv = TV()
   print("utworzenie")
   
   print("II. poczatkowy status")
   my_tv.show_status()

   print("III. wlaczanie tv" )
   my_tv.turn_on()

   print("IV. pokaz status")
   my_tv.show_status()

   print("V. wylaczanie telewizora")
   my_tv.turn_off()

   print("VI. pokaz status")
   my_tv.show_status()


if __name__ == "__main__":
   main() 
