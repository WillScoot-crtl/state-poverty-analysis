import pandas as pd


# tracking historical data of an estimated percent of people
# of all ages in poverty for various states

def data_links():

    root1 = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23ebf3fb&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=866&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PPAA'
    root2 = 'A156NCEN&scale=left&cosd=1989-01-01&coed=2023-01-01&line_color=%230073e6&link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2025-07-06&revision_date=2025-07-06&nd=1989-01-01'
                            
    
    poverty_states = {'California': 'CA06000',
                      'Pennsylvania': 'PA42000',
                      'North Carolina': 'NC37000',
                      'West Virginia': 'WV54000',
                      'Missouri': 'MO29000',
                      'Florida': 'FL12000',
                      'New Jersey': 'NJ34000',
                      'North Dakota': 'ND38000',
                }
    
    return poverty_states, root1, root2
    


def poverty_analysis():
    
    dict_historical_data = {}
    poverty_states, root1, root2 = data_links()

    for state in poverty_states:
        state_data = []
        df_poverty = pd.read_csv(f"{root1}{poverty_states[state]}{root2}.csv")
        state_data.append(df_poverty)

        #renaming headers
        df_poverty.rename(columns={'observation_date': 'Observation Date',
                                    f'PPAA{poverty_states[state]}A156NCEN': 'Annual Percentage'
                                    }, inplace=True)
        df_poverty.rename(index={0: f'{state}'}, inplace=True)


                                    

        # concat individual keys and reassign to historical data
        df_concat = pd.concat(state_data)
        dict_historical_data[state] = df_concat

    return df_poverty, df_concat, dict_historical_data



    

poverty_analysis()

        

def main_analysis():

    df_poverty, df_concat, dict_historical_data = poverty_analysis()


    states = []
    mean   = []
    std    = []
    
    dict_data = {'States': states, 'Mean': mean, 'Standard Deviation': std}

    for state in dict_historical_data:

        df = dict_historical_data[state]
        print(f'{dict_historical_data[state]}\n')
        
        #for each state, printing sum, mead, and standard deviation
        states.append(state)
        mean.append(df['Annual Percentage'].mean())
        std.append(df['Annual Percentage'].std())

       
    df = pd.DataFrame(dict_data)

    
    print(df)
        
    

if __name__ == "__main__":

    main_analysis()






    

            
