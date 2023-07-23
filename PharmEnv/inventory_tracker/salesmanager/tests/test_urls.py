from django.test import SimpleTestCase
from django.urls import resolve, reverse
from salesmanager.views import  CustomLoginView, index, home, product_details, issue_item, add_to_stock, receipt, all_sales, receipt_detail, delete_detail, appointment, appointment_page


class TestUrls(SimpleTestCase):

    def test_login_resolves(self):
        url = reverse('login')
        """since login view is a class based view,
        we add .view_class to the function to overcome
        the error of no reverse match.
        """
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)

    def test_index_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_home_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_about_resolves(self):
        url = reverse('aboutdr.wuhayu')
        self.assertEquals(resolve(url).func, home)
        
    def test_product_detail_resolves(self):
        """Since product details has product_id is typecasted as "int",
        we need to pass an integer value in the argument list as below
        """
        url = reverse('product_detail', args=[3])
        self.assertEquals(resolve(url).func, product_details)
        
    def test_issue_item_resolves(self):
        """Since product details has issue_item is typecasted as "str",
        we need to pass a string value in the argument list as below
        """
        url = reverse('issue_item', args = ['args'])
        self.assertEquals(resolve(url).func, issue_item)

    def test_add_to_stock_resolves(self):
        url = reverse('add_to_stock', args= ['args'])
        self.assertEquals(resolve(url).func, add_to_stock)

    def test_receipt_resolves(self):
        url = reverse('receipt')
        self.assertEquals(resolve(url).func, receipt)

    def test_all_sales_resolves(self):
        url = reverse('all_sales')
        self.assertEquals(resolve(url).func, all_sales)

    def test_receipt_detail_resolves(self):
        """Since receipt detail  is typecasted as "int",
        we need to pass an integer value in the argument list as below
        """
        url = reverse('receipt_detail', args= [2])
        self.assertEquals(resolve(url).func, receipt_detail)

    def test_delete_detail_resolves(self):
        url = reverse('delete_detail', args=[3])
        self.assertEquals(resolve(url).func, delete_detail)
    
    def test_appointment_resolves(self):
        url = reverse('appointment')
        self.assertEquals(resolve(url).func, appointment)

    def test_appointment_page_resolves(self):
        url = reverse('appointment_page')
        self.assertEquals(resolve(url).func, appointment_page)
