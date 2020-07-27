class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name.title()} menu available from {self.start_time}:00 to {self.end_time}:00."
  
  def calculate_bill(self,purchased_items):
    total=0
    for i in purchased_items:
      total+= self.items[i]
    return total

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus

  def __str__(self):
    return f"We are located at {self.address}."

  def available_menus(self,time):
    lst=[]
    for menu in self.menus:
      if menu.start_time<=time and menu.end_time>=time:
        lst.append(menu)
    return lst

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises


brunch_items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch=Menu("brunch",brunch_items,11,16)

earlybird_items={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird=Menu("early bird",earlybird_items,15,18)
dinner_items={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner=Menu("dinner",dinner_items,17,23)

kids_items={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids=Menu("kids",kids_items,11,21)

print(early_bird)

flagship_store=Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment=Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

print(brunch.calculate_bill(["home fries","pancakes","coffee"]))
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

print(flagship_store.available_menus(17))

busy1=Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
arepas_menu={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas=Menu("arepas",arepas_menu,10,20)

arepas_place=Franchise("189 Fitzgerald Avenue",[arepas,kids])
busy2=Business("Take a' Arepa",[arepas_place])
print(flagship_store.available_menus(17))
print(arepas_place)

print(arepas_place.available_menus(14))
