import tkinter
import customtkinter
from CTkTable import *
from customtkinter import * 
from CTkMessagebox import CTkMessagebox
import sqlite3
from datetime import datetime
import time
import requests
import pytz
import csv
import threading

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)

# Cria banco e instacia conexão
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create tables if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        created_at TEXT,
                        password TEXT)''')    


class App(customtkinter.CTk):

    frames = {"frame1": None, "frame2": None, "frame3": None, "frame4": None, "frame5": None, "frame6": None}

    def frame1_selector(self):
        App.frames["frame5"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["frame6"].pack_forget()

    def frame2_selector(self):
        App.frames["frame5"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame2"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["frame6"].pack_forget()

    def frame3_selector(self):
        App.frames["frame5"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame3"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["frame6"].pack_forget()

    def frame4_selector(self):
        App.frames["frame5"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame4"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["frame6"].pack_forget()

    def frame5_selector(self):
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame5"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["frame6"].pack_forget()

    def frame6_selector(self):
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame5"].pack_forget()
        App.frames["frame6"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)


#=======================================================================================================================================================================================================

    def __init__(self):

        def get_candlestick_data(symbol, interval, limit):
            endpoint = "https://api.binance.com/api/v3/klines"
            params = {
                'symbol': symbol,
                'interval': interval,
                'limit': limit
            }
            response = requests.get(endpoint, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print("Error fetching candlestick data:", response.text)
                return None

        def calculate_percentage_difference(current_price, old_price):
            return ((current_price - old_price) / old_price) * 100

        def convert_ms_to_date_string(milliseconds):
            # Convert milliseconds to seconds
            seconds = milliseconds / 1000.0
            
            # Get the current time in UTC
            utc_time = datetime.utcfromtimestamp(seconds)

            # Convert UTC time to America/Sao_Paulo timezone
            sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
            sao_paulo_time = utc_time.replace(tzinfo=pytz.utc).astimezone(sao_paulo_tz)
            
            # Format the datetime object to a string
            date_string = sao_paulo_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
            
            return date_string

        def changeBack():
            val = switch.get()
            if val:
                customtkinter.set_appearance_mode("light")
            else:
                customtkinter.set_appearance_mode("dark")

        def periodic_task(interval, running):
            symbols = ['BTCUSDT', 'ADABRL', 'XRPBRL', 'CHZBRL', 'DOGEBRL']
            candleNum = 24
            while running.is_set():
                for i, symbol in enumerate(symbols): 
                        candlestick_data = get_candlestick_data(symbol, '1h', candleNum+1) 
                        if candlestick_data:
                            
                            #diferença 1hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[23][4])  # Close price of the past candlestick
                            percentage_difference = calculate_percentage_difference(current_price, past_price)
                            print(past_price)

                            #diferença 2hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[22][4])  # Close price of the past candlestick
                            percentage_difference2 = calculate_percentage_difference(current_price, past_price)

                            #diferença 4hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[20][4])  # Close price of the past candlestick
                            percentage_difference4 = calculate_percentage_difference(current_price, past_price)

                            #diferença 6hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[18][4])  # Close price of the past candlestick
                            percentage_difference6 = calculate_percentage_difference(current_price, past_price)

                            #diferença 8hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[16][4])  # Close price of the past candlestick
                            percentage_difference8 = calculate_percentage_difference(current_price, past_price)

                            #diferença 12hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[12][4])  # Close price of the past candlestick
                            percentage_difference12 = calculate_percentage_difference(current_price, past_price)

                            #diferença 24hora
                            current_price = float(candlestick_data[-1][4])  # Close price of the latest candlestick
                            past_price = float(candlestick_data[0][4])  # Close price of the past candlestick
                            percentage_difference24 = calculate_percentage_difference(current_price, past_price)

                            #symbol
                            entry_text = f"{symbol}:" #                                                                                          {percentage_difference2:.2f}%, {percentage_difference4:.2f}%, {percentage_difference6:.2f}%, {percentage_difference8:.2f}%, {percentage_difference12:.2f}%, {percentage_difference24:.2f}%"
                            label = customtkinter.CTkLabel(masterFrame21, text=entry_text, font=("Arial Black", 20))
                            label.grid(row=i+3, column=1, padx=10, pady=10)

                            #currentPrice
                            entry_text2 = f"{current_price}"
                            label1 = customtkinter.CTkLabel(masterFrame21, text=entry_text2, font=("Arial Black", 20))
                            label1.grid(row=i+3, column=11, padx=60, pady=10)

                            #1h
                            entry_text3 = f"{percentage_difference:.2f}%"
                            label3 = customtkinter.CTkLabel(masterFrame21, text=entry_text3, font=("Arial Black", 20))
                            label3.grid(row=i+3, column=12, padx=15, pady=10)

                            #2h
                            entry_text4 = f"{percentage_difference2:.2f}%"
                            label4 = customtkinter.CTkLabel(masterFrame21, text=entry_text4, font=("Arial Black", 20))
                            label4.grid(row=i+3, column=13, padx=15, pady=10)

                            #4h
                            entry_text5 = f"{percentage_difference4:.2f}%"
                            label5 = customtkinter.CTkLabel(masterFrame21, text=entry_text5, font=("Arial Black", 20))
                            label5.grid(row=i+3, column=14, padx=15, pady=10)

                            #6h
                            entry_text6 = f"{percentage_difference6:.2f}%"
                            label6 = customtkinter.CTkLabel(masterFrame21, text=entry_text6, font=("Arial Black", 20))
                            label6.grid(row=i+3, column=15, padx=15, pady=10)

                            #8h
                            entry_text7 = f"{percentage_difference8:.2f}%"
                            label7 = customtkinter.CTkLabel(masterFrame21, text=entry_text7, font=("Arial Black", 20))
                            label7.grid(row=i+3, column=16, padx=15, pady=10)

                            #12h
                            entry_text8 = f"{percentage_difference12:.2f}%"
                            label8 = customtkinter.CTkLabel(masterFrame21, text=entry_text8, font=("Arial Black", 20))
                            label8.grid(row=i+3, column=17, padx=15, pady=10)

                            #24h
                            entry_text9 = f"{percentage_difference24:.2f}%"
                            label9 = customtkinter.CTkLabel(masterFrame21, text=entry_text9, font=("Arial Black", 20))
                            label9.grid(row=i+3, column=18, padx=15, pady=10)

                        
                            csv_file = f"{symbol}_{interval}_candles.csv"
                            field_names = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseAssetVolume', 'takerBuyQuoteAssetVolume', 'ignore']
                            
                            with open(csv_file, mode='w', newline='') as file:
                                writer = csv.DictWriter(file, fieldnames=field_names)
                                writer.writeheader()
                                for candle in candlestick_data:
                                    #print(f'{interval}h - {candle}')
                                    candle_data = {
                                        'timestamp': convert_ms_to_date_string(candle[0]),
                                        'open': candle[1],
                                        'high': candle[2],
                                        'low': candle[3],
                                        'close': candle[4],
                                        'volume': candle[5],
                                        'closeTime': candle[6],
                                        'quoteAssetVolume': candle[7],
                                        'numberOfTrades': candle[8],
                                        'takerBuyBaseAssetVolume': candle[9],
                                        'takerBuyQuoteAssetVolume': candle[10],
                                        'ignore': candle[11],
                                    }
                                    writer.writerow(candle_data)

                            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            txtboxLogs.insert(5000.0, f"\n{symbol} 24 hours ok at {created_at}")
                        else:
                            txtboxLogs.insert(5000.0, f"\nFailed to fetch candlestick data for {symbol} 24h at {created_at}")

                        candlestick_data = get_candlestick_data(symbol, '1m', 61) 
                        if candlestick_data:
                                csv_file = f"{symbol}_{60}_MINUTES_candles.csv"
                                
                                field_names = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseAssetVolume', 'takerBuyQuoteAssetVolume', 'ignore']
                                
                                with open(csv_file, mode='w', newline='') as file:
                                    writer = csv.DictWriter(file, fieldnames=field_names)
                                    writer.writeheader()
                                    for candle in candlestick_data:
                                        #print(f'{60}m - {candle}')
                                        candle_data = {
                                            'timestamp': convert_ms_to_date_string(candle[0]),
                                            'open': candle[1],
                                            'high': candle[2],
                                            'low': candle[3],
                                            'close': candle[4],
                                            'volume': candle[5],
                                            'closeTime': candle[6],
                                            'quoteAssetVolume': candle[7],
                                            'numberOfTrades': candle[8],
                                            'takerBuyBaseAssetVolume': candle[9],
                                            'takerBuyQuoteAssetVolume': candle[10],
                                            'ignore': candle[11],
                                        }
                                        writer.writerow(candle_data)
                                created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                txtboxLogs.insert(5000.0, f"\n{symbol} 1 mintute ok at {created_at}")
                        else:
                                txtboxLogs.insert(5000.0, f"\nFailed to fetch candlestick data for {symbol} 1 minute at {created_at}")
                time.sleep(interval * 1)  # Sleep for 1 hour (3600 seconds)


        def stop_periodic_task():
            global running
            running.clear()  # Signal the thread to stop


        def start_periodic_task():
            global task_thread, running
            running = threading.Event()
            running.set()
            task_thread = threading.Thread(target=periodic_task, args=(1, running))
            task_thread.start()
    

        def turnOnApp():
            val = onApp.get()
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if val:
                start_periodic_task()
                txtboxLogs.insert(5000.0, f"\nApplication turned ON at {created_at}")
            else:
                stop_periodic_task()
                txtboxLogs.insert(5000.0, f"\nApplication turned OFF at {created_at}")
                

        super().__init__()
        self.state('withdraw')
        
        self.title("BINANCE SYSTEM")

        self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(True, True)

        # contains everything
        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)

        title_label = customtkinter.CTkLabel(left_side_panel, text="SYSTEM", font=("Arial Black", 20))
        title_label.grid(row=0, column=0, padx=20, pady=10)
        title_label = customtkinter.CTkLabel(left_side_panel, text="BINANCE SYSTEM", font=("Arial Black", 5))
        title_label.grid(row=1, column=0, padx=20, pady=1)

     
        # buttons to select the frames
        bt_frame1 = customtkinter.CTkButton(left_side_panel, text="Sobre", text_color=("#000000", "#ffffff"),fg_color="transparent",hover=True, hover_color=("#e3c857", "#9A97F3"), font=("Arial Black", 15),anchor='w',command=self.frame1_selector)
        bt_frame1.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        bt_frame2 = customtkinter.CTkButton(left_side_panel, text="Aplicação", text_color=("#000000", "#ffffff"),fg_color="transparent",hover=True, hover_color=("#e3c857", "#9A97F3"),font=("Arial Black", 15),anchor='w',command=self.frame2_selector)
        bt_frame2.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        bt_frame3 = customtkinter.CTkButton(left_side_panel, text="Configuração", text_color=("#000000", "#ffffff"),fg_color="transparent",hover=True, hover_color=("#e3c857", "#9A97F3"),font=("Arial Black", 15),anchor='w',command=self.frame3_selector)
        bt_frame3.grid(row=4, column=0, padx=20, pady=10,  sticky="ew")

        bt_frame4 = customtkinter.CTkButton(left_side_panel, text="Banco de dados", text_color=("#000000", "#ffffff"),fg_color="transparent",hover=True, hover_color=("#e3c857", "#9A97F3"),font=("Arial Black", 15),anchor='w',command=self.frame4_selector)
        bt_frame4.grid(row=5, column=0, padx=20, pady=10,  sticky="ew")

        bt_frame5 = customtkinter.CTkButton(left_side_panel, text="Suporte", text_color=("#000000", "#ffffff"),fg_color="transparent",hover=True, hover_color=("#e3c857", "#9A97F3"),font=("Arial Black", 15),anchor='w',command=self.frame5_selector)
        bt_frame5.grid(row=6, column=0, padx=20, pady=10,  sticky="ew")

        # right side panel -> to show the frame1 or frame 2
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel,fg_color="#333333")
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        App.frames['frame1'] = customtkinter.CTkFrame(main_container)
        label1 = customtkinter.CTkLabel(App.frames['frame1'], text="BINANCE CANDLE SYSTEM", font=("Arial Black", 20))
        label1.pack(padx=10, pady=10)
        masterFrame1 = customtkinter.CTkFrame(App.frames['frame1'], width=990, height=570)
        masterFrame1.pack(padx=10, pady=10, fill='both')
        txtbox1 = customtkinter.CTkTextbox(masterFrame1, scrollbar_button_color="#d6830f", corner_radius=16, border_color="#d6830f",width=950, height=500) 
        txtbox1.pack(padx=10, pady=10, fill='both') 
        txtbox1.insert("0.0", "Descrição:\nAplicação criada para visualizar candles de criptomoedas da BINANCE e variação de moedas dentro dos periodos de 1, 2, 4, 6, 8, 12 e 24 horas, além de gerar relatórios CSV com todas as informações dos candles") 
        txtbox1.insert("1000.0", "\nresgatados.") 
#===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

        App.frames['frame2'] = customtkinter.CTkFrame(main_container)
        
        label1 = CTkLabel(App.frames['frame2'], text="Aplicação", font=("Arial Black", 20))
        label1.pack(padx=10, pady=10) 

        masterFrame2 = customtkinter.CTkFrame(App.frames['frame2'], width=990, height=150)
        masterFrame2.pack(padx=10, pady=10, fill='both', expand=True)

        symbol = customtkinter.CTkLabel(masterFrame2, text="Symbol", font=("Arial Black", 20)) 
        symbol.pack(padx=35, pady=10,side=customtkinter.LEFT)
        
        currentPrice = customtkinter.CTkLabel(masterFrame2, text="Current Price", font=("Arial Black", 20)) 
        currentPrice.pack(padx=35, pady=10,side=customtkinter.LEFT)
        
        oneHour = customtkinter.CTkLabel(masterFrame2, text="1H", font=("Arial Black", 20))
        oneHour.pack(padx=35, pady=10, side=customtkinter.LEFT)

        twoHour = customtkinter.CTkLabel(masterFrame2, text="2H", font=("Arial Black", 20))
        twoHour.pack(padx=35, pady=10, side=customtkinter.LEFT)

        fourHour = customtkinter.CTkLabel(masterFrame2, text="4H", font=("Arial Black", 20))
        fourHour.pack(padx=35, pady=10, side=customtkinter.LEFT)

        sixHour = customtkinter.CTkLabel(masterFrame2, text="6H", font=("Arial Black", 20))
        sixHour.pack(padx=35, pady=10, side=customtkinter.LEFT)

        eightHour = customtkinter.CTkLabel(masterFrame2, text="8H", font=("Arial Black", 20))
        eightHour.pack(padx=35, pady=10, side=customtkinter.LEFT)

        twelveHour = customtkinter.CTkLabel(masterFrame2, text="12H", font=("Arial Black", 20))
        twelveHour.pack(padx=35, pady=10, side=customtkinter.LEFT)

        oneDay = customtkinter.CTkLabel(masterFrame2, text="24H", font=("Arial Black", 20))
        oneDay.pack(padx=35, pady=10, side=customtkinter.LEFT)

        onApp = customtkinter.CTkSwitch(masterFrame2, text= "OFF/ON",progress_color=("#e3c857", "#9A97F3"), font=("Arial Black", 15),onvalue=1, offvalue=0, command=turnOnApp)
        onApp.pack(padx=30, pady=10, side=customtkinter.LEFT)

        text1 = customtkinter.CTkLabel(App.frames['frame2'], text="Resultados", font=("Arial Black", 20))#.pack(expand=True, padx=30, pady=20) 
        text1.pack(padx=10, pady=10, fill='both', expand=True) 

        masterFrame21 = customtkinter.CTkScrollableFrame(App.frames['frame2'], width=990, height=570)
        masterFrame21.pack(padx=10, pady=10, fill='both', expand=True)
        
 
#===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

        App.frames['frame3'] = customtkinter.CTkFrame(main_container)

        label1 = CTkLabel(App.frames['frame3'], text="Configurações", font=("Arial Black", 20))
        label1.pack(padx=10, pady=10)

        topFrame = customtkinter.CTkFrame(App.frames['frame3'], width=990, height=150)
        topFrame.pack(padx=10, pady=10, fill='both')

        switch = customtkinter.CTkSwitch(topFrame, text= "Mudar tema",progress_color=("#e3c857", "#9A97F3"), font=("Arial Black", 15),onvalue=1, offvalue=0, command=changeBack)
        switch.pack(padx=70, pady=10,side=customtkinter.LEFT)

        bomFrame = customtkinter.CTkFrame(App.frames['frame3'], width=500, height=590)
        bomFrame.pack(padx=10, pady=10, side=customtkinter.LEFT, fill='both', expand=True)

        dbFrame = customtkinter.CTkFrame(App.frames['frame3'], width=295, height=590)
        dbFrame.pack(padx=10, pady=10, side=customtkinter.LEFT, fill='both', expand=True)

        label1 = CTkLabel(bomFrame, text="OP1", font=("Arial Black", 20))
        label1.pack(padx=200, pady=0)

        label1 = CTkLabel(dbFrame, text="OP2", font=("Arial Black", 20))
        label1.pack(padx=80, pady=0)

        labelDB = customtkinter.CTkLabel(dbFrame, text="" )
        labelDB.pack(padx=10, pady=5)

        labelBom = customtkinter.CTkLabel(bomFrame, text="" )
        labelBom.place(relx=0.55, rely=0.90)

        buttonlogs = customtkinter.CTkButton(dbFrame, text="LOGS",text_color=("#000000", "#ffffff") , corner_radius=32, fg_color="transparent", hover_color=("#e3c857", "#9A97F3"), border_color="#FFCC70", border_width=2, font=("Arial Black", 15),command=self.frame6_selector) 
        buttonlogs.pack(padx=10, pady=10, side=customtkinter.BOTTOM)

#===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

        App.frames['frame4'] = customtkinter.CTkFrame(main_container)
        
        label1 = CTkLabel(App.frames['frame4'], text="Banco de dados", font=("Arial Black", 20))
        label1.pack(padx=10, pady=10) 
        frameDB = customtkinter.CTkScrollableFrame(App.frames['frame4'], width=990, height=570)
        frameDB.pack(padx=10, pady=30, fill='both') 

        table = CTkTable(master=frameDB, row=50, column=10)
        table.pack(expand=True, fill="both", padx=20, pady=30)
        
#===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
    
        App.frames['frame5'] = customtkinter.CTkFrame(main_container)

        label1 = CTkLabel(App.frames['frame5'], text="Suporte", font=("Arial Black", 20))
        label1.pack(padx=10, pady=10) 

        label2 = CTkLabel(App.frames['frame5'], text="Tem alguma dúvida, não consegue usar ou encontrou um bug? Contate-me!", font=("Arial Black", 15))
        label2.pack(padx=10, pady=15) 

        frame1 = customtkinter.CTkFrame(App.frames['frame5'], fg_color="transparent", height=350, width=450, border_color="#FFCC70", border_width=2)
        frame1.pack(padx=10, pady=20)

        label2 = CTkLabel(master=frame1, text="Desenvolvido por:", font=("Arial Black", 15))
        label2.place(relx=0.1, rely=0.05)

        label2 = CTkLabel(master=frame1, text="Nome: Igor Machado", font=("Arial Black", 15))
        label2.place(relx=0.1, rely=0.25) 

        label2 = CTkLabel(master=frame1, text="Computer Engineer", font=("Arial Black", 15))
        label2.place(relx=0.1, rely=0.35) 

        label2 = CTkLabel(master=frame1, text="Email: igor.gabriel.machado@gmail.com", font=("Arial Black", 15))
        label2.place(relx=0.1, rely=0.55) 

#===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
    
        App.frames['frame6'] = customtkinter.CTkFrame(main_container)

        label1 = CTkLabel(App.frames['frame6'], text="LOGS", font=("Arial Black", 20))
        label1.pack(padx=10, pady=10) 

        txtboxLogs = customtkinter.CTkTextbox(App.frames['frame6'], scrollbar_button_color="#d6830f", corner_radius=16, border_color="#d6830f", width=990, height=490) 
        txtboxLogs.pack(padx=20, pady=80) 


a = App()
a.mainloop()
'''
def register_user():

    def create_user(username, password):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
                    (username, password, created_at))
        conn.commit()

    def validateNewregister():
        newUsername = newUsernameentry.get()
        newPassword = newPassword_entry.get()
        confirmNewPassword = confirmPassword_entry.get()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (newUsername,))
        user = cursor.fetchone()
        if not user or newUsername not in user:
                if newUsername and newPassword and confirmNewPassword:
                    if newPassword == confirmNewPassword:
                        create_user(newUsername, newPassword)
                        CTkMessagebox(title="Success", message=f"Usuário registrado com sucesso!", icon="check")
                        registerWindow.withdraw()
                    else:
                        CTkMessagebox(title="Success", message=f"Senhas divergentes!", icon="check")
                else:
                    CTkMessagebox(title="Error", message=f"Faltam campos a serem preenchidos!", icon="cancel")
        else:
                CTkMessagebox(title="Error", message=f"Uusário ja registrado!", icon="cancel")

    registerWindow = customtkinter.CTk()
    registerWindow.title("Register - SYSTEM")
    registerWindow.geometry("{0}x{0}+0+0".format(registerWindow.winfo_screenwidth(), registerWindow.winfo_screenheight()))
    registerWindow.resizable(True, True)

    registerLabel = customtkinter.CTkLabel(registerWindow, text="Registre-se", font=("Arial Black", 20))
    registerLabel.pack(padx=10, pady=10)

    frameRegister = customtkinter.CTkFrame(registerWindow, fg_color="transparent", height=350, width=450, border_color="#FFCC70", border_width=2)
    frameRegister.pack(padx=10, pady=150)
    # Username Label and Entry
    newUsernamelabel = customtkinter.CTkLabel(frameRegister, text="Usuário:")
    newUsernamelabel.place(relx=0.23, rely=0.05)
    newUsernameentry = customtkinter.CTkEntry(frameRegister, placeholder_text="Insira o registro aqui",width=250)
    newUsernameentry.place(relx=0.23, rely=0.15) 

    # Password Label and Entry
    newPassword_label = customtkinter.CTkLabel(frameRegister, text="Senha:")
    newPassword_label.place(relx=0.23, rely=0.35) 
    newPassword_entry = customtkinter.CTkEntry(frameRegister,placeholder_text="Insira a senha aqui", show="*", width=250)
    newPassword_entry.place(relx=0.23, rely=0.45) 

    confirmPassword_label = customtkinter.CTkLabel(frameRegister, text="Confirmar Senha:")
    confirmPassword_label.place(relx=0.23, rely=0.55)
    confirmPassword_entry = customtkinter.CTkEntry(frameRegister,placeholder_text="Confirme sua senha aqui", show="*", width=250)
    confirmPassword_entry.place(relx=0.23, rely=0.65)

    # Login Button
    newRegisterButton = customtkinter.CTkButton(frameRegister, text="Registrar", width=250,command=validateNewregister)
    newRegisterButton.place(relx=0.23, rely=0.85)

    registerWindow.mainloop()

