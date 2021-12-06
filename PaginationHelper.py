class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page=items_per_page

  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)

  # returns the number of pages
  def page_count(self):
      self.page_count_number = len(self.collection)//self.items_per_page
      if len(self.collection)%self.items_per_page!=0:
          self.page_count_number +=1
      return self.page_count_number

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      if page_index < self.page_count_number-1:
          return self.items_per_page
      elif page_index == self.page_count_number-1:
          return len(self.collection)%self.items_per_page
      elif page_index > self.page_count_number-1:
          return -1

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if len(self.collection) ==0:
          return -1
      if item_index > len(self.collection)-1 or item_index <0:
          return -1
      self.page_index_value=(item_index+9)//self.items_per_page
      if self.page_index_value !=0:
          self.page_index_value-=1
      return self.page_index_value
