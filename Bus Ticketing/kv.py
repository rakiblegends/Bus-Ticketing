WindowManager:
	MainWindow:
	SignupWindow:
	LoginWindow:
	TicketBuyWindow:
	ChooseBusWindow:

<MainWindow>:
	name: 'home'
	Screen:
		MDCard:
			size_hint: None, None
			size: 1000,700
			pos_hint: {"center_x": 0.5, "center_y":0.5}
			elevation: 10
			padding: 25
			spacing: 25
			orientation: 'vertical'
			md_bg_color: "darkgrey"
			unfocus_color: "darkgrey"
			focus_color: "grey"
			FitImage:
				#size_hint_y: 1
				source: 'logo.jpg'
			MDLabel:
				id: welcome_label
				text: "Welcome to Bus Ticketing Sytem, Please Sign Up in order to Buy Ticket."
				font_size: 18
				halign: 'center'
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15
			MDRoundFlatButton:
				text: "LOG IN"
				font_size: 18
				pos_hint: {"center_x":.5}
				on_release: 
					app.root.current = 'login'
					root.manager.transition.direction = "left"
			MDRoundFlatButton:
				text: "SIGN UP"
				font_size: 18
				pos_hint: {"center_x":.5}
				on_release: 
					app.root.current = 'signup'
					root.manager.transition.direction = "left"
			Widget:
				size_hint_y: None
				height: 10
<SignupWindow>:
	name: 'signup'
	Screen:
		MDRoundFlatButton:
			text: "Go Back"
			font_size: 15
			pos_hint: {"center_x":.2, "center_y": 0.9}
			on_release: 
				app.root.current = 'home'
				root.manager.transition.direction = "right"
		MDCard:
			size_hint: None, None
			size: 300,400
			pos_hint: {"center_x": 0.5, "center_y":0.5}
			elevation: 10
			padding: 25
			spacing: 25
			orientation: 'vertical'
			md_bg_color: "darkgrey"
			unfocus_color: "darkgrey"
			focus_color: "grey"

			MDLabel:
				id: signup_label
				text: "Sign Up to buy ticket."
				font_size: 20
				halign: 'center'
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15

			MDTextField:
				id: sign_user
				hint_text: "Username"
				mode: "round"
				icon_right: "account"
				size_hint_x: None
				width: 200
				font_size: 18
				pos_hint: {"center_x": 0.5}

			MDTextField:
				id: sign_password
				hint_text: "Password"
				mode: "round"
				icon_right: "eye-off"
				size_hint_x: None
				width: 200
				font_size: 18
				pos_hint: {"center_x": 0.5}
			MDTextField:
				id: names
				hint_text: "Name"
				mode: "round"
				icon_right: "account"
				size_hint_x: None
				width: 200
				font_size: 18
				pos_hint: {"center_x": 0.5}
			MDTextField:
				id: phones
				hint_text: "Phone Number"
				mode: "round"
				icon_right: "cellphone"
				size_hint_x: None
				width: 200
				font_size: 18
				pos_hint: {"center_x": 0.5}

			MDRoundFlatButton:
				text: "SIGN UP"
				font_size: 12
				pos_hint: {"center_x":.5}
				on_press:
					app.root.current = 'login'
					root.manager.transition.direction = "left"



<LoginWindow>:
	name: 'login'
	Screen:
		MDRoundFlatButton:
			text: "Go Back"
			font_size: 15
			pos_hint: {"center_x":.2, "center_y": 0.9}
			on_release: 
				app.root.current = 'home'
				root.manager.transition.direction = "right"
		MDCard:
			size_hint: None, None
			size: 300,400
			pos_hint: {"center_x": 0.5, "center_y":0.5}
			elevation: 10
			padding: 25
			spacing: 25
			orientation: 'vertical'
			md_bg_color: "darkgrey"
			unfocus_color: "darkgrey"
			focus_color: "grey"

			MDLabel:
				id: welcome_label
				text: "Log in to buy ticket."
				font_size: 20
				halign: 'center'
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15

			MDTextField:
				id: user
				hint_text: "Username"
				mode: "round"
				icon_right: "account"
				size_hint_x: None
				width: 200
				font_size: 18
				pos_hint: {"center_x": 0.5}

			MDTextField:
				id: password
				hint_text: "Password"
				mode: "round"
				icon_right: "eye-off"
				size_hint_x: None
				width: 200
				font_size: 18
				pos_hint: {"center_x": 0.5}
				password:True
			MDRoundFlatButton:
				text: "LOGIN"
				font_size: 12
				pos_hint: {"center_x":.5}
				on_press: 
					app.logger(user.text,password.text)
					root.manager.transition.direction = "left"
			Widget:
				size_hint_y: None
				height: 10

