import surfshop
import unittest
import datetime

#CREATE YOUR TESTS
class Shop_Tests(unittest.TestCase):
  #Method to run before each test
  def setUp(self):
      self.cart = surfshop.ShoppingCart()

  def test_add_surfboards(self):
    check = self.cart.add_surfboards(quantity=1)
    self.assertEqual(check, f'Successfully added 1 surfboard to cart!')
  
  def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()
  
  #Parameterized Test above
  '''def test_add_surfboards(self):
    check = self.cart.add_surfboards(quantity=2)
    self.assertEqual(check, f'Successfully added 2 surfboards to cart!')'''

  @unittest.skip
  def test_too_many_surf_boards(self):
    self.assertRaises(surfshop.TooManyBoardsErorr, self.cart.add_surfboards, 5)
  
  #@unittest.expectedFailure
  def test_discounts(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_add_invalid_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)

#RUN AND MAINTAIN TESTS

unittest.main()