from django.urls import path,include
from .import views
from django.urls import re_path

urlpatterns = [
    # path('',views.index,name='index'),
    # path('register',views.register,name='register'),
    path('freereg',views.freereg,name='freereg'),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about$', views.about, name='about'),
     re_path(r'^about_two$', views.about_two, name='about_two'),
    re_path(r'^checkout$', views.checkout, name='checkout'),
    re_path(r'^contact$', views.contact, name='contact'),
    re_path(r'^contact_two$', views.contact_two, name='contact_two'),
    re_path(r'^model$', views.model, name='model'),
    re_path(r'^model_two$', views.model_two, name='model_two'),
    re_path(r'^product$', views.product, name='product'),
    path('profile/<int:pk>',views.profile, name='profile'),
    re_path(r'^registration$', views.registration, name='registration'),
    re_path(r'^freelancer$', views.freelancer, name='freelancer'),
    # re_path(r'^login/$', views.login, name="login"),
    re_path(r'^registration$', views.registration, name='registration'),



	re_path(r'^admin_log$', views.admin_log, name='admin_log'),
    re_path(r'^admin_login$', views.admin_login, name='admin_login'),
    
    re_path(r'^admin_logout$', views.admin_logout, name='admin_logout'),
    re_path(r'^user_logout$', views.user_logout, name='user_logout'),
    re_path(r'^admin_settings$', views.admin_settings, name='admin_settings'),
    re_path(r'^admin_edit_picture$', views.admin_edit_picture, name='admin_edit_picture'),
    re_path(r'^admin_edit_profile$', views.admin_edit_profile, name='admin_edit_profile'),
    re_path(r'^admin_edit_password$', views.admin_edit_password, name='admin_edit_password'),
    # re_path(r'^modelshow/(?P<id>\d+)$', views.modelshow, name='modelshow'),
    re_path(r'^admin_dashboard$', views.admin_dashboard, name='admin_dashboard'),
    re_path(r'^registration$', views.registration, name='registration'),
    re_path(r'^Signup_emailval$', views.Signup_emailval, name='Signup_emailval'),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^userhome$', views.userhome, name='userhome'),
    
    re_path(r'^new_page/(?P<id>\d+)$', views.new_page, name='new_page'),
    re_path(r'^sub/(?P<id>\d+)$', views.sub, name='sub'),
    
    #category
    re_path(r'^category$', views.show_category, name="category"),
    re_path(r'^Sub_categories$', views.Sub_categories, name="Sub_categories"),
    re_path(r'^add_subcategory$', views.add_subcategory, name="add_subcategory"),
    re_path(r'^add_category$', views.add_category, name="add_category"),
    re_path(r'^cat_delete/(?P<cat_id>\d+)$', views.cat_delete, name="cat_delete"),
    re_path(r'^subcat_delete/(?P<id>\d+)$', views.subcat_delete, name="subcat_delete"),
    
    #models
    re_path(r'^admin_models$', views.admin_models, name='admin_models'),
    
    #add model
    re_path(r'^addmodel$', views.addmodel, name="addmodel"),
    re_path(r'^createmodel$', views.createmodel, name="createmodel"),
    
    #payment history
    re_path(r'^admin_payment_history$', views.admin_payment_history, name='admin_payment_history'),
    re_path(r'^payment_table$', views.payment_table, name='payment_table'),
    
    #registered users
    re_path(r'^registeredusers$', views.registeredusers, name='registeredusers'),
    re_path(r'^delete/(?P<reg_id>\d+)$', views.delete, name='delete'),
    
    #model edit
    re_path(r'^adminedit/(?P<id>\d+)$', views.adminedit,name="adminedit"),
    re_path(r'^admin_editmodel/(?P<id>\d+)$', views.admin_editmodel,name="admin_editmodel"),
    re_path(r'^modeledit/(?P<id>\d+)$', views.modeledit,name="modeledit"),

    #current models
    re_path(r'^admin_current_models$', views.admin_current_models, name='admin_current_models'),
    re_path(r'^model_delete/(?P<id>\d+)$', views.model_delete,name="model_delete"),
    # re_path(r'^test_page$', views.test_page,name="test_page"),
    
    
   
	#Leave as empty string for base url
	# re_path(r'^store$', views.store, name="store"),
	re_path(r'^cart/$', views.cart_item, name="cart"),
	re_path(r'^checkout/$', views.checkout, name="checkout"),

	re_path(r'^update_item/$', views.updateItem, name="update_item"),
	re_path(r'^process_order/$', views.processOrder, name="process_order"),
	
	
	re_path(r'^logout/$', views.logout, name="logout"),
    re_path(r'^newcart/$',views.newcart,name='newcart'),
    re_path(r'^request/$',views.request,name='request'),
    re_path(r'^reqlist/$',views.reqlist,name='reqlist'),
    re_path(r'^savereq/$',views.savereq,name='savereq'),
    path('deletereq/<int:reg_id>',views.deletereq,name='deletereq'),
    
    # re_path(r'requestnew',views.requestnew,name='requestnew'),
    #...........category..................filter...........
    path('three',views.three,name='three'),
    
    path('fbx',views.fbx,name='fbx'),
    path('obj',views.obj,name='obj'),
    path('view/<int:pk>',views.view_items,name='view_items'),
    path('view_two/<int:pk>',views.view_items_two,name='view_items_two'),
    path('cartitem/<int:pk>',views.cartitem,name='cartitem'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('price_low',views.price_low,name='price_low'),
    path('price_high',views.price_high,name='price_high'),
    path('photoshop',views.photoshop,name='photoshop'),
    path('uidesign',views.ui_design,name='ui_design'),
    path('house_plans',views.house_plans,name='house_plans'),
    path('logo_creation',views.logo_creation,name='logo_creation'),
    path('drawings',views.drawings,name='drawings'),

    #shebin shaji

    path('freelancers',views.freelancers,name='freelancers'),
    
]