<TicketBuyWindow>:
	name: 'buy_ticket'
	Screen:
		md_bg_color : [1,1,1,1]
		MDRoundFlatButton:
			text: "Go Back"
			font_size: 15
			pos_hint: {"center_x":.2, "center_y": 0.9}
			on_release: 
				app.root.current = 'login'
				root.manager.transition.direction = "right"
		MDLabel:
			id: ticketing
			text: "Buy Tickets"
			font_size: 20
			halign: 'center'
			pos_hint: {"center_x": 0.5, "center_y": 0.8}
			size_hint_y: None
			height: self.texture_size[1]
			padding_y: 15
		MDTextField:
			id: from
			hint_text: "From"
			mode: "round"
			icon_right: "google-maps"
			size_hint_x: None
			width: 500
			font_size: 18
			pos_hint: {"center_x": 0.5, "center_y": 0.7}
		MDTextField:
			id: to
			hint_text: "To"
			mode: "round"
			icon_right: "google-maps"
			size_hint_x: None
			width: 500
			font_size: 18
			pos_hint: {"center_x": 0.5, "center_y": 0.6}
		MDFloatLayout:
			pos_hint: {"center_x": .45, "center_y": 0.5}
			MDTextField:
				id: date
				hint_text: "Pick a Date"
				mode: "round"
				size_hint_x: None
				width: 500
				font_size: 18
				pos_hint: {"center_x": 0.55, "center_y": 0.5}
			MDIconButton:
				icon: "calendar-account"
				pos_hint: {"center_x": .715, "center_y": .5}
				theme_icon_color: "Custom"
    			icon_color: app.theme_cls.primary_color
				on_release: app.show_date_picker()
		MDRoundFlatButton:
			text: "Search Buses"
			font_size: 15
			pos_hint: {"center_x":.5, "center_y": 0.4}
			on_release:
				app.root.current = 'buses'
				root.manager.transition.direction = "left"

<ChooseBusWindow>:
	name: 'buses'
	Screen:
		MDRoundFlatButton:
			text: "Go Back"
			font_size: 15
			pos_hint: {"center_x":.1, "center_y": 0.9}
			on_release: 
				app.root.current = 'buy_ticket'
				root.manager.transition.direction = "right"
		MDLabel:
			id: select_bus
			text: "Choose a bus select ticket"
			font_size: 20
			halign: 'center'
			pos_hint: {"center_x": 0.5, "center_y": 0.8}
			size_hint_y: None
			height: self.texture_size[1]
			padding_y: 15

		MDFloatLayout:
			MDLabel:
				id: bus_type
				text: "Bus Type"
				font_size: 14
				halign: 'center'
				pos_hint: {"center_x": 0.2, "center_y": 0.7}
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15
				theme_text_color: "Custom"
				text_color: "#681D94"
			MDLabel:
				id: dep_time
				text: "Dep. Time"
				font_size: 14
				halign: 'center'
				pos_hint: {"center_x": 0.35, "center_y": 0.7}
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15
				theme_text_color: "Custom"
				text_color: "#681D94"
			MDLabel:
				id: arr_time
				text: "Arr. Time"
				font_size: 14
				halign: 'center'
				pos_hint: {"center_x": 0.5, "center_y": 0.7}
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15
				theme_text_color: "Custom"
				text_color: "#681D94"
			MDLabel:
				id: available_seats_1
				text: "Available Seats"
				font_size: 14
				halign: 'center'
				pos_hint: {"center_x": 0.65, "center_y": 0.7}
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15
				theme_text_color: "Custom"
				text_color: "#681D94"
			MDLabel:
				id: fare
				text: "Fare"
				font_size: 14
				halign: 'center'
				pos_hint: {"center_x": 0.8, "center_y": 0.7}
				size_hint_y: None
				height: self.texture_size[1]
				padding_y: 15
				theme_text_color: "Custom"
				text_color: "#681D94"
		MDCard:
			size_hint: .7, .25
			focus_behavior: True
			pos_hint: {"center_x": .5, "center_y": .5}
			md_bg_color: "darkgrey"
			unfocus_color: "darkgrey"
			focus_color: "grey"
			elevation: 6
			MDFloatLayout:
				MDLabel:
					id: bus_type_1
					text: "HANIF ENTERPRISE"
					font_size: 14
					halign: 'center'
					pos_hint: {"center_x": 0.1, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: dep_time_1
					text: "8:15 AM"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": 0.28, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: arr_time_1
					text: "1:15 PM"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": 0.5, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: available_seats_1
					text: "40"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": 0.7, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: fare_1
					text: "650/-"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": .93, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDRoundFlatButton:
					text: "View Seats"
					font_size: 13
					pos_hint: {"center_x":.5, "center_y": 0.4}

		MDCard:
			size_hint: .7, .25
			focus_behavior: True
			pos_hint: {"center_x": .5, "center_y": .23}
			md_bg_color: "darkgrey"
			unfocus_color: "darkgrey"
			focus_color: "grey"
			elevation: 6
			MDFloatLayout:
				MDLabel:
					id: bus_type_2
					text: "ROYAL EXPRESS"
					font_size: 14
					halign: 'center'
					pos_hint: {"center_x": 0.1, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: dep_time_2
					text: "2:15 PM"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": 0.28, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: arr_time_2
					text: "10:15 PM"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": 0.5, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: available_seats_2
					text: "20"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": 0.7, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
				MDLabel:
					id: fare_2
					text: "650/-"
					font_size: 13
					halign: 'center'
					pos_hint: {"center_x": .93, "center_y": 0.75}
					size_hint_y: None
					height: self.texture_size[1]
					padding_y: 15
    				
				MDRoundFlatButton:
					text: "View Seats"
					font_size: 13
					pos_hint: {"center_x":.5, "center_y": 0.4}


		