def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        CTkMessagebox(title="Success", message=f"Login efetuado com sucesso!", icon="check")
        callApp()
    else:
        CTkMessagebox(title="Error", message=f"Nome de usuário ou senha invalidos!", icon="cancel")

def callApp():
    login_window.withdraw()
    a.mainloop()

# Create login window
login_window = customtkinter.CTk()
login_window.title("Login - SYSTEM")
login_window.geometry("{0}x{0}+0+0".format(login_window.winfo_screenwidth(), login_window.winfo_screenheight()))
login_window.resizable(True, True)

loginLabel = customtkinter.CTkLabel(login_window, text="Login", font=("Arial Black", 20))
loginLabel.pack(padx=10, pady=10)

frameLogin = customtkinter.CTkFrame(login_window, fg_color="transparent", height=350, width=450, border_color="#FFCC70", border_width=2)
frameLogin.pack(padx=10, pady=150)
# Username Label and Entry
username_label = customtkinter.CTkLabel(frameLogin, text="Usuário:")
username_label.place(relx=0.23, rely=0.05)
username_entry = customtkinter.CTkEntry(frameLogin, placeholder_text="Insira o registro aqui",width=250)
username_entry.place(relx=0.23, rely=0.15) 

# Password Label and Entry
password_label = customtkinter.CTkLabel(frameLogin, text="Senha:")
password_label.place(relx=0.23, rely=0.35) 
password_entry = customtkinter.CTkEntry(frameLogin,placeholder_text="Insira a senha aqui", show="*", width=250)
password_entry.place(relx=0.23, rely=0.45) 

# Login Button
login_button = customtkinter.CTkButton(frameLogin, text="Login", width=250,command=authenticate_user)
login_button.place(relx=0.23, rely=0.65) 

register_button = customtkinter.CTkButton(frameLogin, text="Registrar", width=250,command=register_user)
register_button.place(relx=0.23, rely=0.85) 

login_window.mainloop()

# Close connection
conn.close()
'''