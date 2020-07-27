class Art:
  def __init__(self,owner,artist,title,medium,year):
    self.owner = owner
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year

  def __repr__(self):
    return f"{self.artist}. \"{self.title}\". {self.year}, {self.medium}. Currently with {self.owner.name} in {self.owner.location}"

class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self,new_listing):
    self.listings.append(new_listing)

  def remove_listing(self,remlisting):
    i=self.listings.index(remlisting)
    self.listings.pop(i)

  def show_listings(self):
    for li in self.listings:
      print(li)
    if len(self.listings)==0:
      print("None for sale right now")

class Client:
  def __init__(self,name,location,is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  def sell_artwork(self,artwork,price):
    if artwork.owner==self:
      veneer.add_listing(Listing(artwork,price,self))
  
  def buy_artwork(self,artwork):
    #print(artwork)
    if artwork.owner!=self:
      for i in veneer.listings:
        if artwork == i.art:
          artwork.owner=self
          veneer.remove_listing(i)

class Listing:
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return f"{self.art.title} for {self.price}"


veneer=Marketplace()
# veneer.add_listing("hi")
# veneer.remove_listing("hi")
edytta=Client("Edytta Halpirt","Private Collection",False)
moma=Client("The MOMA","New York",True)
girl_with_mandolin=Art(edytta,"Picasso, Pable","Girl with a Mandolin (Fanny Tellier)","oil on canvas",1910)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin,"6M USD")

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
veneer.show_listings()

