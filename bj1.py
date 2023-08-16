import tkinter
from tkinter import Tk

#Todo create another gui within the gui for a redumentary card counter ie the first card counter you made

class CardCounter(Tk):
    def __init__(self):
        super().__init__()
        self.deck = {}
        self.cards_remaining = []
        self.counter = 0
        self.probability = 0
        self.value_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        
        #Window Screen 1
        self.title("Johnny Yang Card Counter")
        self.geometry("460x325")
        self.resizable(False, False)
        self.configure(background ='black')
        self.main_frame = tkinter.Frame(self, relief= 'sunken', borderwidth = 2, background = 'black')
        self.main_frame.grid(row=0, column=0, padx=8, pady=8, sticky='nsew')
        
        
        # Number of decks 
        tkinter.Label(self.main_frame, text="Number of Decks:", background='black', fg='white').grid(row=1, column=1, sticky='nw', padx=5, pady=5)
        
        # Number of decks entry
        self.num_decks = tkinter.IntVar()
        deck_entry = tkinter.Entry(self.main_frame, textvariable=self.num_decks)
        deck_entry.grid(row=1, column=2, sticky='ne', pady=5)
        
        # Number of deck buttons 
        deck_button = tkinter.Button(self.main_frame, text='Enter', command=self.create_deck)
        deck_button.grid(row=1, column=3, sticky='nw', padx=5, pady=5)
        
        # Number of decks results
        self.deck_result_label = tkinter.Label(self.main_frame, background='black', fg='#5bfba3')
        self.deck_result_label.grid(row=2, column=1, sticky='nw', columnspan=2, padx=5)
        
        #remove cards
        tkinter.Label(self.main_frame, text="Remove Card:", background='black', fg='white').grid(row=3, column=1, sticky='nw', padx=5)
        tkinter.Label(self.main_frame, text="Value (A, K, 7, 4):", background='black', fg='white').grid(row=4, column=1, sticky='e', padx=2)
        tkinter.Label(self.main_frame, text="Suite (H, D, S, C):", background='black', fg='white').grid(row=5, column=1, sticky='e', padx=2)
        
        #remove Cards entry
        self.face = tkinter.StringVar()
        face_entry = tkinter.Entry(self.main_frame, textvariable=self.face)
        face_entry.grid(row=4, column=2, sticky='ne')
        self.suite = tkinter.StringVar()
        suite_entry = tkinter.Entry(self.main_frame, textvariable=self.suite)
        suite_entry.grid(row=5, column=2, sticky='ne')
        
        # remove cards button
        face_button = tkinter.Button(self.main_frame, text='Remove Card', command=self.remove_card)
        face_button.grid(row=5, column=3, sticky='nw', padx=5)
        
        #remove card results label
        self.card_result_label1 = tkinter.Label(self.main_frame, background='black', fg='#5bfba3')
        self.card_result_label1.grid(row=6, column=1, sticky='nw')
        self.card_result_label2 = tkinter.Label(self.main_frame, background='black', fg='#fda1a1')
        self.card_result_label2.grid(row=6, column=2, sticky='nw')

        #target cards text
        tkinter.Label(self.main_frame, text="Target Cards (234):", background='black', fg='white').grid(row=7, column=1, sticky='nw', padx=5)
        
        #target card entry
        self.selected_cards = tkinter.StringVar()
        target_entry = tkinter.Entry(self.main_frame, textvariable=self.selected_cards)
        target_entry.grid(row=7, column=2, sticky='ne')
        
        #target card button
        target_button = tkinter.Button(self.main_frame, text='Enter', command=self.count_selected)
        target_button.grid(row=7, column=3, sticky='nw', padx=5)
        
        #target cards result label
        self.target_card_result = tkinter.Label(self.main_frame, background='black', fg='white')
        self.target_card_result.grid(row=8, column=1, sticky='nw', columnspan=3)
        
        #remaining cards label and results
        tkinter.Label(self.main_frame, text="Remaining Cards:", background='black', fg='white').grid(row=1, column=4, sticky='nw', padx=5)
        self.remaining_probability_label = tkinter.Label(self.main_frame, background='black', fg='white')
        self.remaining_probability_label.grid(row=2, column=4, rowspan=8, sticky='ne', padx=5)

        #reset button
        reset_button = tkinter.Button(self.main_frame, text='Reset', command=self.reset_deck)
        reset_button.grid(row=10, column=4, sticky='se', pady=5, padx=5)

        # blank row in order to help with sizing of remaining cards message (long vertical message)
        tkinter.Label(self.main_frame, background='black', fg='white', pady=30).grid(row=9, column=4, sticky='e')

        # count suites label and results
        tkinter.Label(self.main_frame, text="Remaining Suites:", background='black', fg='white').grid(row=9, column=1, sticky='sw', padx=5)
        self.remaining_suites_label = tkinter.Label(self.main_frame, background='black', fg='white')
        self.remaining_suites_label.grid(row=10, column=1, columnspan=2, sticky='nw', padx=5)
    
    def create_deck(self):
        card_deck = {
            "H" : ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
            "D" : ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
            "C" : ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
            "S" : ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        }
        
        # uses list comprehension to create duplicates of the cards
        new_suit_list = [value for value in self.value_list for x in range(self.num_decks.get())]
        
        # updates the card_deck
        for suit in card_deck:
            card_deck[suit] = new_suit_list.copy()
        self.deck = card_deck
        
        # text to show deck has been updated
        return_text = "Updated with {} decks".format(self.num_decks.get())
        self.deck_result_label.config(text= return_text)
        
        # uses list comprehension to create a list of all the cards (regardless of suit)
        self.cards_remaining = [cards for suite in self.deck for cards in self.deck[suite]]
        
        # count the number of suites
        self.count_cards()
        self.count_suites()
        

    def count_cards(self):
        #Counts the remaining cards and give the probability of receiving each card
        all_card_prob = {}
        for card in self.value_list:
            all_card_prob[card] = "{}, {:.2f}%".format(self.cards_remaining.count(card),
                                                       self.cards_remaining.count(card) /
                                                       len(self.cards_remaining) * 100)
        
        # dictionary -> string -> printable
        printable_results = f"{len(self.cards_remaining)}\n"
        for key in all_card_prob:
            printable_results = ''.join([printable_results, f"{key}: {all_card_prob[key]}\n"])
            
        self.remaining_probability_label.config(text=printable_results)
        
        
    def count_suites(self):
        #Counts the number of cards left in each suite
        suite_prob = {}
        for suite in self.deck:
            suite_prob[suite] = "{}".format(len(self.deck[suite]))
            
        printable_results = ""
        new_line = 0
        for suite in suite_prob:
            if new_line != 1:
                printable_results = "".join([printable_results, f"{suite}: {suite_prob[suite]}, "
                                             f"{(int(suite_prob[suite])/len(self.cards_remaining))*100:.2f}% "])
                new_line += 1
            else:
                printable_results = "".join([printable_results, f"{suite}: {suite_prob[suite]}, " 
                                             f"{(int(suite_prob[suite])/len(self.cards_remaining))*100:.2f}% \n"])
                new_line += 1
                
        self.remaining_suites_label.config(text=printable_results)
        
    def remove_card(self):
        #Removes card from the deck 
        try: 
            suite = self.suite.get()
            card_list = self.deck[suite.upper()]
            face = self.face.get()
            card_index = card_list.index(face.upper())
            card_list.pop(card_index)
            
            card_index = self.cards_remaining.index(face.upper())
            self.cards_remaining.pop(card_index)
            
            self.card_result_label1.config(text="Card Removed")
            self.deck_result_label.after(2000, self.reset_card_text)
            
        except ValueError as error:
            self.card_result_label2.config(text="Card is not in the Deck")
            self.deck_result_label.after(2000, self.reset_card_text)
            
        except KeyError as error:
            self.card_result_label2.config(text="Not A Suit!!")
            self.deck_result_label.after(2000, self.reset_card_text)
        
        self.count_cards()
        self.count_suites()
        
    def count_selected(self):
        #Counts the remaining cards, and gives the probability for each card
        number_of_selected_cards = 0
        for card in self.cards_remaining:
            if card in self.selected_cards.get():
                number_of_selected_cards += 1
                
        self.probability = (number_of_selected_cards / len(self.cards_remaining)) *100
        
        text_to_return = f"The probability of receiving a {(self.selected_cards.get())} is {self.probability:.2f}%"
        self.target_card_result.config(text=text_to_return)
        
    def reset_deck(self):
        self.deck = {}
        self.cards_remaining = []
        self.probability = 0
        
        self.deck_result_label.destroy()
        self.deck_result_label = tkinter.Label(self.main_frame, background='black', fg='#5bfba3')
        self.deck_result_label.grid(row=2, column=1, sticky='nw', columnspan=2)
        
        self.remaining_probability_label.destroy()
        self.remaining_probability_label = tkinter.Label(self.main_frame, background='black', fg='white')
        self.remaining_probability_label.grid(row=2, column=4, rowspan=8, sticky='ne', padx=5)
        
        self.target_card_result.destroy()
        self.target_card_result = tkinter.Label(self.main_frame, background='black', fg='white')
        self.target_card_result.grid(row=8, column=1, sticky='nw', columnspan=3)

        
        self.remaining_suites_label.destroy()
        self.remaining_suites_label = tkinter.Label(self.main_frame, background='black', fg='white')
        self.remaining_suites_label.grid(row=10, column=1, columnspan=2, sticky='nw', padx=5)
        
    def reset_card_text(self):
        self.card_result_label1.destroy()
        self.card_result_label1 = tkinter.Label(self.main_frame, background="black", fg='#5bfba3')
        self.card_result_label1.grid(row=6, column=1, sticky='nw')
    
        self.card_result_label2.destroy()
        self.card_result_label2 = tkinter.Label(self.main_frame, background='black', fg='#fda1a1')
        self.card_result_label2.grid(row=6, column=2, sticky='nw')
        
        
if __name__ == "__main__":
    run = CardCounter()
    run.mainloop()
        