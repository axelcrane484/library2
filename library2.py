 # library
 # multiple books that you can choose from
 # name of book with prices
 #button buy now
 #image at top, label at middle, buy now at bottom
 # budget £15

import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from IPython.display import display
import ipywidgets as widgets
import io
import random

Lord_of_the_Rings = 7
Harry_potter = 6
Fallen_Kingdom = 5
budget = 15

books = {"Lord of the Rings" : 7, "Harry Potter" : 6, "Fallen Kingdom" : 5}

book_widget = widgets.RadioButtons(
          options = list(books.keys()),
          description='book:',
          disabled=False
   )

def buy(b):
  selected_book = book_widget.value
  price = books[selected_book]
  if price < budget:
    print("you have bought", selected_book)
    budgetans = budget - price
    print("you have £",budgetans,"left")
  else:
    print("you do not have any money")

buy_now = widgets.Button(
    description = 'buy now',
    disabled = False,
)

buy_now.on_click(buy)

def search(b):
  search_query = search_widget.value.lower()
  matching_books = [book for book in books if search_query in book.lower()]
  if matching_books:
    book_widget.options = matching_books
  else:
    book_widget.options = ["no found books"]



search_widget = widgets.Text(
    description = 'search book:',
    disabled = False,

  )

search_widget.on_submit(search)

display(book_widget)
display(buy_now)
display(search_widget)

