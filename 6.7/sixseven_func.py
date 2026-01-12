def colour(r, g, b):
        if  (1 <= r <= 200 and 54 <= g <= 255 and 1 <= b <= 120):
            return "green"
        
def search(listname, min, max):
      first = 0
      last = len(listname) - 1
      
      while first <= last:
            mid =int((first+last)/2)

            if min <= listname[mid] <= max:
                  return listname[mid]
            