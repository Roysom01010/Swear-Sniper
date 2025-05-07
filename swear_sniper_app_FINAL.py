# Swear Sniper - Streamlit App
# Requirements: streamlit, pandas

import streamlit as st
import pandas as pd
import re

def load_foul_words():
    data = [
        {'Word': 'Ana ni nzana la', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Annathai kaluthai', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Tamil'},
        {'Word': 'Arse', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'ass bag', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'ass cock', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'asscock', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'ass hat', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'ass sucker', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'asssucker', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'ass hole', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'ass', 'Base Rating': '7+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'scum', 'Base Rating': '7+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'asshole', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Baal', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Bahen Chod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'BahenChod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Bakchodi', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Balls', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Banging', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'bedhei pua', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Oriya'},
        {'Word': 'Benegod', 'Base Rating': '16+', 'Max Count': 3, 'Language': ''},
        {'Word': 'Bhadava', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Bhadhava', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Bhenchod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Bhosadike', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Bhosdike', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'bin gotyaachya', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Marathi'},
        {'Word': 'Biya chudi', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Oriya'},
        {'Word': 'blow job', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Blow me', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'blowjob', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Boka choda', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Bengali'},
        {'Word': 'Boner', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Breasts', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Bullshit', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'shit', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Bastard', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Bitch', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'bunghole', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'chaat', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'chaatu', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Charam Sukh', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Chinaal', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Chod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Chodu', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Chodhru', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'chudail', 'Base Rating': '7+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Chutiya', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'clitoris', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'clit', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'cock', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Cocksucker', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Sucker cock', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Coon', 'Base Rating': '18+ (A)', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Cope', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Koppu', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Crotch', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Cum', 'Base Rating': '16+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'dagaar', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Kannada'},
        {'Word': 'Damn', 'Base Rating': '7+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Damnit', 'Base Rating': '7+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Damn it', 'Base Rating': '7+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Darn', 'Base Rating': 'U', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'dick', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'dickhead', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'dickhole', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'dillhole', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Dong', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Dyke', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Gay', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'erection', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Fingering', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Fucker', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Fuck', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Fuddu', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Chaatu', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Ullu', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Gaand Marwana', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Gaen', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'gang bang', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Gavaar', 'Base Rating': '7+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Gayee de', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'god dammit', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'god dammit', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Gook', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Goto', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Gota', 'Base Rating': '16+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Hag', 'Base Rating': '7+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Haraamkhor', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Harami', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Hell', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'hooker', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Hui thu', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Manipuri'},
        {'Word': 'Idiot', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Jackoff', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Jap', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Japs', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Spic', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Kyke', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Fag', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Faggot', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Jerk off', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'jhantoo', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Junk', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Kalla nayinte makkale', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'kambakhat', 'Base Rating': '7+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Kanjar', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Katua', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'Hindi'},
        {'Word': 'khankir pola', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Bengali'},
        {'Word': 'Koodhi', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Tamil'},
        {'Word': 'Koothi Mayir', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Tamil'},
        {'Word': 'Kukuraha', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'kutaar baaccha', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Bengali'},
        {'Word': 'Kuttiya', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'lag gaye', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'Hindi'},
        {'Word': 'Kat gayi', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'Hindi'},
        {'Word': 'Lagi padi hai', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'Hindi'},
        {'Word': 'Lag gayi', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'Hindi'},
        {'Word': 'Lendi', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Lulli', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Maa-bahen karna', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Maataripurushaha', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Sanskrit'},
        {'Word': 'Motherfucker', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Jesusfucking', 'Base Rating': '16+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Mary', 'Base Rating': '16+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Motherfucker', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Motherchod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Madarchod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Maadharjhant', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Madarjaat', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Maderchod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Maderchodh', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Maderchodna', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Maadher chod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Lund', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Choot', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Chutiya', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'majigod', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Mayir', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Mayiru', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Mooth', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Munna', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Nalayak', 'Base Rating': '7+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'nigga', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'nigger', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'nikka', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'nipples', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Nips', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Oh My God', 'Base Rating': 'U', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Oombi', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'Malayalam'},
        {'Word': 'Oomb', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'Malayalam'},
        {'Word': 'Ootan', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'Malayalam'},
        {'Word': 'orgasm', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Paagal', 'Base Rating': '7+', 'Max Count': 10, 'Language': 'Hindi'},
        {'Word': 'Paki', 'Base Rating': '18+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Patti', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'poda','Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'poda patti', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'phallus', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'Piss off', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Poott', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'poori', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'poori mole', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'Pottan', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Pranthan', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'pranth', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'Malayalam'},
        {'Word': 'Pussy', 'Base Rating': '16+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Puss', 'Base Rating': '16+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Queer', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Randhwa', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Randwa', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Randi', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Rand', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Raand', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'Rundi', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Hindi'},
        {'Word': 'rub one out', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Samanam', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'screw', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'English'},
   	    {'Word': 'Scrotum', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
    	{'Word': 'Sex Toy', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Dildo', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Vibrator', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
        {'Word': 'Gspot', 'Base Rating': '13+', 'Max Count': 3, 'Language': 'English'},
    	{'Word': 'Shikhwmwn', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Assamese'},
    	{'Word': 'Shoot', 'Base Rating': 'U', 'Max Count': 3, 'Language': 'English'},
    	{'Word': 'Skank', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
    	{'Word': 'slutty', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
    	{'Word': 'Son of a Bitch', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
    	{'Word': 'Sperm', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'English'},
    	{'Word': 'Stupid', 'Base Rating': '7+', 'Max Count': 3, 'Language': 'English'},
    	{'Word': 'Suar', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Hindi'},
    	{'Word': 'Sudirbai', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Assamese'},
    	{'Word': 'Tits', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'Titties', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
    	{'Word': 'Thevidichi', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'thevidichi mole', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'thevidichi mone', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'thevidchide makkale', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
        {'Word': 'Thanthayillatharam', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'Malayalam'},
    	{'Word': 'Twat', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
    	{'Word': 'Ullu ke pathe', 'Base Rating': '13+', 'Max Count': 999, 'Language': 'Hindi'},
    	{'Word': 'Veri pukka', 'Base Rating': '16+', 'Max Count': 3, 'Language': 'Telugu'},
    	{'Word': 'wank', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'wanker', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
    	{'Word': 'whackoff', 'Base Rating': '13+', 'Max Count': 10, 'Language': 'English'},
        {'Word': 'whore', 'Base Rating': '13+', 'Max Count': 5, 'Language': 'English'},
        {'Word': 'terrorist', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'lgbtq', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'lgbtq+', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'pedophile', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'beasitiality', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Hindu', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Islam', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Buddhism', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Sikh', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Narendra Modi', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Kashmir', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'POK', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Sanatan', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Saddam Hussain', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
        {'Word': 'Turkey', 'Base Rating': '13+', 'Max Count': 1, 'Language': 'English'},
]
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Handle rating conversions
    df['Base Rating'] = df['Base Rating'].str.replace('A', '18+')
    
    # Handle unlimited values
    df['Max Count'] = df['Max Count'].replace('No limit', 999).astype(int)
    
    return df

foul_words_df = load_foul_words()

# App UI
st.set_page_config(page_title="Swear Sniper", layout="centered")
st.title(" Swear Sniper")
st.markdown("Created by **Soumarghyo Roy**")
st.markdown ("Copyright (c) 2025 Soumarghyo Roy. All Rights Reserved.")
st.markdown (" Protected by applicable Indian and International Copyright Laws. Unauthorized use is prohibited.")

# Input boxes
script = st.text_area("📜 Paste your script here:", height=300)
language_options = sorted(foul_words_df['Language'].unique())
age_ratings = ['U', '7+', '13+', '16+', '18+']

filter_language = st.multiselect(" Filter Language:", 
                               options=language_options, 
                               default=language_options)
filter_words = st.multiselect(" Filter Words:", 
                            options=foul_words_df['Word'].tolist(), 
                            default=foul_words_df['Word'].tolist())
selected_rating = st.multiselect(" Select One or More Age Ratings:", 
                             options=age_ratings, default=age_ratings)

if st.button(" ANALYZE SCRIPT"):
    if not script:
        st.warning("Please paste a script first.")
    else:
        # Filter words
        df_filtered = foul_words_df[
            (foul_words_df['Language'].isin(filter_language)) &
            (foul_words_df['Word'].isin(filter_words))
        ]

        results = []
        word_counts = {}
        lines = script.splitlines()

        # Analysis logic
        for line_num, line in enumerate(lines, 1):
            for _, row in df_filtered.iterrows():
                word = row['Word']
                pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
                matches = pattern.findall(line)
                if matches:
                    count = len(matches)
                    word_counts[word] = word_counts.get(word, 0) + count
                    results.append({
                        'Word': word,
                        'Line': line.strip(),
                        'Line No': line_num,
                        'Count': count,
                        'Base Rating': row['Base Rating'],
                        'Max Allowed': row['Max Count']
})
        # Display results
        if results:
            output_df = pd.DataFrame(results)
            st.subheader(" Found Instances")
            st.dataframe(output_df)

            # Calculate ratings
            st.subheader(" Rating Analysis")
            count_df = pd.DataFrame(
                [(word, count) for word, count in word_counts.items()],
                columns=['Word', 'Total Count']
            ).merge(foul_words_df, on='Word')

            # Determine violations
            violations = []
            for _, row in count_df.iterrows():
                allowed = row['Max Count']
                actual = row['Total Count']
                if actual > allowed:
                    violations.append(row['Base Rating'])
                else:
                    violations.append(None)
            
            count_df['Violation'] = violations
            st.dataframe(count_df)

            # Final rating calculation
            
            if isinstance(selected_rating, list):
                selected_max = max(selected_rating, 
                                   key=lambda x: age_ratings.index(x))
            else:
                selected_max = selected_rating
                final_rating = max(max_violation, selected_max, 
                                   key=lambda x: age_ratings.index(x))
            
# Determine final rating from violations if available
if 'count_df' in locals() and not count_df.empty and 'Suggested Rating' in count_df.columns:
    # Pick the highest (strictest) rating from the list
    rating_order = ['U', '7+', '13+', '16+', '18+']
    count_df['Rating Index'] = count_df['Suggested Rating'].apply(lambda x: rating_order.index(x))
    final_rating = count_df.sort_values(by='Rating Index', ascending=False)['Suggested Rating'].iloc[0]

    st.subheader(f" Final Rating: {final_rating}")
else:
    st.info(" No rating escalation needed based on selected age filter.")

